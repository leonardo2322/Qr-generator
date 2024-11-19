from django import forms
from .models import M_Qr_image
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import logging
logger = logging.getLogger(__name__)

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
    
    
    def save(self, commit=True):
        user = super().save(commit=False)
        # No otorgar privilegios de superusuario
        user.is_superuser = False
        user.is_staff = False  
        if commit:
            user.save()
        return user
    
class Qr_Form(forms.ModelForm):
    class Meta:
        model = M_Qr_image
        fields = ['titulo', 'url', 'logo_url', 'color_qr','qr_icono_imagen']
        widgets = {
            'qr_icono_imagen': forms.HiddenInput()  # Hacerlo oculto
        }

    def save(self, commit=True):
        obj = super().save(commit=False)  # Crear el objeto sin guardar aún
        print(obj,"-----------objeto---------en form")
        # Validar los campos requeridos
        if not obj.titulo or not obj.url:
            raise ValueError("Título y URL son campos obligatorios.")

        # Generar el QR solo después de que el objeto se haya guardado en la vista
        if commit:
            obj.save()  # Guarda el objeto si commit=True
            try:
                logo_url = obj.logo_url.path if obj.logo_url else None
                result = obj.generate_qr(logo_url=logo_url, Qrcolor=obj.color_qr)
                if not result.get("success", True):
                    raise ValueError(result.get("message", "Error inesperado al generar el QR."))
            except Exception as e:
                logger.error(f"Error generando el QR para el objeto {obj}: {e}")
                raise ValueError(f"Error al generar el QR: {str(e)}")

        return obj
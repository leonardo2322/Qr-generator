from django.views.generic import ListView,CreateView,DeleteView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
import logging
from .models import M_Qr_image
from .forms import Qr_Form, CustomUserCreationForm


logger = logging.getLogger(__name__)


class User_Register_View(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')  

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

class InicioView(TemplateView):
    template_name = 'base.html'


class login_view(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('lista_qrs')



class V_Qr_lista(LoginRequiredMixin, ListView):
    model = M_Qr_image
    template_name = "App/qr_list.html"
    context_object_name = "list_qrs"
    login_url = 'login'
    def get_queryset(self):
        # Filtrar los QR por el usuario autenticado
        return M_Qr_image.objects.filter(user=self.request.user)
    
class Create_qr_view_form(CreateView):
    model = M_Qr_image
    form_class = Qr_Form
    template_name = 'App/create_qr.html'
    success_url = reverse_lazy('lista_qrs')

    def form_valid(self, form):
        try:
            # Guardar la instancia usando el formulario
            obj = form.save(commit=False)  # No guarda aún el objeto
            print(obj,"-----------objeto---------en form")

            obj.user = self.request.user  # Asigna el usuario al objeto
            obj.save()  # Guarda el objeto para asegurar que user_id no sea NULL
        except ValueError as e:
            logger.error(f"Error al guardar el formulario: {e}")
            form.add_error(None, str(e))
            return self.form_invalid(form)
        except Exception as e:
            logger.error(f"Error inesperado: {e}")
            form.add_error(None, f"Ocurrió un error inesperado al procesar el formulario {str(e)}")
            return self.form_invalid(form)

        return super().form_valid(form)
    
class Delete_qr_view(DeleteView):
    model = M_Qr_image
    template_name = 'App/delete_temp.html'
    success_url = reverse_lazy('lista_qrs')
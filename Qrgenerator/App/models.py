import qrcode
import logging
from PIL import Image, ImageDraw, ImageOps
from io import BytesIO
from django.db import models
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
# Create your models here.
logger = logging.getLogger(__name__)


class M_Qr_image(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    fecha_actualizado = models.DateTimeField(auto_now=True)
    titulo = models.CharField(max_length=100,blank=True)
    url = models.URLField(max_length=500,blank=False,null=False)
    qr_icono_imagen = models.ImageField(upload_to='images/', null=True, blank= True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    logo_url = models.ImageField(upload_to='images/', null=True, blank=True)
    color_qr = models.CharField(max_length=7,null=True,blank=True)


    def generate_qr(self, logo_url=None, Qrcolor=None):
            try:
                print("-----------objeto---------en model")

                QRcode = qrcode.QRCode(
                    error_correction=qrcode.constants.ERROR_CORRECT_H
                )
                QRcode.add_data(self.url)
                QRcode.make()

                QRcolor = Qrcolor if Qrcolor else "#000000"
                QRimg = QRcode.make_image(
                    fill_color=QRcolor, back_color="white"
                ).convert('RGB')

                # Procesar el logo solo si se proporciona
                if logo_url:
                    try:
                        logo = Image.open(logo_url)
                        base_width = 100
                        wpercent = base_width / float(logo.size[0])
                        hsize = int(float(logo.size[1]) * float(wpercent))
                        logo = logo.resize((base_width, hsize), Image.LANCZOS)

                        # Crear un logo redondeado
                        mask = Image.new("L", logo.size, 0)
                        draw = ImageDraw.Draw(mask)
                        draw.ellipse((0, 0, logo.size[0], logo.size[1]), fill=255)
                        rounded_logo = ImageOps.fit(logo, mask.size, centering=(0.5, 0.5))
                        rounded_logo.putalpha(mask)

                        # Colocar el logo en el centro del QR
                        pos = ((QRimg.size[0] - rounded_logo.size[0]) // 2,
                            (QRimg.size[1] - rounded_logo.size[1]) // 2)
                        QRimg.paste(rounded_logo, pos, rounded_logo)
                    except Exception as e:
                        logger.error(f"Error procesando el logo: {e}")
                        raise ValueError(f"Error procesando el logo: {str(e)}")

                # Guardar la imagen del QR generado
                buffer = BytesIO()
                QRimg.save(buffer, format='PNG')
                buffer.seek(0)
                self.qr_icono_imagen.save(f'{self.titulo}_qr.png', ContentFile(buffer.read()), save=False)

                if self.qr_icono_imagen.name:
                        self.save()
                print("-----------objeto---------en model")
                return {"success": True}
            except Exception as e:
                logger.error(f"Error generando el QR: {e}")
                return {"success": False, "message": f"Error generando QR: {str(e)}"}
            



    def __str__(self):
        return f"{self.titulo}, {self.url}  {self.qr_icono_imagen} {self.logo_url}"
    
    
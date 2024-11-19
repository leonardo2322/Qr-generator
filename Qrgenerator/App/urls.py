from django.urls import path
from .views import V_Qr_lista,InicioView,login_view, Create_qr_view_form, Delete_qr_view
from django.contrib.auth.views import LogoutView
from .views import User_Register_View
urlpatterns = [
    path('',InicioView.as_view(),name="inicio"),
    path('login/', login_view.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', User_Register_View.as_view(), name='register'),
    path('lista_qrs/', V_Qr_lista.as_view(),name='lista_qrs'),
    path('crear_qr/',Create_qr_view_form.as_view(), name='add_qr'),
    path('eliminar/<int:pk>/',Delete_qr_view.as_view(), name='eliminar')
] 
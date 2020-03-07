from django.urls import path
from django.contrib.auth import views as auth_views
from cuenta.views import inicio, productos, cliente, registrarOrden, actualizarOrden, eliminarOrden, registrarse, iniciarSesion, cerrarSesion, usuario, opcionCuenta

urlpatterns = [
    path('registrarse/', registrarse, name="registrarse"),
    path('iniciarSesion/', iniciarSesion, name="iniciarSesion"),
    path('cerrarSesion/', cerrarSesion, name="cerrarSesion"),
    path('', inicio, name="inicio"),
    path('usuario/', usuario, name="usuario"),
    path('cuenta/', opcionCuenta, name="opcionCuenta"),
    path('productos/', productos, name="productos"),
    path('cliente/<str:idCliente>/', cliente, name="cliente"),
    path('registrarOrden/', registrarOrden, name="registrarOrden"),
    path('actualizarOrden/<str:idOrden>/', actualizarOrden, name="actualizarOrden"),
    path('eliminarOrden/<str:idOrden>/', eliminarOrden, name="eliminarOrden"),
    # path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    # path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    # path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    # path('reiniciarContrasena/', auth_views.PasswordResetView.as_view(template_engine="cuenta/reiniciarContrasena.html"), name="reiniciarContrasena"),
    # path('reiniciarContrasenaEnviado/', auth_views.PasswordResetDoneView.as_view(template_engine="cuenta/reiniciarContrasenaEnviado.html"), name="reiniciarContrasenaEnviado"),
    # path('reiniciar/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_engine="cuenta/reiniciarContrasenaForm.html"), name="reiniciarContrasenaForm"),
    # path('reiniciarContrasenaRealizado/', auth_views.PasswordResetCompleteView.as_view(template_engine="cuenta/reiniciarContrasenaRealizado.html"), name="reiniciarContrasenaRealizado"),
]

'''
1 - Enviar formulario de email                        // PasswordResetView.as_view()
2 - Enviado mensaje de exito al correo                // PasswordResetDoneView.as_view()
3 - Enlace al formulario de recuperar contraseña      // PasswordResetConfirmView.as_view()
4 - Mensaje de cambio de contraseña                   // PasswordResetCompleteView.as_view()
'''

from django.urls import path
from .views import ClienteViews
from .views import Creditosview
from .views import UsuarioViews
from . import views


urlpatterns=[

  path('cliente/',ClienteViews.as_view(), name="Listar"),
  path('cliente/<int:doc>',ClienteViews.as_view(), name="actualizar"),
  path('cliente/<int:documento>',ClienteViews.as_view(), name="actualizar"),
  path('credito/',Creditosview.as_view(), name="Listar"),
  path('usuario/',UsuarioViews.as_view(), name="Listarusuarios"),
  path('login/',views.loginusuario, name="loginusu" ),
  path('gestioncliente',views.gestioncliente, name="gestion" ),
  path('frminsertar/',views.frminsertar, name="registrar" ),
  path('actualizarcliente/<int:documento>',views.frmmodificar, name="actual" ),
  path('eliminarcliente/<int:documento>',views.eliminarcli, name="eliminar" ),
  path('actualizarcliente/',views.editar, name="mscdsds" ),
  path('consultaru/<int:documento>',views.consultainner, name="consultainner" ),
   path('',views.principal, name="principal" ),
  
]
from django.urls import path, include
from .views import home, insumos, nosotros, galeria, modificar, eliminar, registro, InsumoViewset, error_facebook, token, contacto, ContactoViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register("insumo", InsumoViewset)
router.register("contacto", ContactoViewset)

urlpatterns = [
    path('',home, name="home"),
    path('insumos/', insumos, name="insumos"),
    path('nosotros/', nosotros, name="nosotros"),
    path('galeria/', galeria, name="galeria"),
    path('modificar/<id>/', modificar, name ="modificar"),
    path('eliminar/<id>/', eliminar, name="eliminar"),
    path('registro/', registro, name="registro"),
    path('api/', include(router.urls)),
    path('error-facebook/', error_facebook, name="error_facebook"),
    path('save-token/', token, name="save_token"),
    path('contacto/', contacto, name="contacto"),
]



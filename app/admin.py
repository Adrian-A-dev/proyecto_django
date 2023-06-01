from django.contrib import admin
from .models import Insumo, Servicio, Slider, Galeria, Nosotros, Contacto, Tipo_contacto
from .forms import InsumoForms, ContactoForms, Tipo_contactoForms
# Register your models here.

class Tipo_contactoAdmin(admin.ModelAdmin):
    form = Tipo_contactoForms
    list_display = ["nombre"]
    search_fields = ["nombre"]
    list_per_page = 10

class ContactoAdmin(admin.ModelAdmin):
    form = ContactoForms
    list_display = ["nombre", "apellido", "asunto", "tipo_contacto", "mensaje"]
    search_fields = ["tipo_contacto"]
    list_per_page = 10

class InsumoAdmin(admin.ModelAdmin):
    form = InsumoForms
    list_display = ["nombre", "precio", "descripcion"]
    search_fields = ["nombre"]
    list_per_page = 10


class ServicioAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "descripcion"]
    search_fields = ["nombre"]
    list_per_page = 10

class SliderAdmin(admin.ModelAdmin): 
    list_display = ["nombre", "imagen"] 
    search_fields = ["nombre"]
    list_per_page = 10

class GaleriaAdmin(admin.ModelAdmin):
    list_display = ["nombre", "imagen"]
    search_fields = ["nombre"]
    list_per_page = 10

class NosotrosAdmin(admin.ModelAdmin):
    list_display = ["fecha", "nosotros", "historia", "mision", "vision"]
    search_fields = ["fecha"]
    list_per_page = 10



admin.site.register(Insumo, InsumoAdmin)
admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Galeria, GaleriaAdmin)
admin.site.register(Nosotros, NosotrosAdmin)
admin.site.register(Contacto, ContactoAdmin)
admin.site.register(Tipo_contacto, Tipo_contactoAdmin)

admin.site.site_header = "Administración CarWash"
admin.site.site_title = "CarWash"
admin.site.index_title = "Sitio Administrativo de CarWash"
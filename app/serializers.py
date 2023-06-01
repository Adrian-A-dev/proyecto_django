from .models import Insumo, Contacto
from rest_framework import serializers

class ContactoSerializer(serializers.ModelSerializer):

    nombre_tipo_contacto = serializers.CharField(read_only=True, source="tipo_contacto.nombre")
    
    class Meta:
        model = Contacto

        fields = '__all__'


class InsumoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Insumo

        fields = '__all__' 


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(required=True)
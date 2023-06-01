from django.shortcuts import render, redirect, get_object_or_404
from .models import Servicio, Slider, Galeria, Nosotros, Insumo, Contacto
from .forms import InsumoForms, CustomUserCreationForm, ContactoForms
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from django.http import Http404
from .serializers import InsumoSerializer, TokenSerializer, ContactoSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from django.http import JsonResponse
from rest_framework.decorators import api_view
from fcm_django.models import FCMDevice


# Create your views here.
@api_view(['POST'])
def token(request):
    #{"token": "dfasdflkjl234234sdfskldjflkj234jlskdjflksjdflkj234k"}
    serializer = TokenSerializer(data=request.data)

    if serializer.is_valid():
        token = serializer.data["token"]

        dispositivo = FCMDevice.objects.filter(registration_id=token, active=True).first()

        if not dispositivo:
            dispositivo = FCMDevice(registration_id=token, active=True)

        if request.user.is_authenticated:
            dispositivo.user = request.user
        
        dispositivo.save()

        return JsonResponse({"mensaje":"ok"}, status=200)
    return JsonResponse({"mensaje": "no viene el token"}, status=400)#badrequest


def home(request):
    servicios = Servicio.objects.all()
    slider = Slider.objects.all()
    
    data = {
        "servicios":servicios,
        "slider":slider,   
    }


    return render(request, 'app/home.html', data)


@permission_required('app.add_insumo')
def insumos(request):

    insumos = Insumo.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(insumos, 5)
        insumos = paginator.page(page)
    except:
        raise Http404

    data = {
        "form": InsumoForms(),
        "entity": insumos,
        "paginator": paginator
    }

    if request.method == 'POST':
        formulario = InsumoForms(data=request.POST, files=request.FILES)

        if formulario.is_valid():
            formulario.save()

            dispositivos = FCMDevice.objects.all()

            dispositivos.send_message(
                title="Nuevo insumo ingresado",
                body="Se ha ingreado un nuevo insumo al sistema!!!!!!",
                icon="/static/app/img/icono.png"
            )

            messages.success(request, "Guardado con exito")
        data["form"] = formulario

    return render(request, 'app/insumos.html', data)

def contacto(request):
    contacto = Contacto.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(contacto, 5)
        contacto = paginator.page(page)
    except:
        raise Http404

    data = {
        "form":ContactoForms(),
        "entity": contacto,
        "paginator": paginator
    }

    if request.method == 'POST':
        formulario = ContactoForms(data=request.POST, files=request.FILES)

        if formulario.is_valid():
            formulario.save()

            contacto = FCMDevice.objects.filter(user__is_superuser = True)

            contacto.send_message(
                title="Nuevo contacto  ingresado",
                body="Se ha ingreado un nuevo contacto al sistema!!!!!!",
                icon="/static/app/img/icono.png"
            )

            messages.success(request, "Guardado con exito")
        data["form"] = formulario
    return render(request,'app/contacto.html',data)

def nosotros(request):
    nosotros = Nosotros.objects.all()
    
    data = {
        "nosotros":nosotros
    }
    return render(request, 'app/nosotros.html',data)

def galeria(request):
    galeria = Galeria.objects.all()

    data = {
        "galeria":galeria
    }

    return render(request, 'app/galeria.html', data)

#@login_required
@permission_required('app.change_insumo')
def modificar(request, id):
    #insumo = Insumo.objects.get(id=id)
    insumo = get_object_or_404(Insumo, id=id)

    data = {
        "form":InsumoForms(instance=insumo)
    }

    if request.method == "POST":
        formulario = InsumoForms(data=request.POST, instance=insumo, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "El registro ha sido modificado!")
            return redirect(to="insumos") 
        data["form"] = formulario

    return render(request,'app/modificar.html', data)

#@login_required
@permission_required('app.delete_insumo')
def eliminar(request, id):
    #insumo = Insumo.objects.get(id=id)
    insumo = get_object_or_404(Insumo, id=id)

    insumo.delete()
    messages.success(request, "El registro ha sido eliminado!")
    return redirect(to="insumos")


def registro(request):

    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            #debo autenticar al usuario
            user = authenticate(username=formulario.cleaned_data["username"],
                password=formulario.cleaned_data["password1"]
            )
            login(request, user)
            return redirect(to="home")
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)

class InsumoViewset(viewsets.ModelViewSet):
    queryset = Insumo.objects.all()
    serializer_class = InsumoSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        
        insumos = Insumo.objects.all()

        nombre = self.request.GET.get("nombre")
        stock = self.request.GET.get("stock")

        if nombre:
            insumos = insumos.filter(nombre__contains=nombre)

        if stock:
            insumos = insumos.filter(stock=stock)

        return insumos

class ContactoViewset(viewsets.ModelViewSet):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        
        contacto = Contacto.objects.all()

        nombre = self.request.GET.get("nombre")
        tipo_contacto = self.request.GET.get("nombre")

        if nombre:
            contacto = contacto.filter(nombre__contains=nombre)

        if tipo_contacto:
            contacto = contacto.filter(tipo_contacto=tipo_contacto)

        return contacto

def error_facebook(request):
    return render(request, 'registration/error_facebook.html')


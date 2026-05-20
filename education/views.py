from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import Curiosity, AIDefinition, Concept, NeuralNetworkType

# Vista de la Landing Page (Pública)
def landing_page(request):
    """
    Renderiza la página de inicio pública.
    Muestra el título del proyecto y las curiosidades cargadas en la base de datos.
    """
    curiosities = Curiosity.objects.all()
    # Si el usuario ya está autenticado, podemos facilitarle un botón al panel directo en el template
    return render(request, 'education/landing.html', {
        'curiosities': curiosities
    })


# Vista para el Registro de Usuarios (Pública)
def register_user(request):
    """
    Maneja el registro de nuevos usuarios en el sistema.
    Si el usuario se registra exitosamente, se inicia sesión automáticamente 
    y se lo redirige a la página de contenido protegido.
    """
    if request.user.is_authenticated:
        return redirect('content')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Iniciar sesión automáticamente después de registrarse
            login(request, user)
            messages.success(request, f"¡Registro exitoso! Bienvenido/a, {user.username}.")
            return redirect('content')
        else:
            messages.error(request, "Hubo un error en el registro. Por favor, verifica los datos e intenta nuevamente.")
    else:
        form = UserCreationForm()

    return render(request, 'education/register.html', {
        'form': form
    })


# Vista para el Inicio de Sesión (Pública)
def login_user(request):
    """
    Maneja la autenticación de usuarios existentes utilizando el formulario integrado de Django.
    """
    if request.user.is_authenticated:
        return redirect('content')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"¡Hola de nuevo, {username}!")
                return redirect('content')
            else:
                messages.error(request, "Usuario o contraseña incorrectos.")
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()

    return render(request, 'education/login.html', {
        'form': form
    })


# Vista para el Cierre de Sesión (Pública)
def logout_user(request):
    """
    Cierra la sesión del usuario actual y redirige a la landing page.
    """
    logout(request)
    messages.info(request, "Has cerrado sesión correctamente.")
    return redirect('landing')


# Vista del Contenido Educativo (Protegida)
@login_required(login_url='login')
def educational_content(request):
    """
    Renderiza la sección educativa principal, accesible únicamente para usuarios autenticados.
    Obtiene las definiciones de IA, el concepto principal de redes neuronales y sus 7 tipos.
    """
    ai_definitions = AIDefinition.objects.all()
    # Obtenemos el concepto de Redes Neuronales Artificiales
    nn_concept = Concept.objects.filter(name__icontains="Redes Neuronales Artificiales").first()
    # Si por alguna razón no se encuentra por filtro, traemos el primero disponible
    if not nn_concept:
        nn_concept = Concept.objects.first()
    
    nn_types = NeuralNetworkType.objects.all()

    return render(request, 'education/content.html', {
        'ai_definitions': ai_definitions,
        'nn_concept': nn_concept,
        'nn_types': nn_types
    })

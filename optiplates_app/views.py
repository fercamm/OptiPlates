from django.shortcuts import render

# Create your views here.
# mi_app/views.py
from django.shortcuts import render, redirect
import hashlib
from datetime import datetime
from django.contrib import messages
from .utils import generate_secure_hash
from .queries import users
from django.utils.translation import gettext as _
from django.contrib.auth import logout

def login_view(request):
    if request.session.get('username'):
        provided_hash = request.GET.get('secure_hash')
        if provided_hash != request.session.get('secure_hash'):
            messages.error(request, _("Invalid user credentials"))
            request.session['username'] = None
            request.session['secure_hash'] = None
            return redirect('login') # Problema con el token
        return redirect('home') # Usuario ya logueado

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password = hashlib.sha256(password.encode()).hexdigest()

        user_found = users.findUser({"username": username, "password": password})

        if user_found:
            request.session['username'] = user_found["username"]

            request.session['secure_hash'] = generate_secure_hash()

            return redirect('home')  # Redirigir a la página de inicio
        else:
            messages.error(request, _("Invalid user credentials"))
            return redirect('login')

    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        # Encriptación de la contraseña
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Verificar si el usuario ya existe
        existing_user = users.findUserByMultipleFields([{"username": username},
                                                       {"email": email}])
        if existing_user:
            messages.error(request, _("User already exists"))
            return redirect('register')

        # Datos para insertar
        user = {
            "username": username,
            "email": email,
            "password": hashed_password,
            "first_name": first_name,
            "last_name": last_name,
            "created": datetime.now(),
            "modified": datetime.now(),
            "deleted_at": None
        }

        # Insertar en MongoDB
        users.insertUser(user)

        messages.success(request, _("User created"))
        return redirect('login')  # Redirigir a la página de inicio de sesión

    return render(request, 'register.html')


def home_view(request):
    if not request.session.get('username'):
        messages.error(request, _("Invalid user credentials"))
        return redirect('login')  # Si el usuario no está logueado, redireccionar al login

    logged_user = users.findUser({"username": request.session.get('username')})

    context = {
        'username': logged_user['username']
    }

    return render(request, 'home.html', context)

def logout_view(request):
    logout(request)
    messages.success(request, _("Logout successfully"))
    request.session['username'] = None
    request.session['secure_hash'] = None
    return redirect('login')  # Redirigir al login después del logout
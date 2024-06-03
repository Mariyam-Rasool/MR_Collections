# from django.shortcuts import render
# def signup_view(request):
#     return render (request, 'signup.html')

# def login_view(request):
#     return render(request,'login.html')
# def logout_view(request):
#     return render(request,'logout.html')
# def profile_view(request):
#     return render(request,'profile.html')



# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import login, authenticate, logout

# def signup_view(request):
#     if request.method == 'POST':
#         signup_form = UserCreationForm(request.POST)
#         if signup_form.is_valid():
#             user = signup_form.save()
#             user.refresh_from_db()
#             login(request, user)
#             return redirect('base')
#     signup_form = UserCreationForm()
#     context = {
#         'signup_form' : signup_form,
#     }
#     return render (request, 'signup.html', context)

# def base_view(request):
#     return render(request, 'base.html')

# def login_view(request):
#     if request.method == 'POST':
#         login_form = AuthenticationForm(request=request, data=request.POST)
#         if login_form.is_valid():
#             email = login_form.cleaned_data.get('email')
#             password = login_form.cleaned_data.get('password')
#             user = authenticate(email=email, password=password)
#             login(request, user)
#             return redirect ('base')
#     login_form = AuthenticationForm()
#     context = {
#         'login_form' : login_form,
#     }
#     return render(request, 'login.html', context)






# from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib import messages

# def signup_view(request):
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         username = request.POST['username']
#         email = request.POST['email']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']

#         if password1 != password2:
#             messages.error(request, "Passwords do not match")
#             return render(request, 'signup.html')

#         if User.objects.filter(username=username).exists():
#             messages.error(request, "Try another username")
#             return render(request, 'signup.html')

#         if User.objects.filter(email=email).exists():
#             messages.error(request, "Email already exists")
#             return render(request, 'signup.html')

#         user = User.objects.create_user(
#             username=username,
#             email=email,
#             password=password1,
#             first_name=first_name,
#             last_name=last_name
#         )
#         login(request, user)
#         return redirect('base')
#     return render(request, 'signup.html')

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('base')
#         else:
#             messages.error(request, "Invalid username or password")
#             return render(request, 'login.html')
#     return render(request, 'login.html')

# def base_view(request):
#     return render(request, 'base.html')






# from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from django.core.mail import send_mail

# def signup_view(request):
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         username = request.POST['username']
#         email = request.POST['email']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']

#         if password1 != password2:
#             messages.error(request, "Passwords do not match")
#             return render(request, 'signup.html')

#         if User.objects.filter(username=username).exists():
#             messages.error(request, "Username already taken")
#             return render(request, 'signup.html')

#         # if User.objects.filter(email=email).exists():
#         #     messages.error(request, "Email already registered")
#         #     return render(request, 'signup.html')

#         user = User.objects.create_user(
#             username=username,
#             email=email,
#             password=password1,
#             first_name=first_name,
#             last_name=last_name
#         )
#         login(request, user)
        
#         send_mail(
#             'Welcome to MR Collections',
#             'Thank you for signing up, {}!'.format(first_name),
#             'your_email@example.com',
#             [email],
#             fail_silently=False,
#         )
        
#         return redirect('profile')  # Redirect to profile page after signup
#     return render(request, 'signup.html')

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
            
#             send_mail(
#                 'Login Notification',
#                 'You have logged in, {}!'.format(user.first_name),
#                 'your_email@example.com',
#                 [user.email],
#                 fail_silently=False,
#             )
            
#             return redirect('profile')  # Redirect to profile page after login
#         else:
#             messages.error(request, "Invalid username or password")
#             return render(request, 'login.html')
#     return render(request, 'login.html')

# def logout_view(request):
#     user = request.user
#     logout(request)
#     send_mail(
#         'Logout Notification',
#         'You have logged out, {}!'.format(user.first_name),
#         'your_email@example.com',
#         [user.email],
#         fail_silently=False,
#     )
#     return redirect('login')

# # @login_required
# # def profile_view(request):
# #     return render(request, 'profile.html')

# @login_required
# def profile_view(request):
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         email = request.POST['email']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']

#         user = request.user
#         user.first_name = first_name
#         user.last_name = last_name
#         user.email = email

#         if password1 and password1 == password2:
#             user.set_password(password1)
#         elif password1:
#             messages.error(request, "Passwords do not match")
#             return redirect('profile')

#         user.save()
#         messages.success(request, "Profile updated successfully")
#         return redirect('profile')

#     return render(request, 'profile.html')






from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def signup_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return render(request, 'signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return render(request, 'signup.html')

        # if User.objects.filter(email=email).exists():
        #     messages.error(request, "Email already registered")
        #     return render(request, 'signup.html')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1,
            first_name=first_name,
            last_name=last_name
        )
        login(request, user)
        
        send_mail(
            'Welcome to MR Collections',
            f'Thank you,{first_name}, for signing up !',
            'settings.EMAIL_HOST_USER',
            [email],
            fail_silently=False,
        )
        
        return redirect('profile')
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            send_mail(
                'Login Notification',
                f'You have logged in, {user.first_name}!',
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )
            return redirect('profile')
        else:
            messages.error(request, "Invalid username or password")
            print("Invalid credentials") # Moved here
            return render(request, 'login.html')
    return render(request, 'login.html')


# @login_required
# def profile_view(request):
#      return render(request, 'profile.html')

def logout_view(request):
    user = request.user
    logout(request)
    send_mail(
        'Logout Notification',
        f'You have logged out, {user.first_name}!',
        settings.EMAIL_HOST_USER,
        [user.email],
        fail_silently=False,
    )
    return redirect('login')

def profile_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 and password1 == password2:
            user.set_password(password1)
        
        user.save()
        messages.success(request, "Profile updated successfully")
        return redirect('profile')
    
    return render(request, 'profile.html')

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib import messages

CustomUser = get_user_model()

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Üyeliğiniz başarıyla oluşturuldu, {username}!')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

def last_samurai_detay(request):
    # Burada "The Last Samurai" filmine ait detayları alabilir ve gösterebilirsiniz.
    # Örneğin, film adını, açıklamasını, görüntüsünü vb. alabilirsiniz.
    return render(request, 'last_samurai_detay.html')
def color_purple(request):
    return render(request,'purple.html')
def the_place(request):
    return render(request,'the_place.html')
def about_us(request):
    return render(request,'about_us.html')
def index(request):
    return render(request,'index.html')
def filmler(request):
    return render(request,'filmler.html')
def top_gun(request):
    return render(request,'top_gun.html')
def bythesea(request):
    return render(request,'bythesea.html')
def flower_moon(request):
    return render(request,'flower_moon.html')
def the_father(request):
    return render(request,'the_father.html')
def Australia(request):
    return render(request,'Australia.html')
def basterdan(request):
    return render(request,'basterdan.html')
def carlito(request):
    return render(request,'carlito.html')
def a_separation(request):
    return render(request,'a_separation.html')
def requim(request):
    return render(request,'requim.html')
def godfather(request):
    return render(request,'godfather.html')
def titanic(request):
    return render(request,'titanic.html')
def dark_knight(request):
    return render(request,'dark_knight.html')
def matrix(request):
    return render(request,'matrix.html')
def gladiator(request):
    return render(request,'gladiator.html')
def troy(request):
    return render(request,'troy.html')
def action(request):
    return render(request,'action.html')
def dram(request):
    return render(request,'dram.html')
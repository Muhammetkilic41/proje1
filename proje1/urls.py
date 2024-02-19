from django.contrib import admin
from django.urls import path
from appMy import views  # appMy uygulamasından views modülünü içe aktarın
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Ana sayfa
    path('login/', views.login, name='login'),  # Giriş yapma sayfasının URL'si
    path('register/', views.register, name='register'),  # Üye olma sayfasının URL'si
    path('film_detay/last_samurai/', views.last_samurai_detay, name='last_samurai_detay'),
    path('film_detay/the_color_purple/',views.color_purple,name='purple'),
    path('film_detay/the_place/',views.the_place,name='the_place'),
    path('about_us/',views.about_us,name='about_us'),
    path('ana_Sayfa/',views.index,name='index'),
    path('filmler/', views.filmler, name='filmler'),
    path('film_detay/top_gun/',views.top_gun,name='top_gun'),
    path('film_detay/bythesea/',views.bythesea,name='bythesea'),
    path('film_detay/flower_moon/',views.flower_moon,name='flower_moon'),
    path('film_detay/the_father/',views.the_father,name='the_father'),
    path('film_detay/Australia/',views.Australia,name='Australia'),
    path('film_detay/basterdan/',views.basterdan,name='basterdan'),
    path('film_detay/carlito/',views.carlito,name='carlito'),
    path('film_detay/a_separation/',views.a_separation,name='a_separation'),
    path('film_detay/requim/',views.requim,name='requim'),
    path('film_detay/godfather/',views.godfather,name='godfather'),
    path('film_detay/titanic/',views.titanic,name='titanic'),
    path('film_detay/dark_knight/',views.dark_knight,name='dark_knight'),
    path('film_detay/matrix/',views.matrix,name='matrix'),
    path('film_detay/gladiator/',views.gladiator,name='gladiator'),
    path('film_detay/troy/',views.troy,name='troy'),
    path('film_detay/action/',views.action,name='action'),
    path('film_detay/dram/',views.dram,name='dram'),
     path('accounts/', include('django.contrib.auth.urls')),
  
] 


from django.contrib import admin
from django.urls import path
from django.core.mail import send_mail
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bands/', views.band_list, name='band-list'),
    path('about-us/', views.about, name='about-us'),
    path('contact-us/', views.contact, name='contact-us'),
    path('email/', views.send_mail, name='email-sent'),
    path('listings/', views.listings,name='list'),
    path("bands/<int:band_id>/",views.band_detail, name='band-detail'),
    path('listings/<int:id>', views.listing_detail, name = 'list-detail'),
    path('bands/<int:id>/change', views.band_update, name = 'band-update'),
    path('bands/add/', views.band_create, name = 'band-create'),
    path('bands/<int:id>/delete', views.band_delete, name = 'band-delete'),
]

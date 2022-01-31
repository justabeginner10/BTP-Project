from django.urls import path
from . import views

urlpatterns = [
    # path('', views.main, name='main'),
    path('doctorProfile/', views.doctorProfile, name='doctorProfile'),
    # path('services/', views.services, name='services'),
    # path('about/', views.about, name='about'),
    # path('doctors/', views.doctors, name='doctors'),
    path('doctorRegister/<str:pk>/', views.doctorRegister, name='doctorRegister'),
    path('doctorRegister2/<str:pk>/', views.doctorRegister2, name='doctorRegister2'),
    path('doctorRegister3/<str:pk>/', views.doctorRegister3, name='doctorRegister3'),

    path('doctorLogin/', views.doctorLogin, name='doctorLogin'),
    
    # path('contact/', views.contact, name='contact'),
    # path('bookAppointment/', views.bookAppointment, name='bookAppointment'),
    # path('review/', views.review, name='review'),
    # path('blogs/', views.blogs, name='blogs'),
    # path('login/', views.login, name='login'),
    
    
]




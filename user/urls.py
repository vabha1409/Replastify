from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact_form, name="Contact"),
    path('services/', services, name='services'),
    path('servicesdetails/', servicesdetails, name='servicesdetails'),
    path('servicesdetails1/', servicesdetails1, name='servicesdetails1'),
    path('servicesdetails2/', servicesdetails2, name='servicesdetails2'),
    path('servicesdetails3/', servicesdetails3, name='servicesdetails3'),
    path('servicesdetails4/', servicesdetails4, name='servicesdetails4'),
    path('servicesdetails5/', servicesdetails5, name='servicesdetails5'),
    path('replastform/', service_form, name='service_form'),
    path('collect/',collect_form, name='collect_form'),
    path('subscribe/', subscribe_form, name='subscribe_form'),
    path('projects/', projects, name="projects"),
    path('blog/', blog,name ='blog'),
    path('blogdetails/', blogdetails, name='blogdetails'),
    path('projectdetails/', projectdetails, name='projectdetails'),
    path('signup/',signup, name='signup'),
    path('login/',loginpage, name='login'),
    path('logout/',logoutpage, name='logout'),
    path('voice_search/', voice_search, name='voice_search'),
    path('dynamic_theme/', dynamic_theme, name='dynamic_theme'),
#blog
    path('blogdetails2/', blogdetails2, name='blogdetails2'),
    path('blogdetails3/', blogdetails3, name='blogdetails3'),
    path('blogdetails4/', blogdetails4, name='blogdetails4'),
    path('blogdetails5/', blogdetails5, name='blogdetails5'),
    path('blogdetails6/', blogdetails6, name='blogdetails6'),



    # path('translate/', translate_text, name='translate_text'),

]
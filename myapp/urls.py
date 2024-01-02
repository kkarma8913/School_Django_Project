from django.urls import path
from .models import *
from .import views

urlpatterns = [
    path('',views.home,name='home'),
  
    path('about',views.about,name='about'),
    path('applyad',views.applyad,name='applyad'),
    path('feestr',views.show_fees,name='feestr'),
   
    path('nco',views.nco,name='nco'),
    
    
    path('ttpg',views.ttpg,name='ttpg'),
    path('do',views.do,name='do'), 
    path('feed',views.feed,name='feed'),
    path('contact',views.contact,name='contact'),

   
    path('signup',views.sign_up,name='signup'),
    path('login',views.log_in,name='login'),
    path('logout',views.log_out,name='logout'),
    path('kg1',views.kg1,name='kg1'),
    path('kg2',views.kg2,name='kg2'),
    path('showfees',views.show_fees,name='showfees'),
    path('img',views.show_img,name='img'),
       path('pgc',views.show_plyg,name='pgc'),
       path('tt',views.show_tt_play,name='tt')
     

]

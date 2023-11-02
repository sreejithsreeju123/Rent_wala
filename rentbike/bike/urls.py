
from .import views
from django.urls import path
from.views import Homepage,detail,booknow,car_view,detail_car,carbook,BikeAndCarSearchView,Notavailable
urlpatterns = [
    path('',Homepage.as_view(),name='home'),
    path('two__wheeler/', views.two_wheeler_view,name='twowheeler'),
    path('honda/',views.honda_vech,name='honda'),
    path('tvs/',views.tvs_vech,name='tvs'),
    path('yamaha/',views.yamaha_vech,name='yamaha'),
    path('hero/',views.hero_vech,name='hero'),
    path('enfield/',views.enfield_vech,name='enfield'),
    path('suzuki/',views.suzuki_vech,name='suzuki'),
    path('detail/<int:pk>/',detail.as_view(),name='detailpage'),
    path('payment/<int:pk>/',booknow.as_view(),name='payment'),
    path('toprated/',views.Top_rated,name='toprated'),
    path('newvech/',views.new_vech,name='newvech'),
    path('carlist/',car_view.as_view(),name='carlist'),
    path('maruthi/',views.maruthi_view,name='maruthi'),
    path('hyundai/',views.hyunadi_view,name='hyundai'),
    path('tata/',views.tata_views,name='tata'),
    path('kia/',views.kia_views,name='kia'),
    path('toyoto/',views.toyoto_views,name='toyoto'),
    path('renualt/',views.renualt_views,name='renualt'),
    path('detail-car/<int:pk>/',detail_car.as_view(),name='detailcar'),
    path('payment_car/<int:pk>/',carbook.as_view(),name='car_payment'),
    path('bike_and_car_search/', BikeAndCarSearchView.as_view(), name='bike-and-car-search'),
    path('notavailable/',Notavailable.as_view(),name='notavailable'),
    path('contact/',views.contact_form,name='contact'),
    
   
    
   
     
    

    
    
   
]

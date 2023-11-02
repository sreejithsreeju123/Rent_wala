from django.shortcuts import render,redirect,get_list_or_404
from django.views.generic import ListView,DetailView
from.models import bike,car,contact
import random
from django.db.models import Q
from django.http import HttpResponse


# Create your views here.
class Homepage(ListView):
    model=bike
    template_name='home.html'

def two_wheeler_view(request):
    two_wheelr = bike.objects.all()
    return render(request, 'twowheeler.html', {'object': two_wheelr})

def honda_vech(request):
    honda_vechile=bike.objects.filter(maker="HONDA",rating__gt=8)
    honda=bike.objects.filter(maker='HONDA')
    return render(request,'honda.html',{'object':honda,'honda_vechile':honda_vechile})

def tvs_vech(request):
    tvs_vehicles = bike.objects.filter(maker="TVS", rating__gt=8)
    all_vehicles = bike.objects.filter(maker="TVS")
    return render(request, 'tvs.html',{'tvs_vehicles': tvs_vehicles,'all_vehicles': all_vehicles,})

def yamaha_vech(request):
    yamaha_vechile=bike.objects.filter(maker='YAMAHA',rating__gt=8)
    all_vechile=bike.objects.filter(maker="YAMAHA")
    return render(request,'yamaha.html',{'yamaha_vechile':yamaha_vechile,'all_vechile':all_vechile,})

def hero_vech(request):
    hero_vechile=bike.objects.filter(maker='HERO',rating__gt=8)
    all_vechile=bike.objects.filter(maker="HERO")
    return render(request,'hero.html',{'hero_vechile':hero_vechile,'all_vechile':all_vechile,})

def enfield_vech(request):
    enfield_vechile=bike.objects.filter(maker='ENFIELD',rating__gt=8)
    all_vechile=bike.objects.filter(maker="ENFIELD")
    return render(request,'enfield.html',{'enfield_vechile':enfield_vechile,'all_vechile':all_vechile,})

def suzuki_vech(request):
    suzuki_vechile=bike.objects.filter(maker='SUZUKI',rating__gt=8)
    all_vechile=bike.objects.filter(maker="SUZUKI")
    return render(request,'suzuki.html',{'enfield_vechile':suzuki_vechile,'all_vechile':all_vechile,})

def Top_rated(request):
    top_bike=bike.objects.filter(rating__gt=8)
    top_car=car.objects.filter(rating__gt=8)
    return render(request,'toprated.html',{'object':top_bike,'top_car':top_car})


class detail(DetailView):
    model=bike
    template_name='detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_bike = context['object']
        all_vehicles = bike.objects.all()
        other_vehicles = all_vehicles.exclude(pk=current_bike.pk)
        random_vehicles = random.sample(list(other_vehicles),5)
        context['random_vehicles'] = random_vehicles
        return context


class booknow(DetailView):
    model=bike
    template_name='payment.html'
    
        
class car_view(ListView):
    model=car
    template_name='carlist.html'
    
def maruthi_view(request):
    maruthi_vec=car.objects.filter(maker='MARUTHI', rating__gt=8)
    all_vech=car.objects.filter(maker='MARUTHI')
    return render(request,'maruthi.html',{'maruthi_vechile':maruthi_vec,'all_vechile':all_vech,})

def hyunadi_view(request):
    hyundai_vech=car.objects.filter(maker='HYUNDAI', rating__gt=8)
    all_vech=car.objects.filter(maker='HYUNDAI')
    return render(request,'hyundai.html',{'hyundai_vech':hyundai_vech,'all_vechile':all_vech,})

def tata_views(request):
    tata_vech=car.objects.filter(maker='TATA', rating__gt=8)
    all_vech=car.objects.filter(maker='TATA')
    return render(request,'tata.html',{'tata_vech':tata_vech,'all_vechile':all_vech,})

def kia_views(request):
    kia_vech=car.objects.filter(maker='KIA', rating__gt=8)
    all_vech=car.objects.filter(maker='KIA')
    return render(request,'kia.html',{'kia_vech':kia_vech,'all_vechile':all_vech,})

def toyoto_views(request):
    toyoto_vech=car.objects.filter(maker='TOYOTO', rating__gt=8)
    all_vech=car.objects.filter(maker='TOYOTO')
    return render(request,'toyoto.html',{'toyoto_vech':toyoto_vech,'all_vechile':all_vech,})

def renualt_views(request):
    renualt_vech=car.objects.filter(maker='RENAULT', rating__gt=8)
    all_vech=car.objects.filter(maker='RENAULT')
    return render(request,'renault.html',{'renault_vech':renualt_vech,'all_vechile':all_vech,})

def new_vech(request):
    two_vech=bike.objects.filter(yearofproduction__gt=2022)
    four_vech=car.objects.filter(yearofproduction__gt=2022)
    return render(request,'newvech.html',{'two_vech':two_vech,'four_vech':four_vech,})


class detail_car(DetailView):
    model=car
    template_name='detail_car.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_car = context['object']
        all_vehicles = car.objects.all()
        other_vehicles = all_vehicles.exclude(pk=current_car.pk)
        random_vehicles = random.sample(list(other_vehicles),5)
        context['random_vehicles'] = random_vehicles
        return context
    
class carbook(DetailView):
    model=car
    template_name='payment_car.html'
    
    
class SearchView(ListView):
    template_name = 'search.html'
    context_object_name = 'search_results'
    models = []

    def get_queryset(self):
        query = self.request.GET.get('q')
        search_results = {}

        for model in self.models:
            results = model.objects.filter(
                Q(maker__icontains=query) |
                Q(vechile_name__icontains=query) |
                Q(cc__icontains=query) |
                Q(yearofproduction__icontains=query)
            )
            search_results[model.__name__.lower()] = results

        return search_results

class BikeAndCarSearchView(SearchView):
    models = [bike, car]
    
    
class Notavailable(ListView):
    model=car
    template_name='notavailable.html'
    
def contact_form(request):
    if request.method=='POST':
        contact1=contact()
        name=request.POST.get('name')
        last_name=request.POST.get('lastname')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        contact1.name=name
        contact1.last_name=last_name
        contact1.email=email
        contact1.subject=subject
        contact1.save()
        return HttpResponse('<h1>THANKS FOR CONTACTING US OUR TEAM WILL CONTACT YOU SHORTALLY.HAVE A NICE DAY!!!!!</h1>')
    return render(request,'subscribe.html')








    

        



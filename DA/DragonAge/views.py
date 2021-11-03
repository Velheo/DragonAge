from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Q
from django.http import HttpResponseRedirect
from .models import *



# Create your views here.
def index(request):
    context={
        'g_game':Game.objects.all(),
    }
    return render(request, 'DA/index.html', context)
class GameDetailView(DetailView):
    model = Game
    template_name='DA/game_detail.html'
    context_object_name ='game'
#def game_detail(request,pk):
#    game=Game.objects.get(pk=pk)
#    context={
#        'game': game,
#    }
 #   return render(request,'DA/game_detail.html', context)
#def race_list(request):
#    race=Race.objects.all()
 #   context={
 #       'race': race,
 #   }
 #   return render(request,'DA/race_list.html', context)
class RaceListView(ListView):
    model = Race
    template_name = 'DA/race_list.html'
    context_object_name = 'race'

#def clasess_list(request):
#    classes=Classes.objects.all()
#    context={
 #       'classes': classes,
#    }
#    return render(request,'DA/clasess_list.html', context)
class ClasessListView(ListView):
    model = Classes
    template_name = 'DA/clasess_list.html'
    context_object_name = 'class'

#def Locations_list(request):
#    locations=Locations.objects.all()
 #   context={
#        'locations': locations,
 #   }
 #   return render(request,'DA/Locations_list.html', context)
class LocationsListView(ListView):
    model = Locations
    template_name = 'DA/Locations_list.html'
    context_object_name = 'locations'
def Companion_list(request):
    companions=Companion.objects.all()
    context={
        'companion': companions,
    }
    return render(request,'DA/Companion_list.html', context)
#class CompanionListView(ListView):
#    model = Companion
 #   context_object_name = 'companions'
#def Companion_detail(request):
#    companions=Companion.objects.get(pk=pk)
 #   context={
 #       'companion': companions,
 #   }
 #   return render(request,'DA/Companion_detail.html', context)
class CompanionDetailView(DetailView):
    model = Companion
    template_name = 'DA/Companion_detail.html'
    context_object_name = 'companion'

def search(request):
    string=request.POST.get('search')
    if string:
        context={
            'string': string,
            'classes': Classes.objects.filter(first__icontains=string),
            'race': Race.objects.filter(last__icontains=string),
            'companion': Companion.objects.filter(imy__icontains=string),
            'game':Game.objects.filter(name__icontains=string),
        }
        return render(request, 'DA/search.html', context)
    else:
        return HttpResponseRedirect(reverse('DragonAge:index'))
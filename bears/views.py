from django.shortcuts import render, get_object_or_404
from .models import Bear, Sighting

def bear_list(request):
    bears = Bear.objects.all()
    return render(request, 'bear_list.html', {'bears' : bears})

def bear_detail(request, id):
    bear = get_object_or_404(Bear, id=id)
    return render(request, 'bear_detail.html', {'bear' : bear})

def bear_status(request, id):
    bears_status = get_object_or_404(Sighting)
    return render(request, 'bear_status.html', {'bears_status' : bears_status})

# Create your views here.

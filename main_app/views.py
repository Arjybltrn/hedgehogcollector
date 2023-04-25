from django.shortcuts import render, redirect
# Add the following import
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Hedgehog
from .forms import FeedingForm


# Create your views here.

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')


def hedgehogs_index(request):
  hedgehogs = Hedgehog.objects.all()
  return render(request, 'hedgehogs/index.html', {'hedgehogs': hedgehogs })

def hedgehogs_detail(request, hedgehog_id):
  hedgehog = Hedgehog.objects.get(id=hedgehog_id)
  feeding_form = FeedingForm()
  return render(request, 'hedgehogs/detail.html', { 'hedgehog': hedgehog, 'feeding_form':feeding_form })

def add_feeding(request, hedgehog_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.hedgehog_id = hedgehog_id
    new_feeding.save()
  return redirect('detail', hedgehog_id=hedgehog_id)


class HedgehogCreate(CreateView):
  model = Hedgehog
  fields = '__all__'

class HedgehogUpdate(UpdateView):
  model = Hedgehog
  fields = ['breed', 'description', 'age']

class HedgehogDelete(DeleteView):
  model = Hedgehog
  success_url = '/hedgehogs/'
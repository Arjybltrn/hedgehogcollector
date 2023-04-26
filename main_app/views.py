from django.shortcuts import render, redirect
# Add the following import
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Hedgehog, Toy
from .forms import FeedingForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

@login_required
def hedgehogs_index(request):
  hedgehogs = Hedgehog.objects.filter(user=request.user)
  return render(request, 'hedgehogs/index.html', {'hedgehogs': hedgehogs })

@login_required
def hedgehogs_detail(request, hedgehog_id):
  hedgehog = Hedgehog.objects.get(id=hedgehog_id)
  toys_hedgehog_doesnt_have = Toy.objects.exclude(id__in = hedgehog.toys.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'hedgehogs/detail.html', { 'hedgehog': hedgehog, 'feeding_form':feeding_form, 'toys': toys_hedgehog_doesnt_have })

@login_required
def add_feeding(request, hedgehog_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.hedgehog_id = hedgehog_id
    new_feeding.save()
  return redirect('detail', hedgehog_id=hedgehog_id)

@login_required
def assoc_toy(request, hedgehog_id, toy_id):
  # Note that you can pass a toy's id instead of the whole object
  Hedgehog.objects.get(id=hedgehog_id).toys.add(toy_id)
  return redirect('detail', hedgehog_id=hedgehog_id)

@login_required
def remove_toy(request, hedgehog_id, toy_id):
  Hedgehog.objects.get(id=hedgehog_id).toys.remove(toy_id)
  return redirect('detail', hedgehog_id=hedgehog_id)


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)



class HedgehogCreate(LoginRequiredMixin, CreateView):
  model = Hedgehog
  fields = ('name', 'breed', 'description', 'age')

  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the hedgehog
    # Let the CreateView do its job as usual
    return super().form_valid(form)

class HedgehogUpdate(LoginRequiredMixin, UpdateView):
  model = Hedgehog
  fields = ['breed', 'description', 'age']

class HedgehogDelete(LoginRequiredMixin, DeleteView):
  model = Hedgehog
  success_url = '/hedgehogs/'

# <---- Toys Classes ---->

class ToysIndex(LoginRequiredMixin, ListView):
  model = Toy

class ToysDetail(LoginRequiredMixin, DetailView):
  model = Toy

class ToyCreate(LoginRequiredMixin, CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(LoginRequiredMixin, UpdateView):
  model = Toy
  fields = '__all__'

class ToyDelete(LoginRequiredMixin, DeleteView):
  model = Toy
  success_url = '/toys/'
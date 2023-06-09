from django.db import models
from django.urls import reverse
# Create your models here.
from datetime import date
from django.contrib.auth.models import User

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.color} {self.name}'

    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'pk': self.id})

class Hedgehog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    toys = models.ManyToManyField(Toy)

    user = models.ForeignKey(User, on_delete=models.CASCADE)


	# new code below
    def __str__(self):
        return f'{self.name}'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'hedgehog_id': self.id})
    
    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)
    

class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=MEALS,
    # set the default value for meal to be 'B'
    default=MEALS[0][0]
  )
    # Create a hedgehog_id FK ( the many is going to hav the FK )
    hedgehog = models.ForeignKey(Hedgehog, on_delete=models.CASCADE)

    def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_meal_display()} on {self.date}"
    class Meta:
        ordering = ['-date']  

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('hedgehogs/', views.hedgehogs_index, name='index'), #index
    path('hedgehogs/<int:hedgehog_id>/', views.hedgehogs_detail, name='detail'), # show
    path('hedgehogs/create/', views.HedgehogCreate.as_view(), name='hedgehogs_create'), #create form
    path('hedgehogs/<int:pk>/update/', views.HedgehogUpdate.as_view(), name='hedgehogs_update'), #edit
    path('hedgehogs/<int:pk>/delete/', views.HedgehogDelete.as_view(), name='hedgehogs_delete'), # delete
    path('hedgehogs/<int:hedgehog_id>/add_feeding/', views.add_feeding, name='add_feeding'), #add feeding path
]
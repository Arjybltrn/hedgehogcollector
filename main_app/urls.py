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
    path('hedgehogs/<int:hedgehog_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'), # associate a toy with a hedgehog (M:M)
    path('hedgehogs/<int:hedgehog_id>/remove_toy/<int:toy_id>/', views.remove_toy, name='remove_toy'), #remove a toy from a hedgehog(m:m)
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'), #toy_form
    path('toys/', views.ToysIndex.as_view(), name='toys_index'), #toy_list
    path('toys/<int:pk>/', views.ToysDetail.as_view(), name='toys_detail'), #toy_detail
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'), #toy form edit
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'), #toy delete
]
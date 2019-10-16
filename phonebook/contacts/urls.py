from django.urls import path
from . import views

urlpatterns = [
    path('', views.all, name="allcontacts"),
    path('add_contact', views.add_contacts, name="contacts"),
    path('<int:pk>', views.details, name="details"),
    path('<int:pk>/update', views.update, name="update"),
    path('search', views.search, name='search'),
    path('<int:pk>/delete', views.delete, name='delete')

]

from django.urls import path
from .views import ListPeopleView, AddPersonView, PeopleAPI, DeletePeople
from .views import DeletePeople

urlpatterns = [
    path('', AddPersonView.as_view(), name='add'),
    path('add/', ListPeopleView.as_view(), name='lista'),
    path('api/', PeopleAPI.as_view(), name='api'),
    path('api/usuarios/<int:pk>/delete/',DeletePeople, name='delete'),
]

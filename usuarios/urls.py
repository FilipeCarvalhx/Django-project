from django.urls import path
from .views import ListPeopleView, AddPersonView, PeopleAPI, DeletePeople
from .views import DeletePeople

urlpatterns = [
    path('', ListPeopleView.as_view(), name='lista'),
    path('add/', AddPersonView.as_view(), name='add'),
    path('api/', PeopleAPI.as_view(), name='api'),
    path('api/usuarios/<int:pk>/delete/', DeletePeople.as_view(), name='delete'),
]

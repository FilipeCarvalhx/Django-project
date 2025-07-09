from django.shortcuts import render, redirect
from django.views import View
from rest_framework.views import APIView
from .models import Usuario
from .forms import PersonForm
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse


class ListPeopleView(View):
    def get(self, request):
        people = Usuario.objects.all()
        return render(request, 'usuarios/list.html', {'people': people})

class AddPersonView(View):
    def get(self, request):
        form = PersonForm()
        return render(request, 'usuarios/form.html', {'form': form})

    def post(self, request):
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista')
        return render(request, 'usuarios/form.html', {'form': form})


class PeopleAPI(View):
    def get(self, request):
        people = list(Usuario.objects.values('nome', 'idade', 'email'))
        return JsonResponse(people, safe=False)


def DeletePeople(request, pk):
    pessoa = get_object_or_404(Usuario, pk=pk)
    pessoa.delete()
    return redirect("lista")
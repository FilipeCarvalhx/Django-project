from django.shortcuts import render, redirect
from django.views import View
from .models import Person
from .forms import PersonForm
from django.http import JsonResponse

class ListPeopleView(View):
    def get(self, request):
        people = Person.objects.all()
        return render(request, 'pessoas/lista.html', {'people': people})

class AddPersonView(View):
    def get(self, request):
        form = PersonForm()
        return render(request, 'pessoas/form.html', {'form': form})

    def post(self, request):
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista')
        return render(request, 'pessoas/form.html', {'form': form})

class PeopleAPI(View):
    def get(self, request):
        people = list(Person.objects.values('name', 'age'))
        return JsonResponse(people, safe=False)

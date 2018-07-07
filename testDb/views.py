from django.shortcuts import render
from testDb.form import UserForm

from testDb.models import Person

# Create your views here.
def User(request):
    if not request.POST:
        form = UserForm
        
        return render(request, 'user.html', {
            "form": form,
            "ary": [],
        })

    if 'userSearch' in request.POST:
        form = UserForm(request.POST)
        q = Person.objects.all()

        # q.filter(name='aaa')

        ary = []
        for data in q:
            ary.append(data)
            print(data)
        
        return render(request, 'user.html', {
            "form": form,
            "ary": ary,
        })

    if 'userAdd' in request.POST:
        form = UserForm(request.POST)

        if not form.is_valid():
            return render(request, 'user.html', {
                "form": form,
                "ary": [],
            })

        name = form.cleaned_data['name']
        age = form.cleaned_data['age']

        q = Person.objects.create(
            name = name,
            age = age,
        )

        return render(request, 'user.html', {
            "form": form,
            "ary": [],
        })
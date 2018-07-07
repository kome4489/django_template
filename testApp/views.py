from django.shortcuts import render
from testApp.form import SearchForm

from testApp.models import Person, Category

# Create your views here.
def home(request):
    if not request.POST:
        form = SearchForm

        # q = Person.objects.all()

        # q.filter(name='aaa')

        # totalNum = q.count()

        # ary = []
        # for data in q:
        #     ary.append(data.modelname)
        
        # print(ary)

        q = Person.objects.create(
            name = 'aaa',
            age = 11,
        )
        
        return render(request, 'home.html', {
            "form": form,
        })

    if request.POST:
        context = {
            "aaa": "bbb",
        }
        form = SearchForm(request.POST)

        if not form.is_valid():


            return render(request, 'home.html', {
                "form": form,
            })

        a = form.cleaned_data['a']
        b = form.cleaned_data['b']
        sum = a + b

        data = {
            "a": a,
            "b": b,
            "sum": sum,
        }

        print(data)
        print(data)

        form = SearchForm(data)

        return render(request, 'home.html', {
            "form": form,
        })
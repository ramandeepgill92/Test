from django.shortcuts import render

# Create your views here.
def home(request):
    marks = [1,2,3,4,5,6,7,8,9,10]
    context = {
        'marks':marks,
        'name': 'Raman'
    }
    return render(request, 'index.html', context)
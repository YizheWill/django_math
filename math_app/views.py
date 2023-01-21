from django.shortcuts import render
from math_app.forms import ZScoreForm

# Create your views here.


def index(request):
    return render(request, 'math_app/index.html')


def zscore(request):
    if request.method == 'POST':
        print(request.POST)
        mean = float(request.POST['mean'])
        std = float(request.POST['std'])
        val = float(request.POST['val'])
        z = (val - mean) / std
        return render(request, 'math_app/zscore.html', {'mean': mean, 'std': std, 'val': val, 'z': z})
    else:
        return render(request, 'math_app/zscore.html', {'mean': '', 'std': '', 'val': '', 'z': ''})


def binom(request):
    return render(request, 'math_app/binom.html')


def clt(request):
    return render(request, 'math_app/clt.html')


def hp_testing(request):
    return render(request, 'math_app/hp_testing.html')

from django.urls import path
from math_app.views import index, zscore, binom, clt, hp_testing

urlpatterns = [
    path('', index, name='index'),
    path('zscore', zscore, name='zscore'),
    path('binom', binom, name='binom'),
    path('clt', clt, name="clt"),
    path('hp_testing', hp_testing, name='hp_testing)
]

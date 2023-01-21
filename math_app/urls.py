from django.urls import path
from math_app.views import index, zscore, binom, clt

urlpatterns=[
    path('', index, name='index'),
    path('zscore', zscore, name='zscore'),
    path('binom', binom, name='binom'),
    path('clt', clt, name="clt")
]
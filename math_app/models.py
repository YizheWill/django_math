import scipy
import numpy as np
import matplotlib.pyplot as plt
from django.db import models
from django.conf import settings
from scipy.stats import norm, binom, iqr
from numpy.random import seed
from numpy.random import normal

# Create your models here.
class Calculations(models.Model):
  title = models.CharField(max_length=200)
  formula = models.CharField(max_length=200)

class Zscore(models.Model):
  mean = models.FloatField()
  std = models.FloatField()
  val = models.FloatField()
  z = models.FloatField()

  def calc_z(self):
    self.z = (self.val - self.mean) / self.std
    return self.z
  


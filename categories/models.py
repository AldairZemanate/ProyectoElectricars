from pyexpat import model
from statistics import mode
from turtle import update
from unittest.mock import create_autospec
from django.db import models
from django.utils.translation import gettext_lazy as _
from products.models import Product

# Create your models here.
class Category(models.Model):
    name=models.CharField(_('Nombre'),max_length=20)
    create_at=models.CharField(_('Creacion'))
    update_at=models.DateTimeField(_('Fecha actualizacion'))
    product= models.ManyToOneRel(Product)
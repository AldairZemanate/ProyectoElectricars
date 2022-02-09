from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.reverse_related import ManyToOneRel
from django.utils.translation import gettext_lazy as _
from graphene.types.structures import NonNull
# Create your models here.
class Product(models.Model):
    prod_name= models.CharField(_('nombre'), max_length=30)
    prod_count=models.IntegerField(_('cantidad'),blank=True)
    prod_description= models.CharField(_('descripcion'),max_length=200)
    prod_image_url=models.ImageField(_('imagen'),null=True,blank=True)
    prod_trademark=models.CharField(_('marca'), max_length=30,blank=True)
    prod_warranty=models.CharField(_('garantia'), max_length=10,blank=True)
    prod_tutorial_url=models.CharField(max_length=30,null=True,blank=True)
    prod_creat_at=models.DateField(auto_now=True)
    prod_is_active=models.BooleanField(_('activo'))
    prod_discount=models.IntegerField()

    class Meta:
        verbose_name=_('producto')
        verbose_name_plural=_('productos')
    
    def __str__(self):
        return self.prod_name

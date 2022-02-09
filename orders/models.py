from django.db import models
from django.db.models.base import Model, ModelBase
from django.db.models.deletion import CASCADE
from django.utils import translation, tree
from django.utils.translation import gettext_lazy as _
from products.models import Product
from users.models import User
# Create your models here.

class Order(models.Model):
    state_Choises=[
        ('1','unconfirmed'),
        ('2','confirmed'),
        ('3','cancelled'),
        ('4','dispatched'),
        ('5','delivered'),
    ]
    user_id=models.ForeignKey(User,on_delete=CASCADE,blank=True, null=False)
    ord_date=models.DateField(auto_now=True)
    ord_state=models.CharField(_('estado'),max_length=30,choices=state_Choises)
    ord_total=models.IntegerField()
    #personalizacion tasbla intermedia
    ord_product=models.ManyToManyField(Product,blank=True,through='OrderProduct')
    
    class Meta:
        verbose_name=_('orden')
        verbose_name_plural=_('ordenes')

    def __str__(self):
        return self.ord_state
class OrderProduct(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE,blank=True,null=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)
    quantity=models.IntegerField()
    
    class Meta:
        verbose_name=_('OrdenProducto')
        verbose_name_plural=_('OrdenesProductos')
    
    def __str__(self):
        return str(self.quantity)
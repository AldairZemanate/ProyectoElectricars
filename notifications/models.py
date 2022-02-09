from typing import Callable
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from orders.models import Order
from users.models import User

from django.utils.translation import gettext_lazy as _
# Create your models here.
class Notification(models.Model):
    not_date= models.DateField(auto_now=True)
    not_title=models.CharField(_('Titulo_Notificacion'), max_length=100)
    not_body=models.CharField(_('cuerpo_notificacion'),max_length=100)
    ord_id=models.ForeignKey(Order,on_delete=CASCADE, blank=True,null=False)
    user_id=models.ForeignKey(User,on_delete=CASCADE,blank=True,null=False)

    class Meta:
        verbose_name=_('notificacion')
        verbose_name_plural=_('notificaciones')
    
    def __str__(self) :
        return self.not_title
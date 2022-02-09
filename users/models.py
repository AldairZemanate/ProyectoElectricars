from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class User(models.Model):
    type_choices=(
        ('1','client'),
        ('2','manager'),
    )
    user_name= models.CharField(_('nombre'), max_length=30)
    user_lastname=models.CharField(_('apellido'),max_length=30)
    user_birthday=models.DateField(_('cumpleaños'))
    user_address=models.CharField(_('direccion'),max_length=64)
    user_email= models.EmailField()
    user_password=models.CharField(_('contraseña'),max_length=20)
    user_ocupation=models.CharField(_('ocupacion'),max_length=40)
    user_type=models.CharField(_('tipo'),max_length=10,choices=type_choices)
    is_active= models.BooleanField()
    creat_at=models.DateField(auto_now=True)

    class Meta:
        verbose_name=_('Usuario')
        verbose_name_plural=_('Usuarios')

    def __str__(self):
        return self.user_name
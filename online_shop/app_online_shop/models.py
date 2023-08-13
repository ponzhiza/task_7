from django.db import models

# Create your models here.

class OnlineShop(models.Model):
    def __str__(self): 
        return f'<Onlineshop: Onlineshop(id={self.id}, title={self.title}, price={self.price})>'

    id = models.CharField('id', max_length=10, primary_key=True)

    title = models.CharField('Заголовок', max_length=128)

    description = models.TextField('Описание')

    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)

    auction = models.BooleanField('Торг', help_text='Отметьте, уместен ли торг')

    creation_time = models.DateTimeField(auto_now_add=True)

    update_time = models.DateTimeField(auto_now=True)

    class Meta: 
        db_table = 'online_shop'

    
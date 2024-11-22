from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Products(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.PositiveIntegerField(verbose_name='Цена')
    icon = models.ImageField(upload_to='icon/', verbose_name='Иконка', **NULLABLE)
    categories = models.CharField(max_length=100, verbose_name='Категория', **NULLABLE)
    available = models.BooleanField(default=True, verbose_name='Доступен')
    rating = models.FloatField(default=0, verbose_name='Рейтинг')

    def __str__(self):
        return f'{self.title, self.description} : {self.price}'

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

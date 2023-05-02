from django.db import models


class Occupation(models.Model):
    """Модель работника."""

    name = models.CharField(max_length=200, verbose_name='Имя')
    company_name = models.CharField(max_length=100, verbose_name='Компания')
    position_name = models.CharField(max_length=100, verbose_name='Должность')
    hire_date = models.DateField(verbose_name='Дата приема')
    fire_date = models.DateField(null=True, verbose_name='Дата увольнения')
    salary = models.IntegerField(verbose_name='Ставка, руб')
    fraction = models.IntegerField(verbose_name='Ставка, %')
    base = models.IntegerField(verbose_name='База')
    advance = models.IntegerField(verbose_name='Аванс')
    by_hours = models.BooleanField(verbose_name='Почасовая оплата')

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

    def __str__(self):
        """Возвращает строковое представление модели."""

        return self.name

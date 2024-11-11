from django.db import models


class Product(models.Model):
    GROUP = [
        ('fruits', 'Фрукты'),
        ('vegetables', 'vegetables'),
        ('meats', 'meats'),
    ]
    code = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    group = models.CharField(max_length=255, choices=GROUP)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f"Название: {self.title} код: {self.code} Группа: {self.group}"


class Storage(models.Model):
    title = models.CharField(max_length=255)
    products = models.ManyToManyField(Product, related_name="storage")

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'

    def __str__(self):
        return self.title

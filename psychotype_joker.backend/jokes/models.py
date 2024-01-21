from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Joke(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    text = models.TextField()

    class Meta:
        verbose_name = 'Анекдот'
        verbose_name_plural = 'Анекдоты'

    def __str__(self):
        return f"{self.category}: {self.text}"

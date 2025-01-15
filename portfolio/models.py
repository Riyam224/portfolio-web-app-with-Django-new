from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


# todo category _____
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        '''Meta definition for Category.'''

        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

    def __str__(self):
        return self.name

class PortfolioItem(models.Model):
    title = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category, related_name='portfolio_items')  # Change to ManyToManyField
    image = models.ImageField(upload_to='portfolio/')

    def __str__(self):
        return self.title

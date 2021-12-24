from django.db import models
from django.utils import timezone


class Categories(models.Model):

    name = models.CharField(verbose_name='Название категории', max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категория для товара'


class Product(models.Model):

    SIZE_CHOICE = (
        ('ph1', 'PH1'),
        ('ph2', 'PH2'),
        ('ph3', 'PH3'),
        ('pz', 'PZ')
    )

    category = models.ForeignKey(Categories, verbose_name='Категория товара', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='Название товара')
    image = models.ImageField()
    slug = models.SlugField()
    description_1 = models.CharField(max_length=255, verbose_name='something1')
    description_2 = models.IntegerField(verbose_name='something2')
    description_3 = models.CharField(max_length=255, verbose_name='something3')
    description_4 = models.IntegerField(verbose_name='something4')
    description_5 = models.CharField(max_length=255, verbose_name='something5', choices=SIZE_CHOICE)
    description_6 = models.IntegerField(verbose_name='something6')
    description_7 = models.CharField(max_length=255, verbose_name='something7')
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Товар | {self.name}, Категория товара | {self.category.name}'

    class Meta:
        verbose_name_plural = 'Основной продукт'


class Products(models.Model):

    product_id = models.ForeignKey(Product, verbose_name='Продукт к которому относитья товар', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='Название товара')
    slug = models.SlugField('Slug для товара')
    image = models.ImageField(verbose_name='Изображение для товара')
    price = models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена товара')
    description_1 = models.CharField(max_length=255, verbose_name='something1')
    description_2 = models.IntegerField(verbose_name='something2')
    description_3 = models.CharField(max_length=255, verbose_name='something3')
    description_4 = models.IntegerField(verbose_name='something4')
    description_5 = models.CharField(max_length=255, verbose_name='something5')
    description_6 = models.IntegerField(verbose_name='something6')
    description_7 = models.CharField(max_length=255, verbose_name='something7')
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return f'Товар | {self.name}, Категория товара | {self.product_id.category.name}'

    class Meta:
        verbose_name_plural = 'Продукты относящиеся с товару'


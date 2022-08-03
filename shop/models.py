from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='Email', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    first_name = models.CharField(max_length=250, verbose_name='Имя')
    last_name = models.CharField(max_length=250, verbose_name='Фамилия')
    address = models.CharField(max_length=250, verbose_name='Адрес', blank=True, null=True)
    phone = models.CharField(max_length=150, verbose_name='Телефон', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email


class Category(models.Model):
    """
    Category of products
    """

    name = models.CharField(max_length=150, verbose_name='Название', unique=True)
    description = models.TextField(max_length=200, verbose_name='Описание')

    class Meta:
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Product in shops
    """

    category = models.ForeignKey(Category, on_delete=models.CASCADE,  related_name='category', verbose_name='Категория')
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    creation_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='products/%y/%m/%d/', blank=True, verbose_name='Изображение')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Скидка', blank=True)
    supplier = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Админ')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title


class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total_price = models.FloatField(blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    is_order = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Корзина'

    def __str__(self):
        return f"Cart {self.id} {self.user}"


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart')
    quantity = models.IntegerField(default=1)
    cart_item_price = models.FloatField(default=0)

    class Meta:
        verbose_name_plural = 'Товары в корзине'

    def __str__(self):
        return f"{self.product} * {self.quantity}"

    def save(self, *args, **kwargs):
        self.cart_item_price = self.quantity * self.product.price
        super().save(*args, **kwargs)


class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total_price = models.FloatField(default=0, blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f"{self.id} {self.user} Total price: {self.total_price}"


class Comment(models.Model):
    rates = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rate = models.IntegerField(choices=rates, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.TextField(blank=True, verbose_name='Содержание')
    creation_date = models.DateTimeField(auto_now_add=True)
    replies = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f"Author: {self.author} Comment: {self.content}"


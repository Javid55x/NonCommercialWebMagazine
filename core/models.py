from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Məhsulun adı')
    mehsulun_kodu = models.CharField(max_length=20, verbose_name='Məhsulun kodu')
    date = models.DateTimeField(auto_now=True)
    alt_dolap_eni = models.CharField(max_length=10, verbose_name='Alt şkafın eni')
    alt_dolap_hundurluyu = models.CharField(max_length=10, verbose_name='Alt şkafın hündürlüyü')
    alt_dolap_derinliyi = models.CharField(max_length=10, verbose_name='Alt şkafın dərinliyi')
    ust_dolap_eni = models.CharField(max_length=10, verbose_name='Üst şkafın eni')
    ust_dolap_hundurluyu = models.CharField(max_length=10, verbose_name='Üst şkafın hündürlüyü')
    ust_dolap_derinliyi = models.CharField(max_length=10, verbose_name='Üst şkafın dərinliyi')
    image = models.ImageField(upload_to='images/%Y/%m/%d/', verbose_name='Məhsulun şəkli')
    available = models.BooleanField(default=False, verbose_name='Yayımlanır')
    product_of_month = models.BooleanField(default=False, verbose_name='Ayın məhsulu')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-date',)
        verbose_name = 'Məhsul'
        verbose_name_plural = 'Məhsullar'


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Mesaj'
        verbose_name_plural = 'Mesajlar'


from django.db import models

# Create your models here.
class Home(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Заголовок'
    )

    description = models.TextField(
        verbose_name='Описание'
    )
    
    banner = models.ImageField(
        upload_to='Banners',
        verbose_name='Банне'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главные страницы'

class AboutUs(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Заголовок'
    )

    description = models.TextField(
        verbose_name='Описание'
    )
    
    logo_1 = models.ImageField(
        upload_to='logo1',
        verbose_name='Логотип'
    )
    logo_2 = models.ImageField(
        upload_to='logo2',
        verbose_name='Логотип2'
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'
class Artist(models.Model):
    name = models.CharField(
        max_length=40,
        verbose_name='Имя'
    )

    description = models.TextField(
        verbose_name='Описание'
    )
    
    image_artist = models.ImageField(
        upload_to='image_artist',
        verbose_name='Фото артиста'
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Артист'
        verbose_name_plural = 'Артисты'
class Reviews(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Заголовок'
    )

    description = models.TextField(
        verbose_name='Описание'
    )
    
    image_people = models.ImageField(
        upload_to='image_artist',
        verbose_name='Фото артиста'
    )
    name = models.CharField(
        max_length=40,
        verbose_name='Имя'
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

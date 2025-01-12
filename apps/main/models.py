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
        return self.name
    
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
class Faq(models.Model):
    title =  models.CharField(
        max_length=50,
        verbose_name='Заголовок'
    )
    question = models.CharField(
        max_length=50,
        verbose_name='вопрос'
    )
    answer = models.TextField(
        verbose_name='Ответ'
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

class Contacts(models.Model):
    name = models.CharField(
        max_length = 255,
        verbose_name = 'Имя'
    )
    email = models.EmailField(
        verbose_name = 'Почта'
    )
    message = models.TextField(
        verbose_name = 'Сообщение'
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = '11) Обратная связь'
        verbose_name_plural = '11) Обратная связь'
        
class ConactUs(models.Model):
     Address = models.CharField(
        max_length=40,
        verbose_name='Адресс'
     )
     Phone = models.CharField(
         max_length=40,
         verbose_name='Номер телефона'
     )
     Fax = models.CharField(
         max_length=40,
         verbose_name='Номер телефона'
     )
     Mail = models.EmailField(
         verbose_name='Электронная почта'
     )
     facebook = models.URLField(
         verbose_name='Ссылка на facebook'
     )
     twitter = models.URLField(
         verbose_name='Ссылка на twitter'
     )
     pinterest = models.URLField(
         verbose_name='Ссылка на pinterest'
     )
     youtube = models.URLField(
         verbose_name='Ссылка на youtube'
     )
     def __str__(self):
         return self.Address
     class Meta:
         verbose_name = 'Связь'
         verbose_name_plural = 'Связи'

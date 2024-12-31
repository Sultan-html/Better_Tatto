from django.contrib import admin
from apps.main.models import Home, AboutUs, Artist,Reviews
# Register your models here.
@admin.register(Home)
class HomaAdmin(admin.ModelAdmin):
    list_display = ('title','description','banner')
    search_fields = ['title']
@admin.register(AboutUs)
class HomaAdmin(admin.ModelAdmin):
    list_display = ('title','description','logo_1','logo_2')
    search_fields = ['title']
@admin.register(Artist)
class HomaAdmin(admin.ModelAdmin):
    list_display = ('name','description','image_artist')
    search_fields = ['name']
@admin.register(Reviews)
class HomaAdmin(admin.ModelAdmin):
    list_display = ('title','description','image_people','name')
    search_fields = ['name']
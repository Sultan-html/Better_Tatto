from django.contrib import admin
from apps.main.models import Home, AboutUs, Artist,Reviews,Faq,ConactUs
# Register your models here.
@admin.register(Home)
class HomaAdmin(admin.ModelAdmin):
    list_display = ('title','description','banner')
    search_fields = ['title']
@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title','description','logo_1','logo_2')
    search_fields = ['title']
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name','description','image_artist')
    search_fields = ['name']
@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('title','description','image_people','name')
    search_fields = ['name']
@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('title','question','answer')
    search_fields = ['question ']
@admin.register(ConactUs)
class ConactUsAdmin(admin.ModelAdmin):
    list_display = ('Address','Phone','Fax','Mail','facebook','twitter','pinterest','youtube')
    search_fields = ['Mail ']
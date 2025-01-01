from django.shortcuts import render
from apps.main.models import Home,AboutUs,Artist,Reviews,Faq,ConactUs
from apps.telegram.views import get_text
from apps.main import models
# Create your views here.


#Главная страницы
def index(request):
    home = Home.objects.latest('id')
    aboutus = AboutUs.objects.latest('id')
    artist = Artist.objects.all()
    reviews = Reviews.objects.all()
    faq = Faq.objects.all()
    contactus = ConactUs.objects.latest('id')
    category_id = request.GET.get('data-filter')  # Получаем ID выбранной категории из запроса
    print
    if category_id:  # Если указана категория, фильтруем проекты
        projects = models.Project.objects.filter(catigory=category_id)

    if request.method == 'POST':
        if "newslater" in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            page_contact = models.Contacts.objects.create(name=name, email=email, message=message)
            if page_contact:
                get_text(f"""
                Оставлена заявка на обратный звонок 📞
                            
    Имя пользователя:  {name}
    Почта: {email}
    Сообщение: {message}

    """)

    return render(request, 'index.html',locals())

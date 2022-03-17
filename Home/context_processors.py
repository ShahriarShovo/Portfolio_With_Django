from Home.models import Index, Home, About, Resume, Services, Contact

def font_index(request):
    return {'font_index': Index.objects.all()}

def home(request):
    return {'home': Home.objects.all()}

def about(request):
    return {'about': About.objects.all()}

def resume(request):
    return {'resume': Resume.objects.all()}

def services(request):
    return {'services': Services.objects.all()}

def contact(request):
    return {'contact': Contact.objects.all()}
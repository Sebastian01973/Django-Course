from django.http import HttpResponse
from django.shortcuts import render

from OnlineStore import settings
from gestionPedidos.models import Article
from django.core.mail import send_mail


# Create your views here.


def search_article(request):
    return render(request, "Search_Article.html")


def search(request):
    if request.GET["pdr"]:
        # mensaje = "Articulo Buscado %r" % request.GET["pdr"]
        product = request.GET["pdr"]
        if len(product) > 20:
            mensaje = "Texto de busqueda demasiado largo"
        else:

            articulos = Article.objects.filter(name__icontains=product)
            return render(request, 'Result_search.html', {'articulos': articulos, 'query': product})

    else:
        mensaje = "Nos has introducido nada"

    return HttpResponse(mensaje)


def contact(request):

    if request.method == "POST":
        subject=request.POST["asunto"]

        message = request.POST["mensaje"] + " " + request.POST["email"]

        email_from = settings.EMAIL_HOST_USER

        recipent_list = ["sebastian0197333@gmail.com"]

        # send_mail(subject, message, email_from, recipent_list)
        #Ya no sirve porque google no tiene habilitado el acceso a aplicaciones poco seguras

        return render(request, "thanks.html")

    return render(request,'Contact.html')

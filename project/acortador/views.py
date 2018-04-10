from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

from .models import Paginas

FORMULARIO = '''
            <form action="" Method="POST">
            Introduce URL:<br>
            <input type="text" name="URL" placeholder="For Example: 'www.gooogle.es'"><br>
            <input type="submit" value="Enviar">
</form>
'''

def retocarurl(url):
    print(type(url))
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'http://' +url
    return url

@csrf_exempt
def barra(request):
    if request.method == "POST":
        nuevo = Paginas(url=request.POST['URL'])
        nuevo.url = retocarurl(str(nuevo.url))
        nuevo.save()
    lista = Paginas.objects.all()
    respuesta = '<ul>'
    for pagina in lista:
        respuesta += '<li><a href="/' + str(pagina.id) + '">' + str(pagina.id) + '-->' + pagina.url + '</a>'
    respuesta += "</ul>"
    respuesta += FORMULARIO
    return HttpResponse(respuesta)

def url(request,numero):
    try:
        pagina = Paginas.objects.get(id=str(numero))
    except:
        raise Http404("No existe")
    return redirect(str(pagina))

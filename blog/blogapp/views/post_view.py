#IMPORTA O POST E AS VIEWS GENERICAS DO DJANGO
from django.views import generic
from ..models import Post

#CRIA UMA VIEW DE LISTAGEM
class PostView(generic.ListView):
    #ACESSA O MODEL POST, FILTRANDO APENAS OS DE STATUS 1 E MOSTRA EM ORDEM CRESCENTE
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    #O TEMPLATE USADO PARA MOSTRAR A LISTA
    template_name = "index.html"

#CRIA UMA VIEW PARA MOSTRAR UM POST EM DETALHES
class PostDetail(generic.DetailView):
    #DJANGO BUSCA O POST PELO ID OU SLUG
    model = Post
    #MOSTRA COM O TEMPLATE
    template_name = "post_detail.html"
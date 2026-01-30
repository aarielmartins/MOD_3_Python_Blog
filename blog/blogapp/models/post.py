from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Post(models.Model):
    #TITULO
    #CHARFIELD - ACEITA TEXTO
    title = models.CharField(max_length=200, unique=True)
    #IDENTIFICACAO DO POST
    #SLUGFIELD - ACEITA TEXTO E +
    slug = models.SlugField(max_length=200, unique=True)
    #AUTOR (USA O MODELO PRONTO DE USER DO DJANGO)
    #FOREIGNKEY - MODELO DE RELACIONAMENTO
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    #QUANDO O CONTEUDO FOI ATUALIZADO
    #DATATIME - DATA E HORA
    updated_on = models.DateTimeField(auto_now=True)
    #TEXTO DO POST
    #TEXTFIELD - CRIA TEXTOS
    content = models.TextField()
    #QUANDO FOI CRIADO
    created_on = models.DateTimeField(auto_now_add=True)
    #STATUS(RASUCUNHO OU POSTADO)
    #INTEGERFIELD -  CHOICES - ARRAY DE OBJETOS PARA CONSTRUIR A ESTRUTURA DE TIPO
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
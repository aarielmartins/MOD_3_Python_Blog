#IMPORTA O FACTORY BOY
import factory
#IMPORTA O FAKER, QUE GERA NOMES, EMAIL, FRASES E ETC
from faker import Factory as FakerFactory

#IMPORTA O USER PADRAO DO DJANGO
from django.contrib.auth.models import User
#IMPORTA A FUNCAO NOW PARA DATA/HORA ATUAL
from django.utils.timezone import now

#IMPORTA O MODELO DE POST
from blogapp.models import Post

#CRIA O GERADOR DE DADOS FALSOS
faker = FakerFactory.create()

#CRIA A PRIMEIRA FACTORIE E CADA VEZ QUE VC USA OS VALOERS MUDAM
class UserFactory(factory.django.DjangoModelFactory):
    #DEFINE QUE CRIA OBJETOS DO MODELO USER
    class Meta:
        model = User

    #CRIA EMAIL E USERNAME FALSOS
    email = factory.Faker("safe_email")
    username = factory.LazyAttribute(lambda x: faker.name())

    #TRATA A SENHA
    @classmethod
    def _prepare(cls, create, **kwargs):
        password = kwargs.pop("password", None)
        user = super(UserFactory, cls)._prepare(create, **kwargs)
        if password:
            user.set_password(password)
            if create:
                user.save()
        return user

#CRIA A SEGUNDA FACTURE PARA O OBJETOS DO MODELO POST
class PostFactory(factory.django.DjangoModelFactory):
    #GERA TITULO
    title = factory.LazyAttribute(lambda x: faker.sentence())
    #GERA DATA ATUAL
    created_on = factory.LazyAttribute(lambda x: now())
    #GERA AUTOR
    author = factory.SubFactory(UserFactory)
    #STATUS PADRAO 0
    status = 0

    #DEFINE QUE CRIA OBJETOS DO MODELO POST
    class Meta:
        model = Post
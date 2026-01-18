#IMPORTA A BIBLIOTECA DE TESTES
import pytest
#IMPORTA A FACTORY
from blogapp.facotories import PostFactory

#DECLARA QUE A FUNCAO E UMA FIXTURE E PODE SER REPLICADA
#USADA PARA CRIAR OBJETOS OU DADOS DE TESTE AUTOMATICAMENTE
@pytest.fixture
def post_published():
    #CRIA UM TITULO NO POSTFACTURE SEMPRE QUE A FUNCAO E CHAMADA
    return PostFactory(title='pytest with factory')

#APENAS PARA AVISAR O PYTEST QUE ESSE TESTE VAI ACESSAR O BANCO DE DADOS
@pytest.mark.django_db
def test_create_published_post(post_published):
    assert post_published.title == 'pytest with factory'
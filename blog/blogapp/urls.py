from django.urls import path

from blogapp import views


urlpatterns = [
    #URL DA HOME QUE MOSTRA TODOS OS POSTS EM LISTA
    path("", views.PostView.as_view(), name="home"),
    #SLUG E O TEXTO QUE APARECE NA URL, GERALMENTE O TITULO
    path("<slug:slug>/", views.PostDetail.as_view(), name="post_detail"),
]

from django.conf.urls import url
from django.urls import path, include

from .views import IndexView, PostDetailView, about, comment_new

urlpatterns = [
    # Url equivale a '' ou '/', ela irá ser o index da amplicação
    url(r'^$', IndexView.as_view(), name='post-list'),
    # Url equivale a 'post/<id>' ela irá mostrar os detalhes de um post
    url(r'post/(?P<pk>[0-9]+)/', PostDetailView.as_view(), name='post-detail'),
    # Url equivale a 'about/' ela irá mostrar os detalhes do que for inserido em About
    url(r'about/', about, name='about'),
    # Url equivale a 'comment/new/', será usada para inserir os comentários
    url(r'^comment/new/$', comment_new, name='comment-new'),
]

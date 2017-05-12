from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^node_links$', views.node_links, name='node_links'),
    url(r'^draw_graph$', views.draw_graph, name='draw_graph'),
]

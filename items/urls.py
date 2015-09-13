from django.conf.urls import patterns, url
from items.views import IndexView, ListView, ItemsDetailView, PhotosDetailView
"""
urlpatterns= patterns('',
    # ex: /items/
    url(r'^$', views.IndexView.as_view(), name='index'),
    #ex: /items/5/
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    #ex: /items/5/results/
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(),name='results'),
    #ex: /items/5/vote/
    url(r'^(?P<item_id>\d+)/vote/$', views.vote, name = 'vote'),
)
"""

urlpatterns = patterns('',
    #/items/
    url(r'^$', IndexView.as_view(), name = 'index'),
    
    #/items/items/
    url(r'^items/$', ListView.as_view(), name='item_list'),
    
    #/items/items/5/
    url(r'^items/(?P<pk>\d+)/$', ItemsDetailView.as_view(), name = 'item_detail'),
    
    #/items/photos/2/
    url(r'^photos/(?P<pk>\d+)/$', PhotosDetailView.as_view(), name = 'photo_detail'),
)



from django.conf.urls import patterns, url
from items.views import IndexView, ListView, ItemsDetailView, PhotosDetailView, change_rating

urlpatterns = patterns('',
    #/items/
    url(r'^$', IndexView.as_view(), name = 'index'),
    
    url(r'^change_rating/$', change_rating, name='change_rating'),
    #/items/items/
    url(r'^items/$', ListView.as_view(), name='item_list'),
    
    #/items/items/5/
    url(r'^items/(?P<object_id>\d+)/$', ItemsDetailView.as_view(), name = 'item_detail'),
   
    #/items/photos/2/
    url(r'^photos/(?P<object_id>\d+)/$', PhotosDetailView.as_view(), name = 'photo_detail'),

)



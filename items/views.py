from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from items.models import Item, Photo

class IndexView(generic.ListView):
    model = Item
    allow_empty=True
    template_name = 'index.html'
    #extra_context = {'full_item_list': Item.objects.all()}
    def get_queryset(self):
        return Item.objects.all()


class ListView(generic.ListView):
    model=Item
    template_name = 'items_list.html'
    allow_empty=True
    #context_object_name = 'latest_item_list'
    def get_queryset(self):
        return Item.objects.all()


class ItemsDetailView(generic.DetailView):
    template_name='items_detail.html'
    model = Item
    
    def get_queryset(self):
        return Item.objects.all()
    def get_object(self):
        return get_object_or_404(Item, pk=self.kwargs['object_id'])


class PhotosDetailView(generic.DetailView):
    template_name='photos_detail.html'
    def get_queryset(self):
        return Photo.objects.all()
    def get_object(self):
        return get_object_or_404(Photo, pk=self.kwargs['object_id'])



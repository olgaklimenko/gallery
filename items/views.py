from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from items.models import Item, Photo

class IndexView(generic.TemplateView):
    template_name = 'index.html'
    extra_context = {'full_item_list': Item.objects.all()}
    def get_queryset(self):
        return Item.objects.all()

class ListView(generic.ListView):
    model=Item
    template_name = 'items_list.html'
    allow_empty=True
    #context_object_name = 'latest_item_list'
    def get_queryset(self):
        return Item.objects.all()
    def head(self, *args, **kwargs):
	items_list = self.get_queryset()
	return HttpResponse(json.dumps({"success": True}), content_type="application/json")

class ItemsDetailView(generic.DetailView):
    template_name='items_detail.html'
    model = Item
    
    def get_queryset(self):
        return Item.objects.all()
    def get_object(self):
        return get_object_or_404(Item, pk=1)


class PhotosDetailView(generic.DetailView):
    template_name='photos_detail.html'
    def get_queryset(self):
        return Photo.objects.all()
    def get_object(self):
        return get_object_or_404(Photo, pk=1)

"""
class ResultsView(generic.DetailView):
    model = Item
    template_name = 'items/results.html'

def vote(request, item_id):
    p = get_object_or_404(Item, pk=item_id)
    try:
        selected_photo= p.photo_set.get(pk=request.POST['photo'])
    except (KeyError, Photo.DoesNotExist):
        return render(request, 'items/detail.html', {
            'photo':p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_photo.votes +=1
        selected_photo.save()
        return HttpResponseRedirect(reverse('items:results', args=(p.id,)))
"""

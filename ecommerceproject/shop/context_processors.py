from .models import category,Product
def menu_links(request):
    links=category.objects.all()
    return dict(links=links)

from django.conf import settings
from django.http import HttpResponseRedirect
from django_mako_plus import view_function
from catalog import models as cmod

from .. import dmp_render, dmp_render_to_string

@view_function
def process_request(request):
    pid = request.urlparams[0]
    try:
        product = cmod.Product.objects.get(id=pid)
    except cmod.Product.DoesNotExist:
        return HttpResponseRedirect('/catalog/index')

    # add to the last 5 viewed items
    request.last5.insert(0, product.id)
    
    return dmp_render(request, 'detail.html'){

    })

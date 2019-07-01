import csv,io
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .models import Product
from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q


def searchposts(request):


    if request.method == 'GET':

        query= request.GET.get('q')
        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(name__icontains=query) | Q(description__icontains=query)

            results= Product.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'display.html', context)

        else:
            return render(request, 'display.html')

    else:
        return render(request, 'display.html')


def IndexListing(request):
    if request.method == 'GET':
        res= Product.objects.all()
        context={
            'res' : res
        }
        return render(request, 'list.html',context)




@permission_required('admin can log entry')
def csv_upload(request):
    template ="csv_upload.html"
    prompt={
        'order':'order'
    }
    if request.method=="GET":
        return render(request,template,prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request,'not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string=io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string):
        _,created = Product.objects.update_or_create(
            name=column[0],
            sku=column[1],
            description=column[2],
        )

    context= {}

    return render(request,template,context)



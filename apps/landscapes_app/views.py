from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'landscapes_app/index.html')

def pics(request, id):
    context = {}
    if int(id) >0 and int(id) <=10:
        context['image']='snow.jpg'
    elif int(id) >10 and int(id) <=20:
        context['image']='desert.jpg'
    elif int(id) >20 and int(id) <=30:
        context['image']='forest.jpg'
    elif int(id) >30 and int(id) <=40:
        context['image']='vineyard.jpg'
    elif int(id) >40 and int(id) <=50:
        context['image']='tropical.jpg'
    else:
        context['image']='hellno.jpg'

    return render(request, 'landscapes_app/picture.html', context)



    
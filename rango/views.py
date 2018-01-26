from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

    return render(request, 'rango/index.html', context=context_dict)
    #return HttpResponse('Rango says hey there partner! <br/> <a href="/rango/about/">About</a>')

def about(request):

	context_dict = {'boldmessage': "Rango says here is the about page."}

	return render(request, 'rango/about.html', context=context_dict)
    #return HttpResponse('Rango says here is the about page. <a href="/rango/">Index</a>')

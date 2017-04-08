from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner! Check out the <a href='/rango/about/'>about page</a>.")

def about(request):
	return HttpResponse("Rango says here is the about page. Return to <a href='/rango/'>index</a>")
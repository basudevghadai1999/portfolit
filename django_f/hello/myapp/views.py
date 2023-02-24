from django.shortcuts import render,HttpResponse

from myapp.models import Person1

# Create your views here.

def index(request):
    #return HttpResponse("This is home page")
    if request.method == 'POST':
        fastname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        email = request.POST.get('email')
        # #image = request.POST.get('image')
        # person = Person1(first_name=fastname, last_name=lastname,email=email,image=image)
        # person.save()
            # do something with the form data
        return render(request, 'index.html')
    context ={
        'variable': "This is changing varibale",
        'variable': "This is varibale 2 data"
    }
    return render(request,'index.html',context)

def signup(request):
    return render(request,'signup.html')

def login(request):
    return render(request,'login.html')
def contact(request):
    return HttpResponse('This is contact page')
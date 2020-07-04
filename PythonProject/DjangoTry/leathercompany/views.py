from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'letherhome.html');


def registerRawMaterials(request):
    if request.method =="post":
        pass
    else:
        return render(request,'')
    pass


def listOfRawMaterials(request):
    pass

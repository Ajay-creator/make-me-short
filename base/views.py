from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages

# utils
from .utils import generate_random_suffix

# models
from .models import URLMapping

# forms
from .forms import URLForm

# Create your views here.
def check_object(suffix) -> int:
    urls = URLMapping.objects.filter(pk=suffix)
    return len(urls)

def call_random_code_generator():
    length = 6
    code = generate_random_suffix(length)
    while check_object(code):
        code = generate_random_suffix(length)

    return str(code)

def Home(request):
    url = None
    suffix = None
    if request.method == "POST":
        actual_url = request.POST["url"]
        suffix = call_random_code_generator()
        form = URLForm({'url':actual_url,'suffix':suffix})
        if form.is_valid():         
            form.save()
            url = form.cleaned_data.get('url')
            suffix = form.cleaned_data.get('suffix')

        else:
            suffix = None
            url = actual_url
            messages.error(request,'❌ Please, enter a valid URL')
    
    context = {"url":url,"code":suffix}
    return render(request,'home.html',context)


def Redirect(request,suffix):
    context = {}
    try:
        actual_url = URLMapping.objects.get(pk=suffix)
        return redirect(actual_url.url)
    except:
        return HttpResponse('<h1>No url is mapped to this End Point</h1>')

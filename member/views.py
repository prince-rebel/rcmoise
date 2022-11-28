from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse
from .models import Article

from django.http import HttpResponse



def index(request):
    latest_question_list = Article.objects.order_by('designation')[:5]
    template = loader.get_template('index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                historyConnection(pseudo=user,last_login=datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S")).save()
                login(request,user)
                return redirect('index')
            else:
                messages.info(request," Mot de passe ou  nom utilisateur incorrect")
 
                return render (request,'index.html',{})
        else:
            return render (request,'index.html',{})
    else:
        return redirect('index')


def logout_view(request):
    logout(request)
    return redirect('login_view')
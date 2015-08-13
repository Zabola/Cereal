from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from main.models import Manufacturer, Cereal, Nutritional_Information
from main.forms import CerealSearch, CreateCereal,UserSignUp, UserLogin
from django.contrib.auth.models import User
from main.forms import UserSignUp
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect





def home(request):

    manus = Manufacturer.objects.all()

    context = {}

    context['manus'] = manus

    return render_to_response('home.html', context, context_instance=RequestContext(request))


def cereal_list_view(request):

    manufacturers = Manufacturer.objects.all()

    cereal_string = ""

    for manufacturer in manufacturers:

        cereal_string += "<h4>%s<h4>" %manufacturer

        for cereal in manufacturer.cereal_set.all():

            cereal_string += "%s </br>" %cereal.name

    return HttpResponse(cereal_string)

def cereal_list_template2(request):

    manufacturers = Manufacturer.objects.all()

    context = {}

    context['manufacturers'] = manufacturers

    return render_to_response('cereal_list2.html', context, context_instance=RequestContext(request))


def cereal_detail(request, pk):

    context = {}
    cereal = Cereal.objects.get(pk=pk)
    context['cereal'] = cereal

    return render_to_response('cereal_detail.html', context, context_instance=RequestContext(request))


def form_view(request):
    context = {}

    get = request.GET
    post = request.POST

    context ['get'] = get
    context ['post'] = post

    if request.method == "POST":
        cereal = request.POST.get('cereal', None)

        cereals = Cereal.objects.filter(name__startswith=cereal)

        context['cereals'] = cereals

    elif request.method == "GET":
        context['method'] = 'The method is GET'


    return render_to_response('form_view.html', context, context_instance=RequestContext(request))

def cereal_create(request):

    context = {}

    form = CreateCereal()
    context['form'] = form

    if request.method == 'POST':
        form = CreateCereal(request.POST)

        if form.is_valid():
            form.save()

            context['valid'] = "Cereal Saved"
    elif request.method == "GET":
        context['valid'] = form.errors

    return render_to_response('create_cereal.html', context, context_instance=RequestContext(request))



def form_view2(request):
    context = {}

    get = request.GET
    post = request.POST

    context ['get'] = get
    context ['post'] = post

    form = CerealSearch()
    context['form'] = form

    if request.method == "POST":
        form = CerealSearch(request.POST)

        if form.is_valid():
            cereal = form.cleaned_data['name']

            cereals = Cereal.objects.filter(name__startswith=cereal)

            context['cereals'] = cereals
            context['valid'] = "the form was Valid"

        else:
            context['valid'] = form.errors

    elif request.method == "GET":
        context['method'] = "The method was GET"


    return render_to_response('form_view2.html', context, context_instance=RequestContext(request))



def cereal_search(request, cereal):

    cereals = Cereal.objects.filter(name__istartswith=cereal)

    cereal_string = ""

    for cereal in cereals:

        cereal_string += "<b>%s, <b>Manufacturer:</b>%s  </br>" % (cereal.name, cereal.manufacturer)

    return HttpResponse(cereal_string)



def get_cereal_search(request):

    print request.GET
    #cereal1 = request.GET['cereal]']
    cereal = request.GET.get('cereal', 'None')
    cereals = Cereal.objects.filter(name__istartswith=cereal)

    cereal_string = """

    <form action='/get_cereal_search/' method='GET'>

    Cereal:
    </br>
    <input type="text" name="cereal">
    <input type="submit" value="submit" >

    </form>
    """

    for cereal in cereals:

        cereal_string += "<b>Cereal: </b>%s</br> <b> Manufacturer:</b>%s </br></br>" % (cereal.name, cereal.manufacturer)

    return HttpResponse(cereal_string)
    

def manufacturer_list_template(request):

    manufacturers = Manufacturer.objects.all()

    context = {}

    context['manufacturers'] = manufacturers

    return render(request, 'cereal_list.html', context)










def manufacturer_search(request, manufacturer):
    manufacturers = Manufacturer.objects.filter(name__istartswith=manufacturer)

    manu_string = ""

    for manufacturer in manufacturers:

        manu_string += "<b>Manufacturer:</b>%s  </br>" % (manufacturer.name)

    return HttpResponse(manu_string)









def get_manufacturer_search(request):
    print request.GET
    #cereal1 = request.GET['cereal]']
    manufacturer = request.GET.get('name', 'None')
    manufacturers = Manufacturer.objects.filter(name__istartswith=manufacturer)

    manu_string = """

    <form action='/get_manufacturer_search/' method='GET'>

    Manufacturer:
    </br>
    <input type="text" name="manufacturer">
    <input type="submit" value="submit" >

    </form>
    """

    for manufacturer in manufacturers:

        manu_string += "<b>Manufacturer: </b>%s</br>" % (Manufacturer.name)

    return HttpResponse(manu_string)



def signup(request):

    context = {}

    form = UserSignUp()
    context ['form'] = form

    if request.method == "POST":
        form = UserSignUp(request.POST)
        if form.is_valid():

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                new_user = User.objects.create_user(name, email, password)
                context['valid'] = "Thank you for Signing up!"

                auth_user = authenticate(username=name, password=password)
                login(request, auth_user)
                return HttpResponseRedirect('/cereal_list_template/')
            except IntegrityError, e:
                context['valid'] = "A user with that name already Exists"

        else:
            context['valid'] = form.errors

    if request.method == "GET":
        context['valid'] = " PLease Sign Up man"

    return render_to_response('signup.html', context, context_instance=RequestContext(request))


def login_view(request):

    context = {}

    context['form'] = UserLogin()

    username = request.POST.get('username', None)
    password = request.POST.get('password', None)

    auth_user = authenticate(username=username, password=password)

    if auth_user is not None:
        if auth_user.is_active:
            login(request, auth_user)
            context['valid'] = "Login Successful"

            return HttpResponseRedirect('/home/')
        else:
            context['valid']= "Invalid User"
    else: 
        context['valid'] = "Please enter a User Name"

    return render_to_response('login.html', context, context_instance=RequestContext(request))

def logout_view(request):

    logout(request)

    return HttpResponseRedirect('/home/')
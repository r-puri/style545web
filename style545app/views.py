from django.shortcuts import render
from style545app.models import Stylemaster
from style545app.models import Itemmaster
from style545app.forms import Itemselector
from style545app.models import Stylemaster
from style545app.models import Occassionmaster
from style545app.models import Budgetmaster
from style545app.models import Looksmaster
from style545app.models import Categorymaster
from style545app.models import Bodymaster
import json
from django.http import JsonResponse
from style545app.forms import SignUpForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout





# Create your views here.
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/style545app/looks')

def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/style545app/looks.html')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your style545 account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            auth=False
            #return HttpResponse("Invalid login details supplied.")
            return render(request, 'style545app/login.html',{'authenticated':auth})

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'style545app/login.html', {})

def register(request):
 if  not request.user.is_authenticated():
    return HttpResponseRedirect('/style545app/login/')
 registered = False
 if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = SignUpForm(data=request.POST)
        if user_form.is_valid():
            user_form.save()
            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            #user.set_password(user.password)
            #user.save()
            registered = True
        else:
            print user_form.errors
 else:
     user_form = SignUpForm()
 return render(request,
            'style545app/register.html',
            {'user_form': user_form, 'registered': registered} )

def getitemsbycat(request):
    cat_id=None
    if request.method == 'GET':
        cat_id = request.GET.get("category_id","")
        item_list=Itemmaster.objects.all().filter(itemcategoryid=cat_id).values('itemid','item_name','item_price','itemimageurl')

    return (JsonResponse({'results': list(item_list)}))
    #return HttpResponse(context_dict)

def lookconfirm(request):
     return render(request,'style545app/lookconfirm.html')
def index(request):
    #NumberofItems={} # Minimum number of items of a look
     number_of_items_list=3
     if  not request.user.is_authenticated():
         return HttpResponseRedirect('/style545app/login/')
     if request.method == 'POST':
         savelook(request,number_of_items_list)
         return render(request,'style545app/lookconfirm.html')
     else:
        item_list = Itemmaster.objects.order_by('-item_name')
        style_list= Stylemaster.objects.order_by('-stylename')
        occasion_list= Occassionmaster.objects.order_by('-occassion_name')
        budget_list= Budgetmaster.objects.order_by('-budgetname')
        body_list=Bodymaster.objects.order_by('-bodytype')
        context_dict = {'items': item_list,'styles':style_list,'occasions':occasion_list,'budgets':budget_list,'body_list':body_list,'noofitems': range(number_of_items_list)}
        return render(request, 'style545app/looks.html',context_dict)
def savelook(request,number_of_items):
    #get all the selected items
    #j1=json.loads(request.POST.get("item1",""))
    #j2=json.loads(request.POST.get("items2",""))
    mylook=Looksmaster()
    item=[]
    no_of_items_cols=7# number of columns in DB
    for x in range(number_of_items): #number of items exposed on ui
       print("item"+str(x+1), json.loads(request.POST.get("item"+str(x+1),"")))
       item.append(json.loads(request.POST.get("item"+str(x+1),"")))

    for x in range(len(item)):
        if x<(no_of_items_cols):
            print("item"+str(x+1)+"ID"," is %s",item[x]["itemid"])
            setattr(mylook, "item"+str(x+1)+"id",item[x]["itemid"])

    # print ("price1 %s" %items[0]['item_price'])
    # print ("price2 %s" %j1['item_price'])
    # print ("id1 %s" %j1['itemid'])
    # print ("id2 %s" %j2['itemid'])
    print ("style%s"% request.POST.getlist("stylescheck",""))
    print ("Occasions%s"% request.POST.getlist("occasioncheck",""))
    print ("Budgets%s",request.POST.get("budgettype",""))
    print ("LookName%s",request.POST.get("lookname",""))
    print ("BodyType%s",request.POST.getlist("bodytype",""))

    occasion_list=request.POST.getlist("occasioncheck","")
    style_list=request.POST.getlist("stylescheck","")

    # for checkboxes need to determine how are dynamically checked. See list length.

    mylook.lookname=request.POST.get("lookname","")
    # read body tags 1-5
    body_type_list=request.POST.getlist("bodytype","")
    #check if len is more than the columns and throw error
    for x in range(len(body_type_list)):
        setattr(mylook, "custom_tag_bodytype"+str(x+1),body_type_list[x])
    mylook.look_active="Y"
    #Occ, Style, Budget
    #occID is non nullable so default to something when nothing recieved from page
    occ_type_list=request.POST.getlist("occasioncheck","")
    if len(occ_type_list)==0:
        mylook.occid=1
    else:
        mylook.occid=occ_type_list[0] # assuming first one is primary, change later
        no_of_occasion_cols=3
        for x in range(len(occ_type_list)-1):
            if x<(no_of_occasion_cols):
                print("likeoccid%s",str(x+1))
                setattr(mylook, "likeoccid_"+str(x+1),occ_type_list[x+1])

    style_type_list=request.POST.getlist("stylescheck","")
    if len(style_type_list)==0:
        mylook.styleid=1
    else:
        mylook.styleid=style_type_list[0] # assuming first one is primary, change later
        no_of_style_cols=3
        for x in range(len(style_type_list)-1):
            if x<(no_of_style_cols):
                print("likestyleid%s",str(x+1))
                setattr(mylook, "likestyleid_"+str(x+1),style_type_list[x+1])

    budgetid=request.POST.get("budgettype","")[0]
    try:
        val=int(request.POST.get("budgettype","")[0])
        mylook.budgetid=val
    except ValueError:
        mylook.budgetid=0
    print ("budgetid=%s",mylook.budgetid)

    mylook.look_stylist=request.user.username
    print ("user %s", mylook.look_stylist)
    mylook.save()

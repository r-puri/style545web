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
from style545app.models import Customermaster
from style545app.models import Vendormaster
from style545app.models import Surveymaster

import json
from django.http import JsonResponse
from style545app.forms import SignUpForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from rolepermissions.roles import assign_role
from rolepermissions.decorators import has_role_decorator
from rolepermissions.checkers import has_permission
from rolepermissions.permissions import available_perm_status
from rolepermissions.roles import get_user_roles
import datetime
from django.db import connection
from itertools import chain
from django.conf import settings
from django.db import IntegrityError

from django.db.models import Q
from django.db.models import Max, Min


def instore(request):
    return render(request,'style545app/instore.html')

def instoreview(request):
    if request.method=='POST':
        context_dict = {'post': True}
        return render(request,'style545app/instorelook1.html',context_dict)
    else:
        return render(request,'style545app/instorelook1.html')

def surveycomplete(request):
    return render(request,'style545app/surveycomplete.html')
def findmid(range):
    if range=="50":
        return(50)
    if range=="50-100":
        return(75)
    if range=="100-200":
        return(150)
    if range=="200":
        return(200)

def getbudgetid(budget):
    #gets budget ranges and allocates id #need to go to DB and fix DB table. DB table needs budget by vendor
    if budget <= 50:
        return(3)
    if budget > 50 and budget <=100:
        return(4)
    if budget > 100 and budget <=300:
        return(6)
def createvendor(request):
    if  not request.user.is_authenticated():
       return HttpResponseRedirect('/style545app/login/')
    if request.method=='POST':
        vendorname=request.POST.get('VendorName')
        if vendorname=="":
            print('Error:Create Vendor:VendorName is empty')
            created=False
        else:
            vendor=Vendormaster()
            vendor.Vendorname=vendorname
            try:
                vendor.save()
                created=True
            except IntegrityError as e:
                print e.message
                created=False
                context_dict = {'created': created,'post': True, 'Message':'Vendor Name exsists. Please use another name'}
                return render(request,'style545app/createvendor.html',context_dict)
            else:
                context_dict = {'created': created,'post': True}
                return render(request,'style545app/createvendor.html',context_dict)
    else:
        return render(request,'style545app/createvendor.html')


def createsurvey(request):
    if  not request.user.is_authenticated():
       return HttpResponseRedirect('/style545app/login/')
    if request.method=='POST':
        surveyname=request.POST.get('SurveyName')
        vendorid=request.POST.get('vendorlist')
        if surveyname=="":
            print('Error:Create Survey:SurveyName is empty')
            created=False
        if vendorid=="":
            print('Error:Create Survey:VendorID is empty')
            created=False
        survey=Surveymaster()
        survey.surveyname=surveyname
        survey.surveykey=None
        survey.createddate=datetime.datetime.now()
        vendor_list=Vendormaster.objects.all()
        message=""
        try:
            vendor=Vendormaster.objects.get(id=vendorid)
            survey.vendorid=vendor
        except Vendormaster.DoesNotExist:
             print ('Error:Create Survey: Cannot find vendor')
             created=False
        if Surveymaster.objects.all().filter(vendorid=vendorid,surveyname=surveyname).exists(): #survey name/vendor id exsists
            created=False
            message="Survey Name already exists for the vendor. Try another name."
            context_dict = {'created': created,'post': True,'vendor_list': vendor_list,'message': message}
            return render(request,'style545app/createsurvey.html',context_dict)
        else:
            try:
                survey.save()
                created=True
            except Exception as ex:
                created=False
                message="Error creating survey.Contact admin."
                print ("Error:Create Survey" + ex)
            finally:
                context_dict = {'created': created,'post': True,'vendor_list': vendor_list,'message': message}
                return render(request,'style545app/createsurvey.html',context_dict)
    else:
        #get list of vendors
        vendor_list=Vendormaster.objects.all()
        context_dict = {'vendor_list': vendor_list}
        return render(request,'style545app/createsurvey.html',context_dict)




def survey(request):
    #defines the customer survey

    if request.method=='POST':
        customername=request.POST.get('validate-text')
        customeremail=request.POST.get('validate-email')
        customerzipcode=request.POST.get('zipcode')
        customerage=request.POST.get('radioage')
        customertopsize=request.POST.get('topsize')
        customerpantsize=request.POST.get('pantsize')
        customerdresssize=request.POST.get('dresssize')
        customertopbudget=request.POST.get('budgettop')
        customerpantbudget=request.POST.get('budgetpants')
        customerdressbudget=request.POST.get('budgetdress')
        customeraccessorybudget=request.POST.get('budgetaccessory')
        customerouterbudget=request.POST.get('budgetouterwear')
        customeroccid=request.POST.get('radioocc')
        customerstyle=request.POST.getlist('checkboxstyle')
        customerceleb=request.POST.get('celeb')
        customercomments=request.POST.get('comments')
        customerbodytype=request.POST.get('bodytype')
        surveykey=request.POST.get('surveyid')
        print('skey=' + str(surveykey))
        survey=Surveymaster()
        if (surveykey==""):
                survey=Surveymaster.objects.get(id=1)
        else:
            try:
                survey=Surveymaster.objects.get(surveykey=surveykey)
            except Surveymaster.DoesNotExist:
                survey=Surveymaster.objects.get(id=1)
                pass



        if (customername==""):
            raise ValueError ('Error:Survey:Customer name is empty')
        if (customeremail==""):
            raise ValueError ('Error:Survey:Customer email address is empty')
        #create customer object
        #customer=Customermaster()
        #try:
        qscustomer=Customermaster.objects.filter(customer_email=customeremail)
        print(len(qscustomer))
        if len(qscustomer)==0:
            customer=Customermaster()
        if len(qscustomer)>=1:
            customer=Customermaster()
            customer=qscustomer[0]
        #except customer.DoesNotExist:
            #customer=Customermaster()

        #print ('found records' + str(len(customer)))
        #if len(customer)==0:
            #customer=Customermaster()
        customer.customer_name=customername
        customer.customer_email=customeremail
        customer.customer_comments=customercomments
        customer.customer_age=customerage
        customer.customer_topsize=customertopsize
        customer.customer_dresssize=customerdresssize
        customer.customer_pantsize=customerpantsize
        customer.customer_bodytype=customerbodytype
        topbudget=findmid(customertopbudget)
        pantbudget=findmid(customerpantbudget)
        dressbudget=findmid(customerdressbudget)
        accessbudget=findmid(customeraccessorybudget)
        outerbudget=findmid(customerouterbudget)
        budget=(topbudget+pantbudget+dressbudget+accessbudget+outerbudget)/5
        customer.customer_current_budgetid=getbudgetid(budget)
        customer.surveyid=survey

        print ("budget=" + str(budget))


        if len(customerstyle)==0:
            customer.customer_current_styleID=1
        if len(customerstyle)==1:
            customer.customer_current_styleid=customerstyle[0] # assuming first one is primary, change later
        if len(customerstyle)>=2:
            customer.customer_current_styleid=customerstyle[0]
            customer.customer_current_styleid_secondary=customerstyle[1]
        customer.customer_current_occid=customeroccid#customerstylepref
        customer.customer_celebrity_closet=customerceleb
        #customer.customer_current_budgetid=1
        customer.save()


        print (customeremail)
        print (customername)
        print (customerzipcode)
        print (customerage)
        print (customertopsize)
        print (customerpantsize)
        print (customerdresssize)
        print (customerpantbudget)
        print (customertopbudget)
        print (customerdressbudget)
        print (customeraccessorybudget)
        print (customerouterbudget)
        print (customeroccid)
        print (customerstyle)
        print (customerceleb)
        print (customercomments)
        return render(request,'style545app/surveycomplete.html')


    else:
        stylelist=Stylemaster.objects.all()
        occasion_list= Occassionmaster.objects.order_by('-occassion_name')
        body_list=Bodymaster.objects.order_by('-bodytype')
        context_dict = {'styles_list': stylelist,'occasion_list':occasion_list,'body_list':body_list}
        return render(request,'style545app/survey.html',context_dict)

def updatelook(request):
 if request.method=='POST':
    #  return HttpResponse("updatinglook")
    #read form data
    #look id & look name
    lookid=request.POST.get('lookid')
    lookname=request.POST.get('lookname')
    noofitems=len(request.POST.get('itemnumber').split(","))
    if (lookid==""):
        raise ValueError ('Error:LookID is empty')
    try:
        int(lookid)
    except ValueError:
        raise ValueError ('Error: LookID is not a number')
    if (lookname==""):
        raise ValueError('Error:No lookname found')

    #read itemslist
    mylook=Looksmaster()
    #read  look oject from string
    mylook=getlookfromrequest(request,mylook,noofitems)
    mylook.save()

    #print everything for debug
    print ('look name%s',mylook.lookname)
    print ('look id%s', mylook.lookid)
    print ('item%s' ,mylook.item1id)
    print ('Occasion%s' ,mylook.occid)
    print ('Style%s' ,mylook.styleid)
    print ('Body%s' ,mylook.custom_tag_bodytype1)
    print ('Budget%s' ,mylook.budgetid)

    print (request.POST)
    return render(request,'style545app/lookconfirm.html')
 else:
    return render(request,'style545app/viewlook.html')


def viewlook(request):
 if  not request.user.is_authenticated():
    return HttpResponseRedirect('/style545app/login/')
 number_of_items=settings.NUMBER_OF_ITEMS
 if request.method=='POST':
             lookid=(request.POST.get('looklist'))
             #Get look
             look=Looksmaster.objects.all().filter(lookid=lookid)
             #Get list of items in look
             lookitemlist=[]
             occlist=[]
             styleidlist=[]
             bodyidlist=[]
             if (len(look))==1:
                 for l in look:
                     for x in range(number_of_items):
                         itemid=getattr(l, "item"+str(x+1)+"id")
                         print(itemid)
                         if (isinstance(itemid,long)):
                             lookitemlist.append(itemid)
                     occlist.append(l.occid)
                     for x in range(3):
                        occid=getattr(l, "likeoccid_"+str(x+1))
                        if (isinstance(occid,long)):
                            occlist.append(occid)
                     print ('occasions')
                     print (occlist)
                     styleidlist.append(l.styleid)
                     for x in range(3):
                        styleid=getattr(l, "likestyleid_"+str(x+1))
                        if (isinstance(styleid,long)):
                            styleidlist.append(styleid)
                     print ('styles')
                     print (styleidlist)
                     bodytypeid=long()
                     for x in range(5):#figure out why we need to conver to long. Its returning unicode frmo db.
                        try:
                            bodytypeid=long(getattr(l, "custom_tag_bodytype"+str(x+1)))
                            print (type(bodytypeid))
                            if (isinstance(bodytypeid,long)):
                                bodyidlist.append(bodytypeid)
                                print (bodyidlist)
                        except:
                            pass
                 boydtypelist=Bodymaster.objects.all().filter(id__in=bodyidlist)
                 for i in boydtypelist:
                   print ('Body  Type : ' + str(i.bodytype))

                 styleslist=Stylemaster.objects.all().filter(styleid__in=styleidlist)
                 for i in styleslist:
                    print ('style  Name : ' + str(i.stylename))
                 occasionslist=Occassionmaster.objects.all().filter(occassionid__in=occlist)
                 for i in occasionslist:
                    print ('Occ Name : ' + str(i.occassion_name))
                 #Get item                  #get a sample 0 row
                 item0=Itemmaster.objects.all().filter(itemid=0)
                 # create full list
                 fullitemslist = []
                 fullitemslist.extend(list(Itemmaster.objects.all().filter(itemid__in=lookitemlist).order_by('-itemid')))
                 print ('here2')
                 while len(fullitemslist)<5:
                     fullitemslist.extend(item0)
                 print (len(fullitemslist))

                #  while (len(itemslist)<6):
                #     itemslist.append(list(item0))
                #  for  i in itemslist:
                #      i[0][itemid]

                 return render(request,'style545app/viewlook.html',
                 { 'boydtypelist': boydtypelist,'showlook': True,'itemlist':fullitemslist,'occasionslist':occasionslist,'styleslist':styleslist,'look':look,'noofitems':range(len(fullitemslist))} )
             else:
                 print ('more than 1 look found')
                 return render(request,'style545app/viewlook.html')

 else:
    return render(request,'style545app/viewlook.html')



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
 # print has_permission(request.user, 'create_user')
 # print get_user_roles(request.user)
 # users=User.objects.all()
 # for user in users:
 #     print (user.username)
 #     print (get_user_roles (user))
 #     if user.username != 'Admin1':
 #        assign_role(user,'admin')
 if not has_permission(request.user, 'create_user'):
     return HttpResponse("You dont have access")
 registered = False
 if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = SignUpForm(data=request.POST)
        if user_form.is_valid():
            user_form.save()
            assign_role(request.user,'admin')
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
    print (datetime.datetime.now())
    if request.method == 'GET':
        cat_id = request.GET.get("category_id","")
        #item_list=Itemmaster.objects.filter(itemcategoryid=cat_id).exclude(itemimageurl = '0').values('itemid','item_name','item_price','itemimageurl').order_by('item_name')
    #q = Itemmaster.objects.filter(
    # itemid__in=Itemmaster.objects.values('item_name')
    #                            .distinct()
    #                            .values_list('itemid', flat=True)).values('itemid','item_name','item_price','itemimageurl')
    # print list(q)
    #q=Itemmaster.objects.values('item_name').distinct().values('itemid')
    q1 = Itemmaster.objects.values('item_name').distinct().filter(item_inventory__gt=0).annotate(x=Max('itemid'))
    q2 = Itemmaster.objects.filter(itemid__in=[i["x"] for i in q1],itemcategoryid=cat_id).values('item_inventory','itemid','item_name','item_price','itemimageurl').order_by('item_name')
    #print (q2)
    # print (len(list(q)))
    return (JsonResponse({'results': list(q2)}))
    #return HttpResponse(context_dict)

def lookconfirm(request):
     return render(request,'style545app/lookconfirm.html')
def index(request):
    #NumberofItems={} # Minimum number of items of a look
     number_of_items_list=settings.NUMBER_OF_ITEMS
     if  not request.user.is_authenticated():
         return HttpResponseRedirect('/style545app/login/')
     if request.method == 'POST':
         savelook(request,number_of_items_list)
         return render(request,'style545app/lookconfirm.html')
     else:
        #item_list = Itemmaster.objects.order_by('-item_name')
        item_list=()
        style_list= Stylemaster.objects.order_by('-stylename')
        occasion_list= Occassionmaster.objects.order_by('-occassion_name')
        budget_list= Budgetmaster.objects.order_by('-budgetname')
        body_list=Bodymaster.objects.order_by('-bodytype')
        context_dict = {'items': item_list,'styles':style_list,'occasions':occasion_list,'budgets':budget_list,'body_list':body_list,'noofitems': range(number_of_items_list)}
        return render(request, 'style545app/looks.html',context_dict)
def getlookfromrequest(request,mylook,number_of_items):
    if ('lookid' in request.POST): #lookid will not be there in get new look
        lookid=request.POST.get('lookid')
        if (lookid==""):
            raise ValueError ('Error:LookID is empty')
        try:
            int(lookid)
            mylook.lookid=lookid
        except ValueError:
            raise ValueError ('Error: LookID is not a number')

    lookname=request.POST.get('lookname')
    if (lookname=="" or lookname is None):
        raise ValueError('Error:No lookname found')
    else:
        mylook.lookname=lookname

    item=[]
    no_of_items_cols=7# number of columns in DB
    try:
        number_of_items=int(number_of_items)
    except ValueError:
        raise ValueError ('Error: Number of items not integer')
    for x in range(number_of_items): #number of items exposed on ui
       print("item"+str(x+1), json.loads(request.POST.get("item"+str(x+1),"")))
       item.append(json.loads(request.POST.get("item"+str(x+1),"")))

    for x in range(len(item)):
        if x<(no_of_items_cols):
            print("item"+str(x+1)+"ID"," is %s",item[x]["itemid"])
            setattr(mylook, "item"+str(x+1)+"id",item[x]["itemid"])

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

    body_type_list=request.POST.getlist("bodytype","")
    #check if len is more than the columns and throw error
    for x in range(len(body_type_list)):
        setattr(mylook, "custom_tag_bodytype"+str(x+1),body_type_list[x])

    mylook.look_active="Y"
    mylook.look_stylist=request.user.username

    return(mylook)
def savelook(request,number_of_items):
    #get all the selected items
    #j1=json.loads(request.POST.get("item1",""))
    #j2=json.loads(request.POST.get("items2",""))
    mylook=Looksmaster()
    mylook=getlookfromrequest(request,mylook,number_of_items)

    # print ("price1 %s" %items[0]['item_price'])
    # print ("price2 %s" %j1['item_price'])
    # print ("id1 %s" %j1['itemid'])
    # print ("id2 %s" %j2['itemid'])
    print ("style%s"% request.POST.getlist("stylescheck",""))
    print ("Occasions%s"% request.POST.getlist("occasioncheck",""))
    print ("Budgets%s",request.POST.get("budgettype",""))
    print ("LookName%s",request.POST.get("lookname",""))
    print ("BodyType%s",request.POST.getlist("bodytype",""))
    print ("budgetid=%s",mylook.budgetid)
    print ("user %s", mylook.look_stylist)
    mylook.save()

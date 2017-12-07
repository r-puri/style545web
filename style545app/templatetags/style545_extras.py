from django import template
from style545app.models import Categorymaster
from style545app.models import Itemmaster
from style545app.models import Looksmaster
from style545app.models import Bodymaster
from style545app.models import Occassionmaster
from style545app.models import Stylemaster
from style545app.models import Budgetmaster




register = template.Library()
@register.filter
def indexf(sequence, position):
    return sequence[position][0]

@register.filter
def indexf1(sequence, position):
    return sequence[position]


@register.simple_tag
def rendertable(looksmaster,itemslist):
    rethtml=''
    for j in range(len(looksmaster)):
        rethtml+='<div class="alert alert-success" role="alert"><strong>Look '+ str(j+1)+ '</strong></div>'
        rethtml+='<table><th>Item name</th><th>Designer</th><th>Price</th><th>Image</th>'
        for i in range(len(itemslist)):
            if itemslist[i][0]==looksmaster[j]:
                rethtml=rethtml+'<tr><td>'+itemslist[i][2]+'</td><td>'+itemslist[i][4]+'</td><td>'+str(itemslist[i][6])
                rethtml+='</td><td align="right"><img src="'+itemslist[i][9]+'height="150" width="150"/></td>'
                rethtml+='</tr>'
        rethtml=rethtml+'</table>'
    return rethtml



@register.inclusion_tag('style545app/category.html')
def get_category_list(selectedcat):
    return {'cats': Categorymaster.objects.all(),'selectedcat':selectedcat}

@register.inclusion_tag('style545app/items.html')
def get_item_list(selecteditem,selectedid):
    return {'items': Itemmaster.objects.all().filter(itemcategoryid=selectedid),'selecteditem':selecteditem}

@register.inclusion_tag('style545app/items.html')
def get_item_list_by_cat(selectedid):
    return {'items': Itemmaster.objects.all().filter(itemcategoryid=selectedid)}

@register.inclusion_tag('style545app/lookslist.html')
def get_looks_list(username):
    if (username == 'rpuri' or username=='dgulati'):
        return {'looks': Looksmaster.objects.all()}
    else:
        return {'looks': Looksmaster.objects.all().filter(look_stylist=username)}

@register.inclusion_tag('style545app/bodytype.html')
def get_bodytypes_list(selectbodylist):
    return {'bodytypeslist': Bodymaster.objects.all(),'selectbodylist':selectbodylist}

@register.inclusion_tag('style545app/occasion.html')
def get_occasions_list(selectocclist):
    return {'occasionslist': Occassionmaster.objects.all(),'selectocclist':selectocclist}

@register.inclusion_tag('style545app/style.html')
def get_styles_list(selectstylelist):
    return {'stylelist': Stylemaster.objects.all(),'selectstylelist':selectstylelist}

@register.inclusion_tag('style545app/budget.html')
def get_budget_list(budgetid):
    return {'budgetlist': Budgetmaster.objects.all(),'selectedbudgetid':budgetid}

@register.filter(name='class_name')
def class_name1(obj):
  return obj.__class__.__name__

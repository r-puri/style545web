from django import template
from style545app.models import Categorymaster
from style545app.models import Itemmaster
from style545app.models import Looksmaster
from style545app.models import Bodymaster
from style545app.models import Occassionmaster
from style545app.models import Stylemaster
from style545app.models import Budgetmaster





register = template.Library()

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

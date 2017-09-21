from django import template
from style545app.models import Categorymaster
from style545app.models import Itemmaster

register = template.Library()

@register.inclusion_tag('style545app/category.html')
def get_category_list():
    return {'cats': Categorymaster.objects.all()}

@register.inclusion_tag('style545app/items.html')
def get_item_list():
    return {'items': Itemmaster.objects.all()}

@register.inclusion_tag('style545app/items.html')
def get_item_list_by_cat(selectedid):
    return {'items': Itemmaster.objects.all().filter(itemcategoryid=selectedid)}

@register.filter(name='class_name')
def class_name1(obj):
  return obj.__class__.__name__

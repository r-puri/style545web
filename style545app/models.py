# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models

from django.template.defaultfilters import slugify

from django.db import connection
class MY_UTIL():
    def get_looks(self,cid):
        cursor = connection.cursor()
        #cursor.callproc("Style545.Get_Customer", ())# calls PROCEDURE named LOG_MESSAGE which resides in MY_UTIL Package
        cursor.execute('call style545.GetLooks('+str(cid)+');')
        ret = cursor.fetchall()
        cursor.close()
        return ret

class MyModel(models.Model):
    def class_name(self):
        return "%s"%(slugify(self.name))

class Algoresults(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId')  # Field name made lowercase.
    lookid = models.IntegerField(db_column='LookID')  # Field name made lowercase.
    customer_name = models.CharField(db_column='Customer_Name', max_length=50, blank=True)  # Field name made lowercase.
    look_name = models.CharField(db_column='Look_Name', max_length=50, blank=True)  # Field name made lowercase.
    match_reason = models.CharField(db_column='Match_Reason', max_length=4000, blank=True)  # Field name made lowercase.
    match_reason_code = models.IntegerField(db_column='Match_Reason_Code', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ALGORESULTS'


class Algoresults09062017(models.Model):
    id = models.BigIntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId')  # Field name made lowercase.
    lookid = models.IntegerField(db_column='LookID')  # Field name made lowercase.
    customer_name = models.CharField(db_column='Customer_Name', max_length=50, blank=True)  # Field name made lowercase.
    look_name = models.CharField(db_column='Look_Name', max_length=50, blank=True)  # Field name made lowercase.
    match_reason = models.CharField(db_column='Match_Reason', max_length=4000, blank=True)  # Field name made lowercase.
    match_reason_code = models.IntegerField(db_column='Match_Reason_Code', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ALGORESULTS_09062017'


class Algoresults090620172(models.Model):
    id = models.BigIntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId')  # Field name made lowercase.
    lookid = models.IntegerField(db_column='LookID')  # Field name made lowercase.
    customer_name = models.CharField(db_column='Customer_Name', max_length=50, blank=True)  # Field name made lowercase.
    look_name = models.CharField(db_column='Look_Name', max_length=50, blank=True)  # Field name made lowercase.
    match_reason = models.CharField(db_column='Match_Reason', max_length=4000, blank=True)  # Field name made lowercase.
    match_reason_code = models.IntegerField(db_column='Match_Reason_Code', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ALGORESULTS_09062017_2'


class Budgetmaster(models.Model):
    budgetid = models.IntegerField(db_column='BudgetID', primary_key=True)  # Field name made lowercase.
    budgetname = models.CharField(db_column='BudgetName', max_length=50)  # Field name made lowercase.
    likebudgetid1 = models.IntegerField(db_column='LikeBudgetID1', blank=True, null=True)  # Field name made lowercase.
    likebudgetid2 = models.IntegerField(db_column='LikeBudgetID2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BUDGETMASTER'

class Surveymaster(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    surveyname = models.CharField(db_column='SurveyName', max_length=100)  # Field name made lowercase.
    vendorid = models.ForeignKey('Vendormaster', db_column='VendorID')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    surveykey = models.CharField(db_column='SurveyKey', max_length=45, blank=True)  # Field name made lowercase.


    class Meta:
        managed = False
        db_table = 'SURVEYMASTER'

class Customermaster(models.Model):
    customerid = models.IntegerField(db_column='CustomerID', primary_key=True)  # Field name made lowercase.
    customer_name = models.CharField(db_column='Customer_Name', max_length=50)  # Field name made lowercase.
    customer_email = models.CharField(db_column='Customer_Email', max_length=50, blank=True)  # Field name made lowercase.
    customer_dob = models.CharField(db_column='Customer_DOB', max_length=50, blank=True)  # Field name made lowercase.
    customer_age = models.CharField(db_column='Customer_Age',max_length=100, blank=True, null=True)  # Field name made lowercase.
    customer_topsize = models.CharField(db_column='Customer_TopSize', max_length=100, blank=True)  # Field name made lowercase.
    customer_dresssize = models.CharField(db_column='Customer_DressSize', max_length=100, blank=True)  # Field name made lowercase.
    customer_current_occid = models.IntegerField(db_column='Customer_Current_OccID')  # Field name made lowercase.
    customer_current_styleid = models.IntegerField(db_column='Customer_Current_StyleID')  # Field name made lowercase.
    customer_current_styleid_secondary = models.IntegerField(db_column='Customer_Current_StyleID_Secondary')  # Field name made lowercase.
    customer_current_budgetid = models.IntegerField(db_column='Customer_Current_BudgetID')  # Field name made lowercase.
    customer_bodytype = models.CharField(db_column='Customer_BodyType', max_length=50, blank=True)  # Field name made lowercase.
    customer_actual_budget = models.IntegerField(db_column='Customer_Actual_Budget', blank=True, null=True)  # Field name made lowercase.
    customer_pantsize = models.CharField(db_column='Customer_PantSize', max_length=100, blank=True)  # Field name made lowercase.
    customer_celebrity_closet = models.CharField(db_column='Customer_Celebrity_Closet', max_length=100, blank=True)  # Field name made lowercase.
    customer_comments = models.CharField(db_column='Customer_Comments', max_length=200, blank=True)  # Field name made lowercase.
    surveyid = models.ForeignKey('Surveymaster', db_column='SurveyID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUSTOMERMASTER'


class Categorymaster(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    categoryname = models.CharField(db_column='CategoryName', max_length=200)  # Field name made lowercase.

    def class_name(self):
        return "%s"%(slugify(self.name))
    class Meta:
        managed = False
        db_table = 'CATEGORYMASTER'


class Bodymaster(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    bodytype = models.CharField(db_column='Bodytype', max_length=45)  # Field name made lowercase.

    def class_name(self):
        return "%s"%(slugify(self.name))
    class Meta:
        managed = False
        db_table = 'BODYMASTER'

class Vendormaster(models.Model):
    id = models.IntegerField(db_column='idVENDORMASTER', primary_key=True)  # Field name made lowercase.
    Vendorname = models.CharField(db_column='VendorName', max_length=100)  # Field name made lowercase.

    def class_name(self):
        return "%s"%(slugify(self.name))
    class Meta:
        managed = False
        db_table = 'VENDORMASTER'


class Itemmaster(models.Model):
    itemid = models.IntegerField(db_column='ItemID', primary_key=True)  # Field name made lowercase.
    item_name = models.CharField(db_column='Item_Name', max_length=50, blank=True)  # Field name made lowercase.
    item_desc = models.CharField(db_column='Item_Desc', max_length=4000, blank=True)  # Field name made lowercase.
    item_designer = models.CharField(db_column='Item_Designer', max_length=4000, blank=True)  # Field name made lowercase.
    itemurl = models.CharField(db_column='ItemURL', max_length=4000, blank=True)  # Field name made lowercase.
    itemimageurl = models.CharField(db_column='ItemImageURL', max_length=4000, blank=True)  # Field name made lowercase.
    item_price = models.IntegerField(db_column='Item_Price', blank=True, null=True)  # Field name made lowercase.
    item_sku = models.IntegerField(db_column='Item_SKU', blank=True, null=True)  # Field name made lowercase.
    item_color = models.CharField(db_column='Item_Color', max_length=50, blank=True)  # Field name made lowercase.
    likeitemid1 = models.CharField(db_column='LikeItemID1', max_length=10, blank=True)  # Field name made lowercase.
    likeitemid2 = models.CharField(db_column='LikeItemID2', max_length=10, blank=True)  # Field name made lowercase.
    item_inventory = models.IntegerField(db_column='Item_Inventory', blank=True, null=True)  # Field name made lowercase.
    itemcategoryid = models.IntegerField(db_column='ItemCategoryID', blank=True, null=True)  # Field name made lowercase.
    item_size = models.IntegerField(db_column='Item_size', blank=True, null=True)  # Field name made lowercase.


    class Meta:
        managed = False
        db_table = 'ITEMMASTER'


class Looksmaster(models.Model):
    lookid = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    lookname = models.CharField(db_column='LookName', max_length=50)  # Field name made lowercase.
    custom_tag_bodytype1 = models.CharField(db_column='Custom_Tag_BodyType1', max_length=50, blank=True)  # Field name made lowercase.
    custom_tag_bodytype2 = models.CharField(db_column='Custom_Tag_BodyType2', max_length=50, blank=True)  # Field name made lowercase.
    custom_tag_bodytype3 = models.CharField(db_column='Custom_Tag_BodyType3', max_length=50, blank=True)  # Field name made lowercase.
    custom_tag_bodytype4 = models.CharField(db_column='Custom_Tag_BodyType4', max_length=50, blank=True)  # Field name made lowercase.
    custom_tag_bodytype5 = models.CharField(db_column='Custom_Tag_BodyType5', max_length=50, blank=True)  # Field name made lowercase.
    custom_tag_agerangelow = models.IntegerField(db_column='Custom_Tag_AgeRangeLow', blank=True, null=True)  # Field name made lowercase.
    custom_tag_agerangehigh = models.IntegerField(db_column='Custom_Tag_AgeRangeHigh', blank=True, null=True)  # Field name made lowercase.
    look_active = models.CharField(db_column='Look_Active', max_length=50, blank=True)  # Field name made lowercase.
    occid = models.IntegerField(db_column='OccID')  # Field name made lowercase.
    styleid = models.IntegerField(db_column='StyleID')  # Field name made lowercase.
    budgetid = models.IntegerField(db_column='BudgetID')  # Field name made lowercase.
    item1id = models.IntegerField(db_column='Item1ID')  # Field name made lowercase.
    item2id = models.IntegerField(db_column='Item2ID')  # Field name made lowercase.
    item3id = models.IntegerField(db_column='Item3ID', blank=True, null=True)  # Field name made lowercase.
    item4id = models.IntegerField(db_column='Item4ID', blank=True, null=True)  # Field name made lowercase.
    item5id = models.IntegerField(db_column='Item5ID', blank=True, null=True)  # Field name made lowercase.
    item6id = models.IntegerField(db_column='Item6ID', blank=True, null=True)  # Field name made lowercase.
    item7id = models.IntegerField(db_column='Item7ID', blank=True, null=True)  # Field name made lowercase.
    likeoccid_1 = models.IntegerField(db_column='LikeOccID_1', blank=True, null=True)  # Field name made lowercase.
    likeoccid_2 = models.IntegerField(db_column='LikeOccID_2', blank=True, null=True)  # Field name made lowercase.
    likeoccid_3 = models.IntegerField(db_column='LikeOccID_3', blank=True, null=True)  # Field name made lowercase.
    likestyleid_1 = models.IntegerField(db_column='LikeStyleID_1', blank=True, null=True)  # Field name made lowercase.
    likestyleid_2 = models.IntegerField(db_column='LikeStyleID_2', blank=True, null=True)  # Field name made lowercase.
    likestyleid_3 = models.IntegerField(db_column='LikeStyleID_3', blank=True, null=True)  # Field name made lowercase.
    customer_ranking = models.IntegerField(db_column='Customer_Ranking', blank=True, null=True)  # Field name made lowercase.
    style545_ranking = models.IntegerField(db_column='Style545_Ranking', blank=True, null=True)  # Field name made lowercase.
    look_stylist = models.CharField(db_column='Look_Stylist', max_length=50, blank=True)  # Field name made lowercase.


    class Meta:
        managed = False
        db_table = 'LOOKSMASTER'





class Occassionmaster(models.Model):
    occassionid = models.IntegerField(db_column='OccassionID', primary_key=True)  # Field name made lowercase.
    occassion_name = models.CharField(db_column='Occassion_Name', max_length=50, blank=True)  # Field name made lowercase.
    likeocassionid1 = models.IntegerField(db_column='LikeOcassionID1', blank=True, null=True)  # Field name made lowercase.
    likeoccassionid2 = models.CharField(db_column='LikeOccassionID2', max_length=10, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OCCASSIONMASTER'


class Stylemaster(models.Model):
    styleid = models.IntegerField(db_column='StyleID', primary_key=True)  # Field name made lowercase.
    stylename = models.CharField(db_column='StyleName', max_length=50)  # Field name made lowercase.
    likestyleid1 = models.IntegerField(db_column='LikeStyleID1', blank=True, null=True)  # Field name made lowercase.
    likestyleid2 = models.IntegerField(db_column='LikeStyleID2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'STYLEMASTER'

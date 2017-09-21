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
    id = models.BigIntegerField(db_column='ID')  # Field name made lowercase.
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
    id = models.BigIntegerField(db_column='ID')  # Field name made lowercase.
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


class Categorymaster(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    categoryname = models.CharField(db_column='CategoryName', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CATEGORYMASTER'


class Customermaster(models.Model):
    customerid = models.IntegerField(db_column='CustomerID', primary_key=True)  # Field name made lowercase.
    customer_name = models.CharField(db_column='Customer_Name', max_length=50)  # Field name made lowercase.
    customer_email = models.CharField(db_column='Customer_Email', max_length=50, blank=True)  # Field name made lowercase.
    customer_dob = models.CharField(db_column='Customer_DOB', max_length=50, blank=True)  # Field name made lowercase.
    customer_age = models.IntegerField(db_column='Customer_Age', blank=True, null=True)  # Field name made lowercase.
    customer_size1id = models.IntegerField(db_column='Customer_Size1ID', blank=True, null=True)  # Field name made lowercase.
    customer_size2id = models.IntegerField(db_column='Customer_Size2ID', blank=True, null=True)  # Field name made lowercase.
    customer_current_occid = models.IntegerField(db_column='Customer_Current_OccID')  # Field name made lowercase.
    customer_current_styleid = models.IntegerField(db_column='Customer_Current_StyleID')  # Field name made lowercase.
    customer_current_budgetid = models.IntegerField(db_column='Customer_Current_BudgetID')  # Field name made lowercase.
    customer_bodytype = models.CharField(db_column='Customer_BodyType', max_length=50, blank=True)  # Field name made lowercase.
    customer_actual_budget = models.IntegerField(db_column='Customer_Actual_Budget', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUSTOMERMASTER'


class Customers(models.Model):
    customerid = models.IntegerField(db_column='CustomerID')  # Field name made lowercase.
    coccasion = models.CharField(db_column='cOccasion', max_length=25, blank=True)  # Field name made lowercase.
    cbudget = models.BigIntegerField(db_column='cBudget', blank=True, null=True)  # Field name made lowercase.
    cstyle = models.CharField(db_column='cStyle', max_length=25, blank=True)  # Field name made lowercase.
    age = models.CharField(max_length=25, blank=True)
    cbodytype = models.CharField(db_column='cBodyType', max_length=25, blank=True)  # Field name made lowercase.
    cname = models.CharField(db_column='cName', max_length=25, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Customers'


class Itemmaster(models.Model):
    itemid = models.IntegerField(db_column='ItemID', primary_key=True)  # Field name made lowercase.
    item_name = models.CharField(db_column='Item_Name', max_length=50, blank=True)  # Field name made lowercase.
    item_desc = models.CharField(db_column='Item_Desc', max_length=4000, blank=True)  # Field name made lowercase.
    item_designer = models.CharField(db_column='Item_Designer', max_length=4000, blank=True)  # Field name made lowercase.
    itemurl = models.CharField(db_column='ItemURL', max_length=4000, blank=True)  # Field name made lowercase.
    item_price = models.IntegerField(db_column='Item_Price', blank=True, null=True)  # Field name made lowercase.
    item_sku = models.IntegerField(db_column='Item_SKU', blank=True, null=True)  # Field name made lowercase.
    item_color = models.CharField(db_column='Item_Color', max_length=50, blank=True)  # Field name made lowercase.
    likeitemid1 = models.CharField(db_column='LikeItemID1', max_length=10, blank=True)  # Field name made lowercase.
    likeitemid2 = models.CharField(db_column='LikeItemID2', max_length=10, blank=True)  # Field name made lowercase.
    item_inventory = models.IntegerField(db_column='Item_Inventory', blank=True, null=True)  # Field name made lowercase.
    itemimageurl = models.CharField(db_column='ItemImageURL', max_length=4000, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITEMMASTER'


class Looksmaster(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
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


class Looks(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    occasion = models.CharField(db_column='Occasion', max_length=25, blank=True)  # Field name made lowercase.
    budget = models.BigIntegerField(db_column='Budget', blank=True, null=True)  # Field name made lowercase.
    style = models.CharField(db_column='Style', max_length=25, blank=True)  # Field name made lowercase.
    bodytype = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=25, blank=True)

    class Meta:
        managed = False
        db_table = 'Looks'


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


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class RangoUserprofile(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    website = models.CharField(max_length=200)
    picture = models.CharField(max_length=100)
    user = models.ForeignKey(AuthUser, unique=True)

    class Meta:
        managed = False
        db_table = 'rango_userprofile'


class RegistrationRegistrationprofile(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    activation_key = models.CharField(max_length=40)
    user = models.ForeignKey(AuthUser, unique=True)
    activated = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'registration_registrationprofile'


class RegistrationSupervisedregistrationprofile(models.Model):
    registrationprofile_ptr = models.ForeignKey(RegistrationRegistrationprofile, primary_key=True)

    class Meta:
        managed = False
        db_table = 'registration_supervisedregistrationprofile'

use style545;
SET SQL_SAFE_UPDATES = 0;
Update ITEMMASTER, CategoryMaster
Set ITEMMASTER.itemCategoryID = CategoryMaster.ID
Where CategoryMaster.CategoryName=itemmaster.itemCategoryID;

Select * from itemmaster
Select * from CategoryMaster

Insert Into CategoryMaster (CategoryName)   (
Select distinct itemCategoryID from itemmaster where itemcategoryid not in ('0','37'))

Insert into CategoryMaster (categoryName) values ('0')
Update itemmaster set itemCategoryID='1' where itemCategoryID='37'

LOAD DATA LOCAL INFILE '/Users/rohanpuri/downloads/SHOP_Item Data Load/SHOP Load-Table 1.csv' INTO TABLE style545.ITEMMASTER_BACKUP FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' (ItemID,Item_Name,Item_desc,Item_designer,ItemURL,Item_SKU,Item_Color,LikeItemID1,LikeItemID2,Item_Inventory,ItemImageURL,ItemCategoryID,Item_Size) \w;
use style545;
SET SQL_SAFE_UPDATES = 0;
Update ITEMMASTER, CategoryMaster
Set ITEMMASTER.itemCategoryID = CategoryMaster.ID
Where CategoryMaster.CategoryName=itemmaster.itemCategoryID;

--Update the urls
Update ITEMMASTER
Set ItemImageURL=Replace (ItemImageURL,'drive.google.com/open','docs.google.com/uc');

--Update bad images
Update ITEMMASTER set itemimageurl='0' where itemimageurl ='Y' or itemimageurl='No images available' or itemimageurl='No images online';

--Update basic item
Update ITEMMASTER  set itemimageurl='https://storage.googleapis.com/wzukusers/user-29032408/images/595d35dcaad07y65ba2d/Screen-Shot-2017-07-05-at-1.53.49-PM_d400.png'
where itemid=0



Select * from itemmaster where itemimageurl <> '0' 
Update itemmaster set itemimageurl='https://lh3.googleusercontent.com/zPZo2WPNXMTaBbnnpB7VQdNc5L6fq4oO_7QSL1tDjMaocJJVB-PtZeuY8Z8wIYElerNqbQ6gLT-RaG4=w1804-h1352' where itemid=5979
Select * from CategoryMaster

Insert Into CategoryMaster (CategoryName)   (
Select distinct itemCategoryID from itemmaster where itemcategoryid not in ('0','37'))

Insert into CategoryMaster (categoryName) values ('0')
Update itemmaster set itemCategoryID='1' where itemCategoryID='37'

LOAD DATA LOCAL INFILE '/Users/rohanpuri/downloads/SHOP_Item Data Load/SHOP Load-Table 1.csv' INTO TABLE style545.ITEMMASTER_BACKUP FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' (ItemID,Item_Name,Item_desc,Item_designer,ItemURL,Item_SKU,Item_Color,LikeItemID1,LikeItemID2,Item_Inventory,ItemImageURL,ItemCategoryID,Item_Size) \w;
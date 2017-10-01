SET SQL_SAFE_UPDATES = 0;
Update ITEMMASTER_Backup , CategoryMaster
Set ITEMMASTER_Backup.itemCategoryID = CategoryMaster.ID
Where CategoryMaster.CategoryName=itemmaster_backup.itemCategoryID;

LOAD DATA LOCAL INFILE '/Users/rohanpuri/downloads/SHOP_Item Data Load/SHOP Load-Table 1.csv' INTO TABLE style545.ITEMMASTER_BACKUP FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' (ItemID,Item_Name,Item_desc,Item_designer,ItemURL,Item_SKU,Item_Color,LikeItemID1,LikeItemID2,Item_Inventory,ItemImageURL,ItemCategoryID,Item_Size);
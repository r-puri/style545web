
$(document).ready(function() {


       //sets onchange function for categories
       var mylist=[]
       mylist=$("#itemnumber").val().split(",");

       //gets items per category
       var catid;
       catid = $(this).find(":selected").val();
       $.getJSON('/style545app/getitemsbycat/', {category_id: catid}, function(data){
                 $ (mylist).each(function(itemnumber){ itemnumber=itemnumber+1;
                 $("#item"+itemnumber+" option").remove();
                 $.each(data.results, function(index, item) { // Iterates through a collection
                  $("#item"+itemnumber).append( // Append an object to the inside of the select box
                      $("<option></option>") // Yes you can do this.
                          .text(item.item_name)
                          .val(JSON.stringify(item)))

       });
       //after listbox loads set the default price
       value=$("#item"+itemnumber).eq(0).val() ; getprice(value,itemnumber)   ;
       //set default image
       url=JSON.parse(value)["itemimageurl"];
       if (url == "0") {
         url="https://storage.googleapis.com/wzukusers/user-29032408/images/595d35dcaad07y65ba2d/Screen-Shot-2017-07-05-at-1.53.49-PM_d400.png";
       }
       $("#itemimage"+itemnumber).attr('src',url);
       });
       });

       //sets onchange function for categories
       $ (mylist).each(function(itemnumber){ itemnumber=itemnumber+1;
         $('#selectcategory-'+itemnumber).change(function(){
             var catid;
             catid = $(this).find(":selected").val();
             $.getJSON('/style545app/getitemsbycat/', {category_id: catid}, function(data){
                       $("#item"+itemnumber+ " option").remove();
                       $.each(data.results, function(index, item) { // Iterates through a collection
                        $("#item"+itemnumber).append( // Append an object to the inside of the select box
                            $("<option></option>") // Yes you can do this.
                                .text(item.item_name)
                                .val(JSON.stringify(item)))
             });
             value=$("#item"+itemnumber).eq(0).val() ; getprice(value,itemnumber)   ;
             //set default image
             url=JSON.parse(value)["itemimageurl"];
             if (url == "0") {
               url="https://storage.googleapis.com/wzukusers/user-29032408/images/595d35dcaad07y65ba2d/Screen-Shot-2017-07-05-at-1.53.49-PM_d400.png";
             }
             $("#itemimage"+itemnumber).attr('src',url);
         });
       });
       });
       //set price for all price boxes by default





});//main

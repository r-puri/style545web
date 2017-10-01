$(document).ready(function() {


var mylist=[]
mylist=$("#itemnumber").val().split(",");
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
      //set price for the first item in new list box
      value=$("#item"+itemnumber).eq(0).val() ;
      getprice(value,itemnumber)   ;
  });
});///change function ends
});//item counter ends

});//main

function removeitem(itemnumber){
      var catid;
      catid=0;
      $('#selectcategory-'+itemnumber).val(catid);
    //  catid = $('#selectcategory-'+itemnumber).find(":selected").val();
      $.getJSON('/style545app/getitemsbycat/', {category_id: catid}, function(data){
                $("#item"+itemnumber+ " option").remove();
                $.each(data.results, function(index, item) { // Iterates through a collection
                 $("#item"+itemnumber).append( // Append an object to the inside of the select box
                     $("<option></option>") // Yes you can do this.
                         .text(item.item_name)
                         .val(JSON.stringify(item)))

      });
      //set price for the first item in new list box
      value=$("#item"+itemnumber).eq(0).val() ;
      getprice(value,itemnumber)   ;
  });
      return this;
   };

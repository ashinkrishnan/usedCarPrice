function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var Car_Company  = document.getElementById("uiCar_Company");
    var Fuel_Type    = document.getElementById("uiFuel_Type");
    var Transmission = document.getElementById("uiTransmission");
    var Owner_Type   = document.getElementById("uiOwner_Type");
    var Location     = document.getElementById("uiLocation");


    var Car_Model   = document.getElementById("uiCar_Model");
    var Engine_CC   = document.getElementById("uiEngine_CC");
    var Power_bhp   = document.getElementById("uiPower_bhp");
    var Mileage_kmpl= document.getElementById("uiMileage_kmpl");
    var Kilometers_Driven = document.getElementById("uiKilometers_Driven");
    var Year   = document.getElementById("uiYear");

    var estPrice = document.getElementById("uiEstimatedPrice");
  
    var url = "/api/predict_car_price"; 
    //var url = "http://127.0.0.1:5000/predict_car_price";
    
  
    $.post(url, {
        Car_Company  : Car_Company.value,
        Car_Model    : Car_Model.value,
        Engine_CC: parseFloat(Engine_CC.value),
        Power_bhp: parseFloat(Power_bhp.value),
        Mileage_kmpl : parseFloat(Mileage_kmpl.value),
        Kilometers_Driven : parseInt(Kilometers_Driven.value),
        Fuel_Type : Fuel_Type.value,
        Transmission: Transmission.value,
        Owner_Type : Owner_Type.value,
        Year : parseInt(Year.value),
        Location : Location.value
        

    },function(data, status) {
        console.log(data.Estimated_Price);
        estPrice.innerHTML = "<h2>" + data.Estimated_Price.toString() + " Lakhs</h2>";
        console.log(status);
    });
}



function onPageLoadLoc() {
    console.log( "document loaded" );
    //var url = "http://127.0.0.1:5000/get_location"
    var url = "/api/get_location"; 
    $.get(url,function(data, status) {
        console.log("got response for get_location_names request");
        if(data) {
            var location = data.location;
            var uiLocation = document.getElementById("uiLocation");
            $('#uiLocation').empty();
            for(var i in location) {
                var opt = new Option(location[i]);
                $('#uiLocation').append(opt);
            }
        }
    });
}
  


function onPageLoadCompany() {
    console.log( "document loaded" );
    //var url = "http://127.0.0.1:5000/get_company_names"
    var url = "/api/get_company_names"; 
    $.get(url,function(data, status) {
        console.log("got response for get_company_names request");
        if(data) {
            var Car_Company = data.company;
            var uiCar_Company = document.getElementById("uiCar_Company");
            $('#uiCar_Company').empty();
            for(var i in Car_Company) {
                var opt = new Option(Car_Company[i]);
                $('#uiCar_Company').append(opt);
            }
        }
    });
}

function onPageLoadFuel() {
    console.log( "document loaded" );
    //var url = "http://127.0.0.1:5000/get_fuel"
    var url = "/api/get_fuel"; 
    $.get(url,function(data, status) {
        console.log("got response for get_fuel request");
        if(data) {
            var Fuel_Type = data.fuel;
            var uiFuel_Type = document.getElementById("uiFuel_Type");
            $('#uiFuel_Type').empty();
            for(var i in Fuel_Type) {
                var opt = new Option(Fuel_Type[i]);
                $('#uiFuel_Type').append(opt);
            }
        }
    });
}

function onPageLoadTrans() {
    console.log("document loaded");
    //var url = "http://127.0.0.1:5000/get_transmission"
    var url = "/api/get_transmission";
    $.get(url,function(data, status){
        console.log("got response for get_transmission request");
        if (data){
            var Transmission = data.transmission;
            var uiTransmission = document.getElementById("uiTransmission");
            $('#uiTransmission').empty();
            for (var i in Transmission){
                var opt = new Option(Transmission[i]);
                $('#uiTransmission').append(opt);
            }
        }
    });
}


function onPageLoadOwner() {
    console.log( "document loaded" );
    //var url = "http://127.0.0.1:5000/get_owner"
    var url = "/api/get_owner"; 
    $.get(url,function(data, status) {
        console.log("got response for get_owner request");
        if(data) {
            var Owner_Type = data.owner;
            var uiOwner_Type = document.getElementById("uiOwner_Type");
            $('#uiOwner_Type').empty();
            for(var i in Owner_Type) {
                var opt = new Option(Owner_Type[i]);
                $('#uiOwner_Type').append(opt);
            }
        }
    });
}



function AddOnloadEvent(f) {
    if(typeof window.onload != 'function') { window.onload = f; }
    else {
       var cache = window.onload;
       window.onload = function() {
          if(cache) { cache(); }
          f();
          };
       }
}
    

AddOnloadEvent(onPageLoadCompany);    
AddOnloadEvent(onPageLoadFuel);
AddOnloadEvent(onPageLoadOwner);
AddOnloadEvent(onPageLoadLoc);
AddOnloadEvent(onPageLoadTrans);










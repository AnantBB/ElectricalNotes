
function shape_selected() {                                   
    if (document.getElementById("id_shape").value == '1'){
        document.getElementById("id_Width_to_thickness_ratio").value = 1;        
        //document.getElementById("id_Width_to_thickness_ratio").disabled = true; 
    } else if (document.getElementById("id_shape").value == '2'){
        document.getElementById("id_Width_to_thickness_ratio").value = '1';
        document.getElementById("id_Width_to_thickness_ratio").disabled = true;
    } else if (document.getElementById("id_shape").value == '3'){
        document.getElementById("id_Width_to_thickness_ratio").disabled = false;
    }               
}

function material_selected() {
    if (document.getElementById("id_material").value == '1'){                
        document.getElementById("id_temperature_coefficient").value = 0.00386;                 
    } else if (document.getElementById("id_material").value == '2'){
        document.getElementById("id_temperature_coefficient").value = 0.00429;                
    } else if (document.getElementById("id_material").value == '3'){
        document.getElementById("id_temperature_coefficient").value = 0.0038;
    }
    document.getElementById("id_temperature_coefficient").disabled = true;

}

function ambient_temp_selected(){            
    var l = document.getElementById("id_wire_length").value;
    var a = document.getElementById("id_cross_section").value;
    var m = document.getElementById("id_material").value;
    var roh;
    if (m == 1){ 
        roh = 0.0168;
    }else if (m == 2){
        roh = 0.0256;
    }else if (m == 3){
        roh = 0.0159;
    }            
    document.getElementById("id_resistance").value = (roh*l/a).toFixed(5);
}

function diss_area_selected(){    
    var l = document.getElementById("id_wire_length").value;
    var r = document.getElementById("id_Radius_of_Chamfer").value;
    var a = document.getElementById("id_cross_section").value;
    var wt = document.getElementById("id_Width_to_thickness_ratio").value;
    var s = document.getElementById("id_shape").value;
    var f = (document.getElementById("id_dissipation_area").value / 100);    
    if(s == 1){
        p = 2*Math.PI*(Math.sqrt(a/Math.PI));        /* circular */
    }else if (s == 2){
        p = (4*Math.sqrt(a))-(8*r)+(2*Math.PI*r);    /* square */
    }else {                
        p = (2*Math.sqrt(wt/a))+(2*wt*Math.sqrt(wt/a))-(8*r)+(2*Math.PI*r);   /*  rectangle */        
    }    
    document.getElementById("id_surface_area").value = (f * p * l * 10).toFixed(5); 
}

function cond_weigth_calc(){
    var l = document.getElementById("id_wire_length").value;
    var a = document.getElementById("id_cross_section").value;
    var m = document.getElementById("id_material").value;
    var Cp ;

    if(m == 1){                      /* g/cm^3 */
        density = 8.96;              /* J/kg-C */
        Cp = 376.81;
    }
    else if(m == 2){
        density = 2.70;
        Cp = 921.09;
    }
    else if(m == 3){
        density = 10.49;
        Cp = 238.65;
    }
    document.getElementById("id_conductor_weight").value = (density * l * a * 0.001).toFixed(5); 
    document.getElementById("id_specific_heat").value = Cp;

}
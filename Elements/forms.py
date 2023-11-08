from django import forms
from .models import wire_spec
from django.forms import ModelForm

class wire_spec_form(ModelForm):
    class Meta:
        model = wire_spec
        fields = ['wire_length', 'cross_section', 'shape', 'Width_to_thickness_ratio', 
        'Radius_of_Chamfer', 'material', 'temperature_coefficient', 'ambient_temperature', 
        'resistance', 'dissipation_area', 'surface_area', 'conductor_weight', 'specific_heat', 
        'applied_source', 'source_type', 'peak_source_value', 'period_of_source_connection', 
        'step', 'frequency', 'temperature', 'internal_Energy', 'hot_Resistance']
        QUALIFIER1 = (('1','circular'), ('2','square'), ('3','rectangular'))
        QUALIFIER2 = (('1','copper'), ('2','aluminium'), ('3','silver'))
        QUALIFIER3 = (('1','voltage'), ('2','current'))
        QUALIFIER4 = (('1','constant'), ('2','sinusoidal'), ('3','square'), ('4', 'sawtooth'))
        widgets = {
            'shape': forms.Select(choices=QUALIFIER1,attrs={'class': 'form-control' , 'style': 
            'width: 190px', "onblur":"shape_selected()"}),            
            'material': forms.Select(choices=QUALIFIER2,attrs={'class': 'form-control' , 'style': 
            'width: 190px', "onblur":"material_selected()"}),
            'applied_source': forms.Select(choices=QUALIFIER3,attrs={'class': 'form-control' , 'style': 
            'width: 190px'}),
            'source_type': forms.Select(choices=QUALIFIER4,attrs={'class': 'form-control' , 'style': 
            'width: 190px'}),
            'temperature_coefficient': forms.TextInput(attrs={'disabled' : False }),
            'ambient_temperature': forms.TextInput(attrs={"onblur":"ambient_temp_selected()"}),
            'resistance': forms.TextInput(attrs={'disabled' : True}),
            'dissipation_area': forms.TextInput(attrs={"onblur":"diss_area_selected()"}),
            'specific_heat': forms.TextInput(attrs={'disabled' : True}),
            'surface_area': forms.TextInput(attrs={'disabled' : True, "onblur" : "cond_weigth_calc()"}),
            'conductor_weight': forms.TextInput(attrs={'disabled' : True })            
        }

        def __eq__(self):
            return f"{model.wire_length}"

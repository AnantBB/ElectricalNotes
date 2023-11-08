from django.shortcuts import render
from .graph import get_graph
from .forms import wire_spec_form
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from io import BytesIO
import base64

side_bar_show = False
# Create your views here.
def home(request):
    side_bar_show = True    
    return render(request, 'Elements/layout.html', context={'SB':side_bar_show})

def res_info(request):
    return render(request, 'Elements/res_info.html')

def res_calc(request):
    form = wire_spec_form()    
    return render(request, 'Elements/res_calc.html', context={'form': form})

def res_grph(request):
    conf_data=[['copper', 'circular', 'voltage', 'constant'],
    ['aluminium', 'square', 'current', 'sinusoidal'],
    ['silver', 'rectangular', 'none', 'square'],
    ['none', 'none', 'none', 'sawtooth']]
    if request.method == 'POST':        
        form = wire_spec_form(request.POST)
        print(request.POST['Width_to_thickness_ratio'])                                                            
        G1 = get_graph( conf_data[int(request.POST['material'])-1][0] , \
            conf_data[int(request.POST['shape'])-1][1], request.POST['wire_length'], \
            request.POST['cross_section'], request.POST['Width_to_thickness_ratio'], \
            request.POST['Radius_of_Chamfer'], request.POST['ambient_temperature'], \
            request.POST['ambient_temperature'], request.POST['dissipation_area'], \
            conf_data[int(request.POST['applied_source'])-1][2], \
            request.POST['peak_source_value'], conf_data[int(request.POST['source_type'])-1][3],\
            float(request.POST['frequency']), request.POST['step'], request.POST['period_of_source_connection'], 0)
        [i,t,r,v,c] = G1.graph_data                
        x =  list(range(0, len(r)))
        plt.figure()    
        four_graphs = [1,2,3,4]        
        for graph in four_graphs:
            plt.clf()
            if graph == 1:
                plt.plot(x, r)
                plt.xlabel('Time') 
                plt.ylabel('Resistance')            
            elif graph == 2:
                plt.plot(x, t)                
                plt.xlabel('Time')
                plt.ylabel('Temperature')
            elif graph == 3:
                plt.plot(x, i)                
                plt.xlabel('Time')                
                plt.ylabel('Internal Energy')
            elif graph == 4:
                plt.plot(x, v) 
                plt.plot(x, c)               
                plt.xlabel('Time')                
                plt.ylabel('Voltage and Current')
            buf = BytesIO()
            plt.grid()
            plt.savefig(buf, format='png')            
            buf.seek(0)
            string = base64.b64encode(buf.read())
            if graph == 1:
                graph1 = string.decode('utf-8')
            elif graph == 2:
                graph2 = string.decode('utf-8')
            elif graph == 3:
                graph3 = string.decode('utf-8') 
            elif graph == 4:
                graph4 = string.decode('utf-8')          
    elif request.method == 'GET':
        form = wire_spec_form(request.GET)                         
    return render(request, 'Elements/res_calc.html', 
                context={'form': form,
                        'TPmax' : format( t[len(t)-1], '.2f'),
                        'IEmax' : format( i[len(i)-1], '.0f'),
                        'HRmax' :format( r[len(r)-1], '.4f'),
                        'graph1': graph1,
                        'graph2': graph2,
                        'graph3': graph3,
                        'graph4': graph4                        
                         })
    

def indc_info(request):
    return render(request, 'Elements/indc_info.html')

def help(request):
    side_bar_show = False
    return render(request, 'Elements/help.html', context={'SB':side_bar_show})
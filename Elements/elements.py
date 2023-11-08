import math

m_data = [['copper',0.0168,0.00386,377, 8.954, 410],
        ['aluminium',0.0265, 0.00429,921, 2.707, 207],
        ['silver',0.0159, 0.0038,239, 10.51, 403]]

class Material:
    def __init__(self, name, internal_energy = 0):
        self.name = name
        self.internal_energy = internal_energy        
        self.property(name)

    def property(self, name):
        for x in m_data:
            if x[0] == self.name:
                if name == 'resistivity':
                    return x[1]
                elif name == 'temperature_coefficient':
                    return x[2]
                elif name == 'specific_heat':
                    return x[3]
                elif name == 'density':
                    return x[4]
                elif name == 'dissipation_rate':
                    return x[5]

    def get_data():
        return m_data


class Wire(Material):    
    def __init__(self, M, shape, length, cross_section, width_thickness_ratio, radius_of_chamfer):
         self.M = M
         self.shape = shape
         self.length = length
         self.cross_section = cross_section                           
         self.width_thickness_ratio = width_thickness_ratio         
         self.radius_of_chamfer = radius_of_chamfer
         self.conductor_weight(M)

    def conductor_weight(self, M):
        l = float(self.length)
        a = float(self.cross_section)
        d = M.property('density')
        return d*l*a*0.001


class Resistor(Wire):
    def __init__(self, W, temperature, ambient_temperature, available_dissipation_area):
        self.W = W
        self.ambient_temperature = float(ambient_temperature)
        self.temperature = float(temperature)
        self.available_dissipation_area = float(available_dissipation_area)       
        self.resistance(W)
        self.surface_area(W)

    def resistance(self, W):           
        Tres = float(self.temperature)
        Tamb = float(self.ambient_temperature)
        alpha = W.M.property('temperature_coefficient')
        rho = W.M.property('resistivity')
        l = float(W.length)
        a = float(W.cross_section)
        R = rho * l / a
        if Tres > Tamb:
            Tdel = Tres - Tamb
            return R*(1+alpha *Tdel)
        else:
            return R

    def surface_area(self, W):
        l = float(W.length)
        a = float(W.cross_section)
        Cfr = float(W.radius_of_chamfer)
        Wtr = float(W.width_thickness_ratio)
        Da = float(self.available_dissipation_area)        
        if W.shape == 'circular':
            return (math.sqrt((math.pi) * a) * 2  * l * (Da/100))
        elif W.shape == 'rectangular' or  W.shape == 'square' :
            t = math.sqrt((a+pow(Cfr,2)*(4-math.pi))/Wtr)
            w = math.sqrt((a+pow(Cfr,2)*(4-math.pi))*Wtr)                         
            return (((2*w)+(2*t)-(8*Cfr)+(2*math.pi*Cfr))*l*(Da/100))


class Source():
    def __init__(self, type, max_value, waveform, f, step, period, current_time):        
        self.type = type
        self.max_value = float(max_value)
        self.waveform = waveform
        self.f = f      
        self.step = float(step)*0.001
        self.period = float(period)
        self.current_time = float(current_time)
        self.frequency()        
        self.time()
        self.value(f)

    def frequency(self):
        if self.waveform == 'constant':
            return 0
        elif self.waveform == 'sinusoidal':
            return self.f
        elif self.waveform == 'square':
            return self.f
        elif self.waveform == 'sawtooth':
            return self.f

    def time(self):
        if self.current_time < self.period :
            self.current_time = self.current_time + self.step
            return self.current_time
        else:
            return self.period
    
    def value(self, f):
        if self.waveform == 'constant':
            return self.max_value
        elif self.waveform == 'sinusoidal':
            return self.max_value * math.sin(2*math.pi*f * self.current_time)
        elif self.waveform == 'square':            
            if  math.ceil( self.current_time * 2 * f ) % 2 == 0:
                return self.max_value
            else:
                return (-1 * self.max_value)
        elif self.waveform == 'sawtooth':
            m = self.max_value
            if self.current_time < 1/f :
                return m * (self.current_time/(1/f))
            else:
                t = (self.current_time/(1/f)) % 1
                return m * t


class Graph:
    def __init__(self, index, data_value, graph_data = [[],[],[],[],[]] ):
        self.index = index
        self.data_value = data_value
        self.graph_data = graph_data                        
        self.store(index, graph_data, data_value, pram_index =0)        


    def store(self, index, graph_data, data_value, pram_index):
        if index > 0:            
            graph_data[pram_index].append(data_value)    


class Circuit:
    def __init__(self, R, S, G):        
        self.R = R
        self.S = S
        self.G = G
        self.energy_transfered(R, S, G)
        

    def energy_transfered(self, R, S, G):
        if self.S.type == 'voltage':
            i = 0
            R.temperature = R.ambient_temperature
            while(self.S.current_time < self.S.period):
                incremental_energy = S.value(S.f)* S.value(S.f) * self.S.step/R.resistance(R.W)                
                dissipated_energy = (R.W.M.property('dissipation_rate') * R.surface_area(R.W) * R.available_dissipation_area * (R.temperature - R.ambient_temperature) * self.S.step)/1000000
                self.R.W.M.internal_energy = self.R.W.M.internal_energy + incremental_energy - dissipated_energy
                G.store(i, G.graph_data, self.R.W.M.internal_energy, 0)                
                temperature_rise = self.R.W.M.internal_energy / (R.W.conductor_weight(R.W.M) * R.W.M.property('specific_heat'))
                self.R.temperature = self.R.ambient_temperature + temperature_rise
                G.store(i, G.graph_data, self.R.temperature, 1)                
                G.store(i, G.graph_data, R.resistance(R.W), 2)
                G.store(i, G.graph_data, S.value(S.f), 3)
                G.store(i, G.graph_data, S.value(S.f)/R.resistance(R.W), 4)                                            
                self.S.time()                
                i = i + 1
        return G.graph_data



# M1 = Material('copper')
# print(M1.property('temperature_coefficient'))
# print(M1.property('resistivity'))
# print(M1.property('specific_heat'))
# print(M1.property('density'))
# print(M1.property('dissipation_rate'))
# W1 = Wire(M1,'Rectangular', 50, 5, 2.25, 0.04)
# print(W1.shape)
# print(W1.length)
# print(W1.cross_section)
# print(W1.width_thickness_ratio)
# print(W1.radius_of_chamfer)
# print(W1.conductor_weight(M1))
# R1 = Resistor(W1, 29, 25, 80)
# print(R1.resistance(W1))
# print(R1.surface_area(W1))
# S1 = Source('voltage', 100, 'constant', 50, 8e-3, 200, 0)
# print(S1.frequency())
# print(S1.time())
# print(S1.value())
# G1 = Graph(0,0)
# C1 = Circuit(R1, S1, G1)
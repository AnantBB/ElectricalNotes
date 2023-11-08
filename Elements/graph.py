from Elements.elements import Material, Wire, Resistor,Source, Graph, Circuit
 
def get_graph(material, shape, length, cross_section, width_thickness_ratio, radius_of_chamfer,
               temperature, ambient_temperature, available_dissipation_area, type, max_value, 
               waveform, frequency, step, period, current_time ):           
    M1 = Material(material)
    W1 = Wire(M1, shape, length, cross_section, width_thickness_ratio, radius_of_chamfer)
    R1 = Resistor(W1,temperature, ambient_temperature, available_dissipation_area )
    S1 = Source(type, max_value, waveform, frequency, step, period, current_time)
    G1 = Graph(0, 0, graph_data = [[],[],[],[],[]])
    C1 = Circuit(R1, S1, G1)        
    return G1    
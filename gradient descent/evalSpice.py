import numpy as np

#declaring global variable for node mapping
global node_map
node_map = {'GND' : 0} 

#function for node mapping - adds unique nodes into dictionary
def getNodes(node):
    if node not in node_map:
        node_number = len(node_map)
        node_map[node] = node_number
    return node_map[node]

#function for solving the circuit
def evalSpice(filename):

    try:
        ckt_file = open(filename)
    except FileNotFoundError:
        raise FileNotFoundError("Please give the name of a valid SPICE file as input")
        
    ckt_read = ckt_file.readlines()
 
    #for resetting the node_map after each turn
    global node_map
    node_map = {'GND' : 0} 

    ckt_list = []
    ckt_mod = []
    ckt_final = []
    
    #for components data
    ckt_V = {}
    ckt_I = {}
    ckt_R = {}
    
    # to keep track of no. of each elements
    count_V = 0
    count_I = 0
    count_R = 0
    
    #splits the lines if # is found
    for lines in ckt_read:
        temp = lines.split('#')
        ckt_list.append(temp)
    
    #for ignoring the comments in the file
    for i in range (len(ckt_list)):
        ckt_mod.append(ckt_list[i][0])
    
    #for splitting into different components along with data and adding them to list
    for i in range(len(ckt_mod)):
        temp = ckt_mod[i].split()
        if temp == []:
            continue
        else:
            ckt_final.append(temp)

    #checking if the circuit is of correct format
    if ['.circuit'] not in ckt_final:
        raise ValueError("Malformed circuit file")
    elif ['.end'] not in ckt_final:
        raise ValueError("Malformed circuit file")
    else:
        #reading only between '.circuit' and '.end'
        for i in range(len(ckt_final)):
            if ckt_final[i][0] == '.circuit':
                for j in range(i+1, len(ckt_mod)):
                    if ckt_final[j][0] == '.end':
                        break
                    else:
                        
                        # formatting V components with respective data into dictionary
                        if ckt_final[j][0][0] == 'V':
                            try:
                                count_V += 1
                                cktV ={
                                'node1' : ckt_final[j][1],
                                'node2' : ckt_final[j][2],
                                'value' : float(ckt_final[j][4]),
                                'count' : count_V}
                                ckt_V[ckt_final[j][0]] = cktV
                            except IndexError:
                                raise ValueError("Parameters are missing")    
                        
                        # formatting I components with respective data into dictionary
                        elif ckt_final[j][0][0] == 'I':
                            try:
                                count_I += 1
                                cktI = {
                                'node1' : ckt_final[j][1],
                                'node2' : ckt_final[j][2],
                                'value' : float(ckt_final[j][4]),
                                'count' : count_I}
                                ckt_I[ckt_final[j][0]] = cktI
                            except IndexError:
                                raise ValueError("Parameters are missing")  

                        # formatting R components with respective data into dictionary
                        elif ckt_final[j][0][0] == 'R':
                            try:
                                count_R += 1
                                cktR = {
                                'node1' : ckt_final[j][1],
                                'node2' : ckt_final[j][2],
                                'value' : float(ckt_final[j][3]),
                                'count' : count_R}
                                ckt_R[ckt_final[j][0]] = cktR
                            except IndexError:
                                raise ValueError("Parameters are missing")      
                        else:
                            #making sure there are only V, I, R are there in netlist
                            raise ValueError("Only V, I, R elements are permitted")
            
            #node mapping for V sources
            for component, node_data in ckt_V.items():
                node_num1 = getNodes(node_data['node1'])
                node_num2 = getNodes(node_data['node2'])
                ckt_V[component]['node_num1'] = node_num1
                ckt_V[component]['node_num2'] = node_num2 
                
             #node mapping for R sources   
            for component, node_data in ckt_R.items():
                node_num1 = getNodes(node_data['node1'])
                node_num2 = getNodes(node_data['node2'])
                ckt_R[component]['node_num1'] = node_num1
                ckt_R[component]['node_num2'] = node_num2 
            
            #node mapping for I sources
            for component, node_data in ckt_I.items():
                node_num1 = getNodes(node_data['node1'])
                node_num2 = getNodes(node_data['node2'])
                ckt_I[component]['node_num1'] = node_num1
                ckt_I[component]['node_num2'] = node_num2  

            #building matrices of required size
            number_nodes = len(node_map)  
            dimension_matrix = len(node_map) + count_V - 1
            A = np.zeros((dimension_matrix,dimension_matrix))
            b = np.zeros((dimension_matrix,1)) 
            
            #matrix entries for R - it will be in first no.of nodes * no. of nodes size matrix(excluding ground)
            for component, data in ckt_R.items():
                node1 = int(data['node_num1'])
                node2 = int(data['node_num2'])
                value = data['value']
                if node1 != 0 and node2 == 0:
                    A[node1-1][node1-1] += 1/value
                elif node2 != 0 and node1 == 0:
                    A[node2-1][node2-1] += 1/value
                else:    
                    A[node1-1][node1-1] += 1/value
                    A[node2-1][node2-1] += 1/value    
                    A[node1-1][node2-1] -= 1/value
                    A[node2-1][node1-1] -= 1/value
            
            #matrix entries for V - 1 or -1 with respective to the node in A, its corresponding value in respective row in b
            for component, data in ckt_V.items():
                node1 = int(data['node_num1'])
                node2 = int(data['node_num2'])
                value = data['value']
                if node1 != 0 and node2 == 0:
                    A[number_nodes+data['count']-2][node1-1] += 1
                elif node1 == 0 and node2 != 0:
                    A[number_nodes+data['count']-2][node2-1] -= 1
                else:
                    A[number_nodes+data['count']-2][node1-1] += 1
                    A[number_nodes+data['count']-2][node2-1] -= 1
                b[number_nodes+data['count']-2] += value

            #matrix entries for I source - according to entry or exit of current sign is decided
            for component, data in ckt_I.items():
                node1 = int(data['node_num1']) 
                node2 = int(data['node_num2'])
                value = data['value']
                if node1 != 0 and node2 == 0:
                    b[node1-1] -= value
                elif node1 == 0 and node2 != 0:
                    b[node2-1] += value
                else:
                    b[node1-1] -= value
                    b[node2-1] += value
                    
            # for currents through V sources - according to KCL
            for component, data in ckt_V.items():
                node1 = int(data['node_num1'])
                node2 = int(data['node_num2'])
                value = data['value']
                if node1 != 0 and node2 == 0:
                    A[node1-1][number_nodes+data['count']-2] -= 1
                elif node1 == 0 and node2 != 0:
                    A[node2-1][number_nodes+data['count']-2] += 1
                else:
                    A[node1-1][number_nodes+data['count']-2] -= 1
                    A[node2-1][number_nodes+data['count']-2] += 1    
    try:
        # solving the matrices
        node_voltages = np.linalg.solve(A, b)
        Vout = {}
        Iout ={}
        result = {}
        
        #for results of V to be displayed - they are in starting of the array - equal to no. of nodes
        for i in range(number_nodes-1):
            result[i+1] = node_voltages[i][0]
        # mapping values with respective nodes
        for i in node_map:
            for j in result:
                if node_map[i] == j:
                    Vout[i] = result[j]
        Vout['GND'] = 0.0
        
        # for results of I to be displayed - they are at the end - after no. of nodes to the end
        # mapping the values with respective voltages
        
        for component, data in ckt_V.items():
            Iout[component] = 0 - node_voltages[data['count']+number_nodes-2][0]
        return(Vout, Iout)
    
    #if the circuit is singular matrix
    except np.linalg.LinAlgError:
        raise ValueError("Circuit error: no solution")
        
    filename.close()
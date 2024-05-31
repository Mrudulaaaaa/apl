import io
def evalSpice(filename):
    
    ckt = io.StringIO(filename)
    ckt_file = ckt.readlines()
    ckt_list = []
    ckt_dic = {}
    for lines in ckt_file:
        tmp = lines.split()
        if tmp == []:
            continue
        ckt_list.append(tmp)
    for i in range(len(ckt_list)):
        if ckt_list[i][0] == '.circuit':
            for j in range(i+1,len(ckt_list)):
                if ckt_list[j][0] == '.end':
                    break
                else:
                    ckt_dic[ckt_list[j][0][ckt_list[j][1]][ckt_list[j][2]]] = ckt_list[j][3]

    return ckt_dic

print(evalSpice(""".circuit
 Vs 1 GND dc 2
 R1 1 2 1
 R2 2 GND 1
 .end"""
))

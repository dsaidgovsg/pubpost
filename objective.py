# Adds objective
hold = 0
for vert in V['vertex'].tolist():
    bal_inc = V[V['vertex'] == vert]['nonbalance'].tolist()[0]
    coster = V[V['vertex'] == vert]['cost'].tolist()[0]
    #Desalination plant
    if bal_inc == 2:
    	hold += pulp.lpSum([ coster * flow[(out, into)] for out, into in edge_ind.index if out == vert])
    #Treatment plant
    else:
    	hold += pulp.lpSum([ coster * flow[(out, into)] for out, into in edge_ind.index if into == vert])

m += hold

if bal_inc == 0:
    #treatment plant inflow and outflow have to match
	m += pulp.lpSum([flow[(out, into)] for out, into in edge_ind.index if into == vert]) == pulp.lpSum([flow[(out, into)] for out, into in edge_ind.index if out == vert])
	if cap_up != float('inf'):
		m += pulp.lpSum([flow[(out, into)] for out, into in edge_ind.index if into == vert]) <= cap_up
	if cap_down != 0:
		m += pulp.lpSum([flow[(out, into)] for out, into in edge_ind.index if into == vert]) >= cap_down

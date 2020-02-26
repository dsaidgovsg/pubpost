reshold = []
for out, into in edge_ind.index:
    var_output = {'out' : out, 'into' : into, 'flow': flow[(out, into)].varValue}
    reshold.append(var_output)

results = pd.DataFrame.from_records(reshold)

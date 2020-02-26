E = pd.DataFrame(data = {'edge' : [1, 2, 3, 4, 5, 6],
                         'out' : [1, 1, 2, 3, 5, 4],
                         'into' : [2, 3, 3, 4, 4, 6], 
                         'type' : ['decision'] * 6, 
                         'capacity' : [1000, 100, 100, 100, 100, float('inf')],
                         'cost' : [0, 1, 1, 1, 2, 5] })

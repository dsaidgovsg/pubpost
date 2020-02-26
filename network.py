# Libraries
import pandas as pd

# Creates some data
V = pd.DataFrame(data = {'vertex' : [1, 2, 3, 4, 5, 6], 
                         'name' : ['Reservoir A', 'Reservoir B', 'Plant', 'Tank', 'Insert', 'Demand'],
                         'capacity_l' : [10, 10, 0, 0, 0, 0],
                         'capacity_h' : [1200, 2500, 100, 150, 100, float('inf')],
                         'nonbalance' : [3, 3, 0, 4, 2, 1],
                         'cost' : [0, 0, 10, 0, 15, 0],
                         'startstate' : [1150, 1800, 0, 100, 0, 0],
                         'rainfall' : [100, 200, 0, 0, 0, 0],
                         'demand' : [ 0, 0, 0, 0, 0, 150]})

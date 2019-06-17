# IMMC 2018 Sensitivity Analysis
# Team # US-7680

from SALib.sample import saltelli
from SALib.analyze import sobol
import numpy as np

def P(ta):
	xxx

# Define the model inputs
problem = {
	'num_vars': 3,
	'names': ['t1', 't2', 'Tl'],
	'bounds': [[0, 14], [0,14], [0, 8]]
}

# Generate samples
param_values = saltelli.sample(problem, 100000, calc_second_order=True)

# Run model
Y = np.empty([param_values.shape[0]])

for i, X in enumerate(param_values):
    Y[i] = P(X)

# Perform analysis
Si = sobol.analyze(problem, Y, print_to_console=False)

# Print the first-order sensitivity indices
print "S1: ", Si['S1'], Si['S1_conf']
print "ST: ", Si['ST'], Si['ST_conf']

print "t1-t1:", Si['S2'][0,1], Si['S2_conf'][0,1]
print "t1-Tl:", Si['S2'][0,2], Si['S2_conf'][0,2]
print "t2-Tl:", Si['S2'][1,2], Si['S2_conf'][1,2]
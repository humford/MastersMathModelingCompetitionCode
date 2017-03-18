from SALib.sample import saltelli
from SALib.analyze import sobol
from SALib.test_functions import Ishigami
import numpy as np

def P(ta):
	t1 = ta[0]
	t2 = ta[1]
	Tl = ta[2]
	t = t2 - t1
	if t1 > t2:
		dr1 = round(float(t / 1.53))
		dr2 = round(float(t - 1.53) / ((92.0+5.75*Tl)/60.0) )
		C = ((0.07 * (92.0+5.75*Tl)) / 60.0) + 1.0
		psum = 0
		for d in range(1, 4):
			if d == 1:
				psum += (1.0/(1.10733333333 ** dr1)) * (1.10733333333 ** d)
			else:
				if d > dr2:
					d = dr2
				psum += (1.0/(C ** dr2)) * (C ** d)
		p = psum / 3
		return (1.0-p) * ((50000 / 250) * 3)
	elif t1 < t2:
		dr1 = round(float(t / 0.95))
		dr2 = round(float(t - 1.53) / ((57.0+5.75*Tl)/60.0) )
		C = ((0.07 * (57.0+5.75*Tl)) / 60.0) + 1.0
		psum = 0
		for d in range(1, 4):
			if d == 1:
				psum += (1.0/(1.0665 ** dr1)) * (1.0665 ** d)
			else:
				if d > dr2:
					d = dr2
				psum += (1.0/(C ** dr2)) * (C ** d)
		p = psum / 3
		return (1.0-p) * ((50000 / 250) * 3)
	else:
		return 0

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
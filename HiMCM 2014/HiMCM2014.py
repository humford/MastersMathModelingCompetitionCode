# HiMCM 2014 Problem A Model Calculation 
# Team 4792

ctimes = 5

stimes = 3

c = 2
s = 1
q = 10

unsorted = []
sorted = []

minc = 0
mins = 0
i = 0

def optimize(times):
    opt = 0
    opts = 0
    optc = 0
    min = 10000000000
    minc = 0
    mins = 0
    i = 0
    for c in range(1,times):
        for s in range(1,times):
            val = 60 * ((921.0/(35.0*c*s)) + ((.27*q)/15.24)) + 5
            print "%f seconds with %f staircases and %f lanes." % (val, s, c)
            if(val<min):
                opt = val
                optc = c
                opts = s
            unsorted.append(val)
            i += 1
    unsorted.sort()
    
    print unsorted
    
    difference = unsorted[1] - unsorted[0]
    
    print "The difference is %f" % difference
    
    print "The optimum is %f seconds with %f staircases and %f lanes." % (opt, opts, optc)

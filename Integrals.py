import math
from matplotlib import pyplot as plt

def riemann(str, l, u, n):  #uses the riemann method to approximate integrals
    t = 0   #starts total at 0
    for i in range(int(l*n),int(u*n+1)):    #opens a loop that runs for every increment of 1/n between lower and upper
        #because multiplying by n augments all values, i is divided by n to show its true value in the code
        x = i/n
        t += eval(str)/n   #adds to the total: the area of rectangle that has height f(i/n) and width (1/n)
    return t

def romberg(str, l, u, n):  #more complicated, and more accurate mehtod of integration
    alist = []  #defines two new lists, (used similarly to nder code)
    blist = []
    for k in range(1,n+1):  #loops the number of times that designates accuracy, changes k increases by 1 each time
        alist.append(riemann(str,l,u,2.0**k))
        #each appended value has twice as many rectangles as previous, this makes them more accurate
    while len(alist)>1: #uses richardson method to find where the innaccurate answers converge
        blist = alist   #copies alist onto blist
        for j in range(len(alist)-1):   #runs for all values in list
            alist[j] = blist[j+1]*(4/3)-blist[j]*(1/3) #the richardson method: 4/3 of answer - 1/3 less accurate answer
        del alist[-1]   #removes the unneccessary value off the end of alist
    return alist[0] #once calculated the most accurate convergence with specified accuracy, return that value

window = {      #sets window lower x and upper x, and tstep same as a graphing calculator
    'lx': 0.0,
    'ux': 10.0,
    'tstep': .1
}

def intgraph(eq):   #acts identically to code above^
    xL = ()
    yL = ()
    n = int((window['ux']-window['lx'])/window['tstep'])
    for i in range(n+1):
        x = window['lx']+i*window['tstep']
        xL += (x, )
        yL +=(eval(eq), )
    plt.fill_between(xL, 0, yL) #but plots area under curve instead of plotting line
    plt.show()

def polarriemann(eq,n):
    t = 0   #starts total at 0
    for i in range(0,int(2*math.pi*n+1)):    #opens a loop that runs for every increment of 1/n between lower and upper
        #because multiplying by n augments all values, i is divided by n to show its true value in the code
        x = i/n
        t += 0.5*(eval(eq)**2)/n   #adds to the total: the area of rectangle that has height f(i/n) and width (1/n)
    return t

def polarromberg(eq,n):
    alist = []  #defines two new lists, (used similarly to nder code)
    blist = []
    for k in range(1,n+1):  #loops the number of times that designates accuracy, changes k increases by 1 each time
        t = 0
        alist.append(polarriemann(eq,2**k))
        #each appended value has twice as many rectangles as previous, this makes them more accurate
    while len(alist)>1: #uses richardson method to find where the innaccurate answers converge
        blist = alist   #copies alist onto blist
        for j in range(len(alist)-1):   #runs for all values in list
            alist[j] = blist[j+1]*(4/3)-blist[j]*(1/3) #the richardson method: 4/3 of answer - 1/3 less accurate answer
        del alist[-1]   #removes the unneccessary value off the end of alist
    return alist[0] #once calculated the most accurate convergence with specified accuracy, return that value

def parariemann(xeq,yeq,l,u,n):
    t = 0   #starts total at 0
    for i in range(int(l*n),int(u*n+1)):    #opens a loop that runs for every increment of 1/n between lower and upper
        #because multiplying by n augments all values, i is divided by n to show its true value in the code
        t = i/n
        t = eval(xeq)
        t += eval(str)/n   #adds to the total: the area of rectangle that has height f(i/n) and width (1/n)
    return t

def pararomberg(xeq,yeq,n):
    alist = []  #defines two new lists, (used similarly to nder code)
    blist = []
    for k in range(1,n+1):  #loops the number of times that designates accuracy, changes k increases by 1 each time
        t = 0
        alist.append(2*parariemann(xeq,yeq,2**k))
        #each appended value has twice as many rectangles as previous, this makes them more accurate
    while len(alist)>1: #uses richardson method to find where the innaccurate answers converge
        blist = alist   #copies alist onto blist
        for j in range(len(alist)-1):   #runs for all values in list
            alist[j] = blist[j+1]*(4/3)-blist[j]*(1/3) #the richardson method: 4/3 of answer - 1/3 less accurate answer
        del alist[-1]   #removes the unneccessary value off the end of alist
    return alist[0] #once calculated the most accurate convergence with specified accuracy, return that value

def help(*args):    #see Derivative.help()
    print ''
    if 'riemann' in args:
        print 'riemann(equation, lower x-value, upper x-value, number of rectangles)'
        return 'calculates riemann sum for an equation'
    if 'romberg' in args:
        print 'romberg(equation, lower x-value, upper x-value, accuracy)'
        return 'calculates romberg integral for an equation'
    if 'intgraph' in args:
        print 'intgraph(equation)'
        print 'visualy represents the area under the curve of an equation'
        print 'to change window:'
        print '     window["tstep"] = ... : changes accuracy (smaller is more accurate)'
        print '     window["lx"] = ... : changes the lower x value of the window'
        return '    window["ux"] = ... : changes the upper x value of the window'
    if 'polarriemann' in args:
        print 'polarriemann(equation, number of rectangles)'
        return 'calculates riemann sum for a polar equation (assumes 0..2pi)'
    if 'polarromberg' in args:
        print 'polarromberg(equation, accuracy)'
        return 'calculates romberg integral for a polar equation (assumes 0..2pi)'
    if 'parariemann' in args:
        print 'parariemann(x-equation, y-equation, lower t-value, upper t-value, number of rectangles)'
        return 'calculates riemann sum for a parametric equation'
    if 'pararomberg' in args:
        print 'pararomberg(x-equation, y-equation, lower t-value, upper t-value, accuracy'
        print 'calculates romberg integral for a parametric equation'
    print "Functions are:"
    print "     riemann"
    print "     romberg"
    print "     polarriemann"
    print "     polarromberg"
    print "     parariemann"
    print "     pararomberg"
    return "for information about a function (riemann) use help('riemann')"
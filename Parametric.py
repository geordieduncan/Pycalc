from matplotlib import pyplot as plt

def paradxdy(xeq,yeq,c):    #calculates instantaneous change in x/change in y of parametric
    t = c
    x1 = eval(xeq)  #calculates x at a given t
    y1 = eval(yeq)  #calculates y at a given t
    t = c+0.000000001   #slightly changes t
    x2 = eval(xeq)  #takes new x and y
    y2 = eval(yeq)
    return (y2-y1)/(x2-x1)  #returns change in  x / change in y

def parariemann(xeq,yeq,l,u,n):
    t = 0   #starts total at 0
    for i in range(int(l*n),int(u*n+1)):    #opens a loop that runs for every increment of 1/n between lower and upper
        #because multiplying by n augments all values, i is divided by n to show its true value in the code
        t = i/n
        t = eval(xeq)
        t += eval(str)/n   #adds to the total: the area of rectangle that has height f(i/n) and width (1/n)
    return t

def pararomberg(xeq,yeq,l,u,n):
    alist = []  #defines two new lists, (used similarly to nder code)
    blist = []
    for k in range(1,n+1):  #loops the number of times that designates accuracy, changes k increases by 1 each time
        t = 0
        alist.append(parariemann(xeq,yeq,l,u,2**k))
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

def paragraph(xeq,yeq):    #graphs function inside window from above^
    xL = () #empty x value tuple
    yL = () #empty y-value tuple
    n = int((window['ux']-window['lx'])/window['tstep'])    #n is the number of calculations to be conducted
    for i in range(n+1):
        t = window['lx']+i*window['tstep'] #sets value for evaluating function
        xL += (eval(xeq), ) #adds the x value to the x tuple
        yL +=(eval(yeq), )   #adds y-value to y tuple
    plt.plot(xL, yL)    #plots sets of points as line
    plt.show()  #shows plot

def paraintgraph(xeq,yeq):   #acts identically to code above^
    xL = ()
    yL = ()
    n = int((window['ux']-window['lx'])/window['tstep'])
    for i in range(n+1):
        t = window['lx']+i*window['tstep']
        xL += (eval(xeq), )
        yL +=(eval(yeq), )
    plt.fill_between(xL, 0, yL) #but plots area under curve instead of plotting line
    plt.show()

def paradergraph(xeq, yeq, *args): #identical to paragraph but plots derivative
    xL = ()
    yL = ()
    n = int((window['ux']-window['lx'])/window['tstep'])
    for i in range(n+1):
        t = window['lx']+i*window['tstep']
        xL += (eval(xeq), )
        yL +=(paradxdy(xeq,yeq,t), )
    plt.plot(xL, yL)
    if 'both' in args:
        Xl = ()
        Yl = ()
        for i in range(n+1):
            x = window['lx']+i*window['tstep']
            Xl += (eval(xeq), )
            Yl +=(eval(yeq), )
        plt.plot(Xl, Yl)
    plt.show()

def help(*args):    #see Derivative.help()
    print ''
    if 'paradxdy' in args:
        print 'paradxdy(x-equation, y-equation, t-value)'
        return 'takes numerical derivative at t-value point of a parametric equation'
    if 'parariemann' in args:
        print 'parariemann(x-equation, y-equation, lower t-value, upper t-value, number of rectangles)'
        return 'calculates riemann sum for a parametric equation'
    if 'pararomberg' in args:
        print 'pararomberg(x-equation, y-equation, lower t-value, upper t-value, accuracy'
        print 'calculates romberg integral for a parametric equation'
    if 'paradergraph' in args:
        print 'paradergraph(x-equation, y-equation, optional :"both")'
        print 'graphs the derivative of a parametric equation'
        print 'to change window:'
        print '     window["tstep"] = ... : changes accuracy (smaller is more accurate)'
        print '     window["lx"] = ... : changes the lower x value of the window'
        return '    window["ux"] = ... : changes the upper x value of the window'
    if 'paraintgraph' in args:
        print 'paraintgraph(equation)'
        print 'visualy represents the area under the curve of a parametric equation'
        print 'to change window:'
        print '     window["tstep"] = ... : changes accuracy (smaller is more accurate)'
        print '     window["lx"] = ... : changes the lower x value of the window'
        return '    window["ux"] = ... : changes the upper x value of the window'
    print "Functions are:"
    print "     paradxdy"
    print "     parariemann"
    print "     pararomberg"
    print "     paragraph"
    print "     paraintgraph"
    print "     paradergraph"
    return "for information about a function (paradxdy) use help('paradxdy')"
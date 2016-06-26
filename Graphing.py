import math
from matplotlib import pyplot as plt

def der(eq, c): #uses very close difference quotient to calculate derivative at point
    x = c
    a = eval(eq)
    x = c+0.000000001   #replaced h-value from diffquo with a very small number
    b = eval(eq)
    return (b-a)/0.000000001    #returns near instantaneous change in y / tiny change in x


window = {      #sets window lower x and upper x, and tstep same as a graphing calculator
    'lx': 0.0,
    'ux': 10.0,
    'tstep': .1
}

def eqgraph(eq):    #graphs function inside window from above^
    xL = () #empty x value tuple
    yL = () #empty y-value tuple
    n = int((window['ux']-window['lx'])/window['tstep'])    #n is the number of calculations to be conducted
    for i in range(n+1):
        x = window['lx']+i*window['tstep'] #sets value for evaluating function
        xL += (x, ) #adds the x value to the x tuple
        yL +=(eval(eq), )   #adds y-value to y tuple
    plt.plot(xL, yL)    #plots sets of points as line
    plt.show()  #shows plot

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

def dergraph(eq, *args):
    xL = ()
    yL = ()
    n = int((window['ux']-window['lx'])/window['tstep'])
    for i in range(n+1):
        x = window['lx']+i*window['tstep']
        xL += (x, )
        yL +=(der(eq,x), )
    plt.plot(xL, yL) #but plots area under curve instead of plotting line
    if 'both' in args:
        Xl = ()
        Yl = ()
        for i in range(n+1):
            x = window['lx']+i*window['tstep']
            Xl += (x, )
            Yl +=(eval(eq), )
        plt.plot(Xl, Yl)
    plt.show()

def help(*args):    #see Derivative.help()
    print ''
    if 'der' in args:
        print 'der(equation, x-value)'
        return 'takes derivative of an equation at a given x-value'
    if 'eqgraph' in args:
        print 'eqgraph(equation)'
        print 'graphs an equation'
        print 'to change window:'
        print '     window["tstep"] = ... : changes accuracy (smaller is more accurate)'
        print '     window["lx"] = ... : changes the lower x value of the window'
        return '    window["ux"] = ... : changes the upper x value of the window'
    if 'dergraph' in args:
        print 'dergraph(equation, optional :"both")'
        print 'graphs the derivative of an equation'
        print 'to change window:'
        print '     window["tstep"] = ... : changes accuracy (smaller is more accurate)'
        print '     window["lx"] = ... : changes the lower x value of the window'
        return '    window["ux"] = ... : changes the upper x value of the window'
    if 'intgraph' in args:
        print 'intgraph(equation)'
        print 'visualy represents the area under the curve of an equation'
        print 'to change window:'
        print '     window["tstep"] = ... : changes accuracy (smaller is more accurate)'
        print '     window["lx"] = ... : changes the lower x value of the window'
        return '    window["ux"] = ... : changes the upper x value of the window'
    print "Functions are:"
    print "     der"
    print "     eqgraph"
    print "     intgraph"
    print "     dergraph"
    return "for information about a function (der) use help('der')"
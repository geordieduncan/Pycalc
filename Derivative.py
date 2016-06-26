from matplotlib import pyplot as plt

def diffquo(eq, c, h):  #a difference quotient calculator (approximates slopes)
    x = c   #defines the in the function eq (expressions are inputed with x's)
    a = eval(eq)    #evaluates the function at point c
    x = c+h     #changes explanatory vairable to c+h
    b = eval(eq)    #evaluates at c+h
    return (b-a)/h  #returns the difference between evaluations divided by x-distance between them

def der(eq, c): #uses very close difference quotient to calculate derivative at point
    x = c
    a = eval(eq)
    x = c+0.000000001   #replaced h-value from diffquo with a very small number
    b = eval(eq)
    return (b-a)/0.000000001    #returns near instantaneous change in y / tiny change in x

def nder(d, c, eq): #uses lists to take second thir fourth... derivatives
    n=d+1   #the number of values need is 1 greater than the n derivative (2 points for 1st derivative)
    L=[]    #sets 2 new empty lists
    G=[]
    dist = 0.1**(6-d)   #uses more spread out to conserve accuracy of higher power derivatives
    for i in range(n+1):    #opens for loop that inputs f(x) into list L, at evenly spread out x's
        x = c+dist*i
        L.append(eval(eq))
    for j in range(n-1):    #runs till there is only one number left
        G=L     #copies L into G
        for k in range(len(L)-1):   #loops k = index for each term in list L
            L[k]=(G[k+1]-G[k])/dist     #changes current L[k] to the difference f(L[k]) and f(L[k+1]) then divides by change in x to get slope
        L.remove(L[-1])     #removes the last unneccessay term from List L
    return round(L[0],3)    #rounds because the accuracy is not sound

def derivcoeff(List,d): #uses general power rule on coeffecients of polynomial
    n = len(List)
    for i in range(d):  #repeats for higher powers of derivative, d=1: 1st derivative, d=2: second derivative
        for i in range(n-1):    #for every value in the list...
            List[i]=List[i]*(n-i)   #multiply the coeffecient by the power of the term it represents a coeffecient for
        del List[-1]    #removes last unneccessary term
        n-=1
    return List

window = {      #sets window lower x and upper x, and tstep same as a graphing calculator
    'lx': 0.0,
    'ux': 10.0,
    'tstep': .1
}

def dergraph(eq, *args):    #functions very similarly to Graphing.eqgraph()
    xL = () 
    yL = ()
    n = int((window['ux']-window['lx'])/window['tstep'])
    for i in range(n+1):    #operates for every x specified by the window parameter
        x = window['lx']+i*window['tstep']
        xL += (x, )     #appends to the x-tuple the x
        yL +=(der(eq,x), )  #appends to y-tuple the derivative of the equation at x
    plt.plot(xL, yL) #
    if 'both' in args:
        Xl = ()
        Yl = ()
        for i in range(n+1):
            x = window['lx']+i*window['tstep']
            Xl += (x, )
            Yl +=(eval(eq), )
        plt.plot(Xl, Yl)
    plt.show()

def help(*args): #this is referenced by calling File.help() in this case Derivative.help()
    #With no input, the help shows a list of functions
    #Individual functions are referenced by putting the string of the functions name in the argument of the help function
    print ''
    if 'diffquo' in args:   #if the specific function name is in the arguments
        print 'diffquo(equation, x-value, distance)'    #prints how to enter the function
        return 'takes difference quotient of an equaton at a certain point and distance'
    if 'der' in args:
        print 'der(equation, x-value)'
        return 'takes derivative of an equation at a given x-value'
    if 'nder' in args:
        print 'nder(degree of derivative, x-value, equation)'
        print 'nder(3,1.0,x**4-x**2): takes 3rd derivative of x to the fourth - x squared at the point 1.0'
        return 'takes 2nd, 3rd 4th ... derivatives at a point'
    if 'derivcoeff' in args:
        print 'dervoeff([list, of, coefficients])'
        return 'uses general power rule on coeffecients of polynomials'
    if 'dergraph' in args:
        print 'dergraph(equation, optional :"both")'
        print 'graphs the derivative of an equation'
        print 'to change window:'
        print '     window["tstep"] = ... : changes accuracy (smaller is more accurate)'
        print '     window["lx"] = ... : changes the lower x value of the window'
        return '    window["ux"] = ... : changes the upper x value of the window'
    print "Functions are:"  #The list of functions:
    print "     diffquo"
    print "     der"
    print "     nder"
    print "     derivcoeff"
    print "     dergraph"
    return "for information about a function (der) use help('der')"
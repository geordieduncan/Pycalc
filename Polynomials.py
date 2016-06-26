import math
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
    return round(L[0],6)    #rounds because the accuracy is not sound

def factorial(num): #recursive factorial function
    if num <= 1:    #base case: if number is 1, return 1
        return 1
    else:  #if number is greater than one...
        return num*factorial(num-1)  #multiply current number by the factorial of num-1

def derivcoeff(List,d): #uses general power rule on coeffecients of polynomial
    n = len(List)
    for i in range(d):  #repeats for higher powers of derivative, d=1: 1st derivative, d=2: second derivative
        for i in range(n-1):    #for every value in the list...
            List[i]=List[i]*(n-i)   #multiply the coeffecient by the power of the term it represents a coeffecient for
        del List[-1]    #removes last unneccessary term
        n-=1
    return List

def taylor(eq,c,d,*args): #calculates taylor series coeffecients for a given function
    n=d+1
    coeff=[0]*n
    txt = ""
    for i in range(n): #uses nder to calculate nderivatives and puts
        coeff[i] = nder(i,c,eq)/factorial(i) #calculates derivative / facotrial(degree of term)
        if(coeff[i]!= 0.0): #fills in evaluatable text with that coeffecients times terms
            if txt == "":
                txt+="(%f*(x**%d))" %(coeff[i],i)
            elif coeff[i]>0:
                txt+="+(%f*(x**%d))" %(coeff[i],i)
            elif coeff[i]<0:
                txt+="-(%f*(x**%d))" %(abs(coeff[i]),i)
    if 'c' in args: #if 'c' is designated when calling the function returns just the list of coeffecients
        return coeff
    return txt

def taylorderco(eq,c,d,n,*args):
    coeff = taylor(eq,c,d,'c') #uses coeffecients of taylor series
    done = derivcoeff(coeff,n)  #calculates the nderivative coeffecients
    txt  =''    #uses same txt writing code as taylor series to generate evaluatable code
    for i in range(len(done)):
        if(coeff[i]!= 0.0):
            if txt == "":
                txt+="(%f*(x**%d))" %(done[i],i)
            elif done[i]>0:
                txt+="+(%f*(x**%d))" %(done[i],i)
            elif done[i]<0:
                txt+="-(%f*(x**%d))" %(abs(done[i]),i)
    if 'c' in args: ##if 'c' is designated when calling the function returns just the list of coeffecients
        return done
    return txt

def help(*args):    #see Derivative.help()
    print ''
    if 'der' in args:
        print 'der(equation, x-value)'
        return 'takes derivative of an equation at a given x-value'
    if 'nder' in args:
        print 'nder(degree of derivative, x-value, equation)'
        print 'nder(3,1.0,x**4-x**2): takes 3rd derivative of x to the fourth - x squared at the point 1.0'
        return 'takes 2nd, 3rd 4th ... derivatives at a point'
    if 'factorial' in args:
        print 'factorial(number)'
        return 'calculates the factorial of a number'
    if 'derivcoeff' in args:
        print 'derivcoeff([list, of, coefficients])'
        return 'uses general power rule on coeffecients of polynomials'
    if 'taylor' in args:
        print 'taylor(equation, point, degree, optional "c")'
        print 'calculates taylor series coeffecients, and plugs them in to a evaluatable equation'
        print 'if argument "c" is used then returns as list of coefficients'
    if 'taylorderco' in args:
        print 'taylorderco(equation, point, degree, degree of differentiation, optional "c")'
        print 'uses derivcoeff on taylor series to take the 2nd, 3rd 4th etc. derivative of a taylor series polynomial'
        print 'if argument "c" is used then returns as list of coefficients'
    print "Functions are:"
    print "     der"
    print "     nder"
    print "     factorial"
    print "     derivcoeff"
    print "     taylor"
    print "     taylorderco"
    return "for information about a function (taylor) use help('taylor')"
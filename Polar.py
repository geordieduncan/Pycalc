import math

def RecToPol(x,y):  #converts rectangular coordinates too polar coordinates
    theta = math.atan(float(y)/x)   #defines the angle as atan(y/x)
    if x<0 and y>0:     #because atans range is only one pi in length, changes must be made to show true direction of coordinates
        theta+=math.pi  #if x is negative and y is positive add pi to answer
    if theta<0:         #if angle is below 0, use 2pi - angle, so it represents the angle with a positive value
       theta=2*math.pi+theta
    r = math.sqrt(x**2+y**2) #calculates radius using distance formula
    print '(%f, %f)' %(r, theta) # print (r, theta)

def PolToRec(r,theta):  #converts ploar coordinates too rectangular coordinates
    x = r*math.cos(theta)   #x=rcos(theta)
    y = r*math.sin(theta)   #y=rsin(theta)
    print '(%f, %f)' %(x,y) #print (x, y)

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

def drdt(eq,c): #Measures instantaneous change in r / change in theta
    t = c
    a = eval(eq)    #calculates r at a given theta
    t = c+0.000000001   #slightly increases theta
    b = eval(eq)    #calculates r again
    return (b-a)/0.000000001    #measures change in change in theta / the slight change in theta from before

def help(*args):    #see Derivative.help()
    print ''
    if 'RecToPol' in args:
        print 'RecToPol(x-value, y-value)'
        return 'converts rectangular coordinates into polar coordinates'
    if 'PolToRec' in args:
        print 'PolToRec(r-value, theta-value)'
        return 'converts polar coordinates into rectangular coordinates'
    if 'polarriemann' in args:
        print 'polarriemann(equation, number of rectangles)'
        return 'calculates riemann sum for a polar equation (assumes 0..2pi)'
    if 'polarromberg' in args:
        print 'polarromberg(equation, accuracy)'
        print 'calculates romberg integral for a polar equation (assumes 0..2pi)'
    if 'drdt' in args:
        print 'drdt(equation, theta-value)'
        return 'calculates the derivative of a polar equation at a given theta'
    print "Functions are:"
    print "     RecToPol"
    print "     PolToRec"
    print "     polarriemann"
    print "     polarromberg"
    print "     drdt"
    return "for information about a function (drdt) use help('drdt')"
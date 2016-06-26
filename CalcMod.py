print 'loading: X      X'	#imports all files, with loading screen
import Derivative
print 'loading: X-     X'
import Graphing
print 'loading: X--    X'
import Integrals
print 'loading: X---   X'
import Parametric
print 'loading: X----  X'
import Polar
print 'loading: X----- X'
import Polynomials
import math
print 'loading: X------X'
raw_input("Press Enter to Launch")	#launches with instructions
print "Files are:"
print "     Derivative"
print "     Graphing"
print "     Integrals"
print "     Parametric"
print "     Polar"
print "     Polynomials"
print ''
print 'To access a function within a file, use: File.function(...)'
print 'For function equations use python language and x as variable'
print 'For parametric equations use python language and t as a variable'
print 'For polar equations use t as variable (instead of theta)'
print 'Python language means something that is executable in python:'
print 'x+x or x*3+4 or x**2 or math.sin(x) (if math has been imported)'
print 'When inputting an eqation input is as a string:'
print '"x**2+2*x-1"'
print 'To access help for any file use: File.help()'
print 'For questions about graphing use graphHelp()'

def graphHelp():	#explains how to adjust the window parameter
    print "File.window is a stored dictionary with keys: lx, ux and tstep"
    print "lx stands for lower x-value"
    print "ux stands for upper x-value"
    print "tstep is the x-distance between two values calculated"
    print "to change these values use: File.window['key'] = ..."
#supermarket so we splitour code in different file. module is file that contain some python code.
#there are some tutorial that will teach u short cut to import module like from sale import *
#This is actually a bad practice because in that module you could have several different functions for variable
#and if you blindly import them into the current module some of those object may overwrrite with some object with same name
#in current module so dont import all object like this.only import the stuff that you need. so lest put calc shipping 
#calculate tax here there is nother way to import module so u can import complete module or specific methods from module.
import ecommercepackage.Shoppingsubpackage.sale
ecommercepackage.Shoppingsubpackage.sale.cal_tax()
ecommercepackage.Shoppingsubpackage.sale.calc_shipping()
from ecommercepackage.Shoppingsubpackage.sale import calc_shipping,cal_tax

calc_shipping()
cal_tax()

# compiled python files 
"""there is folder we have compiled version of the modules that we import into our program
#so currently we have compiled version of the sales module. the reason python stored these compiled files in this
# stored folder is to speed up module loading so next time we load our programme,python will look at content of the folder 
#and if we do have the compiled version of this sales module, python will simply load that compiled version so skip
#that compilation step, and this will result in faster loading of the sales module it only speed up laoding of this speed 
#module not the actual performance of the application now how does python know if the compile version up to date with
#the latest code in sale module it basically check the date time of this 2 file, the compiled version as well the source code
#if this date time of this source file is newer it realizes that our source code has changed, so it will recompile it and 
#store in pycache folder. u can see python bytecode here
#note that we dont have compiled version of app module python always recompiles the module that we load directly from the
#command line so in this demo i passed app.py as the entry point to python thats the reason python didnt cache the compiled 
#version of this module.
#if the date time of this folder"""

#module search path
#here we are importing the sale.module when python sees this it will look for a file called sale.py if it doesn't find 
#it will search in a bunch of predefined directories that come with python installation
#ecommercepackage is package and package is a container for one or more module.(Module is files)
import ecommercepackage.Shoppingsubpackage.sale
import sys
print(sys.path)

#Intra-package Reference
#absolute import and relative import
from ecommercepackage.Shoppingsubpackage import sale
#from ..Shoppingsubpackage import sale
#The dir function
from ecommercepackage.Shoppingsubpackage import sale
print(dir(sale))
print(sale.__name__)
print(sale.__package__)
print(sale.__file__)
#Executing modules as a script
#from ecommercepackage.Shoppingsubpackage import sale with this statement it load package and then catche it in memory
#so the statement we write here will be executed once we wrriten print staement in __init__ module of eccomerce package.
#and in sales module at top
#Python standard library
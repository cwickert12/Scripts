# Import system-level operations and add custom module path
import sys
sys.path.append('/home/cwickert/ENDFtk/build/')  # Add ENDFtk build path to import the module

# Import the ENDFtk library for ENDF file parsing 
import ENDFtk
import numpy as np
import writeInputRECONR
import AddAngularDist
import writeInputACER
import os

writeInputRECONR.writeInputRECONR()

os.system('njoy <input_RECONR')
os.system('mv output output_RECONR')

AddAngularDist.AddAngularDist()

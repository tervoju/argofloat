import netCDF4
import numpy as np

f = netCDF4.Dataset('./data/JA3_GPSOPR_2PfS174_018_20201029_121148_20201029_140842.nc')
print(f.variables.keys()) # get all variable names
#sst = f.variables['sst'] # sst variable
#time = f.variables['time']
#print(time)

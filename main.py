from function import *

# This is a test for the value of Rs
# The expected result for i=55 deg, e=0, w=0 deg is Rs = 6371.009 km.

r = Rs(i=55, e=0, w=0)
error_rel = (r - 6371.009)/6371.009
print(error_rel)

# SUPCRT
 
This repository will support the much needed update of the Super Critical analysis code, developed 44 years ago, known to geologists around the world as SUPCRT (pronounced: supercrit). This code revision will focus on the most recent version - the Indiana University version which adjusted the gas and aqueous species database file and included new minerals.

The target of this revision will be to compile a comprehensive python module which will be extendable to fit specific research, but also allow researchers to pull data directly from the SUPCRT model into other software packages for anlysis or ML purposes.

The current Fortran code is approximately ~9650 lines of code, and more than a 100 subroutines and functions.

# Approach
Step 1:
- Rewrite the function and subroutine headers in Python, adding documentation stubs as possible, to get a high level overview of the flow of the code and an idea of the complexity of the SUPCRT code.

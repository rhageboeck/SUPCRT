# SUPCRT
 
This repository will support the much needed update of the Super Critical analysis code developed 5 decades affectionately known to geologists around the world as SUPCRT (pronounced: supercrit). This code revision will focus on the most recent version - the Indiana University version which adjusted the gas and aqueous species database file and altered the mineral analysis to include non-phase transition, landau theory, and bragg williams.

The target of this revision will be to compile a comprehensive python module which will be extendable to fit specific research, but also allow researchers to pull data directly from the SUPCRT model into other software packages for anlysis or ML purposes.

# Approach
1. This repository will approach this revision in 2 steps. The first step will be to convert all of the SUPCRT fortran code to a Python equivalency. Hopefully this will reveal obvious data formatting issues and will give a chance to more fully understand dependencies and routines which can be simplified with more advanced Python syntax.
2. The second step will be to redesign the input and output system to include default arguments for current input fields as well as design a data output system that is consistent with the legacy version, offers a python supported data structure output, and new CSV or Excel formats. In this step, OOP will be a priority to better develop the SUPCRT code and add a useful and well documented API for future research.
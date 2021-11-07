"""
*** REACBL - Calculates the standard molal Gibbs free energy, enthalpy,
***          entropy, heat capacity, and volume of the i[th] reaction
***          (specified in common blocks /icon/ and /reac/) among
***          <= MAXMIN minerals, <= MAXAQS aqueous species, <= MAXGAS
***          gases, and H2O using equations and data given by Helgeson
***          et al. (1978), Tanger and Helgeson (1988), Shock and 
***          Helgeson (1988, 1990), Shock et al. (1989, 1991), Johnson
***          and Norton (1991), Johnson et al. (1991), Sverjensky
***          et al. (1991), and Holland and Powell (2011).
***
***          Computed reaction properties are stored in COMMON blocks
***          /minsp/, /gassp/, /aqsp/, /solvn/, and /fmeq/.
*** 
*******************************************************************
***
*** Author:     James W. Johnson
***             Earth Sciences Department, L-219
***             Lawrence Livermore National Laboratory
***             Livermore, CA 94550
***             johnson@s05.es.llnl.gov
***
*** Revised 2015:   
***             Kurt Zimmer(1), Yilun Zhang(2), Chen Zhu(2), etc.
***             (1) Department of Computer Science 
***             (2) Department of Geology
***             Indiana University
***             Contact: chenzhu@indiana.edu
***
*******************************************************************
"""
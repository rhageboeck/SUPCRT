"""
*** CPRONSBL - Read a sequential-access spronshp.dat file and
***            generate its direct-access dpronshp.dat equivalent.
***
*********************************************************************
***
*** Author:     James W. Johnson
***             Earth Sciences Department, L-219
***             Lawrence Livermore National Laboratory
***             Livermore, CA 94550
***             johnson@s05.es.llnl.gov
***
*** Revised:    By J.Palandri, 19 Apr 1996; reads SPRONSHP.DAT format
***             heat capacity coefficients with a, b, c, d, where
***
***              Cp = a + bT + cT^-2 + dT^-(1/2)
***
*** Revised 2015:   
***             Kurt Zimmer(1), Yilun Zhang(2), Chen Zhu(2), etc.
***             (1) Department of Computer Science 
***             (2) Department of Geology
***             Indiana University
***             Contact: chenzhu@indiana.edu
***
*********************************************************************
"""
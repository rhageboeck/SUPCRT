"""
*** H2OBL - Computes state, thermodynamic, transport, and electroststic 
***         properties of fluid H2O at T,[P,D] using equations and data
***         given by Haar et al. (1984), Levelt Sengers et al. (1983),
***         Johnson and Norton (1991), Watson et al. (1980), Sengers and
***         Kamgar-Parsi (1984), Sengers et al. (1984), Helgeson and Kirkham
***         (1974), Uematsu and Franck (1980), and Pitzer (1983). 
***
***********************************************************************
***
*** Author:     James W. Johnson
***             Earth Sciences Dept., L-219
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
***********************************************************************
*
*   specs  - Input unit, triple point, saturation, and option specs:
*
*****        it, id, ip, ih, itripl, isat, iopt, useLVS, epseqn, icrit;
*
*            note that the returned value of isat may differ from
*            its input value and that icrit need not be specified
*            prior to invocation.
*
*
*   states - State variables: 
*
*****          temp, pres, dens(1), dens(2);
*
*            note that the first three of these must be specified prior
*            to invocation and that, in the case of saturation, vapor
*            density is returned in dens(1), liquid in dens(2).
*
*
*   props  - Thermodynamic, transport, electrostatic, and combined 
*            property values:
*
*****        A, G, S, U, H, Cv, Cp, Speed, alpha, beta, diel, visc,
*****        tcond, surten, tdiff, Prndtl, visck, albe, 
*****        ZBorn, YBorn, QBorn, daldT, XBorn
*
*
*   error  - LOGICAL argument that indicates success ("FALSE") or
*            failure ("TRUE") of the call, the latter value in 
*            response to out-of-bounds specs or states variables.
*
***********************************************************************
"""
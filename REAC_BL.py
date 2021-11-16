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

def reac92(i, P, TC, Dw, Vw, betaw, alphaw, daldTw, Sw, Cpw, Hw, Gw, Zw, Qw, Yw, Xw, qeqn):
  '''
  Calculates the standard molal Gibbs free energy, enthalpy, entropy,
  heat capacity, and volume of the i[th] reaction (specified in COMMON
  blocks /icon/ and /reac/) among <= MAXMIN minerals, <= MAXAWS aqueous
  species, <= MAXGAS gases, and H2O using equations and data given by
  Helgeson et al. (1978), Tanger and Helgeson (1988), Shock and Helgeson
  (1988, 1990), Shock et al. (1989, 1991), Johnson and Norton (1991),
  Johnson et al. (1991), Sverjensky et al. (1991), and Holland and Powell
  (2011).

  Computed reaction properties are stored in COMMON blocks /minsp/, /gassp/,
  /aqsp/, /solvn/, and /fmeq/.

    Parameters:

    Returns:
      Unsure
  '''
  pass

def solids(nmin, P, T):
  '''
  Computes the standard molal thermodynamic properties of nmin minerals at P,T
  using equations given by Helgeson et al. (1978).

    Parameters:

    Returns:
  '''
  pass

def getCpr(imin, T):
  '''
  Computes the effective phase region for temperature integration of Cpr(T) for
  mineral imin (i.e., the phase region specified by T at 1 bar).
  
    Parameters:
    
    Returns:
      Unsure
  '''
  pass

def getphr(imin, P, T, TtranP):
  '''
  Computes the phase region for mineral imin at P, T; and, as a side effect,
  TtranP(1..MXTRAN, imin) as f(P).
  
    Parameters:
    
    Returns:
  '''
  pass

def VCalculations(imin, T, T0, a, b, c, Theta, Eps, Pth): # documentation incomplete
  '''
  a, b, c, Theta, Eps, and Pth
  
    Parameters:
    
    Returns:
  '''
  pass

def Vterms(imin, P, T, phaser, Vmin, Vdp, PtranT):
  '''
  Computes Vmin(P, T), Vmin*dP, and (if necessary) PtranT.

    Parameters:

    Returns:
  '''
  pass

def Cptrms(phase, i, Cpreg, T, Cpr, CprdT, CprdlT):
  '''
  Computes the standard molal heat capacity and heat capacity temperature integrals,
  evaluated from Tref to T at 1 bar.

    Parameters:

    Returns:
  '''
  pass

def Cp(T, a, b, c, d):
  '''
  Computes the standard molal heat capacity at T.

    Parameters:

    Returns:
  '''
  pass

def CpdT(T1, T2, a, b, c, d):
  '''
  Computes the integral CpdT evaluated from T1 to T2.

    Parameters:

    Returns:
  '''
  pass

def CpdlnT(T1, T2, a, b, c, d):
  '''
  Computes the integral CpdlnT evaluated from T1 to T2.

    Parameters:

    Returns:
  '''
  pass

def pttrms(imin, phaser, P, T, Spttrm, Hpttrm, Gpttrm, Cpttrm, VdPtrm):
  '''
  Computes phase transition terms for Smin, Hmin, and Gmin.

    Parameters:

    Returns:
  '''
  pass

def gases(ngas, T):
  '''
  Computes the standard molal thermodynamic properties of ngas gases at P,T
  using equations given by Helgeson et al. (1978).

    Parameters:

    Returns:
  '''
  pass

def aqsps(naqs, P, T, Dw, betaw, alphaw, daldTw, Z, Q, Y, X, qeqn):
  '''
  Computes the standard partial molal thermodynamic properties of naqs aqueous
  species at P,T using equations given by Tanger and Helgeson (1988), Shock et al.
  (1991), and Johnson et al. (1991).

    Parameters:

    Returns:
  '''
  pass

def omeg92(g, dgdP, dgdT, d2gdT2, wref, Z, w, dwdP, dwdT, d2wdT2, aname):
  '''
  Computes the conventional Born coefficient (w) of the current aqueous species,
  dwdP, dwdT, and dw2dT2 as a function of g, dgdP, dgdT, d2gdT2, wref, and Z
  using equations given by Johnson et al. (1991).

    Parameters:

    Returns:
  '''
  pass

def reactn(i, P, T, Vw, Sw, Cpw, Hw, Gw):
  '''
  Computes the standard molal thermodynamic properties of the i[th] reation.

    Parameters:

    Returns:
  '''
  pass

def gfun92(TdegC, Pbars, Dgcm3, betab, alphaK, daldT, g, dgdP, dgdT, d2gdT2, geqn):
  # geqn = 1,2 disabled in current SUPCRTBL
  '''
  Computes the g function (Tanger and Helgeson, 1988; Shock et al., 1991)
  and its partial derivatives (dgdP, dgdT, d2gdT2) at TdegC, Pbars using the
  computational algorithm specified by qeqn.

  geqn = 1 ..... use Tanger-Helgeson (1988) equations
  geqn = 2 ..... use Shock et al. (1991) equations
                 without the f(P,T) difference equation
  geqn = 3 ..... use Shock et al. (1991) equations
                 with the f(P,T) difference function

    Parameters:

    Returns:
  '''
  pass

def gShok2(T, P, D, beta, alpha, daldT, g, dgdP, dgdT, d2gdT2):
  '''
  Computes g, dgdP, dgdT, and d2gdT2 using equations given by Shock et al. (1991)

    Parameters:

    Returns:
  '''
  pass

def solve(x0, y0, res, iters, debug, imin, T, P):
  '''
  Estimate the zero of f(x) using Newton's method.
  
    Parameters:

    Returns:
  '''
  pass
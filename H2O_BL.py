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

def valid(it, id, ip, ih, itripl, isat, iopt, useLVS, epseqn, Temp, Pres, Dens):
  '''
  Checks if the unit and equation specifications are valid and input state
  conditions fall within the HGK equations region of validity.
  
    Parameters:

    Returns:
      ___ (bool): True if the inputs are valid, False otherwise
  '''
  return False

def valspc(it, id, ip, ih, itripl, isat, iopt, useLVS, espeqn):
  '''
  Checks if the input values define valid input.
  
    Parameters:
    
    Returns:
      ___ (bool): True if the inputs are valid, False otherwise
  '''
  return False

def valTD(T, D, isat, epseqn):
  '''
  Checks if T-D defines liquid or vapor H2O within validity limits of the
  HGK equation of state.
  
    Parameters:
    
    Returns:
      ___ (bool): True if T-D is within limits, False otherwise
  '''
  return False

def valTP(T, P):
  '''
  Checks if T-P defines liquid or vapor H2O within validity limits of the
  HGK equation of state.
  
    Parameters:
      T (float): Temperature (__units__)
      P (float): Pressure (__units__)
    
    Returns:
      ___ (bool): True if T-P is which limits, False otherwise
  '''
  return False

def Psublm(Temp):
  '''
  Computes the Psublimation(T) in bars from the equation given by
  Washburn (1924): Monthly Weather Rev., v.52, pp. 488-490
  
    Parameters:
      Temp (float): Temperature (Celcius)
  
    Returns:
      Psublm (float): returns computed Psublimation(T) in bars
  '''
  Psublm = 0.0
  return Psublm

# TODO: HGK Constants Section Line 373-475

# TODO: LVS Constants Section Line 477-548

def unit(it, id, ip, ih, itripl): # function sets state and DOES NOT need a return value
  '''
  Sets internal parameters according to use-specified choice of units.
  Internal program units are degK(T), and gm/cm**3(D); all other properties
  are computed in dimensionless form and dimensioned at output time.

  NOTE:
    Conversion factros for j/g ---> cal/(g,mol) (ffh (4 & 5)) are consistent
    with those given in Table 1, Helgeson & Kirkham (1974a) for thermal
    calories, and differ slightly with those given by Haar et al (1984)
    for international calories.
  
    Parameters:

    Returns:
      None
  '''
  pass

def crtreg(isat, iopt, it, T, P, D):
  '''
  Checks if input state conditions fall within the critical region of H2O.

    Parameters:
      T
      P
      D
  
    Returns:
      ___ (bool): True if conditions are satified, False otherwise
  '''
  return False

def HGKeqn(isat, iopt, itripl, Temp, Pres, Dens, epseqn): # Doesn't appear to return anything
  '''
  Computes the thermodynamic and transport properties of H2O from the equation
  of state given by Haar, Gallagher, & Kell (1984).

    Parameters:

    Returns:
      None
  '''
  pass

def HGKsat(isat, iopt, itripl, Temp, Pres, Dens, epseqn):
  '''
  If isat=1, computes Psat(T) or Tsat(P) (iopt=1,2), liquid and
  vapor densities, and associated thermodynamic and transport properties.
  If isat=0, checks whether T-D or T-P (iopt=1,2) fallse on or within TOL
  of the liquid-vapor surface; if so, sets isat <- 1 and computes properties.

    Parameters:

    Returns:
      None
  '''
  pass

def calcv3(iopt, itripl, Temp, Pres, Dens, epseqn):
  '''
  Compute the dependent state variable.
  
    Parameters:
    
    Returns:
      None
  '''
  pass

def thmHGK(d, t):
  '''
  Computes the thermodynamic functions in dimensionless units from
  the HGK equation of state: Helmholtz, Gibbs, internal energy, and
  enthalpy functions (ad, gd, ud, hd) are per RT; entropy and heat
  capacities (sd, cvd, cpd) are per R.

    Parameters:

    Returns:
      None
  '''
  pass

def bb(t):
  '''
  Computes molecular parameters b, the "excluded volume" (eq A.3), and
  B, the second virial coefficient (eq A.4), in cm3/g (b1,b2) and their
  first and second derivatives with respect to
  temperature (b1t, b1tt, b2t, b2tt).

    Parameters:

    Returns:
      None
  '''
  pass

def base(d, t):
  '''
  Computes Abase, Gbase, Sbase, Ubase, Hbase, Cvbase
  -- all per RT (dimensionless) -- as well as Pbase & dP/dT
  -- both per (DRT) -- for the base function (ab, gb, sb, ub,
  hb, cvb, pb, dpdtb). See Haar, Gallagher & Kell (1979), eq(1).
  
    Parameters:

    Returns:
      None
  '''
  pass

def resid(t, d):
  '''
  Computes residual contributions to pressure (q), the Helmloltz
  function (ar), dP/dD (q5), the Gibbs function (gr), entropy (sr),
  internal energy (ur), enthalpy (hr), ischoric heat capacity (cvr),
  and dP/dT. The first 36 terms of the residual function represent a
  global least squares fit to experimental data outside the critical
  region, terms 37-39 affect only the immediate vicinity of the
  critical point, and the last term (40) contributes only in the high
  temperature, low pressure region.
  
    Parameters:

    Returns:
      None
  '''
  pass

def ideal(t):
  '''
  Computes thermodynamic properties for H2O in the ideal gas state
  using equations given by Wooley (1979).

    Parameters:
      t
    
    Returns:
      None
  '''
  pass

def dalHGK(d, t, alpha):
  '''
    Computes (d(alpha)/dt)p(d, t, alpha) for the Haar et al. (1983)
    equation of state.

      Parameters:

      Returns:
        dalHGK (float): computed (d(alpha)/dt)p(d, t, alpha)
  '''
  dalHGK = 0.0
  return dalHGK

def denHGK(d, p, dguess, t, dpdd):
  '''
  Computes density (d in g/cm3) and dP/dD (dPdd) as f(p(MPa),t(degK))
  from an initial density guess (dguess)

    Parameters:

    Returns:
      Unsure
  '''
  pass

def PsHGK(t):
  '''
  Approximation to Psaturation(T) that agrees within 0.02% of that
  predicted by the HGK surface for temperatures up to within roughly
  a degree of the critical point.

    Parameters:

    Returns:
      PsHGK (float)
  '''
  PsHGK = 0.0
  return PsHGK

def TsHGK(p):
  '''
  Computes Tsaturation(P).

    Parameters:
      p
    
    Returns:
      TsHGK (float)
  '''
  TsHGK = 0.0
  return TsHGK

def TdPsdT(t):
  '''
  Computes T*(dPsat/dT).

    Parameters:
      t
    
    Returns:
      TdPsdT (float)
  '''
  TdPsdT = 0.0
  return TdPsdT

def corr(itripl, t, p, dl, dv, delg, epseqn):
  '''
  Computes liquid and vapor densities (dliq & dvap) and (Gl-Gv)/RT (delg)
  for T-P conditions on or near the saturation surface.

    Parameters:
    
    Returns:
      Unsure
  '''
  pass

def pcorr(itripl, t, p, dl, dv, epseqn):
  '''
  Computes Psaturation(T) (p) and liquid and vapor densities (dl & dv)
  from refinement of an initial approximation (PsHGK(t)) in accord with
  Gl = Gv.
  
    Parameters:
    
    Returns:
      Unsure
  '''
  pass

def tcorr(itripl, t, p, dl, dv, epseqn):
  '''
  Computes Tsaturation(P) (t) and liquid and vapor densities (dl & dv)
  from refinement of an initial approaximation (TsHGK(p)) in accord
  with Gl = Gv

    Parameters:

    Returns:
      t (float) ~ maybe
  '''
  pass

def LVSeqn(isat, iopt, itripl, T, P, Dens, epseqn):
  '''
  '''
  pass

def cpswap():
  '''
  '''
  pass

def LVSsat(iopt, isat, T, P, D):
  '''
  '''
  pass

def denLVS(isat, T, P):
  '''
  '''
  pass

def TsLVS(isat, P):
  '''
  '''
  pass

def Pfind(isat, T, D):
  '''
  '''
  pass

def aux(r1, th1, d2PdT2, d2PdMT, d2PdM2, aa, xk, sd, Cvcoex):
  '''
  '''
  pass

def conver(rho, Tee, amu, th1, r1, rho1s, s1, rhodi, error1):
  '''
  '''
  pass

def rtheta(r, theta, rho, Tee):
  '''
  '''
  pass

def ss(r, th, s, sd):
  '''
  '''
  pass

def thmLVS(isat, T, r1, th1):
  '''
  '''
  pass

def delLVS(D, T, P, alpha):
  '''
  '''
  pass

def backup():
  '''
  '''
  pass

def restor():
  '''
  '''
  pass

def load(phase, ptemp, props):
  '''
  '''
  pass

def tpset():
  '''
  '''
  pass

def triple(T, wpzero):
  '''
  '''
  pass

def power(base, exp):
  '''
  '''
  pass

def TdegK(it, t):
  '''
  '''
  pass

def TdegUS(it, t):
  '''
  '''
  pass

def dimHGK(isat, itripl, t, p, d, espeqn):
  '''
  '''
  pass

def dimLVS(isat, itripl, theta, T, Pbars, dl, dv, tprops, epseqn):
  '''
  '''
  pass

################################################################

def viscos(Tk, Pbars, Dkgm3, betaPa):
  '''
  '''
  pass

def thcond(Tk, Pbars, Dkgm3, alph, betaPa):
  '''
  '''
  pass

def surten(Tsatur):
  '''
  '''
  pass

def Born92(Tk, Pbars, Dgcm3, betab, alphaK, daldT, eps, Z, Q, Y, X, epseqn):
  '''
  '''
  pass

def JN91(T, D, beta, alpha, daldT, eps, dedP, dedT, d2edT2):
  '''
  '''
  pass

def epsBrn(eps, dedP, dedT, d2edT2, Z, Q, Y, X):
  '''
  '''
  pass
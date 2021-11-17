"""
*** SUPCRTBL - Calculates the standard molal thermodynamic properties 
***            of reactions among minerals, gases, and aqueous species
***            using equations and data given by Helgeson et al. (1978),
***            Tanger and Helgeson (1988), Shock and Helgeson 
***            (1988, 1990), Shock et al. (1989, 1991), Johnson and
***            Norton (1991), Johnson et al. (1991), Sverjensky
***            et al. (1991), and Holland and Powell (2011). 
*** 
************************************************************************
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
************************************************************************
"""

def supcrt():
  '''
    Docstring above ^
  
    Parameters:
      None
    
    Returns:
      None
  '''
  pass

def banner():
  '''
  Write program banner to the terminal screen.
  
    Parameters:
      None
    
    Returns:
      None
  '''
  pass

def consts(): # this section needs to be global
  '''
  Constant Declaration

    Parameters:
      None
    
    Returns:
      None
  '''
  pass

def readin(nreac, wetrun, unirun):
  '''
  Open user-specified, direct-access data file (STOP if none can
  be located); open/read or create[/store] an input file containing
  i/o specifications and state conditions; open/read line 1 of an
  existing file containing reaction titles and stoichiometries or
  create[/store] such a file in its entirety.

    Parameters:
      nreac
      wetrun
      unirun
    
    Returns:
      None
  '''

def getdf():
  '''
  Checks if appropriate direct-access data file can be opened.
  
    Parameters:
      None
    
    Returns:
      True if an appropriate DA file can be opened; otherwise False
  '''
  pass

def getcon(wetcon, unirun):
  '''
  Open/read or create[/store] an input (CON) file that contains
  i/o specifications and state conditions.
  
    Parameters:
      wetcon
      unirun
    
    Returns:
      None
  '''
  pass

def defaul(wetcon):
  '''
  Set default options / state conditions.

    Parameters:
      wetcon
    
    Returns:
      None
  '''
  pass

def readcf(wetcon, unirun):
  '''
  Read options / state confitions (CON) file.

    Parameters:
      wetcon
      unirun
    
    Returns:
      None
  '''
  pass

def makecf(wetcon, unirun): # VERY IMPORTANT FUNCTION
  '''
  Prompt for and create options / state conditions (CON) file.
  
    Parameters:
      wetcon
      unirun
    
    Returns:
      None
  '''
  pass

def geteqn(useLVS, epseqn, geqn):
  '''
  Prompt for / read useLVS, epseqn, geqn.
  
    Parameters:
      useLVS
      epseqn
      geqn
    
    Returns:
      None
  '''
  pass

def getrxn(nreac, wetrxn):
  '''
  Open and read an existing reaction file (RXN) or prompt for,
  create, [and save] a new reaction file.
  
    Parameters:
      nreac
      wetrxn
    
    Returns:
      None
  '''
  pass

def parse(chrstr, r8num, name):
  '''
  If the first non-blank substring of the input character string
  (chrstr) represents a valid integer or non-exponential
  floating-point number, parse returns .TRUE. and converts this
  first substring into the corresponding real number (r8num),
  then transfers the second such subset into a CHAR*20 variable
  (name); otherwise, parse returns .FALSE.
  
    Parameters:
      chrstr
      r8num
    
    Returns:
      None
  '''
  pass

def getout():
  '''
  Prompt for and read names for output files.

    Parameters:
      None
    
    Returns:
      None
  '''
  pass

def getH2O(unirun):
  '''
  Calculate/store requisite H2O properties over the user-specified
  state condition grid.
  
    Parameters:
      unirun
    
    Returns:
      None
  '''
  pass

def oddH2O():
  '''
  Calculate/store requisite H2O properties over the user-specified
  set of state conditions.
  
    Parameters:
      None
    
    Returns:
      None
  '''
  pass

def oneH2O():
  '''
  Calculate/store requisite H2O properties over the user-specified
  state confition grid in the one-phase region.
  
    Parameters:
      None
    
    Returns:
      None
  '''
  pass

def twoH2O():
  '''
  Calculate/store requisite H2O properties over the user-specified
  state condition grid along the vaporization boundary.
  
    Parameters:
      None
    
    Returns:
      None
  '''
  pass

def seteps(Tcref, Pref, epseqn, ZPrTr, YPrTr):
  '''
  Set ZPrTr and YPrTr per epseqn value
  
    Parameters:
      Tcref
      Pref
      epseqn
    
    Returns:
      None
  '''
  pass

def H2Ostd(states, props):
  '''
  Archive requisite H2O properties for the standard state of
  25 degC, 1 bar.

    Parameters:
      states
      props
    
    Returns:
      None
  '''
  pass

def H2Osav(row, col, states, props):
  '''
  Archive requisite H2O properties over the user-specified state
  condition grid.
  
    Parameters:
      row
      col
      states
      props
    
    Returns:
      None
  '''
  pass

def getmgi(ireac):
  '''
  Read standard state properties, equation of state parameters,
  and heat capacity coefficients for all mineral, gas, and aqueous
  species in the current reaction.
  
    Parameters:
      None
    
    Returns:
      None
  '''
  pass

def getmin(i, rec1):
  '''
  Read, from dprons.dat or an analogous database (starting at
  record rec1), standard state parameters for the i[th]
  one-phase mineral species in the current reaction;
  set ntran(i) to zero.
  
    Parameters:
      i
      rec1
    
    Returns:
      None
  '''
  pass

def getgas(i, rec1):
  '''
  Read, from dprons.dat or an analogous database (starting at
  record rec1), standard state parameters for the i[th]
  gas species in the current reaction.
  
    Parameters:
      i
      rec1
    
    Returns:
      None
  '''
  pass

def getaqs(i, rec1):
  '''
  Read, from dprons.dat or an analogous database (starting at
  record rec1), standard state parameters for the i[th]
  aqueous species in the current reaction.
  
    Parameters:
      i
      rec1
    
    Returns:
      None
  '''
  pass

def runrxn(i, wetrun):
  '''
  Calculate the standard molal thermodynamic properties of the
  i[th] reaction over the range of user-specified state
  conditions.
  
    Parameters:
      i
      wetrun
    
    Returns:
      None
  '''
  pass

def rungrd(i, wetrun):
  '''
  Calculate the standard molal thermodynamic properties of the
  i[th] reaction over the user-specified state condition grid.

    Parameters:
      i
      rec1
    
    Returns:
      None
  '''
  pass

def m2tran(inc, iso, newiso, nmreac, rptran, ptrans, TPD, TPDtrn, wetrun):
  '''
  Checks if a phase transition occurs for one or more minerals
  in the current reaction between the immediately previous and
  current state conditions.
    
    Parameters:
      Many
    
    Returns:
      rptran (bool): True if phase transition occurs; False otherwise
  '''
  pass

def getsct(inc, iso, imin, iphase, ntrans, TPD, TPDtrn, wetrun):
  '''
  Get s[tate] c[onditions of phase] t[ransition] iphase
  for mineral imin.
    
    Parameters:
      Many
    
    Returns:
      None
  '''
  pass

def Tint(P1, P2, T1, T2, TtrnP2, dPdTtr):
  '''
  Computes the temperature intersection of isochore(T) with a
  mineral phase transition boundary where (dP/dT)tr .NE. 0.
  Approximation involves assumption that (dP/dT) isochore is
  linear between P1, T1, D, and P2, T2, D (consecutive locations
  on isochore D(T)) that bridge the phase transition.

    Parameters:
      Many
    
    Returns:
      None
  '''
  pass

def runodd(i):
  '''
  Calculate the standard molal thermodynamic properties of the
  i[th] reaction over the user-specified set of nonincremental
  state condition pairs.
  
    Parameters:
      i
    
    Returns:
      None
  '''
  pass

def rununi(i):
  '''
  Calculate the standard molal thermodynamic properties of the
  i[th] reaction over the user-specified set of T, logK or
  P, logK pairs.
    
    Parameters:
      i
    
    Returns:
      None
  '''
  pass

def foundK(i, wetrxn, Kfind, isoval, v2min, v2max, v2val, dH2O): # documentation of this is a mess, not sure what it says
  '''
  Documentation is a mess

    Parameters:
      Many
    
    Returns:
      None
  '''
  pass

def makerf(nreac, wetrxn):
  '''
  Prompt for and create a reaction (RXN) file.

    Parameters:
      nreac
      wetrxn
    
    Returns:
      None
  '''
  pass

def nxtrec(irec, mga, nm1234):
  '''
  Get rec1 for the next database species.
    
    Parameters:
      irec
      mga
      nm1234
    
    Returns:
      None
  '''
  pass

def readrf(nreac, wetrxn):
  '''
  Open/read user-specified reaction (RXN) file.
  
    Parameters:
      nreac
      wetrxn
    
    Returns:
      None
  '''
  pass

def wrtbad(ibad, sbad):
  '''
  Write the list of species not found in database pfname;
  prompt for repeats.

    Parameters:
      ibad
      sbad
    
    Returns:
      None
  '''
  pass

def chkrxn(ireac, namem, namea, nameg, formm, forma, formg, rxnok):
  '''
  User checks over the rxn stoichiometry.
  
    Parameters:
      Many
    
    Returns:
      True if stoichiometry is ok; False otherwise
  '''
  pass

def match(specie, form, rec1sp, rec1ty, first, last, nm1234):
  '''
  Checks if specie is found in database pfname.

    Parameters:
      Many
    
    Returns:
      None
  '''
  pass

def umaker(ireac, coeff, specie, form, rec1, namem, namea, nameg,
            formm, forma, formg):
  '''
  Update /reac/ arrays to include current species.
  
    Parameters:
      Many
    
    Returns:
      None'''
  pass

def openf(iterm, iunit, fname, istat, iaccess, iform, irecl):
  '''
  Opens the file specified by fname, fstat, facces, fform, and
  frecl if this file exists and is accessible. Prints any error
  messages to device specified by iterm.
  
    Parameters:
      Many
    
    Returns:
      True if file exists and is accessible; False otherwise
  '''
  pass
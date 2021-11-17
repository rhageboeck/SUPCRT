"""
*** REPBL - Collection of routines that write the calculated standard 
***         molal thermodynamic properties of reactions to the TAB
***         file and, optionally, the PLOT files.
***
*********************************************************************
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
*********************************************************************
"""

def tabtop():
  '''
  Write global header for output file.

    Parameters:
      None
    
    Returns:
      None
  '''
  pass

def wrtopt():
  '''
  Write various switch options to tabular output file.

    Parameters:
      None
    
    Returns:
      None
  '''
  pass

def wrtop2(k):
  '''
  Write various switch options to plot file k.
  
    Parameters:
      k - plot file
    
    Returns:
      None
  '''
  pass

def wrtrxn(i):
  '''
  Write header information for the i[th] reaction to tabulated
  output file tabf and (if appropriate) to the plot files.
  
    Parameters:
      i - reaction information
    
    Returns:
      None
  '''
  pass

def zero(i, nullrx):
  '''
  Zero-out NULL values for reaction i to eliminate their contribution
  to standard molal properties at elevated temperatures and
  pressures; set nullrx to .TRUE. if Gf missing for mineral species
  or a1..4 for aqueous species.
  
    Parameters:
      i
      nullrx
    
    Returns:
      None
  '''
  pass

def wrtssp(i):
  '''
  Write, to tabf, standard molal thermodynamic properties at 25 C
  and 1 bar, equation-of-state parameters, and heat capacity coefficients
  for all species in the i[th] reaction.
  
    Parameters:
      i
    
    Returns:
      None
  '''
  pass

def pltrxn(ireac):
  '''
  Write header information and reaction titles to plot files.

    Parameters:
      ireac
    
    Returns:
      None
  '''
  pass

def plttop(i):
  '''
  Write global banner to plot file i

    Parameters:
      i
    
    Returns:
      None
  '''
  pass

def report(ireac, iso, inc, TPD, TPDtrn, rptran, ptrans,
            dVr, dSr, dCpr, dHr, dGr, logKr, lvdome, H2Oerr, Kfound):
  '''
  Report computes reaction properties.
  
    Parameters:
      Many
    
    Returns:
      None
  '''
  pass

def pltln1(TPD):
  '''
  Write top line of next property block.

    Parameters:
      TPD
    
    Returns:
      None
  '''
  pass

def pltrep(TPD, iso, inc, logKr, dGr, dHr, dSr, dCpr, dVr,
            lvdome, H2Oerr, Klost, xall, xHSVCp, xCp):
  '''
  Report calculated property values to plot files or buffers.

    Parameters:
      Many
    
    Returns:
      None
  '''
  pass

def blanks(T, P, D, m2reac, nm, ng, na, xall, xHSVCp, xCp,
            Mkwarn, Pwarn):
  '''
  Set xall, xCp, Mkwarn per current state conditions.

    Parameters:
      Many
    
    Returns:
      None
  '''
  pass
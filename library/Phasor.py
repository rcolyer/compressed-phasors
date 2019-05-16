"""
Ryan A. Colyer

Store phasor information, corresponding to the linearly accumulated real and
imaginary components of the first harmonic of the Fourier transform of the
fluorescence lifetime response for a given photon, pixel, or area.

"""

from math import cos, sin, tan, atan, atan2, pi, sqrt
from numpy import sign

# Stores photon data with first harmonic phasor information.
class Photon:
  def __init__(self, x, y, nanotime):
    self.x = x
    self.y = y
    self.nanotime = nanotime
    self.g = cos(nanotime*2*pi)
    self.s = sin(nanotime*2*pi)

# Properly accumulates phasor information for a given point.
class Phasor:
  def __init__(self, photon=None):
    if photon is None:
      self.big_G = 0
      self.big_S = 0
      self.count = 0
    else:
      self.big_G = photon.g
      self.big_S = photon.s
      self.count = 1

  def __add__(self, phasor):
    self.big_G += phasor.big_G
    self.big_S += phasor.big_S
    self.count += phasor.count
    return self

  # Return the canonical g coordinate for a phasor.
  def g(self):
    return self.big_G / self.count

  # Return the canonical s coordinate for a phasor.
  def s(self):
    return self.big_S / self.count

# Return the intensity normalized 2D g and s data.
def NormalizePhasorData(bigG, bigS, intensity):
  g = [[G/I for G,I in zip(Grow, Irow)] for Grow,Irow in zip(bigG, intensity)]
  s = [[S/I for S,I in zip(Srow, Irow)] for Srow,Irow in zip(bigS, intensity)]
  return (g,s)

# Return a phi image.
def GetPhiData(g_data, s_data):
  return [[atan2(s, g) for g,s in zip(grow, srow)] for grow,srow in zip(g_data, s_data)]

# Return a modulation image.
def GetModData(g_data, s_data):
  return [[sqrt(g*g+s*s) for g,s in zip(grow, srow)] for grow,srow in zip(g_data, s_data)]


phicap_maxv = atan(100)
def PhiCap(phi):
  maxv = atan(100)
  if phi > maxv:
    return maxv
  else:
    return phi

modcap_minv = sqrt(1/(100**2+1))
def ModCap(m):
  if m < modcap_minv:
    return modcap_minv
  else:
    return m

# Return a TauP image.
def GetTauPData(g_data, s_data, freq):
  phi_data = GetPhiData(g_data, s_data)
  omega = 2 * pi * freq
  return [[tan(PhiCap(phi))/omega for phi in phi_row] for phi_row in phi_data]

# Return a TauM image.
def GetTauMData(g_data, s_data, freq):
  m_data = GetModData(g_data, s_data)
  omega = 2 * pi * freq
  return [[sign(m)*sqrt(abs(1/(ModCap(m)**2)-1))/omega for m in m_row] for m_row in m_data]


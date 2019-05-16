"""
Ryan A. Colyer

Image simulation tools for compressive sensing with FLIM.

"""

from abc import ABC, abstractmethod
from math import log
import random
from library.Phasor import Photon
import library.CompressiveSensing as cs
import copy
import numpy as np


# intensity unit 1 for always on.
# lifetime unit 1 for laser period.  Special value 0 is uncorrelated light.
class Pixel:
  def __init__(self, intensity, lifetime=0):
    self.intensity = intensity
    self.lifetime = lifetime

  # Generate random fluorescence lifetime nanotime with periodicity 1.
  def GetNanotime(self, rng):
    if self.lifetime == 0:
      return rng.random()
    else:
      return (-self.lifetime*log(rng.random())) % 1



# Base class for image simulation.
class ImageSimulator(ABC):
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def GetDim(self):
    return (self.width, self.height)

  @abstractmethod
  def GetPixel(self, x, y):
    return NotImplemented


# Provides a static intensity image with uncorrelated (long lifetime) counts.
class StaticImage(ImageSimulator):
  def __init__(self, width, height):
    super().__init__(width, height)
    self.image_data = [[Pixel(0) for x in range(width)] for y in range(height)]

  def GetPixel(self, x, y):
    return self.image_data[y][x]

  def SetPixels(self, pixel, xy_list):
    for xy in xy_list:
      self.image_data[xy[1]][xy[0]] = copy.deepcopy(pixel)

  def Intensity(self):
    return [[self.image_data[y][x].intensity for x in range(self.width)] for y in range(self.height)]


# Base class for a photon detection sequence.
class PhotonSource(ABC):
  @abstractmethod
  def GetFrame(self):
    return NotImplemented


# Provides a photon detection sequence simulator based on a given image source.
class PhotonSimSource(PhotonSource):
  def __init__(self, image_source, sim_intensity):
    super().__init__()
    self.image_source = image_source
    self.sim_intensity = sim_intensity

  def AddPixelPhotons(self, x, y, iframe):
    pixel = self.image_source.GetPixel(x, y)
    pix_avgcnt = self.sim_intensity * pixel.intensity;
    ph_cnt = np.random.poisson(pix_avgcnt)
    for ph in range(ph_cnt):
      nanotime = pixel.GetNanotime(np.random)
      photon = Photon(x, y, nanotime)
      iframe.Add(photon)

  def GetFrame(self):
    height = self.image_source.height
    width = self.image_source.width
    mask = cs.Mask(width, height)
    iframe = cs.Frame(mask)
    for (x,y) in ((x,y) for y in range(height) for x in range(width)):
      if mask.IsOn(x, y):
        self.AddPixelPhotons(x, y, iframe)
    return iframe


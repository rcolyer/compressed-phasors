"""
Ryan A. Colyer

Compressive Sensing Analysis tools.

"""

import numpy as np
import random
from library.Phasor import Phasor
from sklearn.linear_model import Lasso

# Stores the data for one compressive FLIM frame, consisting of a mask,
# the intensity, and the phasor data.
class Frame:
  def __init__(self, mask):
    self.mask = mask
    self.data = Phasor()

  def Add(self, photon):
    self.data += Phasor(photon)


# A randomly generated mask.
class Mask:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.data = [[np.random.randint(0,2) for x in range(width)] for y in range(height)]

  def IsOn(self, x, y):
    return 1 == self.data[y][x]

  def IsOff(self, x, y):
    return not self.IsOn(x, y)


# Reconstruct the base image with L1 penalization using Lasso.
class Reconstruction:
  def __init__(self, alpha=0.001):
    self.model = Lasso(alpha)
  
  def ModelFit(self, frames, data):
    height = frames[0].mask.height
    width = frames[0].mask.width
    masks = self.GetMasks(frames)
    self.model.fit(masks, data)
    self.result = self.model.coef_.reshape(height, width)
    return self.result

  def GetMasks(self, frames):
    return np.array([np.array(f.mask.data).ravel() for f in frames])

  def FitIntensity(self, frames):
    counts = np.array([f.data.count for f in frames])
    return self.ModelFit(frames, counts)

  def FitG(self, frames):
    bigGs = np.array([f.data.big_G for f in frames])
    return self.ModelFit(frames, bigGs)

  def FitS(self, frames):
    bigSs = np.array([f.data.big_S for f in frames])
    return self.ModelFit(frames, bigSs)


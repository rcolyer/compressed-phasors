"""
Ryan A. Colyer

Predefined images for simulation purposes.
"""

import library.ImageGen as ig


def MakeSmileImage(freq):
  dim = [8, 8]
  img = ig.StaticImage(*dim)

  spec1 = ig.Pixel(1, 4.08e-9*freq) # Rhodamine 6G
  background = ig.Pixel(0.3, 0*freq) # Uncorrelated background light

  # Draw out a smiley face test image for the theory paper.
  img.SetPixels(background, [[x,y] for x in range(dim[0]) for y in range(dim[1])])
  img.SetPixels(spec1, [[2,2],[5,2],[0,5],*[[x,6] for x in range(1,7)],[7,5]])

  return img


def MakeCellImage(freq):
  dim = [16, 16]
  img = ig.StaticImage(*dim)

  GFP = ig.Pixel(0.8, 3.20e-9*freq) # Membrane bound
  DAPI = ig.Pixel(1, 2.20e-9*freq) # Nuclear stain
  autofluor = ig.Pixel(0.4, 100e-9*freq) # Long-lifetime autofluorescence
  background = ig.Pixel(0.2, 0*freq) # Uncorrelated background light

  img.SetPixels(background, [[x,y] for x in range(dim[0]) for y in range(dim[1])])
  img.SetPixels(GFP, [[8,2],[9,2],[7,3],[10,3],[11,3],[4,4],[5,4],[6,4],[12,4],[13,4],[3,5],[14,5],[2,6],[14,6],[2,7],[14,7],[1,8],[14,8],[1,9],[13,9],[2,10],[12,10],[3,11],[12,11],[4,12],[11,12],[5,13],[6,13],[9,13],[10,13],[7,14],[8,14]])
  img.SetPixels(autofluor, [[x,3] for x in range(8,10)])
  img.SetPixels(autofluor, [[x,4] for x in range(7,12)])
  img.SetPixels(autofluor, [[x,5] for x in range(4,14)])
  img.SetPixels(autofluor, [[x,6] for x in range(3,14)])
  img.SetPixels(autofluor, [[x,7] for x in range(3,14)])
  img.SetPixels(autofluor, [[x,8] for x in range(2,14)])
  img.SetPixels(autofluor, [[x,9] for x in range(2,13)])
  img.SetPixels(autofluor, [[x,10] for x in range(3,12)])
  img.SetPixels(autofluor, [[x,11] for x in range(4,12)])
  img.SetPixels(autofluor, [[x,12] for x in range(5,11)])
  img.SetPixels(autofluor, [[x,13] for x in range(7,9)])
  img.SetPixels(DAPI, [[7,7],[8,7],[6,8],[7,8],[8,8],[9,8],[6,9],[7,9],[8,9],[9,9],[7,10],[8,10]])

  return img


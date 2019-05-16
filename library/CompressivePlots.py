"""
Ryan A. Colyer

Generate comparison plots of Compressive Sensing results

"""

import numpy as np
import matplotlib.pyplot as plt

def Plot2(a, Lab_a, b, Lab_b, filename=None, display=True):
  plt.figure(figsize=(8, 4))
  plt.set_cmap('nipy_spectral')

  plt.subplot(1,2,1)
  plt.imshow(np.flipud(a))
  plt.title(Lab_a)
  plt.colorbar()
  plt.axis('off')

  plt.subplot(1,2,2)
  plt.imshow(np.flipud(b))
  plt.title(Lab_b)
  plt.colorbar()
  plt.axis('off')

  plt.subplots_adjust(hspace=0.07, wspace=0.07, top=0.91, bottom=0.02, left=0.005, right=0.99)

  if filename:
    plt.savefig(filename, dpi=300)

  if display:
    plt.show()

  plt.close()


def Plot3(a, Lab_a, b, Lab_b, c, Lab_c, filename=None, display=True):
  plt.figure(figsize=(11, 4))
  plt.set_cmap('nipy_spectral')

  plt.subplot(1,3,1)
  plt.imshow(np.flipud(a))
  plt.title(Lab_a)
  plt.colorbar()
  plt.axis('off')

  plt.subplot(1,3,2)
  plt.imshow(np.flipud(b))
  plt.title(Lab_b)
  plt.colorbar()
  plt.axis('off')

  plt.subplot(1,3,3)
  plt.imshow(np.flipud(c))
  plt.title(Lab_c)
  plt.colorbar()
  plt.axis('off')

  plt.subplots_adjust(hspace=0.07, wspace=0.07, top=0.95, bottom=0.02, left=0.005, right=0.99)

  if filename:
    plt.savefig(filename, dpi=300)

  if display:
    plt.show()

  plt.close()


def Plot4(a, Lab_a, b, Lab_b, c, Lab_c, d, Lab_d, filename=None, display=True, zscale=[None, None, None, None]):
  plt.figure(figsize=(8, 7))
  plt.set_cmap('nipy_spectral')

  plt.subplot(2,2,1)
  if zscale[0]:
    plt.pcolor(a, vmin=zscale[0][0], vmax=zscale[0][1])
  else:
    plt.pcolor(a)
  plt.title(Lab_a)
  plt.colorbar()
  plt.axis('off')

  plt.subplot(2,2,2)
  if zscale[1]:
    plt.pcolor(b, vmin=zscale[1][0], vmax=zscale[1][1])
  else:
    plt.pcolor(b)
  plt.title(Lab_b)
  plt.colorbar()
  plt.axis('off')

  plt.subplot(2,2,3)
  if zscale[2]:
    plt.pcolor(c, vmin=zscale[2][0], vmax=zscale[2][1])
  else:
    plt.pcolor(c)
  plt.title(Lab_c)
  plt.colorbar()
  plt.axis('off')

  plt.subplot(2,2,4)
  if zscale[3]:
    plt.pcolor(d, vmin=zscale[3][0], vmax=zscale[3][1])
  else:
    plt.pcolor(d)
  plt.title(Lab_d)
  plt.colorbar()
  plt.axis('off')

  plt.subplots_adjust(hspace=0.07, wspace=0.07, top=0.95, bottom=0.02, left=0.005, right=0.99)

  if filename:
    plt.savefig(filename, dpi=300)

  if display:
    plt.show()

  plt.close()


def PlotArray(data_arr, label_arr, filename=None, display=True, zscale=None):
  w = len(data_arr[0])
  h = len(data_arr)
  plt.figure(figsize=(3*w+1, 3.5*h))
  plt.set_cmap('nipy_spectral')

  index = 1
  for (x,y) in ((x,y) for y in range(h) for x in range(w)):
    plt.subplot(w, h, index)
    plt.title(label_arr[y][x])
    if zscale:
      plt.pcolor(data_arr[y][x], vmin=zscale[0], vmax=zscale[1])
    else:
      plt.pcolor(data_arr[y][x])
    
#    if x == w-1:
#      plt.colorbar()

    plt.axis('off')

    index += 1
  
  plt.subplots_adjust(hspace=0.07, wspace=0.07, top=0.95, bottom=0.02, left=0.005, right=0.99)

  if filename:
    plt.savefig(filename, dpi=300)

  if display:
    plt.show()

  plt.close()


def IntensityComparison(original, result, filename=None, display=True):
  Plot2(original, '(a) Simulation Input', result, '(b) Compressive Sensing', filename, display)

def IGSComparison(original, intensity, bigG, bigS, filename=None, display=True):
  Plot4(original, '(a) Simulation Input', intensity, '(b) CS Intensity', bigG, '(c) CS BigG', bigS, '(d) CS BigS', filename, display)

def IgsComparison(original, intensity, g, s, filename=None, display=True):
  Plot4(original, '(a) Simulation Input', intensity, '(b) CS Intensity', g, '(c) CS g', s, '(d) CS s', filename, display, zscale=[None,None,[0,1],[0,1]])

def ITauPComparison(original, intensity, taup, filename=None, display=True):
  Plot3(original, '(a) Simulation Input', intensity, '(b) CS Intensity', taup, '(c) CS TauP', filename, display)

def ITauMComparison(original, intensity, taum, filename=None, display=True):
  Plot3(original, '(a) Simulation Input', intensity, '(b) CS Intensity', taum, '(c) CS TauM', filename, display)


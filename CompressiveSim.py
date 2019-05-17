#!/usr/bin/python3
"""
Ryan A. Colyer

Compressive Fluorescence Lifetime Imaging Microscopy simulation testbed.

This simulation is for working out analysis ideas under a controlled system,
and to demonstrate the Compressed Phasors method.

This approach is based on a previous MATLAB simulation done as undergraduate
research by Sarah Grant.

"""

import library.RunTime as rt
import library.MakeImages as make_img
import library.Simulator as cssim
import library.CompressivePlots as cp
import numpy as np

run_timer = rt.RunTime()


randseed = None
freq = 2*((32/17)*100e6)/8
frames_per_s = 60

print('randseed', randseed)
print('freq', freq)
print('frames_per_s', frames_per_s)

np.random.seed(None)
img = make_img.MakeCellImage(freq)
total_brightness = np.sum(img.Intensity())

print('total_brightness', total_brightness)
print('Input', img.Intensity())


def Make_g_array(sim):
  g_arr = []
  labels = []
  index = 'a'
  for frame_count in range(800,3200+1,800):
    g_row = []
    l_row = []
    for sim_cps in range(80000,320000+1,80000):
      sim.SimAndOutput(sim_cps, frame_count)
      g_row.append(sim.g_res)
      l_row.append('('+index+') '+str(sim_cps)+' cps, '+str(frame_count)+' frames')
      index = chr(ord(index)+1)
    g_arr.append(g_row)
    labels.append(l_row)

  cp.PlotArray(g_arr, labels, 'plots/g_array.png', display=False, zscale=[0,1])

def Make_g_noise_data(sim):
  frame_count = 2400
  cps = []
  sdarr = []
  print('# cps, stdev')
  for sim_cps in range(20000,320000+1,20000):
    gvals = []
    for i in range(10):
      sim.SimulateImage(sim_cps, frame_count)
      gvals.append(sim.g_res[8][8])
    sd = np.std(gvals, ddof=1)
    sdarr.append(sd)
    cps.append(sim_cps)
    print(str(sim_cps)+', '+str(sd))


sim = cssim.CSSimulator(img, total_brightness, freq, frames_per_s, run_timer)

#Make_g_array(sim)

#Make_g_noise_data(sim)

sim.SimAndOutput(sim_cps=320000, frame_count=3200)


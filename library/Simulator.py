"""
Ryan A. Colyer

The simulator class for compressive sensing with FLIM.
"""

import library.ImageGen as ig
import library.CompressiveSensing as cs
import library.Phasor as ph
import library.CompressivePlots as plot


class CSSimulator:
  def __init__(self, img, total_brightness, freq, frames_per_s, run_timer):
    self.img = img
    self.total_brightness = total_brightness
    self.freq = freq
    self.frames_per_s = frames_per_s
    self.input_intensity = img.Intensity()
    self.run_timer = run_timer

  # Acquire the full list of compressive sensing frames.
  def GetFrames(self, ph_source, frame_count):
    return [ph_source.GetFrame() for f in range(frame_count)]

  # Run one compressive sensing simulation.
  def SimulateImage(self, sim_cps, frame_count):
    self.sim_intensity = (sim_cps/self.frames_per_s)/(self.total_brightness/2)

    ph_source = ig.PhotonSimSource(self.img, self.sim_intensity)
    self.frames = self.GetFrames(ph_source, frame_count=frame_count)

    l1min = cs.Reconstruction()

    self.intensity_result = l1min.FitIntensity(self.frames)
    self.G_result = l1min.FitG(self.frames)
    self.S_result = l1min.FitS(self.frames)

    (self.g_res, self.s_res) = ph.NormalizePhasorData(self.G_result, self.S_result, self.intensity_result)
    self.taup_res = ph.GetTauPData(self.g_res, self.s_res, self.freq)
    self.taum_res = ph.GetTauMData(self.g_res, self.s_res, self.freq)

  def SimAndOutput(self, sim_cps, frame_count):
    self.SimulateImage(sim_cps, frame_count)

    print('sim_cps', sim_cps)
    print('frame_count', frame_count)
    print('Intensity', self.intensity_result)
    print('sim_intensity,', self.sim_intensity)
    print('frames[0] count', self.frames[0].data.count)
    print("g", self.g_res)
    print("s", self.s_res)
    print('taup', self.taup_res)
    print('taum', self.taum_res)
    print('Simulation run time: ', self.run_timer.SinceStart())

    pltdir = 'plots/'
    suffix = '_' + str(sim_cps) + '_' + str(frame_count)
    plot.IntensityComparison(self.input_intensity, self.intensity_result, pltdir+'intensity_comparison'+suffix+'.png', display=False)
    plot.ITauPComparison(self.input_intensity, self.intensity_result, self.taup_res, pltdir+'taup_comparison'+suffix+'.png', display=False)
    plot.ITauMComparison(self.input_intensity, self.intensity_result, self.taum_res, pltdir+'taum_comparison'+suffix+'.png', display=False)
    plot.IgsComparison(self.input_intensity, self.intensity_result, self.g_res, self.s_res, pltdir+'gs_comparison'+suffix+'.png', display=False)



# Compressed Phasors simulator

This project demonstrates the Compresed Phasors method for combining Compressive Sensing with Fluorescence Lifetime Imaging Microscopy (FLIM).

## Getting Started

To use this simulation, you will need a working python3 installation with numpy, scikit-learn, and matplotlib.  The bash script "run" will execute the program and store the output in date-stamped log files, or you can run the program directly in Python via the CompressiveSim.py file.

## Modifications and Simulation Modalities

Customizations to the simulation's system settings can be made by adjusting the variables at the top of CompressiveSim.py to adjust the frequency or the frame rate for updating the compressive sensing masks.  Adjustment of acquisition settings varies by the simulation modality used.

sim.SimAndOutput, demonstrated at the bottom of CompressiveSim.py, produces a set of plots comparing the input image with compressive sensing intensity, tau\_m lifetime images, tau\_p lifetime images, and the g and s phasor images.

The function Make\_g\_array(sim) in CompressiveSim.py produces a two-dimensional array of g-images varying across the specified range of frame counts in the vertical xis, and across the specified range of whole-image counts per second in the horizontal axis.  This can be used to examine the structural quality of the phasor data obtained under various conditions.

The function Make\_g\_noise\_data(sim) in CompressiveSim.py produces comma-separated values showing the standard deviation of g-values for the given near-center pixel across the range of whole-image counts per second.

## Components

* library/CompressivePlots.py - Uses matplotlib to generate output plots.
* library/CompressiveSensing.py - Contains the compressive sensing routines which use Lasso from scikit-learn to extract the image data.
* library/ImageGen.py - Contains routines to produce a simulated stream of photons from a provided image structure.
* library/MakeImages.py - Has functions for generating demonstration image structures for simulation input.
* library/Phasor.py - Has classes for storing phasor and photon count data, and functions for performing phasor calculations.
* library/RunTime.py - Tracks simulation runtime.
* library/Simulator.py - Contains a compressed phasors simulator class for running a full image acquisition simulation under given conditions.

## License

This project is licensed under the Boost Software License, making it free for use and modification.  See the [LICENSE.txt](LICENSE.txt) file for details.


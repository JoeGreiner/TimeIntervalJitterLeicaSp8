# Time Interval Jitter LeicaSp8

This repository is documentation/analysis scripts for an unexpected time jitter phenomena (jitter between two frame acquisitions/interval between two subsequent frames) we observed with the Leica SP8 platform (observed both with multiphoton and confocal microscope). When recording a timeseries with Navigator, the time between frames is not constant, but exhibits quite a large time jitter (up to 44ms maximal jitter). However, these phenomena is not present when recording outside Navigator with exactly the same acquisition settings (regular jitter of ~1ms or less). This jitter is visualised here:

![timeseries_with_navigator](https://github.com/JoeGreiner/TimeJitterLeicaSp8/assets/24453528/cb76c193-8531-4013-bb56-c33843ab4fb8)

![timeseries_same_settings_no_navigator](https://github.com/JoeGreiner/TimeJitterLeicaSp8/assets/24453528/2ab60260-a0eb-4d1a-9632-813f6605580b)

This is a problem for us in experimental settings in which we are characterising very fast dynamics. For slower acquisition settings, the time jitter is likely a very small error and can be ignored. We are running Windows 10 (version) and LASX software version XX without a graphic card, which may be an unsupported configuration from Leica. 

# Reproducing the analysis
* Create a conda environment: conda create --file environment.yml
* Run run_analysis.py
* Plots will be saved in the folder `analysis/`

# Reproducing the data
* Record a timeseries with and without Navigator at a SP8X 
* Open the lif files with Fiji and Bioformats, in the initial IO dialog, select 'Display OME Metadata'.
* Save the metadata as a xml file. Point to the folder of xml files in run_analysis.py.
* Run run_analysis.py

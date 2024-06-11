# Time Interval Jitter Leica SP8

This repository is documentation/analysis scripts for an unexpected time jitter phenomena (jitter between two frame acquisitions/interval between two subsequent frames) we observed when recording time series with the Leica SP8 platform (observed both with multiphoton and confocal microscope). When recording a timeseries with LAS X Navigator, the time between frames is not constant, but exhibits quite a large time jitter (in our example case up to 44ms maximal jitter). However, these phenomena are not present when recording without LAS X Navigator (regular jitter of ~1ms or less; with exactly the same acquisition settings). This is visualised here:

![timeseries_with_navigator](https://github.com/JoeGreiner/TimeJitterLeicaSp8/assets/24453528/cb76c193-8531-4013-bb56-c33843ab4fb8)

![timeseries_same_settings_no_navigator](https://github.com/JoeGreiner/TimeJitterLeicaSp8/assets/24453528/2ab60260-a0eb-4d1a-9632-813f6605580b)

This can be problem in experimental settings in which very fast dynamics are investigated and precise timing is important. For slower acquisition settings, the time interval jitter only adds a small error (relative to the frame cycling time) and likely can be ignored. We are running Windows 10 Enterprise 2016 LTSB (Version 1607) and LAS X version 3.5.7.23225.

# Reproducing the analysis
* Create a conda environment: conda create --file environment.yml
* Run run_analysis.py
* Plots will be saved in the folder `analysis/`

# Reproducing the data
* Record a timeseries with and without LAS X Navigator at a SP8
* Open the lif files with Fiji/ImageJ and Bioformats, in the initial IO dialog, select 'Display OME Metadata'
* Save the metadata as a xml file. Point to the folder of xml files in run_analysis.py.
* Run run_analysis.py

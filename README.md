# Project

## DNN-DRT: Advancing the deconvolution of the distribution of relaxation times with deep neural networks
This repository contains some of the source code used for the paper titled *Deconvolution of electrochemical impedance spectroscopy data using the deep-neural-network-enhanced distribution of relaxation times*. Electrochimica Acta, 439, 141499. https://doi.org/10.1016/j.electacta.2022.141499. The article is available online at [Link](https://doi.org/10.1016/j.electacta.2022.141499) and in the [docs](docs) folder. 
# Introduction
Electrochemical impedance spectroscopy (EIS) is characterization technique widely used to investigate electrochemical systems, such as batteries and fuel cells. To analyze EIS data, the distribution of relaxation times (DRT) has emerged as a versatile alternative to the equivalent circuits and physical models. Deconvolving the DRT from EIS spectra is however challenging, and several approaches have been proposed for this purpose. In particular, deep neural networks (DNNs) have proven useful to recover and predict the DRT, including when the EIS data is noisy or the DRT is discontinuous, and also to analyze many EIS spectra simultaneously. Recently, our group proposed the DNN-DRT model to speed up the training, assess the DNN accuracy, and investigate EIS data with inductive features.


![image](https://github.com/ciuccislab/pyDRTtools/assets/57649983/c0d8e299-5cac-4b19-a753-1c60d951d337)

# Dependencies

numpy

scipy

matplotlib

pandas

torch

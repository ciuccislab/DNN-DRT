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

cvxpy

# Tutorials

**ex1_2ZARC.ipynb**: this notebook provides a detailed procedure on how to recover the DRT from the impedance generated using $2\times \rm ZARC$ models arranged in series.

**ex2_hook.ipynb**: this notebook provides a detailed procedure on how to recover the DRT from the impedance spectra exhibiting inductive behavior.

**ex3_PEMFC.ipynb**: this notebook provides a detailed procedure on how to recover the DRT from real impedance, which exhibits inductive behavior, obtained from proton exchange membrane fuel cell.


# Citation

```
@article{quattrocchi2023deconvolution,
  title={Deconvolution of electrochemical impedance spectroscopy data using the deep-neural-network-enhanced distribution of relaxation times},
  author={Quattrocchi, Emanuele and Py, Baptiste and Maradesa, Adeleke and Meyer, Quentin and Zhao, Chuan and Ciucci, Francesco},
  journal={Electrochimica Acta},
  volume={439},
  pages={141499},
  year={2023},
  publisher={Elsevier}
}

```

# References
[1] Ciucci, F. (2018). Modeling electrochemical impedance spectroscopy. Current Opinion in Electrochemistry.132-139 https://doi.org/10.1016/j.coelec.2018.12.003

[2] Wan, T. H., Saccoccio, M., Chen, C., & Ciucci, F. (2015). Influence of the discretization methods on the distribution of relaxation times deconvolution: implementing radial basis functions with DRTtools. Electrochimica Acta, 184, 483-499. https://doi.org/10.1016/j.electacta.2015.09.097

[3] Saccoccio, M., Wan, T. H., Chen, C., & Ciucci, F. (2014). Optimal regularization in distribution of relaxation times applied to electrochemical impedance spectroscopy: ridge and lasso regression methods-a theoretical and experimental study. Electrochimica Acta, 147, 470-482. https://doi.org/10.1016/j.electacta.2014.09.058

[4] Effat, M. B., & Ciucci, F. (2017). Bayesian and hierarchical Bayesian based regularization for deconvolving the distribution of relaxation times from electrochemical impedance spectroscopy data. Electrochimica Acta, 247, 1117-1129. https://doi.org/10.1016/j.electacta.2017.07.050

[5] Ciucci, F., & Chen, C. (2015). Analysis of electrochemical impedance spectroscopy data using the distribution of relaxation times: A Bayesian and hierarchical Bayesian approach. Electrochimica Acta, 167, 439-454. https://doi.org/10.1016/j.electacta.2015.03.123

[6] Liu, J., Ciucci, F., The Deep-Prior Distribution of Relaxation Times Journal of The Electrochemical Society, 167.2 (2020): 026506 https://doi.org/10.1149/1945-7111/ab631a

# Project

## DNN-DRT: Advancing the deconvolution of the distribution of relaxation times with deep neural networks
This repository contains some of the source code used for the paper titled *Deconvolution of electrochemical impedance spectroscopy data using the deep-neural-network-enhanced distribution of relaxation times*. Electrochimica Acta, 439, 141499. https://doi.org/10.1016/j.electacta.2022.141499. The article preprint is also available online in [Link](https://chemrxiv.org/engage/chemrxiv/article-details/62dfb097e7fc8fb5b78903a8) and in the [docs](docs) folder. 
# Introduction
Electrochemical impedance spectroscopy (EIS) is a characterization technique widely used to investigate electrochemical systems, such as batteries and fuel cells [1,2,3]. To analyze EIS data, the 
distribution of relaxation times (DRT) has emerged as a versatile alternative to the equivalent circuits and physical models [1-8]. Deconvolving the DRT from EIS spectra is however challenging, and several
approaches have been developed for this purpose [2-8]. In particular, deep neural networks (DNNs) have proven useful to recover and predict the DRT, including when the EIS data is noisy or the DRT is discontinuous [9], and also to analyze many EIS spectra simultaneously [10]. Recently, our group developed the DNN-DRT model to speed up the training, assess the DNN accuracy, and investigate EIS data with inductive features [11].


![image](https://github.com/ciuccislab/pyDRTtools/assets/57649983/c0d8e299-5cac-4b19-a753-1c60d951d337)

# Dependencies

numpy

scipy

matplotlib

pandas

torch

cvxpy

# Tutorials

**ex1_hook.ipynb**: this notebook provides a detailed procedure on how to recover the DRT from the impedance spectra exhibiting inductive behavior.

**ex2_fuel-cell.ipynb**: this notebook provides a detailed procedure on how to recover the DRT from real impedance, which exhibits inductive behavior, obtained from proton exchange membrane fuel cell.


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

[4] Liu, J., & Ciucci, F. (2020). The Gaussian process distribution of relaxation times: A machine learning tool for the analysis and prediction of electrochemical impedance spectroscopy data. Electrochimica Acta, 135316. https://doi.org/10.1016/j.electacta.2019.135316.

[5] Effat, M. B., & Ciucci, F. (2017). Bayesian and hierarchical Bayesian based regularization for deconvolving the distribution of relaxation times from electrochemical impedance spectroscopy data. Electrochimica Acta, 247, 1117-1129. https://doi.org/10.1016/j.electacta.2017.07.050.

[6] Maradesa, A., Py, B., Quattrocchi, E., & Ciucci, F. (2022). The probabilistic deconvolution of the distribution of relaxation times with finite Gaussian processes. Electrochimica Acta, 413, 140119. https://doi.org/10.1016/j.electacta.2022.140119.

[7] Py, B., Maradesa, A., & Ciucci, F. (2023). Gaussian processes for the analysis of electrochemical impedance spectroscopy data: Prediction, filtering, and active learning. Electrochimica Acta, 439, 141688. [doi.org/10.1016/j.electacta.2022.141688] (https://doi.org/10.1016/j.electacta.2022.141688)

[8] Ciucci, F., & Chen, C. (2015). Analysis of electrochemical impedance spectroscopy data using the distribution of relaxation times: A Bayesian and hierarchical Bayesian approach. Electrochimica Acta, 167, 439-454. https://doi.org/10.1016/j.electacta.2015.03.123

[9] Liu, J., Ciucci, F., The Deep-Prior Distribution of Relaxation Times Journal of The Electrochemical Society, 167.2 (2020): 026506 https://doi.org/10.1149/1945-7111/ab631a

[10] E. Quattrocchi, T.H. Wan, A. Belotti, D. Kim, S. Simona, S.V. Kalinin, M. Ahmadi, F. Ciucci, The deep-DRT: A deep neural network approach to deconvolve the distribution of relaxation times from multidimensional electrochemical impedance spectroscopy data. Electrocimica Acta, 392 (2021) 139010.[doi.org/10.1016/j.electacta.2021.139010](https://doi.org/10.1016/j.electacta.2021.139010)

[11] E. Quattrocchi, B. Py, A. Maradesa, Q. Meyer, C. Zhao, F. Ciucci, Deconvolution of electrochemical impedance spectroscopy data using the deep-neural-network-enhanced distribution of relaxation times. Electrocimica Acta, 439 (2023) 141499.[https://doi.org/10.1016/j.electacta.2022.141499](https://doi.org/10.1016/j.electacta.2022.141499)


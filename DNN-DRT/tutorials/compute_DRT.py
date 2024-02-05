import numpy as np
from math import pi, log

def compute_A_re(freq_vec, tau_vec):
    
    omega_vec = 2.*pi*freq_vec
    N_f = freq_vec.size
    N_tau = tau_vec.size

    out_A_re = np.zeros((N_f, N_tau))
    
    for m in range(0, N_f):
        for n in range(0, N_tau):

            if n == 0:
                Delta_log_tau = log(tau_vec[n+1]/tau_vec[n])
            elif n == N_tau-1:
                Delta_log_tau = log(tau_vec[n]/tau_vec[n-1])
            else:
                Delta_log_tau = log(tau_vec[n+1]/tau_vec[n-1])
              
            out_A_re[m,n] = 0.5/(1+(omega_vec[m]*tau_vec[n])**2)*Delta_log_tau
            
    return out_A_re

def compute_A_im(freq_vec, tau_vec):
    
    omega_vec = 2.*pi*freq_vec

    N_tau = tau_vec.size
    N_f = freq_vec.size

    out_A_im = np.zeros((N_f, N_tau))
    
    for m in range(0, N_f):
        for n in range(0, N_tau):
            if n == 0:
                Delta_log_tau = log(tau_vec[n+1]/tau_vec[n])
            elif n == N_tau-1:
                Delta_log_tau = log(tau_vec[n]/tau_vec[n-1])
            else:
                Delta_log_tau = log(tau_vec[n+1]/tau_vec[n-1])
            
            out_A_im[m,n] = -0.5*(omega_vec[m]*tau_vec[n])/(1+(omega_vec[m]*tau_vec[n])**2)*Delta_log_tau
            
    return out_A_im

def compute_L2(log_tau_norm):
    
    N_tau = log_tau_norm.size
    out_L2 = np.zeros((N_tau-2, N_tau))
    
    for n in range(0, N_tau-2):

        delta_loc = log_tau_norm[n+1]-log_tau_norm[n]
        
        out_L2[n,n] = 1./(delta_loc**2)
        out_L2[n,n+1] = -2./(delta_loc**2)
        out_L2[n,n+2] = 1./(delta_loc**2)

    return out_L2

def compute_L1(log_tau_norm):
    
    N_tau = log_tau_norm.size
    out_L1 = np.zeros((N_tau-1, N_tau))
    
    for n in range(0, N_tau-1):

        delta_loc = log_tau_norm[n+1]-log_tau_norm[n]
        
        out_L1[n,n] = 1./delta_loc
        out_L1[n,n+1] = -1./delta_loc

    return out_L1

def compute_L_aristo(log_tau_norm):
    
    N_tau = log_tau_norm.size
    out_L_aristo = np.zeros((2, N_tau))
    
    out_L_aristo[0,0] = 1.0
    out_L_aristo[1,N_tau-1] = 1.0

    return out_L_aristo

def count_parameters(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)
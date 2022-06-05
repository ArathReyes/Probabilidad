# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 00:25:56 2022

@author: Arath Reyes
"""

import pandas as pd
import numpy as np
from scipy.stats import norm
import seaborn as sns
import matplotlib.pyplot as plt

def StockMonteCarlo(days, Y0, target, sigma = 1):
    normal = norm.rvs(0,sigma,size = days)
    price = Y0 + normal.cumsum()
    price = [Y0] + list(price) 
    df = pd.DataFrame({"Days":list(range(0,days+1)),\
                       "Price":price})
    aux = 1 if (price[-1] > target) else 0
    return df, aux

def MonteCarlo(days, Y0, target, nsim, sigma =1):
    c = np.zeros(nsim)
    
    sns.set_style("darkgrid")
    sns.set_palette("hls") # flare, hls
    plt.figure(figsize = (16,8))
    for i in range(nsim):
        df, c[i] = StockMonteCarlo(days, Y0, target, sigma)
        ax = sns.lineplot(x = "Days", y = "Price", data = df)
    plt.axhline(y = target, ls = '--',color = 'black',label = "Objetivo")
    ax.set_title("Stock Monte Carlo, Simulations: {0}, Sigma: {1}".format(nsim, sigma))
    plt.show()
    return c.mean()

days, Y0, target, sigma = 1000, 100, 105, 1
nsim = 500
 

df, aux = StockMonteCarlo(days, Y0, target, sigma)
proba = MonteCarlo(days, Y0, target, nsim, sigma)

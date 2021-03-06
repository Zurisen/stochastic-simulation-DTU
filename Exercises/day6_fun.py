#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 09:54:28 2021

@author: carlos
"""
import numpy as np
from numpy.random import *
import matplotlib.pyplot as plt
from scipy import stats
from random import sample

def mat1():
	M = np.array([[0,5,3,1,4,12],[2,0,22,11,13,30],[6,8,0,13,12,5],\
		   [33,9,5,0,60,17],[1,15,6,10,0,14],[24,6,8,9,40,0]])
	return M 

def mat2():
	M = np.array([
[   0  , 225 , 110 ,   8 , 257 ,  22 ,   83 , 231 ,  277  ,   243  ,    94  ,     30  ,     4 ,  265 ,   274 ,   250 ,    87 ,  83  ,   271 ,      86],
[ 255  ,   0 , 265 , 248 , 103 , 280 ,  236 ,  91 ,    3  ,    87  ,   274  ,    265  ,   236 ,    8 ,    24 ,    95 ,   247 , 259  ,    28 ,     259       ],
[  87  , 236 ,   0 ,  95 , 248 , 110 ,   25 , 274 ,  250  ,   271  ,     9  ,    244  ,    83 ,  250 ,   248 ,   280 ,    29 ,  26  ,   239 ,       7      ],
[   8  , 280 ,  83 ,   0 , 236 ,  28 ,   91 , 239 ,  280  ,   259  ,   103  ,     23  ,     6 ,  280 ,   244 ,   259 ,    95 ,  87  ,   230 ,      84      ],
[ 268  ,  87 , 239 , 271 ,   0 , 244 ,  275 ,   9 ,   84  ,    25  ,   244  ,    239  ,   275 ,   83 ,   110 ,    24 ,   274 , 280  ,    84 ,     274      ],
[  21  , 265 ,  99 ,  29 , 259 ,   0 ,   99 , 230 ,  265  ,   271  ,    87  ,      5  ,    22 ,  239 ,   236 ,   250 ,    87 ,  95  ,   271 ,      91      ],
[  95  , 236 ,  28 ,  91 , 247 ,  93 ,    0 , 247 ,  259  ,   244  ,    27  ,     91  ,    87 ,  268 ,   275 ,   280 ,     7 ,   8  ,   240 ,      27      ],
[ 280  ,  83 , 250 , 261 ,   4 , 239 ,  230 ,   0 ,  103  ,    24  ,   239  ,    261  ,   271 ,   95 ,    87 ,    21 ,   274 , 255  ,   110 ,     280      ],
[ 247  ,   9 , 280 , 274 ,  84 , 255 ,  259 ,  99 ,    0  ,    87  ,   255  ,    274  ,   280 ,    3 ,    27 ,    83 ,   259 , 244  ,    28 ,     274       ],
[ 230  , 103 , 268 , 275 ,  23 , 244 ,  264 ,  28 ,   83  ,     0  ,   268  ,    275  ,   261 ,   91 ,    95 ,     8 ,   277 , 261  ,    84 ,     247      ],
[  87  , 239 ,   9 , 103 , 261 , 110 ,   29 , 255 ,  239  ,   261  ,     0  ,    259  ,    84 ,  239 ,   261 ,   242 ,    24 ,  25  ,   242 ,       5      ],
[  30  , 255 ,  95 ,  30 , 247 ,   4 ,   87 , 274 ,  242  ,   255  ,    99  ,      0  ,    24 ,  280 ,   274 ,   259 ,    91 ,  83  ,   247 ,      91      ],
[   8  , 261 ,  83 ,   6 , 255 ,  29 ,  103 , 261 ,  247  ,   242  ,   110  ,     29  ,     0 ,  261 ,   244 ,   230 ,    87 ,  84  ,   280 ,     100],
[ 242  ,   8 , 259 , 280 ,  99 , 242 ,  244 ,  99 ,    3  ,    84  ,   280  ,    236  ,   259 ,    0 ,    27 ,    95 ,   274 , 261  ,    24 ,     268       ],
[ 274  ,  22 , 250 , 236 ,  83 , 261 ,  247 , 103 ,   22  ,    91  ,   250  ,    236  ,   261 ,   25 ,     0 ,   103 ,   255 , 261  ,     5 ,     247       ],
[ 244  ,  91 , 261 , 255 ,  28 , 236 ,  261 ,  29 ,  103  ,     9  ,   242  ,    261  ,   244 ,   87 ,   110 ,     0 ,   242 , 236  ,    95 ,     259      ],
[  84  , 236 ,  27 ,  99 , 230 ,  83 ,    7 , 259 ,  230  ,   230  ,    22  ,     87  ,    93 ,  250 ,   255 ,   247 ,     0 ,   9  ,   259 ,      24      ],
[  91  , 242 ,  28 ,  87 , 250 , 110 ,    6 , 271 ,  271  ,   255  ,    27  ,    103  ,    84 ,  250 ,   271 ,   244 ,     5 ,   0  ,   271 ,      29      ],
[ 261  ,  24 , 250 , 271 ,  84 , 255 ,  261 ,  87 ,   28  ,   110  ,   250  ,    248  ,   248 ,   22 ,     3 ,   103 ,   271 , 248  ,     0 ,     236       ],
[ 103  , 271 ,   8 ,  91 , 255 ,  91 ,   21 , 271 ,  236  ,   271  ,     7  ,    250  ,    83 ,  247 ,   250 ,   271 ,    22 ,  27  ,   248 ,       0      ]])
	return M


def min_cost_overall(M_cost, a, b, n_iters=10000):
	Mlen = M_cost.shape[1]
	indexes = np.arange(Mlen)
	best_total_cost = 100000
	best_total_cost_array = np.array([])
	k = 0
	T = np.zeros(n_iters)
		
	for iters in range(n_iters):
		T[iters] = 1/np.sqrt(1+k)
		total_cost = 0
		ignore = np.array([a,b])
		possible = np.delete(indexes,ignore)
		n = sample(range(1, len(possible)),1)
		random_steps = np.array(sample(possible.tolist(),n[0]))
		route = np.append(np.append(a,random_steps),b)
		
		for i in range(len(route)-1):
			foo = route[i]
			oof = route[i+1]
			total_cost += M_cost[foo,oof]
			
		u = np.random.normal(0,1)

		if total_cost < best_total_cost:
			best_total_cost = total_cost
			best_total_cost_array = np.append(best_total_cost_array, best_total_cost)
			best_route = route
			
		elif np.exp((-total_cost+best_total_cost)/T[iters])<u:
			best_total_cost = total_cost
			best_total_cost_array = np.append(best_total_cost_array, best_total_cost)
			best_route = route
			
		else:
			best_total_cost_array = np.append(best_total_cost_array, best_total_cost)
		k += 0.1
		
	return best_total_cost_array, best_route, T
			
		
def ex13(a,b,X, n_bootstraps = 500, len_bootstraps= 100):
	Xmean = np.mean(X)
	Xvar = np.var(X)

	boot = np.zeros((n_bootstraps,len_bootstraps))
	boot_value = np.zeros(n_bootstraps)
	for i in range(n_bootstraps):
		boot[i] = choice(X,len_bootstraps, replace=True)
		boot_value[i] = Xmean- np.mean(boot[i])
	
	boot_means = np.mean(boot,axis=1)
	boot_vars = np.var(boot,axis=1)
	
	
	P = 1-np.sum(boot_value>b)+np.sum(boot_value<a)
	
	return P, boot_value, Xmean, Xvar, boot_means, boot_vars
	
def pareto_boot(len_bootstraps=500, n_bootstraps=1000,N= 200,beta=1, k=1.05):
	
	distr = beta*pareto(1.05, size=N)
	boot = np.zeros((n_bootstraps,len_bootstraps))	
	for i in range(n_bootstraps):
		boot[i] = choice(distr, len_bootstraps, replace=True)
	boot_means = np.mean(boot, axis=1)
	boot_vars = np.var(boot, axis=1)
	boot_medians = np.median(boot, axis=1)
	
	return boot_means, boot_vars, boot_medians

def vector_boot(boot_means,len_bootstraps=500, n_bootstraps=1000):
	
	boot = np.zeros((n_bootstraps,len_bootstraps))	
	for i in range(n_bootstraps):
		boot[i] = choice(boot_means, len_bootstraps, replace=True)
	boot_means = np.mean(boot, axis=1)
	boot_vars = np.var(boot, axis=1)
	boot_medians = np.median(boot, axis=1)
	
	return boot_means, boot_vars, boot_medians
		

	
	
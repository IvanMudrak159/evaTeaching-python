# use and edit this file to make all the plots you need - it is generally easier
# than plotting directly after the run of the algorithm

import utils

import matplotlib.pyplot as plt 

plt.figure(figsize=(12,8))
utils.plot_experiments('tsp', ['default', 
                               'direct_insertion_crossover', 'direct_insertion_crossover + inversion_mutation', 
                               'direct_insertion_crossover + inversion_mutation (gen_2500)', 'direct_insertion_crossover + inversion_mutation (gen_2500) (MUT_PROB=0.33)',
                               'distance_based_crossover', 'distance_based_crossover + inversion_mutation', 'distance_based_crossover + inversion_mutation (gen=2500)'])
plt.show()
 
#  'order_1_crossover', 'cycle_crossover', 'pmx_crossover', 
                            #    'order_multiple_crossover', 'direct_insertion_crossover', 'direct_insertion_crossover + inversion_mutation',
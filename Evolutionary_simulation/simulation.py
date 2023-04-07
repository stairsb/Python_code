#! /local/cluster/bin/python3

from sim_module import Population
 
# genomes.txt has 100 individuals with 100bp genomes
pop: Population = Population("genomes.txt")

i: int
for i in range(0, 100):
   pop.grow(10, 0.1)  # grow by 10 individuals, 10% mutation rate
   pop.cull_to_size(100) # cull back down to 100
   # print the generation number, and mean fitness
   print(str(i) + "\t" + str(pop.mean_fitness()))


 

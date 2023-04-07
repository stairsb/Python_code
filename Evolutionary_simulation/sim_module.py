#! /local/cluster/bin/python3

from typing import List,IO
import random
import io


class Bug:
	
	def __init__(self, id: int, genome: List[str]) -> None:
		self.ids = id
		self.genome = genome

	def get_id(self) -> int:
		return self.ids

	def base_composition(self, base: str) -> int:
		occurances = 0
		for contents in self.genome:
			if base == contents:
				occurances += 1
		
		return occurances

	def fitness(self) -> int:
		score = 0
		for cont in self.genome:
			if cont == 'C' or cont == 'G':
				score += 2
			elif cont == 'T':
				score += 3
		return score

	def reproduce(self, mutation_prob: float) -> 'Bug':
		assert mutation_prob >= 0 and mutation_prob <= 1, "Bug reproduce error: mutation_prob not between 0 and 1"
		new_genome: List[str] = []		
		for base in self.genome:
			if random.uniform(0,1) < mutation_prob:
				bases: List[str] = ["A", "C", "G", "T"]
				new_genome.append(bases)
			else:
				new_genome.append(base)

		new_id: int = random.randint(0, 1000000)
		offspring: Bug = Bug(new_id, new_genome)
		return offspring


def bug_fitness(b: Bug) -> float:
	return b.fitness()


class Population:
	
	def __init__(self, file_name: str) -> None:
		self.bugs: List[Bug] = []
		self.file_name = file_name
		
		fhandle: IO = io.open(file_name, "r")
		
		for line in fhandle:
			line_contents = line.split()
			pop_ids: int = line_contents[0]
			pop_genome = line_contents[1]
			bug_object: Bug = Bug(pop_ids, pop_genome)
			self.bugs.append(bug_object)
		fhandle.close()		

	def get_size(self) -> int:	
		return len(self.bugs)


	def mean_fitness(self) -> float:
		total_elements = 0
		for j in self.bugs:
			total_elements += j.fitness()
			
		mean = total_elements/self.get_size()

		return mean

	def grow(self, n: int, mutation_prob: float) -> None:
		for l in range(0, n):
			new_bug: Bug = Bug.reproduce(random.choice(self.bugs), mutation_prob)
			self.bugs.append(new_bug)

	def cull_to_size(self, n: int) -> None:
		self.bugs.sort(key = bug_fitness)
		self.bugs.reverse()
		self.bugs = self.bugs[0:n]
		assert n <= len(self.bugs), "Error the size is getting increase instead of reduced"
		




	

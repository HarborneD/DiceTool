import sys
from collections import OrderedDict
import numpy as np


def GetDiceProbabilityDistribution(num_dice,dice_size):
	total_distribution = GetDiceTotalsDistribution(num_dice,dice_size)

	return GetProbabilityDistributionFromTotals(total_distribution)


def GetDice(dice_size, start_value = 1,step_size = 1):
	return list(range(start_value,dice_size+1,step_size))	

def GetDiceTotalsDistribution(num_dice,dice_size):
	dice = np.array(GetDice(dice_size))
	
	probability_space = dice
	addition_matrix = dice
	
	for dice_count in range(1,num_dice):
		sizing_list = [dice_size] + [1] * len(probability_space.shape)

		probability_space = np.tile(probability_space, tuple(sizing_list))
		
		addition_matrix = [ [dice_num] * dice_size for dice_num in addition_matrix]
		
		probability_space = np.add(addition_matrix,probability_space)
		
	return probability_space

def GetProbabilityDistributionFromTotals(total_distribution):
	num_counts = total_distribution.size

	counts = np.bincount(np.reshape(total_distribution,num_counts))
	
	distribution = OrderedDict()

	possible_values_started = False
	for total_index in range(0,len(counts)):
		count = counts[total_index]
		if(possible_values_started or count != 0):
			distribution[total_index] = count/num_counts

	return distribution

if __name__ == '__main__':
	
	num_dice = 3
	if(len(sys.argv) > 1):
		num_dice = sys.argv[1]

	dice_size = 6
	if(len(sys.argv) > 1):
		dice_size = sys.argv[2]
	
	print("Probability Distribution for "+ str(num_dice) + " x " + str(dice_size) + "-sided dice:" )
	print("")
	distribution = GetDiceProbabilityDistribution(num_dice,dice_size)

	scale_number = 20
	ratio = 1/len(distribution)
	graph_ratio = ratio/scale_number
	for distribution_point in distribution:
		print(str(distribution_point) +": "+ str(distribution[distribution_point]))
		
	for distribution_point in distribution:
		graph_num = distribution[distribution_point] // graph_ratio
		
		print(str(distribution_point) +": "+ str(" " * max(0, 3 - len(str(distribution_point)))) +str("=" * int(graph_num)))
		
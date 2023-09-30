import numpy as np
import os
import sys
import os.path as path

try:
	from .config import get_config
except:
	from config import get_config


def generate_support_file(dataset, domain, seed, support_num):
	
	np.random.seed(seed)
	num_classes = get_config(domain)
	num_classes = num_classes['num_classes']

	train_file = dataset.lower() + '_' + domain.lower() + '_train.txt'
	train_file = path.join(os.getcwd(), dataset, 'raw', 'list_cvt', train_file)
	support_file = dataset.lower() + '_' + domain.lower() + '_train_support' + str(support_num) + '_' + str(seed) + '.txt'
	support_file = path.join(os.getcwd(), dataset, 'raw', 'list_cvt', support_file)

	train_data = []
	train_data_classes = []
	file = open(train_file, 'r')
	for line in file:
		train_data.append(line)	
		video_class = line.split()[1]
		train_data_classes.append(video_class)	
	file.close()
	train_videos = len(train_data)

	support_idx = []
	for i in range(num_classes):
		idx_i = [j for j in range(train_videos) if int(train_data_classes[j]) == i]
		support_idx += list(np.random.choice(idx_i, support_num, replace=False))
	ksupport = [train_data[i] for i in support_idx]

	with open(support_file, 'w') as new_file:
		for line in ksupport:
			new_file.write(line)
	new_file.close()

	print("Write {} success".format(support_file))
	return 0


if __name__ == "__main__":

	dataset_domain = [('HMDB51', 'Daily'), ('ARID', 'Daily'), ('MIT', 'Daily'), ('Kinetics', 'Daily'), ('UCF101', 'Sports'), ('Sports1M', 'Sports'), ('Kinetics', 'Sports')]
	seed_config_range = 5
	support_nums = [3,5]

	for (dataset, domain) in dataset_domain:
		print("Processing dataset {} in domain {}.".format(dataset, domain))
		for seed in range(seed_config_range):
			print("Using seed number: {}.".format(seed))
			for support_num in support_nums:
				support_num = int(support_num)
				print("Support number is now {}.".format(support_num))
				generate_support_file(dataset, domain, seed, support_num)
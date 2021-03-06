import pydbgen
import random
import string
import pandas as pd
import numpy as np
import random
from pydbgen import pydbgen
from collections import defaultdict

"""
Just specify the number of rows that you want for the synthetic dataset at the bottom.
Running this script will provide with 2 synthetic datasets.
The second dataset contains typos with certain edit distances of the entries from the first dataset.
"""

def create_first_df(num_rows):
	myDB = pydbgen.pydb()
	df1 = myDB.gen_dataframe(num_rows,['name', 'age'])

	for index, row in df1.iterrows():
		# row['age'] = np.random.randint(10)
		row['age'] = np.random.zipf(2)

	# Change some age values to negative values
	for index, row in df1.iterrows():
		if index / 2 == 0:
			row['age'] == 0 - row['age']

	return df1

def create_second_df(num_rows):
	# Create 2nd dataframe
	cols = ['name', 'age']
	lst = []
	for a in range(num_rows):
	    lst.append([np.random.randint(10), np.random.randint(10)])
	df2 = pd.DataFrame(lst, columns=cols)

	return df2


def add_typo(df1, num_dup):
	# Keep a list of names to create names with typos in the next step
	name_list = []

	for index, row in df1.iterrows():
		name_list.append(row['name'])

	# Adjust typo degrees: 1,2,3
	name_typo_list = []
	perfect_mapping = defaultdict(list)
	for i in range(0,len(name_list)):
		for k in range(num_dup):
			j = None
			if i==0:
				j = name_list[i] + random.choice(string.ascii_letters)
				name_typo_list.append(j)
				perfect_mapping[name_list[i]].append(j)				
			elif i/5 == 0:
				j = name_list[i] + random.choice(string.ascii_letters)
				name_typo_list.append(j)
				perfect_mapping[name_list[i]].append(j)
			elif i/3 == 0:
				j = name_list[i] + random.choice(string.ascii_letters) + random.choice(string.ascii_letters)
				name_typo_list.append(j)
				perfect_mapping[name_list[i]].append(j)
			else:
				j = name_list[i] + random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + random.choice(string.ascii_letters)
				name_typo_list.append(j)
				perfect_mapping[name_list[i]].append(j)
	# Insert typo name to df2
	cols = ['name', 'age']
	lst = []
	for typo_index in range(0,len(name_typo_list)):
		lst.append([name_typo_list[typo_index], np.random.zipf(2)])
	df2 = pd.DataFrame(lst, columns=cols)
	return df2, perfect_mapping

def create_skewed_typos(df1, num_dup):
	# Keep a list of names to create names with typos in the next step
	name_list = []

	for index, row in df1.iterrows():
		name_list.append(row['name'])

	# Adjust typo degrees: 1,2,3
	name_typo_list = []
	perfect_mapping = defaultdict(list)
	for i in range(0,len(name_list)):
		for k in range(random.randint(1, num_dup)):
			j = None
			if i==0:
				j = name_list[i] + random.choice(string.ascii_letters)
				name_typo_list.append(j)
				perfect_mapping[name_list[i]].append(j)				
			elif i/5 == 0:
				j = name_list[i] + random.choice(string.ascii_letters)
				name_typo_list.append(j)
				perfect_mapping[name_list[i]].append(j)
			elif i/3 == 0:
				j = name_list[i] + random.choice(string.ascii_letters) + random.choice(string.ascii_letters)
				name_typo_list.append(j)
				perfect_mapping[name_list[i]].append(j)
			else:
				j = name_list[i] + random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + random.choice(string.ascii_letters)
				name_typo_list.append(j)
				perfect_mapping[name_list[i]].append(j)
	# Insert typo name to df2
	cols = ['name', 'age']
	lst = []
	for typo_index in range(0,len(name_typo_list)):
		lst.append([name_typo_list[typo_index], np.random.randint(10)])
	df2 = pd.DataFrame(lst, columns=cols)
	return df2, perfect_mapping

def create_skewed_ages(df):

	prob=np.random.binomial(100, 0.8, len(df.index))
	i=0
	for index, row in df.iterrows():
		# row['age'] = prob[i]
		df.at[index,'age'] = prob[i]
		i += 1
	return df
'''
Uncomment the lines below to create synthtetic datasets as a part of the script
'''
# data1 = create_first_df(10)
# data2_nontypo = create_second_df(10)
# data2 = add_typo(data1, data2_nontypo)

# print(data1)
# print(data2)
# data1.to_csv (r's_data1.csv', index = False, header=True)
# data2.to_csv (r's_data2.csv', index = False, header=True)
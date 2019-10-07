import numpy as np
import json

def readInput():
    """Reads the patient txt file as a huge data input file and calls all the
	functions required to complete the program

	The function does not have any inputs or outputs. It reads the input from
	the text file and runs all the required functions to complete the program

    Args:
		None
    Returns:
		None
    """

	data = open("patient.txt","r").readlines()
	(f_names, l_names) = readName(data)
	ages = readAges(data)
	sex = readSex(data)
	tsh_read = readTSH(data)
	(tsh_sorted, diagnosis) = diagnose(tsh_read)
	output(f_names, l_names, ages, sex, tsh_sorted, diagnosis)


def readName(data):
    """Extracts the patient names from the data file and and returns the first
	and last names as string lists.

	The function does not have any inputs or outputs. It reads the input from
	the text file and runs all the required functions to complete the program

    Args:
		data (String list): the entire text file where each line of the text
							file is saved as a separate element in the list
    Returns:
		f_names (String list): List of first names in order of appearance
		l_names (String list): List of last names in order of appearance
    """
	size = int((len(data) - 1)/4)
	counter = 0
	f_names = []
	l_names = []

	while counter < size:
		full_name = data[4*counter].split(" ")
		f_names.append(full_name[0])
		l_names.append(full_name[1].rstrip())
		counter += 1

	return f_names, l_names

def readAges(data):
	size = int((len(data) -  1)/4)
	counter = 0
	ages = []

	while counter < size:
		ages.append(int(data[4*counter + 1].strip()))
		counter += 1

	return ages

def readSex(data):
	size = int((len(data) -  1)/4)
	counter = 0
	sex = []

	while counter < size:
		sex.append(data[4*counter + 2].strip())
		counter += 1

	return sex

def readTSH(data):
	size = int((len(data) -  1)/4)
	counter = 0
	tsh = []

	while counter < size:
		tsh.append(data[4*counter + 3])
		counter += 1

	for x in range(len(tsh)):
		temp = tsh[x].split(",")
		temp.pop(0)
		for y in range(len(temp)):
			temp[y] = float(temp[y])
		tsh[x] = temp

	return tsh

def diagnose(tsh_read):
	diagnosis = []
	for x in range(len(tsh_read)):
		tsh_read[x].sort()
		temp = tsh_read[x]
		d = []
		for y in range(len(temp)):
			if temp[y] < 1:
				d.append("high")
				break
			elif temp[y] > 4:
				d.append("low")
				break
			else:
				d.append("norm")
			y += 1

		if "high" in d:
			diagnosis.append("hyperthyroidism")
		elif "low" in d:
			diagnosis.append("hypothyroidism")
		else:
			diagnosis.append("normal thyroid function")
		x += 1

	return tsh_read, diagnosis

def output(f_names, l_names, ages, sex, tsh_sorted, diagnosis):

	for x in range(len(f_names)):
		patient = {"First Name": f_names[x],
					"Last Name": l_names[x],
					"Age": ages[x],
					"Gender": sex[x],
					"Diagnosis": diagnosis[x],
					"TSH": tsh_sorted[x]
					}
		filename = f_names[x] + '-' + l_names[x] + '.json'
		out_file = open(filename,"w")
		json.dump(patient, out_file)
		out_file.close()

if __name__ == "__main__":
	readInput()

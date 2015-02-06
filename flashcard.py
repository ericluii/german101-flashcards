#!/usr/bin/python
import sys, csv, random, os

# reads from the path, returns list of words
def csv_reader(path, file_name, mode):
	words = []
	if len(path.split('.')) > 1:	
		write_to_array(words, open(path, 'rb'), mode)
	else:
		read_files_to_array(words, path, file_name, mode)
	return words

# recursive function that reads all items in directory
# writes words to word array
def read_files_to_array(words, path, file_name, mode):
	items = os.listdir(path)
	for item in items:
		if len(item.split('.')) > 1:			
			if len(file_name) == 0:
				write_to_array(words, open(path + '/'+item, 'rb'), mode)	
			if (len(file_name) > 0 and item.find(file_name)!= -1):
				print path+'/'+item
				write_to_array(words, open(path + '/'+item, 'rb'), mode)	
		else:
			read_files_to_array(words, path + '/' + item, file_name, mode)

# writes from csv file to word array
def write_to_array(words, file, mode):
	reader = csv.reader(file)
	for row in reader:
		if 'S' in mode:
			words.append({
				'spanish' : row[0],
				'english' : row[1]
			})
		elif 'G' in mode:
			words.append({
				'german' : row[0],
				'english' : row[1]
			})

def main():
	if len(sys.argv) < 4:
		print 'Requires a csv file, flash mode and file name, leaving now...'
		print 'if you want all, put \'\' as last arg'
		exit(1)
	path = sys.argv[1]
	mode = sys.argv[2]		
	file_name = sys.argv[3]		
	if file_name == "''":
		file_name = ''

	if 'S' in mode:
		words = csv_reader(path + '/spanish', file_name, mode)
	elif 'G' in mode:
		words = csv_reader(path + '/german', file_name, mode)

	if len(words) == 0:
		print 'No words found.'
		exit(1)

	answer = 'first'
	i = 0
	modeSet = []
	if mode == 'SE':
		modeSet.append('spanish')
		modeSet.append('english')
	elif mode == 'ES':
		modeSet.append('english')
		modeSet.append('spanish')
	elif mode == 'GE':
		modeSet.append('german')
		modeSet.append('english')
	elif mode == 'EG':
		modeSet.append('english')
		modeSet.append('german')
	else:
		print 'Mode is incorrect :( Please rerun with either ES, SE, EG, or GE'
		exit(1)
	while True:
		if answer != '':
			i =  random.randint(0,len(words)-1)

		print '=================='
		print 'translate: ' + words[i][modeSet[0]]
		answer = raw_input()
		print words[i][modeSet[1]]
		print '\n'


if __name__ == "__main__":
	main()

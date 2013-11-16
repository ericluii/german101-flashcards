import sys, csv, random, os

# reads from the path, returns list of words
def csv_reader(path):
	words = []
	if len(path.split('.')) > 1:	
		write_to_array(words, open(path, 'rb'))
	else:
		read_files_to_array(words, path)
	return words

# recursive function that reads all items in directory
# writes words to word array
def read_files_to_array(words, path):
	items = os.listdir(path)
	for item in items:
		if len(item.split('.')) > 1:
			write_to_array(words, open(path + '/'+item, 'rb'))	
		else:
			read_files_to_array(words, path + '/' + item)

# writes from csv file to word array
def write_to_array(words, file):
	reader = csv.reader(file)
	for row in reader:
		words.append({
			'spanish' : row[0],
			'english' : row[1]
		})

def main():
	if len(sys.argv) < 3:
		print 'Requires a csv file and flash mode, leaving now...'
		exit(1)
	path = sys.argv[1]
	mode = sys.argv[2]
	words = csv_reader(path)
		

	answer = 'first'
	i = 0
	modeSet = []
	if mode == 'SE':
		modeSet.append('spanish')
		modeSet.append('english')
	elif mode== 'ES':
		modeSet.append('english')
		modeSet.append('spanish')
	else:
		print 'Mode is incorrect :( Please rerun with either ES or SE'
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

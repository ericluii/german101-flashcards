import sys, csv, random, os


def main():
	answer = 'start'
	while True:
		if answer != '':
			i =  random.randint(0,1000)

		print '=================='
		print 'translate: ' + str(i)
		answer = raw_input()		
		print '\n'


if __name__ == "__main__":
	main()
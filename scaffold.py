#Ambika Patel
#apate339@charlotte.edu
#801495232


#!/usr/bin/env python3

import sys
import os



#create a python template script
python_template= """#!/usr/bin/env python3

import sys

def main():
    sys.stdout.write("Standard Output")  
    sys.stderr.write("Standard Error")


if __name__ == "__main__":
    main()
"""


def main():
	#Ask user for the name of the output file
	outpt= input("Enter the name of the output file: " )

	#confirm user input is not empty
	if outpt == "" or outpt == " ":
		sys.stderr.write("Error: Ouput filename cannot be empty or a blank space.\n")
		sys.exit(1)

	#check if the file already exists
	if os.path.exists(outpt):
		#if the file exists, ask the user if it can be overwritten (y/n). If the user does not enter y or n, then prompt again. 
		sys.stderr.write("File already exists. Can this be overwritten? [Y/N] \n")
		while True:
			response=sys.stdin.readline().strip().lower()

			if response in ("y","n"):
				#if user says n, then prompt with Aborted
				if response == 'n':
					sys.stderr.write("Aborted. File not overwritten. \n")
				#if the user says y, then overwrite file
				elif response == 'y':
					with open(outpt,"w") as fh:
						fh.write(python_template.format(filename=outpt))
						sys.stdout.write(f"Scaffold overwritten: {outpt}\n")
				break
			else:
				sys.stderr.write("Invalid input. Please enter 'Y' or 'N'. \n")
	#if the file does not exist, output the file to the specified name
	else:
		with open(outpt, "w") as FH:
			FH.write(python_template.format(filename=outpt))
		sys.stdout.write(f"Scaffold created: {outpt}\n")


if __name__ == '__main__':
	main()



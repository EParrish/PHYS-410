import csv

def GrabData():
	Coordinates=[]

	with open("walmart.csv", "r") as csvfile:
		thisreader = csv.reader(csvfile, delimiter=',')

		for row in thisreader:

			latitude = float(row[0])
			longitude = float(row[1])

			Coordinates.append((latitude,longitude))

	return Coordinates

def PartA():
	length_of_data = len(full_data)
	print length_of_data
	return

def PartB():
	

if __name__ == "__main__":
	full_data = GrabData()
	PartA()
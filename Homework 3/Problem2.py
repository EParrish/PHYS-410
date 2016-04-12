from __future__ import division
import csv

####################################################################
########################### Stars ##################################
####################################################################
stars_pixel_values = []
saturation_value = 65535

with open("stars.csv", "r") as csvfile:
	thisreader = csv.reader(csvfile, delimiter=',')

	for row in thisreader:
		x_pos = int(row[0])
		y_pos = int(row[1])
		z_value = int(row[2])

		stars_pixel_values.append(z_value)

stars_unique_pixel_values = set(stars_pixel_values)
mean = sum(stars_pixel_values)/len(stars_pixel_values)
mode = max(stars_unique_pixel_values, key=stars_pixel_values.count)

# print pixel_values
print "Stars Values"
print "\tStars Min: %s" %min(stars_pixel_values)
print "\tStars Max: %s" %max(stars_pixel_values)
print "\tNumber of Saturated Pixels: %s" %(stars_pixel_values.count(saturation_value))
print "\tNumber of Unique Values: %s" %len(stars_unique_pixel_values)
print "\tMean: %s Mode: %s" %(mean, mode)


####################################################################
########################### Galaxy #################################
####################################################################
galaxy_pixel_values = []
saturation_value = 65535

with open("galaxy.csv", "r") as csvfile:
	thisreader = csv.reader(csvfile, delimiter=',')

	for row in thisreader:
		x_pos = int(row[0])
		y_pos = int(row[1])
		z_value = int(row[2])

		galaxy_pixel_values.append(z_value)

galaxy_unique_pixel_values = set(galaxy_pixel_values)
mean = sum(galaxy_pixel_values)/len(galaxy_pixel_values)
mode = max(galaxy_unique_pixel_values, key=galaxy_pixel_values.count)

# print pixel_values
print "Galaxy Values"
print "\tGalaxy Min: %s" %min(galaxy_pixel_values)
print "\tGalaxy Max: %s" %max(galaxy_pixel_values)
print "\tNumber of Saturated Pixels: %s" %(galaxy_pixel_values.count(saturation_value))
print "\tNumber of Unique Values: %s" %(len(galaxy_unique_pixel_values))
print "\tMean: %s Mode: %s" %(mean, mode)
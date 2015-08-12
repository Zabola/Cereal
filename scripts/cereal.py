#!/usr/bin/env python
import csv
import os
import sys

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

import django
django.setup()

from main.models import  Manufacturer, Cereal, Nutritional_Information

Manufacturer.objects.all().delete()
Cereal.objects.all().delete()
# Nutritional_Information.objects.all().delete()

csv_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cereal.csv')

csv_file = open(csv_file_path, 'r')

reader = csv.DictReader(csv_file)

# Cereal Name,Manufacturer,Type,Calories,Protein (g),Fat,Sodium,
# Dietary Fiber,Carbs,Sugars,Display Shelf,Potassium,Vitamins and Minerals,
# Serving Size Weight,Cups per Serving

for row in reader:
	print row
	print row ['Cereal Name']
	print row ['Manufacturer']
	manu_obj, created = Manufacturer.objects.get_or_create(name=row['Manufacturer'])
	print row ['Type']
	print row ['Calories']
	print row ['Protein (g)']
	print row ['Fat']
	print row ['Sodium']
	print row ['Dietary Fiber']
	print row ['Carbs']
	print row ['Sugars']
	print row ['Display Shelf']
	print row ['Potassium']
	print row ['Vitamins and Minerals']
	print row ['Serving Size Weight']
	print row ['Cups per Serving']




	new_cereal, created = Cereal.objects.get_or_create(name=row ['Cereal Name'])

	
	new_cereal.manufacturer = manu_obj
	new_cereal.type = row['Type']
	
	new_cereal.display_shelf = row['Display Shelf']
	
	

	new_cereal.save()

	new_nut, created = Nutritional_Information.objects.get_or_create(cereal=new_cereal)
	new_nut.calories = row['Calories']
	new_nut.protein_in_g = row['Protein (g)']
	new_nut.fat = row['Fat']
	new_nut.sodium = row['Sodium']
	new_nut.dietary_fiber = row['Dietary Fiber']
	new_nut.carbs = row['Carbs']
	new_nut.sugars = row['Sugars']
	new_nut.vitamins_and_minerals = row['Vitamins and Minerals']
	new_nut.serving_size_weight = row['Serving Size Weight']
	new_nut.cups_per_serving = row['Cups per Serving']
	new_nut.potassium = row['Potassium']

	new_nut.save()

csv_file.close()






	# print row ['Cereal Name'].replace('_', ' ')
	# print row ['Manufacturer']

	# manu_obj, created = Manufacturer.objects.get_or_create(name=row['Manufacturer'])

	# print manu_obj.name
	# print created


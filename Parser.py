# coding=utf-8
import sys
import csv

food_kinds = {}
food_transform = {}

food_kinds['Asian'] = [
    'Afghan', 'Asian', 'Bangladeshi', 'Chinese', 'Chinese/Cuban', 'Chinese/Japanese',
    'Filipino', 'Indian', 'Indonesian', 'Iranian', 'Japanese', 'Jewish/Kosher', 'Korean',
    'Middle Eastern', 'Pakistani', 'Thai', 'Turkish', 'Vietnamese/Cambodian/Malaysia'
]
food_kinds['European'] = [
    'Australian', 'Bagels/Pretzeis', 'Czech', 'Eastern European', 'English', 'French',
    'German', 'Greek', 'Irish', 'Italian', 'Mediterranean', 'Pizza', 'Pizza/Italian', 'Polish',
    'Portuguese', 'Russian', 'Scandinavian', 'Spanish', 'Tapas', 'Bagels/Pretzels'
]
food_kinds['NorthAmerican'] = [
    'American', 'Barbecue', 'Cajun', 'Californian', 'Caribbean', 'Chicken', 'Creole', 'Creole/Cajun',
    'Hamburgers', 'Hawaiian', 'Hotdogs', 'Hotdogs/Pretzels', 'Mexican', 'Polynesian', 'Sandwiches',
    'Sandwiches/Salads/Mixed Buffet', 'Southwestern', 'Steak', 'Tex-Mex',
    'Latin (Cuban, Dominican, Puerto Rican, South & Central American)', 'American '
]
food_kinds['SouthAmerican'] = [
    'Brazilian', 'Chilean', 'Latin', 'Peruvian'
]
food_kinds['Africa'] = [
    'African', 'Armenian', 'Egyptian', 'Ethiopian', 'Moroccan'
]
food_kinds['Other'] = [
    'Bakery', 'Bottled beverages', 'Cafe/Coffee/Tea', 'Continental', 'Delicatessen', 'Donuts',
    'Fruit/Vegetables', 'Ice cream', 'Juice', 'Nuts/Confectionary', 'Pancakes/Waffles', 'Salads',
    'Seafood', 'Soul Food', 'Soups', 'Soups/Sandwiches', 'Vegetarian', 'Ice Cream, Gelato, Yogurt, Ices',
    'Caf_/Coffee/Tea', 'Caf/Coffee/Tea', 'Not Listed/Not Applicable', 'Other',
    'Bottled beverages, including water, sodas, juices, etc.', 'Juice, Smoothies, Fruit Salads',
    'Soups & Sandwiches', 'Fruits/Vegetables', 'Café/Coffee/Tea', 'CafÃ©/Coffee/Tea'
]

def change_date_to_season(date, suffix):
	i = date.find('/')
	if 6 > int(date[0:i]) > 2:
		return 'Spring' + suffix
	elif 9 > int(date[0:i]) >= 6:
		return 'Summer' + suffix
	elif 12 > int(date[0:i]) >= 9:
		return 'Fall' + suffix
	else:
		return 'Winter' + suffix

def to_restaurant_type(style):
	if not food_transform:
		for key in food_kinds.keys():
			for item in food_kinds[key]:
				food_transform[item] = key
	return food_transform[style]

def parse(data_path):
	data_set = []
	with open(data_path, 'rbU') as csvfile:
			reader = csv.reader(csvfile, delimiter=',')
			global fields
			fields = next(reader)
			#left only DBA, BORO, CUSINE DESCRIPTION, INSPECTION DATE, ACTION, VIOLATION CODE, VIOLATION DESCRIPTION, CRITICAL FLAG, SCORE, GRADE, GRADE DATE, RECORD DATE, INSPECTION TYPE
			for row in reader:
				

				# remove the rows that doesn't really provide information				
				del row[0]
				del row[2:6]
				del row[4]

				del row[-1]
				del row[10]

				# removed rows with missing data.
				if '' not in row:

					row[3] = change_date_to_season(row[3], "-INSPECTION DATE")
					# print row[8]
					row[9] = change_date_to_season(row[9], "-GRADE DATE")


					# everyone has the same season, FALL RECORD
					# row[10] = change_date_to_season(row[10], "-RECORD DATE")

					# origianl
					
					# row[11] = change_date_to_season(row[11], "-RECORD DATE")

					row[2] = to_restaurant_type(row[2])
					data_set.append(row)

	return data_set


		


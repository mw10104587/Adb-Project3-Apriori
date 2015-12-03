
1. Chi-An Wang, Hao-Hsiang Chung

2. -----*-- main.py
        *-- Apriori.py
        *-- Parser.py
        *-- INTEGRATED-DATASET.csv
        *-- README.txt
        *-- example-run.txt
        *-- output.txt (a file that would be rewritten after each execution)


3. 
  (A) INTEGRATED-DATESET.csv : The original dataset is "Boro Restaurant Grades" from NYC
  Open Data (https://data.cityofnewyork.us/Health/Boro-Restaurant-Grades/uvvk-ab5b).

  main.py : The entrance of our program. First we take the csv file as our input and parse the file with the class Parser. The output will be a list of row vectors from the original csv file.

  Parser.py : The parser for our raw csv file. What it does is 1. Remove any rows that has a missing value in it. 2. Transform any time information to season information so that it is easier to analyze and also makes more sense. 3. Remove all columns that are irrelevant to our association rule such as the phone number or the address. The output will be a list of row vectors from the original csv file. 4. Convert all restaurants to the food type category.


  (B) The mapping of our date to season : 
   Mar - May: Spring
   Jun - Aug: Summer
   Sep - Nov: Fall
   Dec - Feb: Winter

   The mapping of restaurants to restaurant types : 
   Asian : 
    'Afghan', 'Asian', 'Bangladeshi', 'Chinese', 'Chinese/Cuban', 'Chinese/Japanese',
    'Filipino', 'Indian', 'Indonesian', 'Iranian', 'Japanese', 'Jewish/Kosher', 'Korean',
    'Middle Eastern', 'Pakistani', 'Thai', 'Turkish', 'Vietnamese/Cambodian/Malaysia'
   European :
    'Australian', 'Bagels/Pretzeis', 'Czech', 'Eastern European', 'English', 'French',
    'German', 'Greek', 'Irish', 'Italian', 'Mediterranean', 'Pizza', 'Pizza/Italian','Polish', 
    'Portuguese', 'Russian', 'Scandinavian', 'Spanish', 'Tapas', 'Bagels/Pretzels'
   NorthAmerican :
    'American', 'Barbecue', 'Cajun', 'Californian', 'Caribbean', 'Chicken', 'Creole', 'Creole/Cajun',
    'Hamburgers', 'Hawaiian', 'Hotdogs', 'Hotdogs/Pretzels', 'Mexican', 'Polynesian', 'Sandwiches',
    'Sandwiches/Salads/Mixed Buffet', 'Southwestern', 'Steak', 'Tex-Mex',
    'Latin (Cuban, Dominican, Puerto Rican, South & Central American)', 'American '
   SouthAmerican : 
    'Brazilian', 'Chilean', 'Latin', 'Peruvian'
   Africa : 
    'African', 'Armenian', 'Egyptian', 'Ethiopian', 'Moroccan'
   Other : 
    'Bakery', 'Bottled beverages', 'Cafe/Coffee/Tea', 'Continental', 'Delicatessen', 'Donuts',
    'Fruit/Vegetables', 'Ice cream', 'Juice', 'Nuts/Confectionary', 'Pancakes/Waffles', 'Salads',
    'Seafood', 'Soul Food', 'Soups', 'Soups/Sandwiches', 'Vegetarian', 'Ice Cream, Gelato, Yogurt, Ices',
    'Caf_/Coffee/Tea', 'Caf/Coffee/Tea', 'Not Listed/Not Applicable', 'Other',
    'Bottled beverages, including water, sodas, juices, etc.', 'Juice, Smoothies, Fruit Salads',
    'Soups & Sandwiches', 'Fruits/Vegetables', 'Café/Coffee/Tea', 'CafÃ©/Coffee/Tea'


  D. Given the input of raw csv file, we parse it through the class Parser and get a list of processed vectors with each vector indicating a row in the csv file. 

4. python main.py <INTEGRATED-DATASET.csv> <min_supp> <min_conf>


5. There are two main functions in our Apriori algorithm, and we stick to the original version.

  A. Get Frequent Sets: 
    we init the first frequent set with items length = 1, which means it only has one term.
    Try to find larger itemsets that contains the frequent terms in the previous set.

    One of the important function get called in getFrequentSets is "generateCandidate", that sorts everything in lexicographic order which garuntees we don't count repetitive sets. We implement join step that generates all the possible candidate itemsets C_k of length k.
    Also we prune, and remove all the candidate in C_k that cannot be frequent.


  B. Get Associated Rules



6. python main.py INTEGRATED-DATASET.csv 0.2 0.73

  A. Restaurants in Manhattan has the highest confidence ratio(74.3756%) in getting score A. 
  
  B. We can see that inspections in Spring has the highest confidence ratio(75.8125%) in getting score A which may imply that the temperature may be better for food conservation hence better for restaurant score.


7. 


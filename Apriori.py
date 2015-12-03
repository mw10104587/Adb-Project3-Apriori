import json
import collections
import sys


def getAssociatedRulesWith(T, frequentSets, min_sup, min_conf):

	min_conf = float(min_conf)

	associatedRules = []
	# elements in the list are in the following format

	# {
	# 	"lhs":[],
	# 	"rhs":[],
	# 	"conf": 0.67,
	# 	"sup": supp_count
	# }

	for i, k_item_set in enumerate(frequentSets):
		
		# skip the one without rule
		if i == 0 or i == len(frequentSets) -1: 
			continue
		for j, k_item in enumerate(k_item_set):
			
			# k_item is in the following format
			# [['A', 'Fall-RECORD DATE', 'NorthAmerican'], 69273]
			items = k_item[0]

			for idxToRHS, item in enumerate(items):
				
				# idx to right hand side, is the index of the item that we'll be 
				# putting at the assciated rules' right hand side.
				rightHandSide = item

				# use list comprehension to get other items that is not righthandside
				leftHandSide = [x for x in items if x != item]

				# get the support of leftHandSide from the former list in frequentSets
				foundList = filter(lambda x: x[0] == leftHandSide, frequentSets[i-1])

				# get both count to calculate the conf
				lhsCount = foundList[0][1]

				# print "lhs count: " + str(lhsCount)
				rhsUnionlfsCount = k_item[1]
				# print "rhs union count: " + str(k_item[1])

				# *1000000 / 10000
				# so that we can get 4 digits behind 0 
				conf = float( int( float(rhsUnionlfsCount)/ int(lhsCount) *1000000 ) )/10000
				supp_count = int(rhsUnionlfsCount) 
				# print conf 

				# if the conf is larger than min_conf, we append the associated rule into 
				# the list that will be returned. 
				if conf >= min_conf * 100:
					associatedRules.append({
							"lhs": leftHandSide,
							"rhs": rightHandSide,
							"conf": conf,
							"sup": supp_count
						});

	return associatedRules


# a function that generated the required output.txt file
def exportWith(frequentSets, highConfidenceAssoRules, min_sup, min_conf, number_of_rows):

	with open("output.txt", "w") as outFile:

		outFile.write("==Frequent itemsets (min_sup=" + str(int(float(min_sup)*100)) + "%)\n" )

		for frequentSetLength_k in frequentSets:
			for frequentSet in frequentSetLength_k:
				sup_str = str(float(int( float(frequentSet[1])/number_of_rows * 1000000 ))/10000)
				outFile.write(str(frequentSet[0]) + ", " + sup_str + "%\n")

		outFile.write("\n")
		
		outFile.write("==High-confidence association rules (min_conf=" + str(int(float(min_conf)*100)) + "%)\n" )

		for assoRule in highConfidenceAssoRules:
			supp = float(int( float(assoRule["sup"])/ number_of_rows * 1000000 ))/10000
			outFile.write( str(assoRule["lhs"]) + " => " + str([assoRule["rhs"]]) + " (Conf: " + str(assoRule["conf"]) + "%,Supp: " + str(supp) + "%)" + "\n")


def getFrequentSets(T, min_sup):
	
	# the final Sets to return
	frequentList = []

	# C_[NUMBER] are always Candidates dictionary with item as it's key, and count as it's value.
	C_1 = initPass(T)
	
	# number of rows, which is the number of transaction
	number_of_rows = len(T)

	# F_1 is the frequent set with only one item
	F_1 = list(C_1)

	# remove item with support < min_sup
	for i, item in enumerate(C_1):

		if float(C_1[i][1])/number_of_rows < float(min_sup):

			F_1.remove(item)

	# put it into the frquent list
	frequentList.append(F_1)

	# start the loop
	k = 1

	# while the current largest frequent set is not an empty set, we continue
	while not len(frequentList[-1]) == 0:

		C_k = generateCandidate(frequentList[-1])

		for transaction in T:
			for m, c in enumerate(C_k):

				# if it's a subset, we add the counter
				if set(c[0]) & set(transaction) == set(c[0]):
					C_k[m][1] += 1

		# the frequent item list with k terms in an itemset
		F_k = list(C_k)
		
		# remove the ones lower than min_sup
		for i, items in enumerate(C_k):

			if float(items[1])/number_of_rows < float(min_sup):
				F_k.remove(items)

		# print json.dumps(F_k)

		frequentList.append(F_k)
		k += 1

	return frequentList


def generateCandidate(F_k_minus_1):

	# the passed in F_k_minus_1 var means F k-1

	# make sure every items sets in the F_k_minus_1 is sorted 
	for idx in range(0, len(F_k_minus_1) ):
		# print F_k_minus_1[idx][0]
		F_k_minus_1[idx] = [sorted(F_k_minus_1[idx][0]), F_k_minus_1[idx][1] ]

	C_k = [];

	# k, which is the length of items tuple
	k = len(F_k_minus_1[0][0])

	# start join
	for i, k_set_1 in enumerate(F_k_minus_1):

		# find the position and cut the list after this item
		secondList = F_k_minus_1[i+1:]
		for j, k_set_2 in enumerate(secondList):

			# check if the front several elements are the same
			# only the last one is allowed to be different.
			# so we remove the last element at compare the front several terms
			# if cmp == 0, means that the two lists are identical, so we merge them
			# and generate a new item
			if cmp(k_set_1[0][0: k-1], k_set_2[0][0: k-1] ) == 0:

				# merge and sort again
				c = sorted( set(k_set_1[0] + k_set_2[0]) )

				# append into the candidate list
				C_k.append(c)

	# the current structure is not convenient to loop through with,
	# so we make a list that only contains the terms(without the counting)
	F_k_minus_1_set = [itemObject[0] for itemObject in F_k_minus_1]

	# after join, we start to prune here,
	for l, itemsets in enumerate(C_k):

		for x in xrange(0, k+1):
			subset = list(itemsets)
			# by removing one of the element, we can get all of the subsets
			del subset[x]

			# if the subset is not included in the same size frequent list, 
			# we remove it. 
			if not subset in F_k_minus_1_set:

				del	C_k[l]

	# we add the structure with counters back.
	return map(augmentListWithCounter, C_k)


# a function to be called with mapping list
def augmentListWithCounter(x):
	return [x, 0]
	

def initPass(T):

	# get the counted list of tuples
	listOfTuples = collections.Counter(val for row in T
										for val in row).items()

	# turn it into list of item and item count
	return [([k],v) for k,v in listOfTuples]

import Parser
import Apriori
import json, sys


if __name__ == '__main__':

	if len(sys.argv) < 4:
		print "incorrect input format"
		print "Correct Format: <CSV FILE> <min_sup> <min_conf>"

	else:

		csvFile = sys.argv[1]
		min_sup = sys.argv[2]
		min_conf = sys.argv[3]

		print "Finding Associated Pair..."

		# data_set is a list of lists, each item is a row in csv file
		# attributes : DBA, BORO, CUSINE DESCRIPTION, INSPECTION DATE, ACTION, VIOLATION CODE,
		# VIOLATION DESCRIPTION, CRITICAL FLAG, SCORE, GRADE, GRADE DATE, RECORD DATE, INSPECTION TYPE
		data_set = []
		data_set = Parser.parse(csvFile)

		frequentSets = Apriori.getFrequentSets(data_set, min_sup)
		# frequentSets = []

		associatedRules = Apriori.getAssociatedRulesWith(data_set, frequentSets, min_sup, min_conf)

		number_of_rows = len(data_set)
		Apriori.exportWith(frequentSets, associatedRules, min_sup, min_conf, number_of_rows)

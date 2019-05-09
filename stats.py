import re
import operator
from bs4 import BeautifulSoup
from collections import OrderedDict


fileName = "initial_accepted_papers.txt"

titles_dataset = []
n_authors_per_paper = dict()
authors_dataset = dict()
institution_dataset = dict()


def fill_datasets(fileName):

	with open(fileName, 'r') as file:
		for paper in file:
			soup = BeautifulSoup(paper, features="html.parser")
			titles_dataset.append( soup.b.get_text() )
			list_authors = soup.i.get_text().split('· ')
			number_authors = len(list_authors )

			if number_authors not in n_authors_per_paper:
				n_authors_per_paper[number_authors] = 1
			else:
				n_authors_per_paper[number_authors] += 1

			for i in range( number_authors ):

				author_afiliation = list_authors[i].split(" (")

				tmp_author = author_afiliation[0][0:]



				if tmp_author not in authors_dataset:
					authors_dataset[tmp_author] = 1
				else:
					authors_dataset[tmp_author] += 1

				tmp_institution = author_afiliation[1].rstrip(") ").rstrip(")").replace('"', '')

				if tmp_institution == '':
					print(list_authors)

				if  tmp_institution not in institution_dataset:
					institution_dataset[tmp_institution] = 1
				else:
					institution_dataset[tmp_institution] += 1


if __name__ == "__main__":
	fill_datasets(fileName)

	
	# sorted_x = sorted(authors_dataset.items(), key=operator.itemgetter(1))
	# print(sorted_x)
	# sorted_x = sorted(authors_dataset.items(), key=lambda kv: kv[1])
	# print(sorted_x)



	sorted_x = sorted(institution_dataset.items(), key=operator.itemgetter(1))
	print(sorted_x)
	sorted_x = OrderedDict(sorted(institution_dataset.items(), key=lambda t: t[0]))
	print("************************************************************************")
	print(sorted_x)
	print(n_authors_per_paper)

	print(OrderedDict(sorted(n_authors_per_paper.items(), key=lambda t: t[0])))

from bs4 import BeautifulSoup


dataset = 'initial_accepted_papers.txt'




with open(dataset, 'r') as data:


	test = data.readline()
	soup = BeautifulSoup(test, features="html.parser")
	print(soup)
	print("Title: ", soup.b.get_text())
	list_authors = soup.i.get_text().split('· ')
	print("Authors: ", list_authors)


	number_authors = len(list_authors )
	for i in range( number_authors ):
		author_afiliation = list_authors[i].split(" (")
		print("Author: ", author_afiliation[0])
		if i == number_authors - 1:
			print("Afiliation: " + author_afiliation[1][:-1] + "*")
		else:
			print("Afiliation: " + author_afiliation[1][:-2] + "*")



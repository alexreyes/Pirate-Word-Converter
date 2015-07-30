import urllib

def read_text():
	quotes = open("file.txt")
	contents_of_file = quotes.read()
	print("=============================================")
	print("Here is the original content of the files:")
	print("=============================================")
	print(contents_of_file)
	quotes.close()
	convertWords(contents_of_file)

def convertWords(text_to_check):
	connection = urllib.urlopen("http://isithackday.com/arrpi.php?text=" + text_to_check)
	output = connection.read()
	print("==============================================")
	print("Here is the altered version of the file:")
	print("=============================================")
	print(output)

read_text()

print("=============================================")
print("Thanks for using pirate converter! Come again!")
print("=============================================")
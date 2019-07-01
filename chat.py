import os
import re
import matplotlib.pyplot as plt
import string
import collections as clt
import numpy as np



# function for converting file in a list of string
def convert_file_to_text(file):

	# open the file
	file = open('chat.txt','r',encoding='utf8')

	# convert file in a list of string
	with open('chat.txt', encoding='utf8') as f:
		text = f.read().strip()

	# close the file
	file.close()

	# return the text
	return text

# count the messages sent from the user of the chat
def message_number(text):

    # list holding the result
	number = [0,0]

    # search for all the string matching the pattern in messages
    # return a list of strings x
	x = re.findall("(?:\\d{2}\\/)\\d{2}\\/\\d{2}, \\d{2}:\\d{2} - [^:]+: ", text)

    # count the occurrences of user name in the chat
	for line in x:
		if "User1" in line:
			number[0] += 1
		if "User2" in line:
			number[1] += 1

    # print the results
	print("Messages sent from User1: %r" % (number[0]))
	print("Messages sent from User2: %r" % (number[1]))
	print("Total messages: %r" % (number[0] + number[1]))

    # return all the headers
	return number


# function for retriving the header of the message in a list
def get_header(text):
	x = re.findall("(?:\\d{2}\\/)\\d{2}\\/\\d{2}, \\d{2}:\\d{2} - [^:]+: ", text)
	return x



def find_hours(text):
	time_search = re.findall('(\\d{2}:)', "".join(text), re.IGNORECASE)
	time_search = [''.join(c for c in s if c not in string.punctuation) for s in time_search]
	grouped_hour = clt.Counter(time_search)

	plt.figure(1, figsize=(20,10))
	plt.bar(grouped_hour.keys(), grouped_hour.values())

	plt.show()


# remove the header and return only the messages
def remove_header(text):
	x = re.sub("(?:\\d{2}\\/)\\d{2}\\/\\d{2}, \\d{2}:\\d{2} - [^:]+: ",'', text)
	return x


# count consonant and vowels in the messages
def count_consonants_vowels(text):
	#words = clt.Counter(text)
	#return words
	wovels='aeiou'
	consonants = 'bcdfghjklmnpqrstvwxyz'
	alphabet = 'abcdefghijklmnopqrstuvwxyz'

	wovel_count = len(re.findall('[%s]' % wovels, text))
	consonants_count = len(re.findall('[%s]' % consonants, text))

	print("Wovel count: %r" % wovel_count)
	print("Consonant count: %r" % consonants_count)

	list_total_w_c = [0,0]
	list_total_w_c[0] = wovel_count
	list_total_w_c[1]= consonants_count

	a = text
	a = a.lower()
	b = dict.fromkeys(a,0)
	for i in a:
		if i in alphabet:
			b[i] += 1


	c = dict((key,value) for key, value in b.items() if key in alphabet)

	dict_wovel = dict((key,value) for key, value in c.items() if key in wovels)
	dict_consonants = dict((key,value) for key, value in c.items() if key in consonants)

	o_dict_wovel = clt.OrderedDict(sorted(dict_wovel.items()))
	plt.bar(range(len(o_dict_wovel)), o_dict_wovel.values(), align='center')
	plt.xticks(range(len(o_dict_wovel)), list(o_dict_wovel.keys()))
	plt.show()
	
	print(o_dict_wovel)

	c_dict_wovel = clt.OrderedDict(sorted(dict_consonants.items()))
	plt.bar(range(len(c_dict_wovel)), c_dict_wovel.values(), align='center')
	plt.xticks(range(len(c_dict_wovel)), list(c_dict_wovel.keys()))
	plt.show()
	
	print(c_dict_wovel)
	#print("Inizio a contare")
	#print('\n'.join('{} : {}'.format(c, s.count(c)) for i, c in enumerate(s) if c in "abcdefghijklmnopqrstuvwxyz!@#$%^&*()! " and c not in s[:i]))

	return list_total_w_c


# plot total wovels and consonants
def plot_total_w_c(names,list_w_c):
	plt.bar(names, list_w_c)
	plt.show()


# function for plotting the total messages
# sent from chat's users
# bar, plot and line chart
def plot_message_number(names,values):
	plt.figure(1, figsize=(20, 10))
	plt.subplot(131)
	plt.bar(names, values)
	plt.subplot(132)
	plt.scatter(names, values)
	plt.subplot(133)
	plt.plot(names, values)
	plt.suptitle('Message number plot')
	plt.show()
	

text = convert_file_to_text("chat.txt")

names_c = ['Wovels', 'Consonants']
messages = remove_header(text)


list_w_c = count_consonants_vowels(messages)

plot_total_w_c(names_c, list_w_c)




user_1 = input('User name 1')
user_2 = input('User name 2')

names = ['0','0']

names[0] = user_1
names[1] = user_2

values = message_number(text)

plot_message_number(names,values)

#print(find_hours(text))










	
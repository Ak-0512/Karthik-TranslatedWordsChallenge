import time

start = time.time()

import pandas as pd
import csv
import psutil

look_up = pd.read_csv('french_dictionary.csv')
find_words = open("find_words.txt", "r")
a = find_words.read()
find_words.close()
with open('french_dictionary.csv', mode='r') as inp:
    reader = csv.reader(inp)
    dict_from_csv = {rows[0]: rows[1] for rows in reader}
words_txt = open("find_words.txt", "r")
find_words = words_txt.read()
words_txt.close()
find_words_inlist = find_words.split()

import re
import string
document_text = open("t8.shakespeare.txt", 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
tot_eng = []
for word in match_pattern:
    if word in find_words_inlist:
        tot_eng.append(word)
eng = set(tot_eng)
eng = list(eng)
with open('french_dictionary.csv', mode='r') as inp:
    reader = csv.reader(inp)
    dict_from_csv = {rows[0]: rows[1] for rows in reader}
french = []
for x in eng:
    for key, value in dict_from_csv.items():
        if x in key:
            french.append(value)
frequency = {}
for y in tot_eng:
    count = frequency.get(y, 0)
    frequency[y] = count + 1

frequency_list = frequency.keys()
f = []
for z in frequency_list:
    f.append(frequency[z])

final = list(zip(eng, french, f))
header = ['English Word', 'French Word', 'Frequency']
with open('frequency.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    writer.writerow(header)

    for row in final:
        for x in row:
            f.write(str(x) + ',')
        f.write('\n')
time_taken = time.time() - start
memory_taken = psutil.cpu_percent(time_taken)
f = open("performance.txt", "w")
f.write(f'Time to process: 0 minutes {time_taken} seconds\nMemory used: {memory_taken} MB')
f.close()
test_str = text_string
print("The original string is : " + str(test_str))
lookup_dict = dict_from_csv
temp = test_str.split()
res = []
for wrd in temp:
    res.append(lookup_dict.get(wrd, wrd))
res = ' '.join(res)
f = open("t8.shakespeare.translated.txt", "w")
f.write(str(res))
f.close()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/

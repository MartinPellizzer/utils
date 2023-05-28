import os
import csv

# if os.path.isfile('ozonoterapia.csv'):
#     with open('ozonoterapia.csv', 'w') as f: pass

file_in = 'ozono.csv'
file_out = 'ozonoterapia.csv'
topic = 'terapia'

def search_keyword(keyword_in, keywords_out):
    found = False
    if not keywords_out:
        return found
    for keyword_out in keywords_out:
        if keyword_in in keyword_out:
            found = True
            break
    return found


with open(file_in) as f:
    keywords_in = f.readlines()

with open(file_out, 'a') as f: pass

with open(file_out) as f:
    keywords_out = f.readlines()

keywords_in_new = []
for keyword_in in keywords_in:
    keyword_in = keyword_in.replace('\n', '')
    if topic not in keyword_in:
        keywords_in_new.append(keyword_in)
        continue
    found = search_keyword(keyword_in, keywords_out)

    if not found:
        print(keyword_in)

        with open(file_out, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([keyword_in])

with open(file_in, 'w', newline='') as f:
    writer = csv.writer(f)
    for keyword in keywords_in_new:
        writer.writerow([keyword])


#     if 'ozonoterapia' in ozonoterapia_keywords:
#         print(ozonoterapia_keywords)

# with open('ozonoterapia.csv', 'a') as f:
#     ozonoterapia_keywords = f.readlines()



# print(keywords)

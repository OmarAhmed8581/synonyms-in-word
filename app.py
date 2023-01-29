import requests,json
from nltk.corpus import wordnet
from datetime import datetime

now = datetime.now()

# dd/mm/YY
d1 = now.strftime("%d/%m/%Y %H:%M:%S")


print("Server start")
print(d1)


f = open("words.txt", "r")
# print(f.read())
word_list = (f.read()).split(" ")




def synonym_antonym_extractor(phrase):
   
    synonyms = []
    antonyms = []

    for syn in wordnet.synsets(phrase):
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())

    # print(set(synonyms))
    return list(synonyms)




data_dict={}

data_dict_temp={}
no_meaning=[]

for i in range(0,len(word_list)):
    phase = word_list[i].replace('?', '')
    load_data = synonym_antonym_extractor(phase)
    flat=True
    if data_dict == {}:
        if phase not in data_dict:
            data_dict[phase] = load_data
            # print(data_dict)
            data_dict_temp[phase]=[]
    else:
        for key in data_dict.keys():
            value1 = list(data_dict[key])
            value2=  list(load_data)
            matching = [s for s in value2 if s in value1]
            if(len(matching)>0):
                data_dict_temp[key].append(phase)
                flat = False
                break
        
        if flat:
            data_dict[phase] = load_data
            data_dict_temp[phase]=[]
            
print(data_dict_temp)
with open('output.txt', 'w') as f:
    for key in data_dict.keys():
        value1 = list(data_dict[key])
        sys = ",".join(value1)
        f.write(key+":")
        f.write('\n')
        f.write(sys)
        f.write('\n')
        f.write('\n')


now = datetime.now()

# dd/mm/YY
d1 = now.strftime("%d/%m/%Y %H:%M:%S")

print(d1)
print("Server end")
print("Processing Complete......")




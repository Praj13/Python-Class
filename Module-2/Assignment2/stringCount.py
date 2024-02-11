sentence="perfect ? he is the perfect . perfect"
print("t-he original sentence is: "+sentence)
sentence_list=sentence.split()

#in normal way
dict_2 = {}
for word in sentence_list:
    count_value = sentence.count(word)
    dict_2[word] = count_value
print(dict_2)



#by dictionary comprehension
dict1={word:sentence.count(word) for word in sentence_list}
print(dict1)


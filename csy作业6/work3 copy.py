from pathlib import Path

path = Path('alice_in_wonderland.txt')
contents = path.read_text()

total_words = contents.split()
different_words = []

for word in total_words :
    a = word.lower()
    if a not in different_words:
        different_words.append(a)

print(len(different_words))


#统计一个单词在整本书中出现的次数

stat = {}
for word in different_words:
    count = 0
    for one_word in total_words:
        if one_word == word:
            count = count + 1
    stat[word] = count

print(stat)

"""
same_words = []
number_list = []
high_frequency = []

for one in different_words:
    if one in total_words:
        same_words.append(one)
        value = len(same_words)
        number_list.append(value)    
        while value == max(number_list):
            b = number_list.pop(value)
            high_frequency.append(b)
            if len(high_frequency)==10:
                break

print(number_list)
print(high_frequency)


"""
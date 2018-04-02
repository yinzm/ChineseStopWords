# -*- coding:utf-8 -*-

file1 = '中文停用词表.txt'
file2 = '哈工大停用词表.txt'
file3 = '四川大学机器智能实验室停用词库.txt'

stopWordsSet = set()

with open(file1, 'r', encoding='utf-8') as f1,\
    open(file2, 'r', encoding='utf-8') as f2,\
    open(file3, 'r', encoding='utf-8') as f3:
    for word in f1.readlines():
        stopWordsSet.add(word.strip())
    for word in f2.readlines():
        stopWordsSet.add(word.strip())
    for word in f3.readlines():
        stopWordsSet.add(word.strip())

stopWords = sorted(list(stopWordsSet))
with open('ChineseStopWords.txt', 'w', encoding='utf-8') as f:
    for word in stopWords:
        f.write("%s\n" % word)
import batch
import re
import os
import string

def extract_data(gram_list):
    gram_dict = {'a' : 0}
    for gram in gram_list:
        with open(gram, 'r') as gramfile:
            for line in gramfile.readlines():
                x = line.replace('\n', '').split(' ')
                x[1] = int(''.join([s for s in x[1] if s in string.digits]))
                if x[0] in gram_dict.keys() : gram_dict[x[0]] += x[1]
                else : gram_dict[x[0]] = int(x[1])
                
    return gram_dict

def create_master_file(gram_dict, size):
    with open(os.getcwd() + '/master/{0}gram-master.txt'.format(size), 'w') as masterfile:
        masterfile.write(str(gram_dict))

def run():
    files = batch.get_all_items_cwd()

    onegram = []
    twogram = []
    threegram = []
    fourgram = []

    for file in files:
        if 'gram' in file and re.search(".txt$", file) is not None:
            if 'onegram' in file:
                onegram.append(file)
            elif 'twogram' in file:
                twogram.append(file)
            elif 'threegram' in file:
                threegram.append(file)
            elif 'fourgram' in file:
                fourgram.append(file)

    print('Files located, extracting data')


    onegram = extract_data(onegram)
    twogram = extract_data(twogram)
    threegram = extract_data(threegram)
    fourgram = extract_data(fourgram)

    print('Data extracted, creating master files...')

    create_master_file(onegram, 'one')
    create_master_file(twogram, 'two')
    create_master_file(threegram, 'three')
    create_master_file(fourgram, 'four')

def generate_gram_list(masterdir):
    def access(e):
        return e[1]

    gram_list = [x for x in batch.get_items_cwd() if 'gram-master' in x]

    onegram = []
    twogram = []
    threegram = []
    fourgram = []
    onelen = 0
    twolen = 0
    threelen = 0
    fourlen = 0

    for gram in gram_list:
        with open(gram, 'r') as gramfile:
            gram_dict = eval(gramfile.readlines()[0])
            for key in gram_dict.keys():

                val = int(gram_dict[key])

                if 'one' in gram:
                    onelen += val
                    onegram.append((key, val))
                elif 'two' in gram:
                    twolen += val
                    twogram.append((key, val))
                elif 'three' in gram:
                    threelen += val
                    threegram.append((key, val))
                elif 'four' in gram:
                    fourlen += val
                    fourgram.append((key, val))
                
    onegram.sort(key=access, reverse=True)
    twogram.sort(key=access, reverse=True)
    threegram.sort(key=access, reverse=True)
    fourgram.sort(key=access, reverse=True)

    onefreq = []
    for gram in onegram:
        onefreq.append((gram[0], gram[1], gram[1] / onelen))
    
    twofreq = []
    for gram in twogram:
        twofreq.append((gram[0], gram[1], gram[1] / onelen))
    twofreq = twofreq[:40]

    threefreq = []
    for gram in threegram:
        threefreq.append((gram[0], gram[1], gram[1] / onelen))
    threefreq = threefreq[:40]

    fourfreq = []
    for gram in fourgram:
        fourfreq.append((gram[0], gram[1], gram[1] / onelen))
    fourfreq = fourfreq[:40]

    with open(masterdir + 'all_data.txt', 'w') as data:
        data.write('length: ' + str(onelen) + '\n')
        
        for gram in onefreq:
            data.write(str(gram[0]) + ': ' + str(gram[1]) + ', ' + str(gram[2]) + '\n')

        for gram in twofreq:
            data.write(str(gram[0]) + ': ' + str(gram[1]) + ', ' + str(gram[2]) + '\n')

        for gram in threefreq:
            data.write(str(gram[0]) + ': ' + str(gram[1]) + ', ' + str(gram[2]) + '\n')

        for gram in fourfreq:
            data.write(str(gram[0]) + ': ' + str(gram[1]) + ', ' + str(gram[2]) + '\n')
    

        





# print(files)

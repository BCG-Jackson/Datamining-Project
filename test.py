from efficient_apriori import apriori
import csv
import codecs
import time

def fix_nulls(s):
    for line in s:
        yield line.replace('\0', ' ')

def getValues(row, col, splitBy = ' '): # returns a list of values 
    t = row[col] # t is a string
    t = t.split(splitBy) # t is now a list of strings
    trimmed = []
    for s in t: # for strings in t
        if s == '' or s == 'Unknown':
            continue
        else:
            trimmed.append(s)

    if len(trimmed) > 0:
        return trimmed
    else:
        return ''

def trimEmpty(transactions): # transactions is a list of strings
    trimmed = []
    for i in transactions: # for all lists of strings in transactions
        if len(i) == 0: # if the list is empty
            continue
        else:
            trimmed.append(i)
    return trimmed



def getTransactions(maxLines = 100, preset='default'): # col defines which column to look at, maxLines is how many lines to evaluate, 
    # presets: default, words in plots, cast and director
    # below are the column names and index
    year = 0 
    title = 1
    ethnicity = 2
    director = 3
    cast = 4
    genre = 5
    wikiURL = 6
    plot = 7
    transactions = [] # list of lists of strings
    csv_reader = csv.reader(fix_nulls(codecs.open('movieData.csv', 'rU', 'utf-8')))
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
            continue
        if preset=='default':
            #print(f'\t{row[0]}, {row[1]}, {row[2]}.') # print 
            transactions.append((row)) # get all columns as transaction (not helpful?)
        elif preset == 'words in plots':
            text = row[plot]
            words = text.split(' ') # gets all words seperated by spaces as list of strings
            transactions.append((words))
        elif preset == 'cast and director':
            casts = getValues(row, cast, splitBy = ', ') # text is alist of strings
            directors = getValues(row, director, splitBy = ', ')
            castsAndDirectors = [*casts, *directors]
            transactions.append(castsAndDirectors)
        line_count += 1
        if line_count == maxLines:
            break
    print(f'Processed {line_count} lines. Trimming...')
    transactions = trimEmpty(transactions)
    return transactions

def apriorize(transactions, support, confidence): # finds rules based on transaction list
    print('Applying apriori...')
    itemsets, rules = apriori(transactions, min_support=support,  min_confidence=confidence)
    print('Rules:')
    for r in rules:
        print(r)
    print('Itemsets:')
    for i in itemsets:
        print(i)

def driver():
    start = time.time()
    t = getTransactions(maxLines= -1, preset = 'words in plots')
    apriorize(t, support = .2, confidence=1)
    end = time.time()
    print('\nExecution took '+(end - start)+' seconds.')

driver()
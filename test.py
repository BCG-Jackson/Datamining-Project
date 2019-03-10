from efficient_apriori import apriori
import csv
import codecs

# with open('movieData.csv', encoding="utf-8") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',') 
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         else:
#             print(f'\t{row[0]}, {row[1]}, {row[2]}.')
#             line_count += 1
#     print(f'Processed {line_count} lines.')

def fix_nulls(s):
    for line in s:
        yield line.replace('\0', ' ')

csv_reader = csv.reader(fix_nulls(codecs.open('movieData.csv', 'rU', 'utf-8')))
line_count = 0
for row in csv_reader:
    if line_count == 0:
        print(f'Column names are {", ".join(row)}')
        line_count += 1
    else:
        print(f'\t{row[0]}, {row[1]}, {row[2]}.')
        line_count += 1
print(f'Processed {line_count} lines.')


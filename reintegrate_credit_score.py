from csv import reader, writer

# Opens raw data file and creates a list containing its lines
raw_file = open("german.data", "r").read().splitlines()

# Locates credit risk attribute and places it into list
credit_risks = []
for i in range(0, len(raw_file)):
    credit_risks.append(raw_file[i][-1])

# Reader/Writer objects for csv
w = writer(open('german_credit_data_updated.csv', 'w'), lineterminator='\n')
r = reader(open('german_credit_data.csv', 'r'))

# List for updated rows
all = []

# Adds new column for 'Credit Risk'
row = next(r)
row.append("Credit Risk")
all.append(row)

# Iterates through and adds credit risk to each row
# Adds new rows to 'all'
i = 0
for row in r:
    row.append(credit_risks[i])
    all.append(row)
    i = i + 1

# Updates the output file
w.writerows(all)




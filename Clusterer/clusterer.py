import csv

# Open the CSV file and read it into a list of dictionaries
with open('sequences2.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Group the rows by matching values in columns 2, 3, and 4
groups = {}
for row in data:
    key = (row['Heavy Chain'], row['Light Chain'], row['type'])
    if key not in groups:
        groups[key] = {'International Non-proprietary Name': [], 'type': row['type']}
    groups[key]['International Non-proprietary Name'].append(row['International Non-proprietary Name'])

# Print out the groups
i = 1
for key, values in groups.items():
    print(f"Cluster {i}: {', '.join(values['International Non-proprietary Name'])} ({values['type']})")
    i += 1

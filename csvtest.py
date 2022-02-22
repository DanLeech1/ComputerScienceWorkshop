import csv

with open('csvtest.csv', 'r') as f:
    csv_reader = csv.reader(f)
    # skip the header
    next(csv_reader)
    
    # read the data
    C = []
    for row in csv_reader:
        data = float(row[0])
        C.append(data)
    
    C_min = min(C)
    C_max = max(C)
    C_ave = sum(C) / len(C)
    print(f"C minimum: {C_min}")
    print(f"C maximum: {C_max}")
    print(f"C average: {C_ave}")
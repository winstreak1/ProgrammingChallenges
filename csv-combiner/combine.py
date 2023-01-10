import pandas as pd
import glob
import os
import csv

#access .csv files
files = glob.glob('fixtures/*.csv')
print(files)

#merge or concatenate rows of each file and remove(split) the basename
df = pd.concat([pd.read_csv(fp).assign(filename=os.path.basename(fp).split('.')[0])
       for fp in files])
print(df)

#output file to output.csv
with open('output.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(df)
import csv

import os
import pathlib

# while read line ; do mv "$line" $(date +%s) ; sleep 2 ; done <<< $(ls -ltr | cut -d ' ' -f 9-)

base_path = pathlib.Path().absolute().parent
data_path = base_path / "data_2"
files = os.scandir(data_path)
data_set = dict()

for entry in files:
    file = open(entry.path)
    csv_reader = csv.reader(file)

    row = csv_reader.__next__()
    model_index = row.index("MODEL")
    firmware_index = row.index("FIRMWARE VERSION")

    for row in csv_reader:
        if data_set.get(row[model_index]):
            data_set[row[model_index]].add(row[firmware_index])
        else:
            data_set[row[model_index]] = {row[firmware_index]}

    file.close()

out = open(base_path / "output_2.csv", "w")
csv_writer = csv.writer(out)

for item in data_set:
    csv_writer.writerow([item, *data_set[item]])

out.close() 

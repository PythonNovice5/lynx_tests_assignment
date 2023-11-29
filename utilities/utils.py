import os
import csv

def read_data_from_csv(file_name):
    data_list = []
    script_dir = os.path.dirname(os.path.abspath(__file__))
    relative_path = os.path.join(script_dir, '..', 'test_data', file_name)
    relative_path = os.path.normpath(relative_path)
    with open(relative_path, 'r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data_list.append(row)
    return data_list


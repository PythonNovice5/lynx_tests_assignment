
import csv

def read_data_from_csv(file_path):
    data_list = []
    file_path = "test_data/" + file_path
    with open(file_path, 'r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data_list.append(row)
    return data_list


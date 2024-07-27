import json
import os
import csv
from selenium.webdriver.support.ui import Select


def read_data_from_csv(file_name):
    data_list = []
    script_dir = os.path.dirname(os.path.abspath(__file__))
    relative_path = os.path.join(script_dir, "..", "test_data", file_name)
    relative_path = os.path.normpath(relative_path)
    with open(relative_path, "r", newline="", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data_list.append(row)
    return data_list


def select_from_dropdown(self, elem, selector_type, to_be_selected):
    dropdown = Select(elem)
    if selector_type == "text":
        dropdown.select_by_visible_text(to_be_selected)
    elif selector_type == "value":
        dropdown.select_by_value(to_be_selected)
    elif selector_type == "index":
        dropdown.select_by_index(int(to_be_selected))
    else:
        raise ValueError("Invalid selector type. Use 'text', 'value', or 'index'.")


def read_data_from_json(file_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    relative_path = os.path.join(script_dir, "..", "test_data", file_name)
    relative_path = os.path.normpath(relative_path)
    with open(relative_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

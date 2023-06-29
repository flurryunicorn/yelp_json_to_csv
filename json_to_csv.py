import json
import csv
import re
from yelp_fieldlists import get_headers, get_data

BUSINESS = "business"
REVIEW = "review"
TIP = "tip"
CHECKIN = "checkin"
USER = "user"

TYPE_LISTS = [BUSINESS, REVIEW, TIP, CHECKIN, USER]


def normalize_text(text):
    """
    Remove non-ASCII chars.
    """
    text = re.sub('[^\x00-\x7F]+', ' ', text)
    return text

def json_to_csv(json_file, csv_prefix, file_type, max_rows=100000):
    current_row = 0
    """
    json_file ==> .json file to be converted
    csv_prefix ==> prefix for output CSV files
    fileType ==> 'business' or 'review' or 'tip'
    max_rows ==> maximum number of rows per CSV file (default: 1,000,000)
    """
    if file_type not in TYPE_LISTS:
        raise ValueError('Type {} not defined.'.format(file_type))

    current_count = 0
    csv_count = 1
    csv_file = f"{csv_prefix}_{csv_count}.csv"

    with open(csv_file, 'w', encoding='utf-8', errors='replace') as file:
        csv_writer = csv.writer(file, lineterminator='\n')
        csv_writer.writerow(get_headers(file_type))
        with open(json_file, encoding='utf-8', errors='replace') as j_file:
            for line in j_file:
                current_row += 1
                print(current_row)
                data = json.loads(line)
                if file_type == REVIEW or file_type == TIP:  
                    data['text'] = ''.join([normalize_text(text) for text in data['text']])
                csv_writer.writerow(get_data(file_type, data))
                current_count += 1

                if current_count == max_rows:
                    print(f"File {csv_file} created successfully.")
                    current_count = 0
                    csv_count += 1
                    csv_file = f"{csv_prefix}_{csv_count}.csv"
                    file = open(csv_file, 'w', encoding='utf-8', errors='replace')
                    csv_writer = csv.writer(file, lineterminator='\n')
                    csv_writer.writerow(get_headers(file_type))

    print(f"File {csv_file} created successfully.")

def main():
    """
    Entry-point for the function.
    """
    _type = TIP
    json_file = "yelp_academic_dataset_tip.json".format(_type)
    csv_prefix = '{0}_part'.format(json_file.split('.json')[0])
    
    json_to_csv(json_file, csv_prefix, _type, max_rows=100000)
    
if __name__ == "__main__":
    main()

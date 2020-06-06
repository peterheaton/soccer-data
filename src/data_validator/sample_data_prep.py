import os
import json
from jsonschema import validate, Draft7Validator
import time
import pandas as pd\


# This function creates sample data json file from an excel file
# For data privacy reasons I'm not including this directory and the files in the repo.
# You'll need to pull the "New Jersey Data.xlsx" from Adam's email sent to us - subject: "Satori Soccer: Documentation and Sample Data"
def create_json_from_excel_file(excel_file_name):


    current_dir = os.path.dirname(__file__)
    sample_data_dir = os.path.abspath(os.path.join(current_dir, '..', '..', 'sample_data'))
    xl_file_path = os.path.join(sample_data_dir, 'New Jersey Data.xlsx')
    json_file_path = os.path.join(sample_data_dir, 'new_jersey_sample.json')

    # Read the sample data from excel-based file and convert it to a json line-delimited format
    df = pd.read_excel(xl_file_path, sheet_name='Sheet1')
    df.to_json(json_file_path, orient='records', lines=True)

    return


def convert_json_file():


    current_dir = os.path.dirname(__file__)
    sample_data_dir = os.path.abspath(os.path.join(current_dir, '..', '..', 'sample_data'))
    json_file_path = os.path.join(sample_data_dir, 'new_jersey_sample.json')
    
    start_time = time.time()
    print(f"Reading json from file")
    with open(json_file_path, 'r') as f:
        json_list = [json.loads(line) for line in f]
    print(f'''Finished reading json file
    Elapsed time: {time.time() - start_time} seconds''')


    new_json_list = []

    for r in json_list:
        r['Zip'] = str(r['Zip']).rjust(5, '0')
            
     
        new_json_list.append(r)

    df = pd.DataFrame(new_json_list) 

    new_json_file_path = os.path.join(sample_data_dir, 'new_new_jersey_sample.json')
    df.to_json(new_json_file_path, orient='records', lines=True)


if __name__ == "__main__": 
    # convert_json_file()
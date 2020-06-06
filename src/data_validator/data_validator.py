import os
import json
from jsonschema import validate, Draft7Validator
import time
import pandas as pd

# This file currently assumes there's a sample_data folder and schema_models folder in the root of the project

def validate_file(file_name, validation_schema):

    current_dir = os.path.dirname(__file__)
    sample_data_dir = os.path.abspath(os.path.join(current_dir, '..', '..', 'sample_data'))
    schema_data_dir = os.path.abspath(os.path.join(current_dir, '..', '..', 'schema_models'))
    json_file_path = os.path.join(sample_data_dir, file_name)

    validation_schema_file = f'{validation_schema}.schema.json'
    validation_schema_path = os.path.join(schema_data_dir, validation_schema_file)

    start_time = time.time()
    print(f"Reading json from file")
    with open(json_file_path, 'r') as f:
        json_list = [json.loads(line) for line in f]
    print(f'''Finished reading json file
    Elapsed time: {time.time() - start_time} seconds''')


    print(f'Reading validation schema file at path: {validation_schema_path}')
    with open(validation_schema_path, 'r') as f:
        json_schema = json.load(f)

    print('Beginning to validate json data')
    start_time = time.time()
    v = Draft7Validator(json_schema)
    for index, record in enumerate(json_list):
        # print(f'validating record {index + 1}')
        try:
            v.validate(record)
        except Exception as e:
            print(f'error on line {index + 1}:')
            print(e)
    print(f'''Finished validating json data.
        Elapsed time: {time.time() - start_time} seconds''')


    return


if __name__ == "__main__": 
    validate_file(file_name='new_jersey_sample.json', validation_schema='jersey-shore-v1')
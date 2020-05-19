import os
import pandas as pd
import great_expectations as ge

# This module is just a script to test the ability of the Great Expectations to read from a generic data source and validate a data set.
# May or may not use this for ingestion raw data files, but it may be use for validating data sets once staged in the database



# The next four lines assume there is a "sample_data" directory in the root of the project (sample level as src directory).
# For data privacy reasons I'm not including this directory and the files in the repo.
# You'll need to pull the "New Jersey Data.xlsx" from Adam's email sent to us - subject: "Satori Soccer: Documentation and Sample Data"
current_dir = os.path.dirname(__file__)
sample_data_dir = os.path.abspath(os.path.join(current_dir, '..', '..', 'sample_data'))
xl_file_path = os.path.join(sample_data_dir, 'New Jersey Data.xlsx')
json_file_path = os.path.join(sample_data_dir, 'new_jersey_sample.json')

# Read the sample data from excel-based file and convert it to a json line-delimited format
df = pd.read_excel(xl_file_path, sheet_name='Sheet1')
df.to_json(json_file_path, orient='records', lines=True)

# exp_df = ge.read_json(json_file_path)
 
# print(exp_df.expect_column_values_to_be_in_set("Sex", ["male", "female"]))
import os
import json
import time
import data_validator
import custom_transformations as ct



def transform_item(data): 

    nj_data_map = {
        'TableLevel': 'Player Season',
        'SeasonType': 'Unknown',
        'PlayerBk': data['Identifier'].strip(),
        'LocationName': 'New Jersey',
        'Season': data['Seasonal Year'].strip(),
        'NationalAssociation': 'USYS',
        'Organization': 'New Jersey', 
        'District': 'Unknown',
        'League': 'Unknown',
        'Club': data['Organization Name'].strip() or 'Unknown',
        'Team': 'Unkown',
        'StreetAddress': 'Unknown',
        'City': 'Unknown',
        'State': 'Unknown',
        'Zip': ct.transform_zip(data['Zip']),
        'PlayerLevel': ct.transform_player_level(data['Player Member Type'])
    }

    return nj_data_map

def transform_data(raw_list):

    # limited_list = raw_list[:10]
    limited_list = [r for r in raw_list if r['Identifier'].strip() == 'ANGELELI20121109']

    transformed_list = []
    for item in limited_list:
        transformed_list.append(transform_item(item))


    print(json.dumps(transformed_list, indent=4))


if __name__ == "__main__": 
    json_list = data_validator.validate_file(file_name='new_jersey_sample.json', validation_schema='jersey-shore-v1')
    transform_data(json_list)
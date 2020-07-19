import os
import json
import time


def transform_zip(input):
    if input[:5].isnumeric():
        return input[:5]

def transform_gender_to_code(input):
    first_input_gender_character = input.strip().lower()[:1]
    value_map = {
        'm': 'M',
        'f': 'F',
        'b': 'M',
        'g': 'F'
    }
    
    output = value_map[first_input_gender_character] or 'Unknown'
    
    return output

def transform_player_level(input):
    input = input.strip().lower()

    value_map = {
        'topsoccer': 'Recreation',
        'recreation': 'Recreation',
        'travel': 'Travel'
    }
    
    output = value_map[input] or 'Unknown'

    return output 



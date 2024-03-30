import io
import pandas as pd
import requests
import json

#https://stackoverflow.com/questions/21104592/json-to-pandas-dataframe
#https://stackoverflow.com/questions/11346283/renaming-column-names-in-pandas
#https://stackoverflow.com/questions/13411544/delete-a-column-from-a-pandas-dataframe

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    theft_types = kwargs.get('theft_types')
    #print(theft_types)
    all_case_type = []
    for theft_type in theft_types:
        theft_type_uuid = kwargs.get(theft_types[theft_type])
        #print(theft_type)

        url = 'https://data.taipei/api/v1/dataset/'+theft_type_uuid+'?scope=resourceAquire'
        response = requests.get(url)
        data = json.loads(response.text)
        # total_count
        total_count = data['result']['count']
        limit = 1000
        all_df = []
        for i in range(0, total_count//limit+1):
            url = 'https://data.taipei/api/v1/dataset/'+theft_type_uuid+'?scope=resourceAquire&limit='+str(limit)+'&offset='+str(i*limit)
            response = requests.get(url)
            data = json.loads(response.text)
            df = pd.json_normalize(data['result']['results'])
            all_df.append(df)

        total_df = pd.concat(all_df)
        all_case_type.append(total_df)
    total_types_df = pd.concat(all_case_type)
    return total_types_df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'

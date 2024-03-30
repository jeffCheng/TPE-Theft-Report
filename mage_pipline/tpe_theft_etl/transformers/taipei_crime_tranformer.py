import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    data = data.rename(columns={'編號': 'case_num', '案類': 'case_type',
    '發生日期':'case_date','發生時段':'case_datetime', 
    '發生地點': 'case_address_range'})

    data = data.drop(columns=['_id', '_importdate.date', '_importdate.timezone_type','_importdate.timezone'])
    #df_filtered = data.dropna()
    df_filtered = data[(data['case_date'] != '') ]
    df_filtered = df_filtered[(df_filtered['case_type'] != '') ]
    d = df_filtered['case_date'] 
    for i in range(len(df_filtered)):
        d.iloc[i]= str(19110000 + int(d.iloc[i]))
    df_filtered['case_date'] = pd.to_datetime(df_filtered['case_date'])
    df_filtered['case_type'] = df_filtered['case_type'].replace(kwargs.get('theft_types'), regex=True)
    
    return df_filtered


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'

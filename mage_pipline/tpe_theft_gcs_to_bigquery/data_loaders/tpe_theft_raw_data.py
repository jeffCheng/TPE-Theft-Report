import pyarrow as pa
import pyarrow.parquet as pq 
import os

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/src/zoomcamp-mage.json'
project_id = '<your_project_id>'
bucket_name = 'tpe_theft_open_data'
table_name = 'theft'

root_path = f'{bucket_name}/{table_name}'

@data_loader
def load_from_google_cloud_storage(*args, **kwargs):
    """
    Template for loading data from a Google Cloud Storage bucket.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#googlecloudstorage
    """
    gcs = pa.fs.GcsFileSystem()
    arrow_df = pa.parquet.ParquetDataset(root_path, filesystem=gcs)
    #print(arrow_df)
    return arrow_df.read().to_pandas()


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'

# data-zoomcamp-project

## Problem statement

This project collects information on car/motorcycle/bicycle thefts and residential burglary hotspots records in Taipei City, Taiwan. We collected this data through an API(https://data.taipei/) and then stream data into Google Cloud Platform's BigQuery. We use Mage to execute ETL tasks. The raw data is written to Google Cloud Storage as a Data Lake. Then, we partitioned the data in Google Cloud Storage and write it to Google Cloud Platform's BigQuery. We connected this records with Looker Studio running twice a week. 





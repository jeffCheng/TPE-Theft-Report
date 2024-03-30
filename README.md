# data-zoomcamp-project

## Problem statement

This project collects information on car/motorcycle/bicycle thefts and residential burglary hotspots records in Taipei City, Taiwan. The main issue is that the data is scattered across various APIs, and there's a need for an integrated map to visualize related theft incidents. We collected this data through an API(https://data.taipei/) and then stream data into Google Cloud Platform's BigQuery. We use Mage to execute ETL tasks. The raw data is written to Google Cloud Storage as a Data Lake. Then, we partitioned the data in Google Cloud Storage and write it to Google Cloud Platform's BigQuery. We connected this records with Looker Studio running ETL jobs twice a week. 

## Dashboard
![image](https://github.com/jeffCheng/data-zoomcamp-project/blob/560eeb0eb8b5d1ecdd1b66a50b5aca3f2e4540e4/img/dashboard.png)


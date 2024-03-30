# TPE-Theft-Report

## Problem statement

This project collects information on car/motorcycle/bicycle thefts and house burglary hotspots records in Taipei City, Taiwan. The main issue is that the data is scattered across various APIs, and there's a need for an integrated map to visualize related theft incidents. Collected these data through an API(https://data.taipei/) and then stream data into Google Cloud Platform's BigQuery. We use Mage to execute ETL tasks. The raw data is written to Google Cloud Storage as a Data Lake. Then, partitioned the data in Google Cloud Storage and wrote it to Google Cloud Platform's BigQuery. It is connected this records with Looker Studio running ETL jobs twice a week. 

## Dashboard
![image](https://github.com/jeffCheng/data-zoomcamp-project/blob/560eeb0eb8b5d1ecdd1b66a50b5aca3f2e4540e4/img/dashboard.png)

## Data Pipeline & Technologies
Use **batch** data pipeline running ETL jobs twice a week.
- **Cloud**: GCP
- **Infrastructure as code (IaC)**: Terraform
- **Workflow orchestration**: Mage
- **Data Warehouse**: BigQuery

### Cloud
- This project is developed in the GCP and Terraform is used for creating Google Cloud Storage and BigQuery dataset.

### Data ingestion 
- Use Batch / Workflow orchestration and Divide into two pipelines:

<img src="https://github.com/jeffCheng/TPE-Theft-Report/blob/ff89b21d85f4ded27f57248500d3aa52add2072f/img/tpe_theft_etl.png" width="400">

  - **tpe_theft_etl** :
    - taipei_crime_loader: load the data from API
    - taipei_crime_tranformer: clean null and empty data and rename columns
    - taipei_crime_export_gloudstroge: use pyarrow to partition the data by case types

<img src="https://github.com/jeffCheng/TPE-Theft-Report/blob/ff89b21d85f4ded27f57248500d3aa52add2072f/img/tpe_theft_etl.png" width="400">

  - **tpe_theft_gcs_to_bigquery**:
    - tpe_theft_raw_data: load the raw data from Google Cloud Storage bucket
    - tpe_theft_to_bigquery: Append the data to Bigquery

### Data warehouse
- Tables are partitioned and clustered in a way in different theft case types including house, motorcycle, bicycle and car because there is different API to call by each types. Although some use cases would use year and month to partition, these API would keep to update the old data from the previous year and month. As a result, I would keep case types as partition keys.
  
### Transformations
- Most of tranformations are completed with Mage. From BigQuery to Looker Studio, we would need to use custom query to display our data:
```
select * from (
select case_num, case_type, case_address_range, DATE(case_date) as case_date1 from tpe_opendata.theft_data) a
where a.case_date1 BETWEEN PARSE_DATE('%Y%m%d', @DS_START_DATE) AND  PARSE_DATE('%Y%m%d', @DS_END_DATE)
```
### Dashboard
- Connected to the Looker Studio
    1. 1 graph that shows the locations of the theft data
    2. 1 graph that shows the distribution of the data across one year

- Here is the Dashboard link: [https://lookerstudio.google.com/s/knsLtdAIIq4](https://lookerstudio.google.com/reporting/d2b9291f-7937-44ad-a40d-91cbe9c2df81)


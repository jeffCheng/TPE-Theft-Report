# TPE-Theft-Report

## Problem statement

This project collects information on car/motorcycle/bicycle thefts and residential burglary hotspots records in Taipei City, Taiwan. The main issue is that the data is scattered across various APIs, and there's a need for an integrated map to visualize related theft incidents. Collected these data through an API(https://data.taipei/) and then stream data into Google Cloud Platform's BigQuery. We use Mage to execute ETL tasks. The raw data is written to Google Cloud Storage as a Data Lake. Then, partitioned the data in Google Cloud Storage and wrote it to Google Cloud Platform's BigQuery. It is connected this records with Looker Studio running ETL jobs twice a week. 

## Dashboard
![image](https://github.com/jeffCheng/data-zoomcamp-project/blob/560eeb0eb8b5d1ecdd1b66a50b5aca3f2e4540e4/img/dashboard.png)

## Data Pipeline & Technologies
Use **batch** data pipeline running ETL jobs twice a week.
- **Cloud**: GCP
- **Infrastructure as code (IaC)**: Terraform
- **Workflow orchestration**: Mage
- **Data Warehouse**: BigQuery

### Cloud
- The project is developed in the cloud and IaC tools are used

### Data ingestion 

- Batch / Workflow orchestration
    - End-to-end pipeline: multiple steps in the DAG, uploading data to data lake

### Data warehouse
- Tables are partitioned and clustered in a way that makes sense for the upstream queries (with explanation)
### Transformations
- Tranformations are defined with dbt, Spark or similar technologies

### Dashboard

1. 1 graph that shows the distribution of some categorical data
2. 1 graph that shows the distribution of the data across a temporal line

### Reproducibility

- Instructions are clear, it's easy to run the code, and the code works


### MISC

Deploying mage to GCP
the video DE Zoomcamp 2.2.7 is missing  the actual deployment of Mage using Terraform to GCP. The steps for the deployment were not covered in the video.
I successfully deployed it and wanted to share some key points:
In variables.tf, set the project_id default value to your GCP project ID.
 2 . Enable the Cloud Filestore API:
 Visit the Google Cloud Console.
Navigate to "APIs & Services" > "Library."
Search for "Cloud Filestore API."
Click on the API and enable it.
To perform the deployment:
terraform init

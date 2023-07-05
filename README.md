
# Data Engineering Project
____


A basic data engineering `ETL` project that uses *Beautiful Soup* web scraping library in Python to scrape information from a [car marketplace](https://www.carpages.ca/used-cars/), *LXML* parser to parse the HTML components and grab the following information about cars - 

1. Title of the ad 
2. Description of the car
3. KMs driven by the car
4. Color of the car
5. Price of the car
6. Web link for the ad

and finally uses *Pandas* library to convert the information into a DataFrame and *Boto3* to load the csv file onto an AWS S3 bucket.

**Airflow** was used as a workflow orchestrator to run the scripts on the Airflow Webserver hosted on AWS EC2 instance.

___


AWS was used as cloud host to deploy and run the scripts.
2 services that were used are -

- Amazon EC2 - Create virtual machines in the cloud which can be used as servers
- Amazon S3 - Simple object store in the AWS cloud <br>
<br>
<br>
<br>

## How to recreate this project??

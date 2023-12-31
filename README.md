
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
This project requires some money(INR 50-100) to be completed successfully as it uses AWS paid services not part of the free tier. If you wish to proceed kindly do so on your own discretion. You have been alerted.


1. First of all clone this repository onto your local machine. Run the following command on the command line <br>
`git clone https://github.com/Omega-84/airflow_data_engg_project.git`

2. Sign up for a free tier AWS account. Check out [YouTube](https://www.youtube.com/results?search_query=create+aws+account) for tutorials if facing difficulty. 
### NOTE - You will require a Credit/Debit Card to create an account

3. Setup billing on AWS to avoid overhead costs. (Advised) [Tutorials](https://www.youtube.com/results?search_query=setup+billing+for+aws)

4. Create an IAM user and attach the full access policies for S3 and EC2 services.
It is advisable not to use root or primary account for any development. 
Once created, save the access credentials for the user as it is necessary to access the account later on. [Tutorial](https://www.youtube.com/results?search_query=create+iam+user+and+attach+policy+)

5. In the local development environment, install the *awscli* library to configure the IAM user to perform operations in the local environment.<br>
`pip install awscli`<br>
The run the command <br>
`aws configure` <br>
When prompted, enter the saved Access Key ID and press enter, now enter the Secret Access Key and press enter, the remaining two inputs are beyond the scope of this project and can be skipped by pressing enter twice. 
Now we can perform some operations on our AWS account from the command line itself.

6. Login in to the AWS management console for the IAM user created. Head on over to the EC2 service web page and click on launch an instance. Follow the following steps
* Provide any desirable name
* Select the **Ubuntu** machine image
* Select the **t2.medium** instance type. 

NOTE - The free tier instance **t2.micro** has just 1 GB of memory which is insufficient to run Airflow, we require a minimum of 4 GB to launch Airflow so we selected the cheapest option available i.e. **t2.medium**
* Create a key pair and save it as a `.pem` file in your local project directory
* Select default values for remaining arguments and click on launch instance.
* Wait for a couple of minutes for the instance to be launched successfully and then edit the inbound rules from the security tab of the instance to allow inbound traffic from your IP address. [Tutorials](https://www.youtube.com/results?search_query=edit+the+inbound+rules+ec2)

7. Now head on to the S3 web page and click on create bucket. Simply provide a unique name to the bucket and click on create bucket.<br>
There is an alternative way to create the bucket via the command line in your local development directory.

Pull up the command line and enter the following command<br>
`aws s3api create-bucket --bucket  {bucket_name} --region {region_name} --create-bucket-configuration LocationConstraint={region_name}`<br>
where `bucket_name` is the derired bucket name and `region_name` is the region where the account is present. You can find out your region name in the top right corner of the AWS console.

8. We need to upload both the scripts on the S3 bucket. You can either do it by the console or through the terminal via the following commands

`aws s3 cp etl_script.py s3://{bucket_name}/etl_script.py`<br>
`aws s3 cp airflow_dag.py s3://{bucket_name}/airflow_dag.py`<br>
`aws s3 cp requirements.txt s3://{bucket_name}/requirements.txt`<br>

Make sure you are in the same directory as the files otherwise specify the relative paths.

9. Connect to the EC2 instance using the `.pem` file saved earlier using SSH client. The command can be found on the EC2 console in the instances tab , click on the desired instance then on the Connect button.
Once successfully connected, run the following commands <br>
`sudo apt-get update`<br>
`sudo apt-get install python3-pip`<br>
`sudo pip install awscli`<br>

Configure the AWS user as done in step 5.

10. Copy the `requirements.txt` file from S3 to the instance using the command<br>
`aws s3 cp s3://{bucket_name}/requirements.txt ./`<br>
and the run  
`sudo pip install requirements.txt`

11. Run the `airflow` command to instantiate Airflow. Run the following commands to copy the scripts and create a DAG to run the script.<br>
`cd home/ubuntu/airflow/dags`<br>
`aws s3 cp s3://{bucket_name}/etl_script.py ./`<br>
`aws s3 cp s3://{bucket_name}/airflow_dag.py ./`<br>
`airflow db init`<br>
`airflow standalone`<br>
A login credential for Airflow webserver must have been generated after running the last command. Save them for the next step.

12. Now head on over to the EC2 console and click on the instance's networking tab and copy the `IPv4` address for the instance and paste it on a new tab and add the following at the end `:8080`. Login with the previously saved access credentials. 
Once you login successfully, click on the DAGs tab towards the left hand upper corner, you will see your DAG on the first place in the list of available DAGs. Click on it and then click on the run button on the right side to run the DAG. 
Monitor the status of the DAG and once it runs successfully, you will see a file `df.csv` stored in the S3 bucket.

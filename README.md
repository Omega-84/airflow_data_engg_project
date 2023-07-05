
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
##NOTE - The free tier instance **t2.micro** has just 1 GB of memory which is insufficient to run Airflow, we require a minimum of 4 GB to launch Airflow so we selected the cheapest option available i.e. **t2.medium**
* Create a key pair and save it as a `.pem` file in your local project directory
* Select default values for remaining arguments and click on launch instance.

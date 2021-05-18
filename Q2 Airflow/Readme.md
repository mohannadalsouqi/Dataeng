# CSV file to PostgreSQL then to MongoDB using airflow

<img src="https://upload.wikimedia.org/wikipedia/commons/d/de/AirflowLogo.png" width="300" alt="Apache Airflow"/>
<img src="https://webassets.mongodb.com/_com_assets/cms/MongoDB_Logo_FullColorBlack_RGB-4td3yuxzjs.png" width="300"  alt="Mongo DB"/>
<img src="https://cdn.iconscout.com/icon/free/png-256/postgresql-11-1175122.png" width="200" alt="PostgreSQL"/>


## About project

![enter image description here](https://i.ibb.co/9cF0nKp/Screen-Shot-2021-05-19-at-12-08-51-AM.png)
The goal of the project is to use airflow to build data pipline to transform data from CSV file to PostgreSQL table and from PostgreSQL to MongoDB .



## Project Content

2. Docker Compose File with run :
    * **Airflow** latest version 
    * **Jupyterlab** latest version
    * **Postgresql** latest version
    * **MongoDB** latest version
3. Generated Data file (**Data.csv**) which have this columns : 
    * **id** as Integer
    * **name** as String
    * **address** as String
    * **company** as String
    * **job_title** as String
    * **phone_number** as String
    * **created_date** as  Date
5. Airflow Dag file (**Q2.py**) which has the following processers:
    * **importdata** BashOperator
    * **load_postgresql** PythonOperator
    * **postgresqltojson** PythonOperator

## Getting Started

To build:
- Execute `docker-compose.yml` using Docker build the containers with following Command `docker-compose up`. 

To access airflow :
- Access airflow Interface using this url [http://localhost:8080/](http://localhost:8080/)
- Add **Q2.py** to **/opt/airflow/dags** on your local machine  
- Enable the **Q2_mohannad_alsouqi** Dag 
- Play the **Q2_mohannad_alsouqi** Dag using play button 

### Thanks

* Developed by with [Mohannad alsouqi](mailto:mohannad.alsouqi@gmail.com)

## Contributing

Feel free to use, extend, and tailor one for needs.

If you have pointers, new ideas, branch out and create a PR.

If you have any questions, message me or throw something in the issues.

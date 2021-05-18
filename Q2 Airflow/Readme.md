# CSV file to PostgreSQL using NIFI

<img src="https://cdn.iconscout.com/icon/free/png-256/postgresql-11-1175122.png" width="200" alt="Apache NiFi"/>
<img src="https://nifi.apache.org/assets/images/apache-nifi-logo.svg" width="300" height="110" alt="Apache NiFi"/>

## About project

![enter image description here](https://i.ibb.co/qpJXHC2/Screen-Shot-2021-05-18-at-6-29-38-PM.png)
The goal of the project is to use nifi to build data pipline to transform data from CSV file to PostgreSQL table .
in this 


## Project Content

1. Python Scripts folder:
    * CSV Data Generator Using Faker (**step_1_generate_data.ipynb**)
    * Postgresql table viewer (**step_2_data_validation.ipynb**)
2. Docker Compose File with run :
    * **Nifi** latest version 
    * **Jupyterlab** latest version
    * **Postgresql** latest version
3. Generated Data file (**Data.csv**) which have this columns : 
    * **id** as Integer
    * **name** as String
    * **address** as String
    * **company** as String
    * **job_title** as String
    * **phone_number** as String
    * **created_date** as  Date
5. Nifi Project template file (**CSV_to_Postgresql_database.xml**) which has the following processers:
    * **Get CSV File** Processer
    * **Add Schema Name Attribute** Processer
    * **PutSQL** Processer

## Requirements
* JDK 1.8 (*ongoing work to enable NiFi to run on Java 9/10/11; see [NIFI-5174](https://issues.apache.org/jira/browse/NIFI-5174)*)
* Apache Maven 3.1.1 or newer
* Git Client (used during build process by 'bower' plugin)

## Getting Started

To build:
- Execute `docker-compose.yml` using Docker build the containers with following Command `docker-compose up`. On a
- Execute `docker cp data.csv  psql_dataenv:/ ` to transfer data.cvs file to nifi dcoker container

To access nifi :
- Access Nifi Interface using this url [http://localhost:8080/nifi/](http://localhost:8080/nifi/)
- Import **CSV_to_Postgresql_database.xml** from Nifi interface   <img src="https://i.ibb.co/WgN9y9B/Screen-Shot-2021-05-18-at-6-51-32-PM.png" width="40" alt="Apache NiFi"/>  after that add template to nifi  <img src="https://i.ibb.co/ByQ79Lf/Screen-Shot-2021-05-18-at-6-55-33-PM.png" width="40" alt="Apache NiFi"/>
- Run the nifi flow using play button 
<img src="https://i.ibb.co/9wKWbg3/Screen-Shot-2021-05-18-at-6-48-29-PM.png" width="400" alt="Apache NiFi"/>

To Generate data, check the result & access Jupyterlab :
- Access Jupyterlab Interface using this url [http://localhost:8888/lab/](http://localhost:8888/lab/)
- Run step_1_generate_data.ipynb to generate new data.csv
- Run step_2_data_validation.ipynb to validate the postgresql record

### Thanks

* Developed by with [Mohannad alsouqi](mailto:mohannad.alsouqi@gmail.com)

## Contributing

Feel free to use, extend, and tailor one for needs.

If you have pointers, new ideas, branch out and create a PR.

If you have any questions, message me or throw something in the issues.
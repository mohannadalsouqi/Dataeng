#!/usr/bin/env python
# coding: utf-8

# In[1]:



import time
from pprint import pprint

from airflow import DAG
from airflow.operators.python import PythonOperator, PythonVirtualenvOperator
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
import psycopg2
from sqlalchemy import create_engine,Table, Column, Integer, String, MetaData,Date
import pandas as pd

args = {
    'owner': 'airflow',
}

with DAG(
    dag_id='Q2_mohannad_alsouqi',
    default_args=args,
    schedule_interval=None,
    start_date=days_ago(2),
    tags=['Dataeng'],
) as dag:

    # [START howto_operator_python]

    def load_postgresql(**kwargs):
        host="de_postgres" # use, 172.26.0.2, "localhost" if you access from outside the localnet decompose env 
        database="psql_data_environment"
        user="psql_user"
        password="psql"
        port='5432'
        engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')
        tablename="client_list"
        rdf = pd.read_sql_table(
            tablename,
            con=engine
        )
        return 'Load PostgreSQL done'

    run1 = PythonOperator(
        task_id='load_postgresql',
        python_callable=load_postgresql,
    )
    # [END howto_operator_python]
    def postgresqltojson(**kwargs):

        return 'Load postgresqltojson done'

    run2 = PythonOperator(
        task_id='postgresqltojson',
        python_callable=postgresqltojson,
    )
    def postgresqltojson1(**kwargs):

        return 'Load postgresqltojson2 done'

    run3 = PythonOperator(
        task_id='postgresqltojson1',
        python_callable=postgresqltojson1,
    )
    run1 >> run2
    run2 >> run3
    # [END howto_operator_python]


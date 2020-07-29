from datetime import datetime, timedelta
import os
import configparser
from airflow import DAG
from operators import AddConnectionOperator

config = configparser.ConfigParser()
config.read('aws.cfg')

KEY                = config.get('AWS','KEY')
SECRET             = config.get('AWS','SECRET')

default_args = {
    'owner': 'franksloan',
    'start_date': datetime(2019, 7, 27),
    'depends_on_past': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG('workflow_dag',
          default_args=default_args,
          description='Capstone project with Redshift with Airflow',
          schedule_interval='0 * * * *',
          catchup=False
        )

add_redshift_connection = AddConnectionOperator(
    task_id='add_redshift_connection',
    dag=dag,
    conn_id='aws_credentials',
    conn_type='Amazon Web Services',
    login=KEY,
    password=SECRET
)

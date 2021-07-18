# from airflow.providers.google.cloud.transfers.gcs_to_local import GCSToLocalFilesystemOperator
from airflow.providers.google.cloud.hooks.gcs import GCSHook
from airflow.utils.dates import days_ago
from airflow.models import Variable
from airflow.models import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow.contrib.operators import dataproc_operator
from airflow.contrib.hooks.bigquery_hook import BigQueryHook
import pendulum
import json

# get the standard UTC time 
local_tz = pendulum.timezone("America/Lima")
print(local_tz)
args={
    'owner': 'djaimes',
    'start_date': datetime(2021, 7, 17, tzinfo=local_tz)
}

dag = DAG(dag_id='ML_covid_infected', default_args=args, schedule_interval=None)

with dag:

    # Loader Poliza_cobertura
    pyspark_ml_perceptron = BashOperator(
        task_id='pyspark_ml_perceptron',
        bash_command="python /opt/airflow/sparkFiles/multilayer_perceptron_classification.py"
    )

    pyspark_ml_perceptron

    
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta


def print_hello():
    print("Hello from Apache Airflow!")


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2025, 12, 5),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="print_hello_dag",
    default_args=default_args,
    description="lalalal",
    schedule_interval=timedelta(days=1),  # veya schedule="@daily"
    catchup=False,
) as dag:

    hello_task = PythonOperator(
        task_id="print_hello_task",
        python_callable=print_hello,
    )

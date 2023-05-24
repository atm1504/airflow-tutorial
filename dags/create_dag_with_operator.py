from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'atm1504',
    'retries': 5,
    'retry_delay': timedelta(minutes=1)
}


def greet(name, age):
    print("Hello devyani tu kitni pagal hain!")
    print(f"Kya re {name}, kinti badi ho gayi re tu {age} saal ki hogayi")


def get_name():
    return "atm"


with DAG(
    dag_id='our_dag__with_python_operator_v3',
    default_args=default_args,
    description='dag using python operator',
    start_date=datetime(2023, 5, 24),
    schedule_interval='@daily'
) as dag:
    # task1 = PythonOperator(
    #     task_id='first_task',
    #     python_callable=greet,
    #     op_kwargs={
    #         'name': 'Devyani',
    #         'age': 22
    #     }
    # )
    task2 = PythonOperator(
        task_id='get_name',
        python_callable=get_name
    )
    task2

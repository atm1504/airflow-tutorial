from airflow.decorators import dag, task
from datetime import datetime, timedelta


default_args = {
    'owner': 'atm1504',
    'retries': 5,
    'retry_delay': timedelta(minutes=1)
}


@dag(
    dag_id='our_dag__with_python_taskflow_v1',
    default_args=default_args,
    description='dag using decorators',
    start_date=datetime(2023, 5, 24),
    schedule_interval='@daily'
)
def hello_world_etl():

    @task()
    def get_name():
        return "Dusht"

    @task()
    def get_age():
        return 19

    @task()
    def greet(name, age):
        print(f"Kya re {name}, kinti badi ho gayi re tu {age} saal ki hogayi")

    name = get_name()
    age = get_age()
    greet(name=name, age=age)


greet_dag = hello_world_etl()

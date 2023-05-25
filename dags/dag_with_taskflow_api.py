from airflow.decorators import dag, task
from datetime import datetime, timedelta


default_args = {
    'owner': 'atm1504',
    'retries': 5,
    'retry_delay': timedelta(minutes=1)
}


@dag(
    dag_id='our_dag__with_python_taskflow_v2',
    default_args=default_args,
    description='dag using decorators',
    start_date=datetime(2023, 5, 24),
    schedule_interval='@daily'
)
def hello_world_etl():

    # @task()
    # def get_name():
    #     return "Dusht"

    @task(multiple_outputs=True)
    def get_name():
        return {
            "first_name": "Jerry",
            "last_name": 'Tom'
        }

    @task()
    def get_age():
        return 19

    @task()
    def greet(first_name, last_name, age):
        print(
            f"Kya re {first_name} {last_name}, kinti badi ho gayi re tu {age} saal ki hogayi")

    name_dict = get_name()
    age = get_age()
    greet(first_name=name_dict['first_name'],
          last_name=name_dict['last_name'], age=age)


greet_dag = hello_world_etl()

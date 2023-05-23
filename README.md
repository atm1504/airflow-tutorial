# airflow-tutorial

Sample tutorial repo for apache airflow for running in docker locally.


## Steps

Doc link: https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html

* curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.6.1/docker-compose.yaml'
* mkdir -p ./dags ./logs ./plugins ./config
* docker compose up airflow-init
* docker compose up -d

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

from news.news_task import NewsTask
from settings import AIRFLOW_ERROR_EMAIL


default_args = {
    'owner': 'Josh Cadruvi',
    'depends_on_past': False,
    'start_date': datetime(2015, 6, 1),
    'email': [AIRFLOW_ERROR_EMAIL],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG('news', default_args=default_args, schedule_interval=timedelta(1))

#t1, t2 and t3 are examples of tasks created by instantiating operators
t0 = PythonOperator(
    task_id="test_hive",
    python_callable=NewsTask().show_table,
    provide_context=True,
    dag=dag
)

t1 = BashOperator(
    task_id='test_spark',
    bash_command='/usr/local/lib/python2.7/site-packages/pyspark/bin/spark-submit --master local[4] /usr/local/airflow/data_pipeline/spark/simple_app.py',
    dag=dag)

t2 = BashOperator(
    task_id='sleep',
    bash_command='sleep 5',
    retries=3,
    dag=dag)

templated_command = """
    {% for i in range(5) %}
        echo "{{ ds }}"
        echo "{{ macros.ds_add(ds, 7)}}"
        echo "{{ params.my_param }}"
    {% endfor %}
"""

t3 = BashOperator(
    task_id='templated',
    bash_command=templated_command,
    params={'my_param': 'Parameter I passed in'},
    dag=dag)

t1.set_upstream(t0)
t2.set_upstream(t1)
t3.set_upstream(t1)

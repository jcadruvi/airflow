# data_pipeline
This is the code for the data pipelines.

Airflow can be found at: http://localhost:8080/
Hue can be found at: http://localhost:8888/
Login for cloudera quickstart:
    username: cloudera
    password: cloudera

In Order to start this project do the following:

1) Open command line and browse to this folder.
2) run: docker-compose up
3) Once this finishes browse to http://localhost:8080/ to verify Airflow server is up and running.
4) Browse to http://localhost:8080/admin/connection/
5) Edit the hiveserver2_default configuration setting to the following:

    Host: cloudera
    Port: 10000
    Login: cloudera
    Password: cloudera

6) In order to bash into Airflow run: docker exec -ti airflow bash
7) Run: airflow list_dags
   This should show several dags.
8) Know you can run airflow commands.

SPARK_HOME locally is /usr/local/lib/python2.7/site-packages/pyspark/bin
Submit Spark job:
    /usr/local/lib/python2.7/site-packages/pyspark/bin/spark-submit --master local[4] spark/simple_app.py
Another alternative
    python spark/simple_app.py

Docker Commands:

    How to connect as root user:
        docker exec -ti --user root airflow bash


Can't connect to clouders:10000 try to do the following:

sudo service hive-metastore start
sudo service hive-server2 start

sudo service hadoop-hdfs-datanode stop
sudo service hadoop-hdfs-datanode start

sudo service hue stop
sudo service hue start


Good Cloudera Quickstart VM Documentation:
    https://www.cloudera.com/documentation/enterprise/5-5-x/PDF/cloudera-quickstart.pdf
    https://www.cloudera.com/documentation/enterprise/5-12-x/PDF/cloudera-quickstart.pdf

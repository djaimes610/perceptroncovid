## Installation

Start the installation with:

	1- docker-compose pull
    2- docker-compose up -d

This command will pull and create Docker images and containers for Airflow, according to the instructions in the [docker-compose.yml] file:

<p align="center"><img src=https://user-images.githubusercontent.com/19210522/114414670-b43ab980-9bb7-11eb-8ea8-061385b14980.gif></p>

After everything has been installed, you can check the status of your containers (if they are healthy) with:

    docker ps

**Note**: it might take up to 30 seconds for the containers to have the **healthy** flag after starting.

<p align="center"><img src=https://user-images.githubusercontent.com/19210522/114403953-ed6e2c00-9bad-11eb-9e6e-8f85d7fced2e.png></p>


## Airflow Interface

You can now access the Airflow web interface by going to http://localhost:8080/. If you have not changed them in the docker-compose.yml file, the default user is **airflow** and password is **airflow**:

<p align="center"><img src=https://user-images.githubusercontent.com/19210522/114421290-d5060d80-9bbd-11eb-842e-13a244996200.png></p>

After signing in, the Airflow home page is the DAGs list page. Here you will see all your DAGs and the Airflow example DAGs, sorted alphabetically. 

Any DAG python script saved in the directory [**dags/**](https://github.com/renatootescu/ETL-pipeline/tree/main/dags), will show up on the DAGs page (e.g. the first DAG, `analyze_json_data`, is the one built for this project).

**Note**: If you update the code in the python DAG script, the airflow DAGs page has to be refreshed

**Note**: If you do not want to see any Airflow example dags, se the `AIRFLOW__CORE__LOAD_EXAMPLES:` flag to `False` in the [docker-compose.yml](https://github.com/renatootescu/ETL-pipeline/blob/main/docker-compose.yml) file before starting the installation.

<p align="center"><img src=https://user-images.githubusercontent.com/19210522/114454069-dbf34700-9be2-11eb-8040-f57407adf856.png></p>

Click on the name of the dag to open the DAG details page:

<p align="center"><img src=https://user-images.githubusercontent.com/19210522/114457291-8882f800-9be6-11eb-9090-1f45af9f92ea.png></p>

On the Graph View page you can see the dag running through each task (`getLastProcessedDate`, `getDate`, etc) after it has been unpaused and trigerred:

<p align="center"><img src=https://user-images.githubusercontent.com/19210522/114459521-50c97f80-9be9-11eb-907a-3627a21d52dc.gif></p>


## Pipeline Task by Task

#### Task `ML_covid_infected`

Activar el DAG ML_covid_infected, luego ejecutarlo para que pueda procesar la información del archivo multilayer_perceptron_classification.py situado en la ruta
"sparkFiles/"


## Shut Down and Restart Airflow

If you want to make changes to any of the configuration files [docker-compose.yml](https://github.com/renatootescu/ETL-pipeline/blob/main/docker-compose.yml), [Dockerfile](https://github.com/renatootescu/ETL-pipeline/blob/main/Dockerfile), [requirements.txt](https://github.com/renatootescu/ETL-pipeline/blob/main/requirements.txt) you will have to shut down the Airflow instance with:

    docker-compose down
    
This command will shut down and delete any containers created/used by Airflow.

For any changes made in the configuration files to be applied, you will have to rebuild the Airflow images with the command:

    docker-compose build

Recreate all the containers with:

    docker-compose up -d


## Learning Resources

These are some useful learning resources for anyone interested in Airflow and Spark:

 - [Apache Airflow Documentation](https://airflow.apache.org/docs/apache-airflow/stable/index.html)
 - [Spark by examples](https://sparkbyexamples.com/pyspark-tutorial/)
 - [DataScience Made Simple](https://www.datasciencemadesimple.com/pyspark-string-tutorial/)
 - [Marc Lambreti](https://marclamberti.com/)
 - [Medium](https://medium.com/@itunpredictable/apache-airflow-on-docker-for-complete-beginners-cf76cf7b2c9a)
 - [Towards Data Science](https://towardsdatascience.com/getting-started-with-airflow-using-docker-cd8b44dbff98)
 - [Precocity](https://precocityllc.com/blog/airflow-and-xcom-inter-task-communication-use-cases/)
 - [Databricks](https://databricks.com/blog/2015/07/15/introducing-window-functions-in-spark-sql.html)

## License
You can check out the full license [here](https://github.com/renatootescu/ETL-pipeline/blob/main/LICENSE)

This project is licensed under the terms of the **MIT** license.

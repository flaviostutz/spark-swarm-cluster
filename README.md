# spark-swarm-cluster
Spark running over Swarm Cluster.

## Usage

docker-compose.yml

```
version: '3.3'

services:

  spark-master:
    image: bde2020/spark-master:2.3.0-hadoop2.7
    ports:
      - "8080:8080"
      - "7077:7077"
    environment:
      - INIT_DAEMON_STEP=setup_spark
    networks:
      - spark

  spark-worker:
    image: bde2020/spark-worker:2.3.0-hadoop2.7
    environment:
      - "SPARK_MASTER=spark://spark-master:7077"
    networks:
      - spark

networks:
  spark:

  
```

* Start Spark cluster using Swarm with

  * ```docker stack deploy spark-cluster -c docker-compose.yml```

* Scale Spark workers

  * ```docker service scale spark-cluster_spark-worker=3```

* Open http://localhost:8080 and check if the master node is running and 3 workers are registered

* Submit a Spark job

docker-compose.yml
```
version: '3.3'

services:

  spark-sample:
    build: .
    image: spark-sample
    environment:
      - SPARK_MASTER_NAME=spark-master

networks:
  default:
    external:
      name: spark-swarm-cluster_spark

```

* Launch a single instance of a sample job
  * ```cd spark-sample```
  * run ```docker-compose up```
  * check for results at http://localhost:8080

* Launch 3 parallel instances of the sample job
  * run ```docker-compose up --build --scale spark-sample=3```
  * check for results at http://localhost:8080


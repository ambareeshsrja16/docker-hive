# docker-trino-fed

Bring up docker containers with Trino to run federated queries on Elastic and Druid instances.
## Services

 1. [Trino](https://hub.docker.com/r/trinodb/trino)
 2. [Hive](https://github.com/big-data-europe/docker-hive)
 3. [Elastic + Kibana](https://www.elastic.co/guide/en/kibana/current/docker.html)
 4. [Druid](https://druid.apache.org/docs/latest/tutorials/docker.html)

## Steps

 1. Bring up services
    * For only Trino, run `docker-compose up -d`
    * For services in addition to Trino use appropriate `profile` options:
        -   `elastic`
        -   `druid`
        -   `hdfs`

    Examples: </br>
        Trino + Elastic + Druid: `docker-compose --profile elastic --profile druid up -d` </br>
        Trino + Elastic + HDFS : `docker-compose --profile elastic --profile hdfs up -d` </br>

    Check containers `docker ps -a`. </br>
    When all profiles are used, these containers will be up `docker ps -a --format '{{.Names}}' | sort` :

    > broker </br>
    > coordinator </br>
    > datanode </br>
    > elastic </br>
    > historical </br>
    > hive-metastore </br>
    > hive-metastore-postgresql </br>
    > hive-server </br>
    > kibana </br>
    > middlemanager </br>
    > namenode </br>
    > postgres </br>
    > router </br>
    > trino </br>
    > zookeeper </br>

 2. Check all services from their UIs:

    > Trino: https://< IP >:8080 </br>
    > Elastic/Kibana: https://< IP >:5601 </br>
    > Druid: https://< IP >:8889 </br>

    Note: Druid Router is mapped to 8889 on the container. Reconfigure any port, if need be, from `docker-compose.yml`.

3.  Add sample data to Elastic and Druid from their UIs and try querying. For e.g: </br>

    > SELECT dayofweek, flags FROM elasticsearch.default.kibana_sample_data_flights, druid.druid.wikipedia

4.  To stop and remove all containers:

    > docker-compose down

## Notes:

 - Druid related docker containers are marked with `#druid related` in
   `docker-compose.yml` and can be commented out if not needed.
 - Download [Trino-cli](https://trino.io/docs/current/installation/cli.html) for  Step 3
 - For sudo access to Trino container `docker exec -u 0 -it trino /bin/bash`
      - Trino logs are at `/data/trino/var/log/`
 - Versions for base docker images can be configured at `docker-compose.yml`. But for the Trino instance it has to be configured at `trino_docker/Dockerfile`
 - To connect a separate instance of Trino (say from an IDE), add `*.properties` files similar to ones under `trino_docker/` and replace relevant fields with correct IPs.
    - If running the full server as described [here](https://github.com/trinodb/trino), add `*.properties` files to `/trino/testing/trino-server-dev/etc/catalog/` and make sure `plugin.bundles` in `/trino/testing/trino-server-dev/etc/config.properties` contains the corresponding `pom.xml` files


Forked off [docker-hive](https://github.com/big-data-europe/docker-hive)

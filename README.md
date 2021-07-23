# docker-trino-fed

Bring up docker containers with trino to run federated queries on elastic and druid instances.
## Services

 1. [trino](https://hub.docker.com/r/trinodb/trino)
 2. [hive](https://github.com/big-data-europe/docker-hive)
 3. [elastic + kibana](https://www.elastic.co/guide/en/kibana/current/docker.html)
 4. [druid](https://druid.apache.org/docs/latest/tutorials/docker.html)

## Steps

 1. Run `docker-compose up -d`

    Check containers  `docker ps -a`.
    Specifically these containers will be up `docker ps -a --format '{{.Names}}' | sort` :


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


 2. Check if all services are functioning from their UIs:

    > trino: https://< IP >:8080 </br>
    > elastic/kibana: https://< IP >:5601 </br>
    > druid: https://< IP >:8889 </br>

    Note: Druid Router has been remapped to 8889 on the container. Reconfigure any port, if need be, from `docker-compose.yml`.

3.    Add sample data for elastic and druid from their UIs and try querying. For e.g: </br>
 `SELECT dayofweek, flags FROM elasticsearch.default.kibana_sample_data_flights, druid.druid.wikipedia`


## Notes:

 - Druid related docker containers are marked with `#druid related` in
   `docker-compose.yml` and can be commented out if not needed.
  - Download [trino-cli](https://trino.io/docs/current/installation/cli.html) for  Step 3
  - For sudo access to trino container `docker exec -u 0 -it trino /bin/bash`
      - Trino logs are at `/data/trino/var/log/`
   - Versions for base docker images can be configured at `docker-compose.yml`. But for the trino instance it has to be configured at `trino_docker/Dockerfile`
   - To connect a separate instance of trino (say from an IDE), add *.properties similar to ones under `trino_docker/` and replace relevant fields with correct IPs.
       - If running the full server as described [here](https://github.com/trinodb/trino), add *.properties files to `/trino/testing/trino-server-dev/etc/catalog/` and make sure `plugin.bundles` in `/trino/testing/trino-server-dev/etc/config.properties` contains the corresponding `pom.xml` files



Forked off [docker-hive](https://github.com/big-data-europe/docker-hive)

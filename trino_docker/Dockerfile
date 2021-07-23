FROM trinodb/trino:353

# To enable catalog connections to {elastic, druid ...}
COPY ./*.properties /etc/trino/catalog/

# To enable server log in trino container
RUN echo "log.path=var/log/server.log" >> /etc/trino/config.properties

WORKDIR /etc/trino

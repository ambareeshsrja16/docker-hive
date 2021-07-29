FROM trinodb/trino:353

# To enable catalog connections to {elastic, druid ...}
COPY ./elasticsearch.properties /etc/trino/catalog/
COPY ./druid.properties /etc/trino/catalog/

# Config file with https enabled
COPY ./config.properties /etc/trino/config.properties

# Copy PEM-encoded TLS certificate
COPY ./clustercoord.pem /etc/trino/clustercoord.pem

# Copy password-authenticator file
COPY ./password-authenticator.properties /etc/trino/password-authenticator.properties

# Copy password file
COPY ./password.db /etc/trino/password.db

WORKDIR /etc/trino

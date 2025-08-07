FROM mysql:9.0
COPY ./create_table.sql /docker-entrypoint-initdb.d/init.sql
EXPOSE 3306

CMD ["mysqld"]
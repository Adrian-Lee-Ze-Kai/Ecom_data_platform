FROM postgres:18

# SQL files in this folder run automatically on first startup, in alphabetical order
COPY sql/ /docker-entrypoint-initdb.d/
COPY data/ /data/
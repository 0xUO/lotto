export MYSQL_ROOT_PASSWORD
export SECRET_KEY
docker stack deploy --compose-file docker-compose.yaml lotto-stack
docker service update --replicas 3 lotto-stack_front-end
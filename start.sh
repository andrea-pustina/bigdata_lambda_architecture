# Stop and delete all docker containers
#docker stop $(docker ps -a -q)
#docker system prune -a --force

#sudo docker-compose exec stream_generator bash

docker-compose down
#docker-compose build
docker-compose up -d

# add cluster in kafka-manager
printf 'waiting to kafka-manager\n'
until $(curl --output /dev/null --silent --head --fail http://localhost:9000); do
    printf '.'
    sleep 5
done
curl localhost:9000/clusters --data 'name=localCluster&zkHosts=zookeeper%3A2181&kafkaVersion=0.9.0.1&jmxEnabled=true&logkafkaEnabled=true&pollConsumers=true&jmxUser=&jmxPass=&tuning.brokerViewUpdatePeriodSeconds=30&tuning.clusterManagerThreadPoolSize=2&tuning.clusterManagerThreadPoolQueueSize=100&tuning.kafkaCommandThreadPoolSize=2&tuning.kafkaCommandThreadPoolQueueSize=100&tuning.logkafkaCommandThreadPoolSize=2&tuning.logkafkaCommandThreadPoolQueueSize=100&tuning.logkafkaUpdatePeriodSeconds=30&tuning.partitionOffsetCacheTimeoutSecs=5&tuning.brokerViewThreadPoolSize=2&tuning.brokerViewThreadPoolQueueSize=1000&tuning.offsetCacheThreadPoolSize=2&tuning.offsetCacheThreadPoolQueueSize=1000&tuning.kafkaAdminClientThreadPoolSize=2&tuning.kafkaAdminClientThreadPoolQueueSize=1000' -X POST > /dev/null


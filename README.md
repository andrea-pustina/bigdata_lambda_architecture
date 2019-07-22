kafka ui	localhost:9000/
hdfs ui 	localhost:8088/home
storm ui	localhost:8085/
spark notebook 	localhost:8888/
spark master	localhost:8080/
spark worker 1	localhost:8081/
spark worker 2	localhost:8082/



# Stop and delete all docker containers
#docker stop $(docker ps -a -q)
#docker system prune -a --force


#sudo docker stop $(sudo docker ps -a -q)
#sudo docker rm $(sudo docker ps -a -q)

# docker exec -it namenode bash
#sudo docker-compose exec stream_generator bash
#sudo docker-compose exec storm_py bash


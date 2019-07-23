See pdf

# Stop and delete all docker containers
#docker stop $(docker ps -a -q)
#docker system prune -a --force


#sudo docker stop $(sudo docker ps -a -q)
#sudo docker rm $(sudo docker ps -a -q)

# docker exec -it namenode bash
#sudo docker-compose exec stream_generator bash

# to delete less important volumes
#sudo rm -R gobblin/logs/ gobblin/work-dir/ hadoop/data/ storm_ssh/supervisor_log/


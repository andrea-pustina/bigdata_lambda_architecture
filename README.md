kafka ui	localhost:9000/
hdfs ui 	localhost:8088/home
storm ui	localhost:8085/
spark notebook 	localhost:8888/
spark master	localhost:8080/
spark worker 1	localhost:8081/
spark worker 2	localhost:8082/


download ad extract dataset into stream_generator/py/data
cd bigdata_lambda_architecture/stream_generator/py
python3 sort_dataset.py
cd bigdata_lambda_architecture
sudo ./start.sh
docker-compose down



# Stop and delete all docker containers
#docker stop $(docker ps -a -q)
#docker system prune -a --force


#sudo docker stop $(sudo docker ps -a -q)
#sudo docker rm $(sudo docker ps -a -q)

# docker exec -it namenode bash
#sudo docker-compose exec stream_generator bash
#sudo docker-compose exec storm_py bash



# to delete less important volumes
#sudo rm -R gobblin/logs/ gobblin/work-dir/ hadoop/data/ storm_ssh/supervisor_log/


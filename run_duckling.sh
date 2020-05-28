docker rm -f $(docker ps -qa)
nohup docker run -p 8000:8000 --name=duckling rasa/duckling > rasa_duckling.log 2>&1 &

train:
	rasa train --domain domain.yml --data data --config config.yml --out models -vv

train-nlu:
	rasa train nlu -u data/nlu -c config.yml --out models/nlu

run:
	rasa run actions --actions actions & 
	rasa run --endpoints endpoints.yml --enable-api -m models --debug

run-nlu:
	rasa run --enable-api -m models/nlu

run-cmdline:
	rasa run actions --actions actions & 
	rasa shell --endpoints endpoints.yml -m models --debug

run-graph:
	rasa visualize --domain domain.yml --stories data/core --config config.yml --nlu data/nlu

run-x:
	rasa run actions --actions actions &
	rasa x -m models --endpoints endpoints.yml

validate:
	rasa data validate

visualize:
	rasa visualize -d domain.yml -s data/core/stories.md  -c config.yml --out graph.html

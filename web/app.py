import yaml
from src import server

if __name__ == '__main__':
	# read config
	stream = open("config.yaml", "r")
	docs = yaml.load_all(stream)
	config = {}

	for doc in docs:
		for k,v in doc.items():
			config[k] = {}

			for m, n in v.items():
				config[k][m] = n

	print "Starting server"
	server.init(config)

.PHONY : start stop logs flush init

.DEFAULT_GOAL := start

start:
	docker-compose up -d

stop:
	docker-compose stop

logs:
	docker-compose logs -f

init:
	cp .env.example .env

flush:
	docker-compose down -v --rmi all
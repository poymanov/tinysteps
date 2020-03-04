.PHONY : start stop logs flush init init_env migrate

.DEFAULT_GOAL := start

init_env:
	cp .env.example .env

migrate:
	docker-compose run web flask db upgrade

start:
	docker-compose up -d

stop:
	docker-compose stop

logs:
	docker-compose logs -f

flush:
	docker-compose down -v --rmi all

init: init_env migrate
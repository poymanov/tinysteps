.PHONY : start stop logs flush

.DEFAULT_GOAL := start

start:
	docker-compose up -d

stop:
	docker-compose stop

logs:
	docker-compose logs -f

flush:
	docker-compose down -v --rmi all
COMPOSE ?= docker-compose
all up:
	$(COMPOSE) up -d

stop:
	$(COMPOSE) stop

view_redis_dockerfile:
	curl https://raw.githubusercontent.com/docker-library/redis/master/3.0/Dockerfile

inspect_volumes:
	docker inspect 0_redis_1
	@echo --------------------
	@echo --------------------
	docker inspect 0_redis_1 | grep -A1 -E '(^    "Volumes":)|(Cmd)'

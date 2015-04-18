COMPOSE ?= docker-compose
all up:
	$(COMPOSE) up -d

stop:
	$(COMPOSE) stop

inspect_volumes:
	docker inspect 0_redis_1
	@echo --------------------
	@echo --------------------
	docker inspect 0_redis_1 | grep -A1 -E '(^    "Volumes":)|(Cmd)'

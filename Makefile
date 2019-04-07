IMAGE_NAME=walli-api
CONTAINER_NAME=testing-walli-api
DOCKER_BUILD_CONTEXT=.
DOCKER_FILE_PATH=./tests/docker/Dockerfile

SHELL=/bin/bash

.PHONY: build-test tests

build-test:
	docker build $(DOCKER_BUILD_ARGS) -t $(IMAGE_NAME) $(DOCKER_BUILD_CONTEXT) -f $(DOCKER_FILE_PATH)

run-test:
	docker run -d --privileged -p 54310:8080 $(IMAGE_NAME)
	
tests:
	pytest --rootdir tests

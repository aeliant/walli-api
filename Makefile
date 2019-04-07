IMAGE_NAME=walli-api
CONTAINER_NAME=testing-walli-api
DOCKER_BUILD_CONTEXT=.
DOCKER_FILE_PATH=./tests/docker/Dockerfile

SHELL=/bin/bash

.PHONY: build-test run-test tests tests-all tests-filter tests-mangle tests-raw
	tests-nat tests-security

build-test:
	docker build $(DOCKER_BUILD_ARGS) -t $(IMAGE_NAME) $(DOCKER_BUILD_CONTEXT) -f $(DOCKER_FILE_PATH)

run-test:
	docker run -d --privileged -p 54310:8080 $(IMAGE_NAME)

tests: tests-all tests-filter tests-mangle tests-raw tests-nat tests-security

tests-all:
	pytest -m all_table

tests-filter:
	pytest -m filter_table

tests-mangle:
	pytest -m mangle_table

tests-raw:
	pytest -m raw_table

tests-nat:
	pytest -m nat_table

tests-security:
	pytest -m security_table

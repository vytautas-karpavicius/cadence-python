all: git-submodules protoc run

git-submodules:
	git submodule update --init --recursive

PROTO_IN = idls/proto
PROTO_OUT = .
PROTO_FILES = $(shell find ./$(PROTO_IN) -name "*.proto")

protoc:
	mkdir -p $(PROTO_OUT)
	python -m grpc_tools.protoc \
		-I=$(PROTO_IN) \
		--python_out=$(PROTO_OUT) \
		--grpc_python_out=$(PROTO_OUT) \
		$(PROTO_FILES)

	find uber -type d -exec sh -c 'touch {}/__init__.py' \;

run:
	python helloworld.py

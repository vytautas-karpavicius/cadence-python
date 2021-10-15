# Cadence python example

This is a minimal example for [Cadence](https://github.com/uber/cadence) client in python. It generates gRPC bindings and uses them start [helloworld](https://github.com/uber-common/cadence-samples/tree/master/cmd/samples/recipes/helloworld) Cadence sample.

## Prerequisites
### 1. Start Cadence server locally
Follow https://github.com/uber/cadence/blob/master/docker/README.md

### 2. Install Cadence CLI
```
brew install cadence-workflow
```
More info: https://cadenceworkflow.io/docs/cli/

### 3. Register samples domain
```
cadence --domain samples-domain domain register
```

### 3. Running helloworld worker
You will need to checkout [cadence-samples](https://github.com/uber-common/cadence-samples) and start helloword worker:
```
git clone git@github.com:uber-common/cadence-samples.git cadence-samples
cd cadence-samples
make helloworld
./bin/helloworld -m worker
```


## Running the example
### 1. Setup virtual env
```
source setup-env.sh
```

### 2. Run the example
```
make
```

### 3. Observe the workflow
```
http://localhost:8088/domains/samples-domain
```

import array
import grpc
import uuid
from google.protobuf.duration_pb2 import Duration
from uber.cadence.api.v1 import common_pb2
from uber.cadence.api.v1 import tasklist_pb2
from uber.cadence.api.v1 import service_workflow_pb2
from uber.cadence.api.v1 import service_workflow_pb2_grpc


# Headers required by YARPC: https://github.com/yarpc/yarpc-go/blob/master/transport/grpc/headers.go
metadata = (
    ('rpc-service', 'cadence-frontend'),
    ('rpc-caller', 'python-example'),
    ('rpc-encoding', 'proto'),
)

with grpc.insecure_channel('localhost:7833') as channel:
    workflowAPI = service_workflow_pb2_grpc.WorkflowAPIStub(channel)

    startRequest = service_workflow_pb2.StartWorkflowExecutionRequest(
        domain='samples-domain',
        workflow_id=str(uuid.uuid4()),
        workflow_type=common_pb2.WorkflowType(name='helloWorldWorkflow'),
        task_list=tasklist_pb2.TaskList(name='helloWorldGroup'),
        execution_start_to_close_timeout=Duration(seconds=60),
        task_start_to_close_timeout=Duration(seconds=60),
        request_id=str(uuid.uuid4()),
        input=common_pb2.Payload(data='"python example"')
        )

    response = workflowAPI.StartWorkflowExecution(request=startRequest, metadata=metadata, timeout=10)
    print(response)

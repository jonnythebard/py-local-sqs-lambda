from aws_cdk import (
    Stack,
    aws_sqs as sqs,
    aws_lambda,
    aws_lambda_event_sources as sources
)
from constructs import Construct


class DeployLocalStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        queue = sqs.Queue(
            self,
            id="DeployLocalQueue",
            queue_name="local-queue"
        )

        handler = aws_lambda.Function(
            self,
            id="DeployLocalLambda",
            runtime=aws_lambda.Runtime.PYTHON_3_8,
            function_name='local-lambda',
            code=aws_lambda.Code.from_asset("../src"),
            handler="lambda_function.lambda_handler"
        )
        handler.add_event_source(sources.SqsEventSource(queue))

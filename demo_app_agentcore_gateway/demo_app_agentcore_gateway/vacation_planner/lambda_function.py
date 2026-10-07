import boto3
import json
import uuid

client = boto3.client('bedrock-agentcore', region_name='us-west-2')

AGENT_RUNTIME_ARN = 'arn:aws:bedrock-agentcore:us-west-2:196715057542:runtime/hosted_agent_ms9gz_test_gateway-nmWRoF2Gz3'

def lambda_handler(event, context):
    topic = event.get('topic', 'Plan a 7-day vacation to New York')
    session_id = event.get('sessionId', str(uuid.uuid4()) + str(uuid.uuid4()))[:33]

    payload = json.dumps({"topic": topic})

    response = client.invoke_agent_runtime(
        agentRuntimeArn=AGENT_RUNTIME_ARN,
        runtimeSessionId=session_id,
        payload=payload
    )

    response_body = response['response'].read()
    response_data = json.loads(response_body)

    return {
        'statusCode': 200,
        'body': json.dumps(response_data)
    }

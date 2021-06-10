import boto3, json, os, logging
import botocore.exceptions

def startConnectOutboundCall(contactFlowId, destinationPhoneNum, sourcePhoneNum, queueId, custAttributes, connectInstance):
    connect_client = boto3.client('connect')
    response = connect_client.start_outbound_voice_contact(
        DestinationPhoneNumber=destinationPhoneNum,
        ContactFlowId=contactFlowId,
        InstanceId=connectInstance,
        # ClientToken='string',
        SourcePhoneNumber=sourcePhoneNum,
        QueueId=queueId,
        Attributes=custAttributes
    )
    return response
    
def lambda_handler(event, context):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    print('Event: %s' % json.dumps(event))
    print('First Name: %s' % json.dumps(event['currentIntent']['slots']['CustomerFirsName']))
    print('Phone Number: %s' % json.dumps(event['currentIntent']['slots']['CustomerPhoneNumber']))
    # places call, and gets vars from lambda environment variables for os.environ
    callResponse = startConnectOutboundCall(os.environ['callFlowId'], event['currentIntent']['slots']['CustomerPhoneNumber'], os.environ['connectSourcePhoneNumber'], os.environ['connectQueueId'], event['currentIntent']['slots'], os.environ['connectInstanceId'])
    return {
        'statusCode': 200,
        'body': json.dumps('Success')
    }
import boto3
import time

# dynamo_client = boto3.client('dynamodb')
dynamo_client = boto3.Session(region_name='us-east-1').client('dynamodb')


def get_all(table):
    return dynamo_client.scan(
        TableName=table
        )

def create_table(table):
        response = dynamo_client.create_table(
            AttributeDefinitions=[{
                'AttributeName': 'event',
                'AttributeType': 'S'
            }
    # , 
	# {
     #additional keys can be added here
	# 	'AttributeName': 'timestamp', 
	# 	'AttributeType': 'S'
	# }
            ], 
                TableName=table, 
                KeySchema=[{
                    'AttributeName': 'event', 
                    'KeyType': 'HASH'
	}
    # , 
	# {
	# 	'AttributeName': 'timestamp', 
	# 	'KeyType': 'RANGE'
	# }
    ]
            , 
            ProvisionedThroughput={
                'ReadCapacityUnits': 1, 
                'WriteCapacityUnits': 2
            }
      )
        time.sleep(5)
        put_item(table)
        return response

def put_item(table):
    dynamo_client.put_item(
    TableName=table,
    Item={
        'event': {'S': 'gaming_nationals_zaf'}, 
        'timestamp': {'S': '2019-02-08T14:53'}, 
        'score': {'N': '11885'}, 
        'name': {'S': 'bob'}, 
        'gamerid': {'S': 'bob9335'},
        'game': {'S': 'counter strike'}, 
        'age': {'N': '76'}, 
        'rank': {'S': 'professional'}, 
        'location': {'S': 'US'}
    }
)

def get_item(table,item):
    response = dynamo_client.get_item(
    Key={
        'event': {'S': item}
    }, 
    TableName=table  #could pass this value in as well to manage multiple tables
    )
    return response

def update_item(item, attribute, value, table):
    dynamo_client.update_item(
    TableName=table, 
    Key={
        'event': {'S': item}
    }, 
    AttributeUpdates={
        attribute: {'Value': {'S': value}}
    }
)


# put_item()
# update_item('gaming_nationals_zaf','gamerid','willz9335')
# response=get_item()
# bob=get_item('gaming_nationals_zaf')
# print(bob)
# print(response)
# dynamo_client.get_item(TableName='fruitSalad', Key={'fruitName':{'S':'Banana'}})

# dynamo_client.put_item(TableName='fruitSalad', Item={'fruitName':{'S':'Banana'},'key2':{'N':'value2'}})


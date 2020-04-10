import boto3

# dynamo_client = boto3.client('dynamodb')
dynamo_client = boto3.Session(region_name='us-east-1').client('dynamodb')
# def get_items():
#     return dynamo_client.scan(
#         TableName='YourTestTable'
#     )

def create_table():
    response = dynamo_client.create_table(
	AttributeDefinitions=[{
		'AttributeName': 'event', 
		'AttributeType': 'S'
	}
    # , 
	# {
	# 	'AttributeName': 'timestamp', 
	# 	'AttributeType': 'S'
	# }
    ], 
	TableName='gamescores', 
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
    return response

def put_item():
    dynamo_client.put_item(
    TableName='gamescores',
    Item={
        'event': {'S': 'gaming_nationals_zaf'}, 
        'timestamp': {'S': '2019-02-08T14:53'}, 
        'score': {'N': '11885'}, 
        'name': {'S': 'will'}, 
        'gamerid': {'S': 'wilson9335'},
        'game': {'S': 'counter strike'}, 
        'age': {'N': '27'}, 
        'rank': {'S': 'professional'}, 
        'location': {'S': 'sweden'}
    }
)

def get_item(item):
    response = dynamo_client.get_item(
    Key={
        'event': {'S': item}
    }, 
    TableName='gamescores'  #could pass this value in as well to manage multiple tables
    )
    return response

def update_item(item, attribute, value):
    dynamo_client.update_item(
    TableName='gamescores', 
    Key={
        'event': {'S': item}
    }, 
    AttributeUpdates={
        attribute: {'Value': {'S': value}}
    }
)

# update_item('gaming_nationals_zaf','gamerid','willz9335')
# response=get_item()

# print(response)
# dynamo_client.get_item(TableName='fruitSalad', Key={'fruitName':{'S':'Banana'}})

# dynamo_client.put_item(TableName='fruitSalad', Item={'fruitName':{'S':'Banana'},'key2':{'N':'value2'}})


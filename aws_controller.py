import boto3
import time
import os

key= os.environ['awskey']
secret= os.environ['awssecret']

# dynamo_client = boto3.client('dynamodb')
#setup a session for boto3 to connect to dynamo.  You need to change the region to the region your Dynamo
#is in.
dynamo_client = boto3.Session(region_name='us-east-1').client('dynamodb',aws_access_key_id=key, aws_secret_access_key=secret)

#This first function get_all() will return all rows from the table in the table variable.
#I would certainly make this an argument in future revisions.
#Only the table variable would need to change to match the table you wish to read.
def get_all():
    table='bobTable'
    return dynamo_client.scan(
        TableName=table
        )

#This code is here just to initalize your table.  This code will create a DynamoDB named per the variable in the function
#Again this should probably be made into an argument
#You only are required to setup the keys for your table

def create_table():
        table='bobTable'
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
	#The ProvisionedThroughput is how to setup your table to perform properly for your use case.
	#Increasing those numbers will increase performance (and cost)
            ProvisionedThroughput={
                'ReadCapacityUnits': 1, 
                'WriteCapacityUnits': 2
            }
      )
        time.sleep(5) #this is just here to allow the table to be created before entering data with putItem()
        put_item() #function to add a single item (this is for the exampe only)
        return response

#put_item() is here to add a single generic row to your table.  I only have this here for demo purposes
#You could certainly alter this to pass one row of data into the table from your application
def put_item():
    dynamo_client.put_item(
    TableName='bobTable',
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

#This function allows you to retrieve a single item from your table (set in the variable)
#This would certainly be done with arguments for your tablename and filtered item
def get_item():
    table='bobTable'
    item='1942Casablanca'
    response = dynamo_client.get_item(
    Key={
        'event': {'S': item}
    }, 
    TableName=table  #could pass this value in as well to manage multiple tables
    )
    return response
#update_item() is here to allow you to update a single item in the table, note that you would always want to 
#use your key to indicate which item to update.
def update_item(item, attribute, value, table): # works, but not going to demo
    dynamo_client.update_item(
    TableName=table, 
    Key={
        'event': {'S': item}
    }, 
    AttributeUpdates={
        attribute: {'Value': {'S': value}}
    }
)

#calls for testing.  These are just here to run test for each item

# put_item()
# update_item('gaming_nationals_zaf','gamerid','willz9335')
# response=get_item()
# bob=get_item('gaming_nationals_zaf')
# print(bob)
# print(response)



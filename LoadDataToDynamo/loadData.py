import boto3
import json
import decimal

#this script is to help you load a fairly simple JSON file to DynamoDB
dynamo_client= boto3.resource('dynamodb', region_name='us-east-1')  #establish connection to your dynamoDB

table = dynamo_client.Table('bobTable') #assign YOUR tablename here
file="moviedata.json" #full path to your json data

#this will loop through your file and put_item each row into your table
#note taht you have to make sure you are "putting" your key and
#you have to add the columnnames for each item
with open(file) as json_file:  
    movies = json.load(json_file, parse_float = decimal.Decimal)
    for movie in movies:
        year = int(movie['year'])
        title = movie['title']
        info = movie['info']
        event = str(year)+title

        print("Adding movie:", year, title)

        table.put_item(
           Item={
               'event':event,
               'year': year,
               'title': title,
               'info': info,
            }
        )

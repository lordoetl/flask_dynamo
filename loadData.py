import boto3
import json
import decimal

# dynamo_client = boto3.Session(region_name='us-east-1').client('dynamodb')
dynamo_client= boto3.resource('dynamodb', region_name='us-east-1')

table = dynamo_client.Table('bobTable')

with open("moviedata.json") as json_file:
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
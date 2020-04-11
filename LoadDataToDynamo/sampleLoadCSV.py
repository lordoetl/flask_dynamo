import csv
import boto3

def convert_csv_to_json_list(file):
   items = []
   with open(file) as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
          data = {}
        #   event,Employee ID,Email,Position,DOB
          data['event'] = row['event']
          data['Employee ID'] = row['Employee ID']
          data['Email'] = row['Email']
          data['Position'] = row['Position']
          data['DOB'] = row['DOB']
          #populate remaining fields here
          #................
          items.append(data)
   return items

def batch_write(items):
   dynamodb = boto3.resource('dynamodb')
   db = dynamodb.Table('gamescores')

   with db.batch_writer() as batch:
      for item in items:
         batch.put_item(Item=item)

if __name__ == '__main__':
   json_data = convert_csv_to_json_list('testfile.csv')
   batch_write(json_data)
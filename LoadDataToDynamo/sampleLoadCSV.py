import csv
import boto3

#convert_csv_to_json_list will convert the file you pass in to a list of json objects.
#this function has to be altered to include the column names of your file
#be sure you include the key
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
   dynamodb = boto3.resource('dynamodb') #attach to dynamodb
   db = dynamodb.Table('gamescores') #put your table name here

   #This process will loop through your data and put_item into your table.
   with db.batch_writer() as batch: 
      for item in items:
         batch.put_item(Item=item) 

if __name__ == '__main__':
   json_data = convert_csv_to_json_list('testfile.csv')  #Full path to your csv file
   batch_write(json_data)

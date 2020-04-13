# flask_dynamo
Example of a flask app using dynamodb to serve as an api

Steps to make this work in Zappa

1. Create a user in IAM and get Access Keys (or use your current AccessKeys)
2. If you haven't done it before then install AWSCLI (pip install awscli)
3. Run `aws configure` and set your access keys and the region you would like to use for you DynamoDb
4. Write and test your Flask code (provided here)<br>
    4a. ensure it is reading and writing to your DynamoDb
5. create virtualenv (you may need to `pip install virtualenv`) <br>
    5a. for windows (and probably Max) `python -m venv \zappenv`
6. activate your virtualenv <br>
    6a. for Windows `\zappenv\Scripts\activate.bat`
    6b.  for Max `source .\zappaenv\bin\activate`
7. install requirements.txt `pip install -r requirements.txt`<br>
    (note) you may need to update pip and remember to include any additional requirements you have added.
    to update pip type `python -m pip install --upgrade pip`
    if you have to upgrade pip you will need to install requirements again.
8. run `zappa init` you are almost always 'ok' if you except the defaults, but you can change them
    (note) you should see a "zappa_settings.json" file appear in your directory.
9. run `zappa deploy dev`
    This is assuming you used the default
10. When this complete you will given a url, that will be running in AWS!

Assuming you have to (or just want to) update your flask application.
1.  Make and test your changes locally
2.  run `zappa update dev`

### Arguably a better and easier way to deploy flask to the cloud.


1. Create an Azure Account.  If you have never had an azure account you will get $200 credit [link to Azure Sign up](https://signup.azure.com/signup?offer=ms-azr-0044p&appId=102&ref=dotnet&redirectURL=%23&l=en-us&correlationId=7d8cdf97c9d64f5db1b23186ba21286d)
2. verify your Flask app is working
    a. Note that the current app is using os.eviron to get the awskey and secret.
3.  install [AzureCLI on windows](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-windows) or [AzureCLI on Mac](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-macos)
4.  After installing, open a terminal and type `az login`
5.  run the following `az webapp up --sku B1 --name <app-name>`  Remember to replace <app-name> with whatever you want your app to be named.
6.  For this repo.  you will need to go to your new app in Azure -> App Services -> <app-name> -> Configuration ->App Settings
    a. Add 2 new "Application Settings" one called awskey (put your aws key as the value) and 'awssecret' (your secret key as the value).
    b. Save.
7.  Check your link (returned when you did az webapp up


To update 

# API-Call-GUI ![exe](https://user-images.githubusercontent.com/43479990/46019167-7a614080-c0a9-11e8-955b-2c2c741a0a09.png)

This Python 3 script can be converted to a standalone .exe that can be distributed to team members. The script makes use of Requests and Pyinstaller modules but can also be used through the console as well.

The standalone .exe was created to be a lightweight command line option to query the Dynatrace API of your Managed cluster or SaaS instance to retrieve timeseries information that can be used for a multitude of use cases.


### Getting started:

First, install the requests and pyinstaller libraries

   ```pip install requests```

   ```pip install pyinstaller```

Edit the variables "envOne" and "envTwo" to match your necessary endpoints. The code can be refactored to include more or less for your needs.

Once the source code is ready to go and you're ready to distribute the .exe, navigate to the folder where api_call.py is located and run:

```pyinstaller --onefile api_call.py```

A new "dist" folder will be created and you will find the .exe file.

### Finalized standalone
![Command Line Program](https://user-images.githubusercontent.com/43479990/46019170-7af9d700-c0a9-11e8-9adb-0bc6b29afd85.png)

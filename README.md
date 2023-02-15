git p# python-gmailFetcher

Fetch all gmails as htmls.
I am using python version=3.9.
If you are having problem using pip install use this following commands: `pip3 install --upgrade -i http://pypi.douban.com/simple --trusted-host pypi.douban.com --packagename`

# Application stetup

- Install python version3.9 on your device.
- Create a folder and pull the repo with command : `git clone https://github.com/sammyview80/python-gmailFetcher`
- cd directory
- Create a python environment with command: `python3 -m venv name-env`.
- Install all dependency with command: `pip3 install -r requirements.txt`
- Create a credentials.json file on root directory. credential.json file is downloaded from `https://console.cloud.google.com/apis/credentials` create credential for OAurh2.0 Client.
- Create and .env file with `SCOPES = https://www.googleapis.com/auth/gmail.readonly`
- Run python3.9 setup.py install
- Run Python3.9 main.py

#### Project folder structure
![Screenshot from 2023-02-15 21-27-15](https://user-images.githubusercontent.com/52382079/219076848-171c0e67-7653-4b31-a566-723923a7029c.png)

## YOU ARE GOOD TO GO!!!!

# Steps

1. Enable the Gmail API: Goto `https://console.cloud.google.com` Login with the google account you want.
![Screenshot from 2023-01-13 19-57-12](https://user-images.githubusercontent.com/52382079/212339833-581a8b1f-3876-4576-b076-dc5b9370964c.png)
2. Download a credentials.json file and store in program root directory `DOWNLOAD JSON`.
![Screenshot from 2023-01-13 19-58-20](https://user-images.githubusercontent.com/52382079/212340007-399e80ad-55d5-4851-acf2-9a2513aade78.png)

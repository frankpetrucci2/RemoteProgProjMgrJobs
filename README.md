# RemoteProgProjMgrJobs
Downloads Remote Program and Project Manager Jobs from Adzuna
With file explorer, find you user folder such as: c:\users\shiloh

Copy all the files I gave you to c:\users\shiloh

how to install the latest version of python on my windows 10 coomputer
I'll guide you through installing the latest version of Python on Windows 10:

Visit the official Python website:

Go to https://www.python.org/
Click on "Downloads"
Click on "Python [latest version] for Windows" (currently it's Python 3.12.1)


Download the installer:

Look for the "Download Python 3.12.1" button
Click it to download the 64-bit installer


Run the installer:

Find the downloaded file (usually in your Downloads folder)
Double-click the installer
Important: Check the box that says "Add Python to PATH"
Click "Install Now" for standard installation


Verify the installation:

Open Command Prompt (you can press Windows + R, type "cmd" and press Enter)
Type python --version and press Enter
Type pip --version and press Enter
Both commands should show version numbers if Python was installed correctly.



Tips:

If you get a "python not found" error, try closing and reopening Command Prompt
Make sure you have admin privileges on your computer
If you need to uninstall an old version, use Windows Settings > Apps > Apps & Features

Would you like me to explain any of these steps in more detail?

Based on the code you've shared, you'll need to install Python first and then use pip (Python's package installer) to install the required Python packages. Here are the specific requirements:

1. First install Python (latest version) if you haven't already - I provided those steps in my previous message.

2. After Python is installed, you'll need to install the following Python packages via pip:
   - requests
   - datetime (usually comes with Python by default)
   - typing (usually comes with Python by default)
   - json (usually comes with Python by default)

To install the required package, open Command Prompt and run:
```bash
pip install requests
```

# Get API credentials from user input
    print ("********************************************************************")
    print ("Get this ID and Key from developer.adzuna.com")
    print ("********************************************************************")
    print ("Login to developer.adzuna.com")
    print ("Go to dashboard. You may need to create an ID and Key the first time.")
    print ("Select API Acess Details")
    print ("Copy the Application ID and Application Key to a text file in notepad")
    print ("********************************************************************")
    
    
That should be all you need to run this program, which appears to be an Adzuna job search application. 


Otherwise, press ctrl-C to cancel and debug with claude.ai by copying your code and pasting it in Claude.ai.
Also paste in your results into Claude.ai.

Next Steps:

Get to a command prompt by doing the following:

In "Type here to search" at the bottom left of your screen, type cmd and press enter

It should bring you to the following folder: c:\users\shiloh

Type in: python adzuna2a.py

It will prompt you for an "Adzuna APP_ID" which you should have retrieved from "First-Step"

It will now prompt you for an "Azuna APP_KEY" which you should have retrieved from "First-Step"


It should respond quickly with a .json file: remote_program_manager_jobs.json

Run Microsoft Excel.

Select Data, "Get Data," "From File," "From JSON," 
Navigate to your folder where you placed the files.(C:\users\shiloh)
Select "To Table."
Don't pick a delimiter. Just click OK.
Click on double arrow next to "ABC 123 Column1."
Include all columns by selecting: "Load More."
Click "OK."
Click the "Close and Load" button in the upper left of the screen and save the file.

# Google-Meet Automation for Linux
__________________________________________________________________________________________________________________________________________________________________

This project showcases the automation of Google-Meet login on *Linux*.

**REQUIREMENTS**
->Chromedriver/Geckodriver
->Selenium module

NOTE:
You need to add Chromedrive/Geckodriver executable to the PATH and the commands for the same are as follows:

#If you are using geckodriver, then replace chromedriver with geckodriver.

#Move file to a directory that's already in PATH
sudo cp <Chromedriver/Geckodriver PATH> /usr/local/bin

#Make file executable
sudo chmod +x /usr/local/bin/chromedriver
__________________________________________________________________________________________________________________________________________________________________


**IMPLEMENTATION:**

Step 1: Enter all the necessary details in my_detailes.py file.
Step 2: Add the path of the google_meet.py file in the gmeet.sh file as mentioned there.
Step 3: Schedule its execution using cron (Task scheduler).

__________________________________________________________________________________________________________________________________________________________________


**Scheduling using cron:**

_# Example of cron job definition:

<min> <hour> <day_of_month> <month> <day> <user-name> <command to be executed>
  
  Attribute sepcification-:
  
  Minute (0 - 59)
  Hour (0 - 23)
  Day of month (1 - 31)
  Month (1 - 12) OR jan,feb,mar,apr ...
  Day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat

Example:
30 07 * * 1-5 vishal /bin/sh <PATH to gmeet.sh file>

If the above command is added to to crontab, then the script will execute from Monday to Friday at 7:30 hrs in the morning.
__________________________________________________________________________________________________________________________________________________________________
  

**Steps for executing adding a cronjob to the crontab-:**
  
Open the terminal and give the following commands:
  
  $~crontab -e
  
  #Choose any editor, I prefer nano though...
  
  #Crontab is opened...
  
  #At the add your job without using '#' (Comment) at the begining...
  
  <min> <hour> <day_of_month> <month> <day> <user_name> /bin/sh <PATH to gmeet.sh file>
  
  #CTRL+X and RETURN
  
  #Press Y to confirm and RETURN
    
__________________________________________________________________________________________________________________________________________________________________

    
**That's it your work is done......
**You will never be late for your meeting again......
**Peace!**

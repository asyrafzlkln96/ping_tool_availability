# ping_tool_availability
A ping tool availability check developed in Django

# Usage
* Run pip install -r requirements.txt to install Django and other dependencies.
* Run python manage.py runserver

# Create Local Database & Import Data From CSV
* Create column names and types in HeidiSQL 
![image](https://user-images.githubusercontent.com/53460015/198984500-b62ca516-b37a-4b28-bdf6-0f12f729a490.png)

Import Data using HeidiSQL:
![image](https://user-images.githubusercontent.com/53460015/199002256-1b7a6f9b-22ae-4f68-a714-3c90de34a7c5.png)

Local Database Created (Table name: data_terminals)
![image](https://user-images.githubusercontent.com/53460015/199062992-3eeacd2c-cb50-4981-aa07-ea5fc5690877.png)




# Django Endpoints:
* /update_switch_status : To update switch status as 0 when P1 to P5 are all zeros and as 1 for other records.
* /create_chart : To create chart to represent switch statuses for 12 hours
* /report: To show alert report page and show records of switches when not reachable.

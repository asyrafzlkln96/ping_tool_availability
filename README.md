# ping_tool_availability
A ping tool availability check developed in Django framework

# Usage
* Run pip install -r requirements.txt to install Django and other dependencies.
* Run python manage.py runserver
* Refer to Django endpoints below for more info

# Run Apache & MySQL in XAMPP Control Panel
* For the sake of simplicity, I ran Apache & MySQL server from XAMPP for the local database
![image](https://user-images.githubusercontent.com/53460015/200130628-cbd76f4d-eec1-4251-8a4e-2865b232109c.png)

# Create Local Database & Import Data From CSV
* Create column names and data types in HeidiSQL 
![image](https://user-images.githubusercontent.com/53460015/198984500-b62ca516-b37a-4b28-bdf6-0f12f729a490.png)

Import Data using HeidiSQL:
![image](https://user-images.githubusercontent.com/53460015/199002256-1b7a6f9b-22ae-4f68-a714-3c90de34a7c5.png)

Local Database Created (Table name: data_terminals)
![image](https://user-images.githubusercontent.com/53460015/199062992-3eeacd2c-cb50-4981-aa07-ea5fc5690877.png)

Alert Report Created:
* Open browser and go to http://127.0.0.1:8000/report
![image](https://user-images.githubusercontent.com/53460015/200037944-8211a893-45f0-4e77-bdbc-766f069b0268.png)

Sample Chart Created(Ping Availability for 12 hours):
![image](https://github.com/asyrafzlkln96/ping_tool_availability/blob/main/Switch%20SW-1%20Ping%20Availability%2028-11-2019%20(12%20am-12%20pm).png)

# Django Endpoints (Browse to http://localhost:8000 and add below endpoint):
* /update_switch_status : To update switch status as 0 when P1 to P5 are all zeros and as 1 for other records.
* /update_timestamp: To bulk update convert unix timestamp to date in DB.
* /create_chart : To create chart to represent switch statuses for 12 hours
* /report: To show alert report page and show records of switches when not reachable.

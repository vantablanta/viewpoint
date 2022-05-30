## ViewPoint
>Developed by [Michelle-Njeri](https://github.com/vantablanta)  
  
## Description  
This project is a personal gallery application that allows you to display your photos for others to see.

##  Live Link  
[View Site](https://viewpoint-mn.herokuapp.com/)  to visit the site
  

## User Story  
  
* View different photos that interest me.
* Click on a single photo to expand it and also view the details of the photo. The photo details must appear on a modal within the same route as the main page.
* Search for different categories of photos. (ie. Travel, Food)
* View photos based on the location they were taken. 
  

  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
```bash 
 https://github.com/vantablanta/viewpoint.git
```
##### Navigate into the folder
 ```bash 
cd project-viewpoint 
```
##### Install and activate Virtual  
 ```bash 
pipenv shell 
```  
##### Install Dependencies  
 ```bash 
 pipenv sync
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations photoapp
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
## Technology used  
  
* [Python3.6](https://www.python.org/)  
* [Django 1.11](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  
  
## Contact Information   
If you have any question or contributions, please email me at [vantablanta@gmail.com]  
  
## License 

* [![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](https://github.com/vantablanta/viewpoint/blob/master/LICENSE)  
* Copyright (c) 2022 **Michelle Njeri**
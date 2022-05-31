# photos

### 31 May 2022

## Author  
  
**Nancy Mwende** 
  
# Description  
This a gallery application with a collection of various pictures.A new User is able to click and view the location,category and description of each picture.User can also add,change,,edit ,delete pictures via the admin dashboard.

##  Live Link  



## User Story  

* View different photos from the galllery 
* Click an image to see the description,location,category and copy the link button.  
* Search for images by different categories.   
* Copy a link to the photo.  
  

  
## Setup and Installation  
  
##### Clone the repository:  


##### Navigate into the folder and install requirements  
 
cd mygallery pip install -r requirements.txt 

##### Install and activate Virtual  
 
- python3 -m venv virtual - source virtual/bin/activate  
 
##### Install Dependencies  

 pip install -r requirements.txt 
 
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations photos
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  

 python manage.py runserver 

Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3.8](https://www.python.org/)  
* [Django==3.2.7](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* No known bugs yet.
Alert if any.  
  
## Support and Contact Information 

To make a contribution to the code used or for any queries feel free to contact me via my email addresses nancy.mwende@student.moringaschool.com or via 0746451157.


## License

### MIT LICENCE

#### Copyright (c) 2022 
**Nancy Mwende**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR 
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
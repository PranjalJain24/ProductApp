# ProductApp
A project to undersatnd the basics of the Django Framework. It deals with creating a few apps like Products, Pages, Blogs and Courses implementing various features of Django including function based views and class based views.

### Installation and Setup

#### Instructions to set up this application from repository:
* Setup virtual Environment for the project.
* Activate the virtual environment.
* Clone the repository using:
```
$ git clone https://github.com/PranjalJain24/pollsApp  
```
If you want to clone the repository into a directory named something other than pollsApp, you can specify the new directory name as an additional argument:
```
$ git clone https://github.com/PranjalJain24/pollsApp/edit/master/README.md mynewgit
```
That command does the same thing as the previous one, but the target directory is called mynewgit.
  
* Install Django related requirements and dependencies using:
```
pip install -r requirements.txt
```
* Make migrations for Database.
* Create admin user using createsuperuser.
* Run django server: 
```
python manage.py runserver
```
For the commands of setup and installations you can refer [https://github.com/PranjalJain24/DjangoArchitecture]

#### Instructions to set up this application from scratch refer to the video series: [Try Django You Tube series](https://www.youtube.com/playlist?list=PLEsfXFp6DpzTD1BD1aWNxS2Ep06vIkaeW)


### Apps
* Products:
* Pages
* Blogs
* Courses

### Features

* Product app stores detail about the product like title, description, price and herein admin can add new products or database can be updated through ORM. 
* Product and Pages include function based views.
* Blogs app has the features like the title of the Blog, it's content and flag to state if it's active or not.
* Courses app just include the title feature as of now. You could more of them by editing ```models.py``` and ```forms.py``` in which you could add more validations.
* Blogs include Class Based Views whereas Courses include Raw Class Based Views.

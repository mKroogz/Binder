# Binder

# Welcome to Binder! 
Have you ever found yourself sick of your notes and docs being in idfferent folders all around your PC? Would you like a way to easily and quickly take notes on the fly, and keep them in one place so that they are quickly accessible?  Most importantly do you value ease of use? If you answered yes, look no futher than Binder.

## Why was Binder created?
I made Binder from a dream for the app I wish I had when going through college.  In college, I had notes and word docs scattered across both physical and virtual folders, that while organized, was still a pain to go back and forth from.  I had the idea for an app where you can log in, start a note right away, and have it categorized and organized within seconds.  Ease of use and accessability were the key things.

## What is Binder?
Binder is a multi-page, full stack django + SQL application that was designed to make notetaking and note tracking insanely easy. With Binder, users have the ability to have nested categories of season, class/topic, and note title, all with some CRUD functionality at every step of the way. In addition to this, once notes are made they can be easily traversed with the nested "manage notes" view, or a search bar to get straight to the note the user wants.


## Want to try Binder for yourself? Follow the instructions below to run the application.

* Clone down this repository by clicking the "Clone or Download" button above, copying the SSH key, and running the following command in your terminal `git clone SSH KEY GOES HERE`.
* `cd` into the root directory of the app.
* Create your OSX/Linux OS virtual environment in Terminal:

  * `python -m venv binderenv`
  * `source ./binderenv/bin/activate`

* Or create your Windows virtual environment in Command Line:

  * `python -m venv binderenv`
  * `source ./binderenv/Scripts/activate`

* Install the app's dependencies:

  * `pip install -r requirements.txt`

* Build your database from the existing models:

  * `python manage.py makemigrations binder`
  * `python manage.py migrate`

* Create a superuser for your local version of the app:

  * `python manage.py createsuperuser`

* Fire up your dev server and get to work!

  * `python manage.py runserver`



* Go to http://localhost:8000/ to view the app. 

## What can you do with Binder?
1. After completing the setup above, in the browser, navigate to http://localhost:8000.
2. If you are a returning user, login to Binder with your account information.
3. Never signed up for Binder before? No problem! Click the register link and complete your registration.

4. Once you have logged into the app, you will be taken to the home page. From here we have several options.  You can get straight into the note writing by clicking the write new note button, manage your existing note with the manage notes view, or search for a specific note or class.
5. If you choose to write a new note from the button on your homepage, the backend logic is smart enough to know what season class combinations already exist so that you don't make needless duplicates to make organization more difficult. 

6. If you choose the manage notes option from the navigation bar, you will be taken to a page where you can see all of your seasons or semesters you have created. From this view, the data is nested in a way that all your classes are contained within your individual seasons, and similarly your notes within your classes.  The is to make it 3 clicks to any note, no matter how many you have.

7. Last but certainly not least is our search bar. This bar allows to very easily search for a class or note if you are not entirely sure where it is in your nested data.  The search crucially takes incomplete searches and tries to complete them for you, and well as if left blank will show ALL classes and notes in an easily digestable view.  The search helps immensely when you know where you want to write but not exactly where it is in the manage view.

8. Lastly when you are finished with your note taking session, logging out is easy right from the navigation bar, you can also rest easy knowing your notes are stored safely in your personal database for later viewing.

## Binder Tech Stack

* Python
* Django
* Sqlite3
* CSS



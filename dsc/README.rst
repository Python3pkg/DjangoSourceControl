=====
DjangoSourceControl
=====

DjangoSourceControl is a simple Django app to create Web-based Python files and projects.
For each project, users can add, update, and create python projects, files, and versions.

Note: Django source control has a unit test suite which can be ran by 'python manage.py test' to run the repo and api authentication tests.

Quick start
-----------

1. Add "djangosourcecontrol" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'djangosourcecontrol',
    ]

2. Include the djangosourcecontrol URLconf in your project urls.py like this::

    url(r'^djangosourcecontrol/', include('djangosourcecontrol.urls')),

3. Run `python manage.py migrate` to create the djangosourcecontrol models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to assign the can_add_project, and/or the can_run_project to user.

5. Visit http://127.0.0.1:8000/djangosourcecontrol/ to start creating projects.



### Setup Virtual enviornment to run build the dist

open a terminal and navigate to %where you put the dsc files%/DjangoSourceControl/dsc Run the following commands to create a virtual environment

### optional steps if you already haven't installed python3
	sudo apt-get install python3
	sudo apt-get install python3-pip

### optional update pip
	sudo pip3 install --upgrade pip

### install virtualenv pip package
	pip3 install virtualenv

### Make the folder and create our virtualenv
	virtualenv distenv 
	source distenv/bin/activate 
	pip3 install django 
	pip3 install djangorestframework 
    
### Run setup.py to build the dist
    python3 setup.py sdist

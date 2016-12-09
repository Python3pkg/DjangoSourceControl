# DjangoSourceControl
DjangoSourceControl is a simple Django app to create Web-based Python files and projects.

NOTE: DjangoSourceControl was developed in windows using visual studio. However it works perfectly well under linux as well.

The reccomended method of using django source control is within a python virtual environment. Below are instructions on how to setup a virtual enviornment and then run the django test server for djangosourcecontrol

## Setup Virtual enviornment to run the test server

open a terminal and navigate to %where you put the dsc files%/DjangoSourceControl/server Run the following commands to create a virtual environment

### optional steps if you already haven't installed python3
	sudo apt-get install python3
	sudo apt-get install python3-pip

### optional update pip
	sudo pip3 install --upgrade pip

### install virtualenv pip package
	pip3 install virtualenv

### Make the folder and create our virtualenv
	virtualenv serverenv 
	source serverenv/bin/activate 
	pip3 install django 
	pip3 install djangorestframework 
	pip3 install djangosourcecontrol

### Finally run the server
	python3 manage.py runserver

### Open up a web browser and navigate to
	http://127.0.0.1:8000/

Note: The test server comes with three sample users.

username:passwords are listed here: 
admin:jello 
daniel:jello 
jamie:jello

## The site consists of serveral pages:

### http://127.0.0.1:8000/ or http://127.0.0.1:8000/home/
The home page, contains different links depending on superuser status.

### http://127.0.0.1:8000/login/
The login page, contains a link to the register page

### http://127.0.0.1:8000/home/register
The registration page where new users are created with the can_add_permission by default

### http://127.0.0.1:8000/djangosourcecontrol/
The project list page. Displays all public projects and projects created by the logged in user.
Note: superuser can see all projects
Note: users with the can_add_project permission, have an additonal button which spawns a modal to create new projects.
http://127.0.0.1:8000/djangosourcecontrol/PK/ where PK is an integer that represents a projects primary key.

Projects the project details page listed at http://127.0.0.1:8000/djangosourcecontrol/PK/ displays a collection of files as dropdown which lists each files versions. This page allows for the creation and renaming of new/existing files, the creation of new file versions and the renaming of projects and their descriptions. Project and files can each be marked as private, which limits visibility to only the owner of the project and superusers.

Each file may have the most recent version compiled and the results displayed.  

Each project may mark one file as the startup.  Only the startup file is allowed to be run on the server. 

### http://127.0.0.1:8000/admin/
The admin page allows manual manipulation of the django users, groups, projects, files, and versions.
NOTE: There is currently no way to remove a project, file, or version from the public controls. Only a superuser may remove project, file, or versions and it must be done through the admin pages.


## Project Proposal:
------------------------------
### Author: Daniel Pepka

### Project Name: DjangoSourceControl
		
### Brief Description:

Django Source Control is a website that lets you log in, create public or private python projects which are collections of files.  Each time you save a file a new version is created which is then compiled and displaying any errors. Each version is retained preserving a history of each previous save. Then using the web page you can revert to a previous version at any time. The project files may be download as zip file, and if authorized, you can run the script directly on the server.

### Give a script (a sequence of actions, not Python code) of a session a user might have with your project.:

    User Story 1:   Register an account
        1.  Open web browser and navigate to http://127.0.0.1:8000/login/
        2.  Select register new user
        3.  Pick username and enter password
        3a. If username is already taken, the user will be informed they must pick a new username.
	optional step 4. Request the site admin to mark the new account as authorized with the can_run_project permission.  Failure to do this step results in only being able to compileand download projects.

    User Story 2:  Create public project with public startup file and private module file
        1.  Open web browser and navigate to http://127.0.0.1:8000/login/
        2.  Log in with existing account
        3.  Create a new project, set project name, description, and mark as public
	4:  Add a new file (#1), set name, description, and mark as private
	5.  Create a second file (#2), set name, description, mark as startup, and as public
        6.  Select file #1, enter text into text box and hit save which creates a new version of the file
	7.  Select file #2 enter text into text box to create a new python modules and save which creates a new version of the file.  The save triggers a compile button to become available, which if clicked will cause the server to compile the code with the results  then displayed to the user. 
        8. If Admin or has the can_run_project permission: Select file #2 and press run, Python script is then executed in a new thread on the server and the results or any exceptions are displayed as a result.
	9. Select download as zip, then extract zip file and run locally.
        10.  Repeat steps 6-9 until satisfied.

    User Story 3:   View and compile existing project, then run.
        1.  Open web browser and navigate to http://127.0.0.1:8000/login/
        2.  Log in
        3.  Select an existing project previously created by current user
        4.  Select which file to modify
        5.  Enter text into text box to create a new python modules and save which creates a new version for the file.  The once a file is saved a compile button to become available, which if clicked will cause the server to compile the code and display the results to the user. 
        6.  Repeat steps 4-5 until satisfied.
	7.  If Admin or has the can_run_project permission: Select startup file and press run, the Python script is then executed in a new thread on the server and the results or any exceptions are displayed as a result.

    User Story 4:   View and run existing public project
        1.  Open web browser and navigate to  http://127.0.0.1:8000/login/
        2.  Log in
        3.  Select an existing public project not created by current user
	4.  Select file to view
	5   Select previous version of the file to view
	4.  Download project as zip file retreiving the most recent version of each public file. 
	5.  Extract zip, modify files then run locally.

    User Story 5:   View and run existing project as guest
        1.  Open web browser and navigate to http://127.0.0.1:8000
        2.  Do not log in, continue as guest to have read only access to public files / projects
        3.  Select an existing project public
        4.  Select which file to view
        5.  Hit compile, Python script is then compiled on the server and the any exceptions are displayed as a result.
        6.  Repeat steps 4-5 until satisfied.
	7.  Download as zip file, extract and then run. 


### What other modules will your project use?:
    Django, and django-rest-framework


### Describe your project in greater detail. What would you say to someone to get them to use (or buy) your project?:

DjangoSourceControl is a website written in Django (https://www.djangoproject.com/) with a sqllite3 database created using Django's ORM. The purpose of the website is to provide end users the ability to log in to and create a project that will allow the user to manage a collection of python scripts. One file would be marked as the startup file, and would be used when a project is requsted to be ran or compiled.  Both Projects and file can be either public or private.  If a project or file is private, only the user who created the project can view or download the project and files. And finally all projects can be downloaded compressed as a zip file which can then be extracted and run locally. 

### If your project provides an API, give some typical functions and/or classes (and their methods) that users would import.:
It has webapi endpoints that allow data to be served and modified from a restful api hosted by the django server. Using javascript or another tool to send get and post requests to the server to interact with the api.  Below is a snippet from the project_details.html file on how to request a project, files, and versions. Below that is a example of a post method to request a new project file version. 

	GET - project, then get all its files, and also all of that files versions. 
		// request the project itself from the api
		// fairly inefficent, it could request groups at a time instead of individuals
		$.get("/djangosourcecontrol/api/project/" + '{{project.id}}')
		.done(function (data) {
		   // foreach
		   ko.utils.arrayForEach(data.projectfiles, function (item) {
		       $.get("/djangosourcecontrol/api/projectfile/" + item)
			   .done(function (data) {
			       var f = new file(data.id, data.projectfile_name, data.projectfile_description, data.public, data.startup, ko.observableArray([]));
			       ko.utils.arrayForEach(data.projectfileversions, function (item) {
				   $.get("/djangosourcecontrol/api/projectfileversion/" + item)
				       .done(function (data) {
					   var v = new version(data.id, moment(data.created_date), data.text);
					   f.versions.push(v)
				       })
				       .fail(function (data) {
					   // get project file version fail
					   self.showFailAlert(JSON.stringify(data));
				       });
			       });
			       self.projectFiles.push(f)
			   })
			   .fail(function (data) {
			       // get project file fail
			       self.showFailAlert(JSON.stringify(data));
			   });
		   });
		})
		.fail(function (data) {
		   // get project fail
		   self.showFailAlert(JSON.stringify(data));
		});

	POST - Create new project file version
		$.post("/djangosourcecontrol/api/projectfileversion/", {
		    "created_date": moment().format('YYYY-MM-DDThh:mm'),
		    "text": self.text(),
		    "projectfile": self.selectedFile().id,
		    'csrfmiddlewaretoken': '{{ csrf_token }}'
		})
		.done(function (data) {
		   // A successful save will return the new data as a dto.
		   self.showSaveAlert();
		   var newVersion = new version(data.id, moment(data.created_date), data.text);
		   self.selectedFile().versions.push(newVersion);
		   self.selectedFile().selectedVersion(newVersion);
		})
		.fail(function (data) {
		   self.showFailAlert(JSON.stringify(data));
		});

If you wanted to work directly in python using the django built in ORM you could import from the djangosourcecontrol models.
	EX:
		from djangosourcecontrol.djangosourcecontrolmodels import Project
		from djangosourcecontrol.djangosourcecontroldjangosourcecontrolmodels import ProjectFile
		from djangosourcecontrol.djangosourcecontrolmodels import ProjectFileVersion

Additionally there is a collection of useful python custom methods for checking for authentication on files, projects and version, as well as the usual rest collection of get,set,update but not delete. 

	EX:
		
		repo = DSCRepository()
		pk = 1 #where 1 is the primary key of a project stored in the database
		project = repo.get_project(pk)


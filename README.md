# DjangoSourceControl
DjangoSourceControl is a simple Django app to create Web-based Python files and projects.

Project Proposal:
------------------------------
Author: Daniel Pepka

Project Name: DjangoSourceControl
		
Brief Description:

Django Source Control is a website that lets you log in, create public or private python projects which are collections of files.  Each time you save a file a new version is created which is then compiled and displaying any errors. Each version is retained preserving a history of each previous save. Then using the web page you can revert to a previous version at any time. The project files may be download as zip file, and if authorized, you can run the script directly on the server.

Give a script (a sequence of actions, not Python code) of a session a user might have with your project.:

    User Story 1:   Register an account
        1.  Open web browser and navigate to dsc.com (or other url).
        2.  Select register user
        3.  Pick username and enter password
        3a. If username is already taken, the user will be informed they must pick a new username.
	optional step 4: Request the site admin to mark the new account as authorized to run code.  Failure to do this step results in only being able to compile projects.

    User Story 2:  Create public project with public startup file and private module file
        1.  Open web browser and navigate to dsc.com (or other url).
        2.  Log in with existing account
        3.  Create a new project, set project name, description, and mark as public
	4:  Add a new file (#1), set name, description, and mark as private
	5.  Create a second file (#2), set name, description, mark as startup, and as public
        6.  Select file #1, enter text into text box and hit save which creates a new version of the file and is marked active
	7.  Select file #2 enter text into text box to create a new python modules and save which creates a new version of the file and is marked active.  The save triggers a compile and the results are then displayed on the page when the current version is selected. 
        8. If Admin: Select file #2 and press run, Python script is then executed in a new thread on the server and the results or any exceptions are displayed as a result.
	9. Select download as zip, then extract zip file and run locally.
        10.  Repeat steps 6-9 until satisfied.

    User Story 3:   View and compile existing project, then run.
        1.  Open web browser and navigate to dsc.com (or other url).
        2.  Log in
        3.  Select an existing project previously created by current user
        4.  Select which file to modify
        5.  Enter text into text box and hit save, which creates a new version of the file and is marked active.  The save triggers a compile and the results are then displayed on the page when the current version is selected.
        6.  Repeat steps 4-5 until satisfied.
	7a. Press run and view results. 

    User Story 4:   View and run existing public project
        1.  Open web browser and navigate to dsc.com (or other url).
        2.  Log in
        3.  Select an existing public project not created by current user
        4.  Select an existing public file to modify
        5.  Enter text into text box and hit run, Python script is then executed in a new thread on the server and the results or any exceptions are displayed as a result.
        6.  Repeat steps 4-5 until satisfied.
        7.  Save the script.  A new version is then saved along with a timestamp into the database.

    User Story 5:   View and run existing project as guest
        1.  Open web browser and navigate to dsc.com (or other url).
        2.  Do not log in, continue as guest to have read only access to public files / projects
        3.  Select an existing project public
        4.  Select which file to view
        5.  Hit compile, Python script is then compiled on the server and the any exceptions are displayed as a result.
        6.  Repeat steps 4-5 until satisfied.
	7.  Download as zip file, extract and then run. 

What other modules will your project use?:
    Django, and django-rest-framework

Describe your project in greater detail. What would you say to someone to get them to use (or buy) your project?:
DjangoSourceControl is a website written in Django (https://www.djangoproject.com/) with a sqllite3 database created using Django's ORM. The purpose of the website is to provide end users the ability to log in to and create a project that will allow the user to manage a collection of python scripts. One file would be marked as the startup file, and would be used when a project is requsted to be ran or compiled.  Both Projects and file can be either public or private.  If a project or file is private, only the user who created the project can view or download the project and files. And finally all projects can be downloaded compressed as a zip file which can then be extracted and run locally. 

If your project provides an API, give some typical functions and/or classes (and their methods) that users would import.:
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
		files = repo.get

Will your application make use of any non-trivial algorithms? If so,describe them.:
Allowing project files to be able to include and use source code from each other will be fairly non-trivial. 

# DjangoSourceControl
DjangoSourceControl is a simple Django app to create Web-based Python files and projects.

Project Proposal:
------------------------------
Author: Daniel Pepka

Project Name: DjangoSourceControl
		
Brief Description:

    Django Source Control is a website that lets you log in, create public or private python projects which are collections of files.  Each time you save a file a new version is created which is then compiled and displaying any errors. Each version is retained preserving a history of each previous save. Then using the web page you can revert to a previous version at any time. If authorized, you can run the script directly on the server, otherwize a download as zip 

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

    DjangoSourceControl is a website written in Django (https://www.djangoproject.com/) with a sqllite3 database created using the built in Django ORM. The purpose of the website is to provide end users the ability to log in to and create a project that will allow the user to manage a collection of python scripts. One file would be marked as the startup file, so when you tell the project to compiled or run it will run that file.  You will also have the ability to mark projects and files as public or private thus preventing anyone other than the owner access to the file.  If a file is in a public project but marked as private you will not be able to view the contents of that file, but you will be able to still include python code from the private module.  This way you can create semi public code that people can use but not see the implementation.  And finally all projects can be downloaded compressed as a zip file which can then be extracted and run locally. 

If your project provides an API, give some typical functions and/or classes (and their methods) that users would import.:

    It will have webapi endpoints that allow the data to be served dynamically from the Django host. Just use javascript or another tool to send a get request to the
    url
        endpoint.
        ex:
          $.get("http://dsc.com/api/Projects", function(projects){
                alert("Projects: " + projects);
            });
        Additionally if you wanted to work directly in python you could import
        from the models directory.
        from dsc.models import Project
        from dsc.models import ProjectFile
        from dsc.models import ProjectFileVersion

Will your application make use of any non-trivial algorithms? If so,describe them.:

    Allowing project files to be able to include and use source code from each other will be fairly non-trivial. 

What platform(s) will your project run on?:

    Windows or Linux, cross platform

If your project is interactive, give some typical user commands.:

    The website will consist of several pages.

    http://dsc.com/ - home page, displays a slash screen + logo and a list of actions, like login or continue as guest with warning that it will be read only. It will also display a list the users projects and all of the public projects.
      
    Each project in the list will have a summery of what the project is and what files are in it.  Each project has a link to its project page (ex project #1: http://dvc.com/project/1) where the files in that project will be listed.  Each file then will show its name, last modified date, and if the last time it was compiled or executed and the result of that action. Each file will also have a link that allows you to edit that file (ex file #1: http://dcv.com/file/1)

    If you click on a file it will bring you to a page with a place to edit the code associated with the python script.  It will also have a dropdown which will allow you to pick and display a previously saved version of the script.  There will be a button that lets you test the script which will execute the python code and display the results on the page.  Any exceptions that are thrown will also be displayed. Project files can be included in other project files, external non python3 core functionality may not be allowed, testing will determine if that is possible.

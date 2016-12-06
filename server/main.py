from django.core.management import call_command
import django
import os
    
def start_server():
    """
    Start server is the 
    """
    os.environ['DJANGO_SETTINGS_MODULE'] = "DjpStudios.settings"
    django.setup()

    print("\n###\n### DJP DEBUG: Checking Migrations: \n###\n")
    call_command('migrate')

    #print("Running Seed Methods: ")
    #call_command('populate_interpret_db')

    print("\n###\n### DJP DEBUG: Starting Server: \n###\n")
    call_command('runserver')

if __name__ == '__main__':
    start_server()

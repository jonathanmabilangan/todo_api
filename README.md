# ***************************** #

## Todo api for creating, updating, listing, and removing tasks.

## Requirements
- Postman (for api testing)
- Python 

## Local setup and requirements installation

- 1. Clone the repository. In your terminal
``` bash
git clone git@github.com:jonathanmabilangan/todo_api.git
```

- 2. Install Python or if you have it proceed to step 3
- 3. Create a virtual environment using the command below
``` bash
python3 -m venv venv 
```

- 4. Enter the virtual environment through the command below
``` bash
source venv/bin/activate/ 
```

- 5. Install the libraries needed to run the system
``` bash
pip install -r requirements.txt
```

- 6. Run migration inside the project's directory
``` bash
python manage.py makemigrations
```
``` bash
python manage.py migrate
```

- 7. Run the project
``` bash
python manage.py runserver
```

- 8. Create a superadmin user
``` bash
python manage.py createsuperuser
```

### The project is now running

### Trying the project's API endpoint

- Through swagger:
    - Create an admin account and use it in basicAuth








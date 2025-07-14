# Choose-Your-Own-Adventure

- For this project we will code out `backend` first in PyCharm.
- Build UI around this backend using `react`

## Setup

### Backend

- Commands to run:

```bash
PS C:\Users\abhis\Desktop\PythonDev\Choose-Your-Own-Adventure\backend> uv init .
Initialized project `backend` at `C:\Users\abhis\Desktop\PythonDev\Choose-Your-Own-Adventure\backend`

PS C:\Users\abhis\Desktop\PythonDev\Choose-Your-Own-Adventure\backend> uv add fastapi[all] langchain langchain-google-genai python-dotenv sqlalchemy uvicorn psycopg2-binary
# Creates the Virtual environment for us and install above dependencies needed for the project.
Using CPython 3.12.7
Creating virtual environment at: .venv
Resolved 77 packages in 698ms
Prepared 19 packages in 491ms
Installed 73 packages in 900ms

# To run our server
PS C:\Users\abhis\Desktop\PythonDev\Choose-Your-Own-Adventure\backend> uv run main.py
INFO:     Will watch for changes in these directories: ['C:\\Users\\abhis\\Desktop\\PythonDev\\Choose-Your-Own-Adventure\\backend']
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit) # Go to http://localhost:8000/redoc in browser
INFO:     Started reloader process [15560] using WatchFiles
INFO:     Started server process [22540]
INFO:     Waiting for application startup.
INFO:     Application startup complete.

```

- `psycopg2-binary` : Allows us to connect to postgresSQL Database.
- An `API` is just a way for us to communicate data between different services. like the backend and frontend to
  communicate.In order to communicate with best practice, we should define the type of data that we expect to come in
  and to come out. It makes our lives a lot easier and help other devs easily by looking at our schema and understanding
  what our application is actually going to do.
- Let's create a skeleton(in `backend`) for our project to have a structure to begin with.
    - First add `__init__.py` file to our backend directory to make it an python package.
    - Then add another file - `.env` to store our API Keys or any secrets like Database credentials ..etc.
    - Let's create some folders.
        - `core` - contains core operations for our applications like `generating the story`.
        - `db` - For our database operations.
        - `models` - For our database models.
        - `routers` - Handling all our API routes we're going to have.
        - `schemas` - Defines the data that comes into our API and go out of our API.
- Let's add `python files` to our folders accordingly.
    - `core`:
        - Add `__init__.py` - makes the folder as package and makes it easy for us to import files or functions that we
          define in this folder.
        - Add `config.py`
        - Add `models.py`
        - Add `prompts.py` - will have our prompts to communicate with our LLMs.
        - Add `story_generator.py` - use `snake_case` to define files/variables with two or more words in python which
          is a standard convention to name things.
    - `db`:
        - Add `__init__.py`
        - Add `database.py`
    - `models`:
        - Add `__init__.py`
        - Add `story.py` - this file defines the type of data we want to store in our DB
        - Add `job.py` - represents the status of creating a story
    - `routers`:
        - Add `job.py` - define all the routes for handling our jobs.
        - Add `story.py` - All the routes for handling our story.
        - Add `__init__.py`
    - `schemas`: defines the type of data that our API will be returning & the type of data that our API will expect.
        - Add `__init__.py`
        - Add `story.py`
        - Add `job.py`

## Write/define code - Step by Step

### Backend

- Add Uvicorn and fastapi to `main.py` to create our backend server to serve api - setup.
- Add Environment variables and configuration - `.env` & what all we need to add will be seen in `.env.example`.
- Then we will load our `.env` variables into our app , which will be defined in `core/config.py` and use that
  `settings` in our `main.py` file.
- `Database Setup:` we will start handling our database models. **It's important to understand the date that your
  application is going to use & the relationships between those pieces of data. Once you understand that the system
  becomes significantly easier for you to build.**
    - Go to our `db/database.py`: need to define the database initialization to be then create database models.
    - In our `models/story.py`: I want to define the information that we need to store for a story and how this is going
      to work. - resource for [sqlalchemy](https://www.sqlalchemy.org/)
    - In our `models/job.py` : we use it because the stories take a little bit of time to populate from LLM , so when
      someone submits a request to create a new story , it won't be created right away.so we create a `job` which is
      going to represent the intent to make a story & this is going to have particular progress like "IN_PROGRESS","
      COMPLETED" etc. we will be keep checking for the status of this job to be completed & then the story will be
      complete, and we can grab it.
    - Now we go to `schemas`: define the python class that specifies the type of data that we want our api to accept &
      to return.This is really important because it allows FastAPI to automatically do some data validation for us to
      ensure that the data is correct that's coming into the API. write necessary schemas to story and job.
- `API Routers`: we will start with `routers/story.py` - here we write the endpoints that are going to be hit by our user.

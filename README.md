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
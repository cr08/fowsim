# This is a modified repo of FoWSim to add an automated card overlay for live streams and a few related fixes. Demo video posted below. Full original README and install instructions at the bottom of this file.


## To-Do:
* ✅ Adding custom card overlay template for streaming
* ❌ Finalize/fix overlay animations and formatting
* ❌ Add separate animation for J-Ruler flips that flip directly to the back side instead of the static 'Force of Will' cardback.
* ✅ Adding 'push' mechanism to card display pages to push out new cards to stream overlay from a remote user
* ❌ Tracking down missing card images that do not exist on FOWTCG at the time of this commit
    * If you wish to request access to the AWS repo as lined out in CONTRIBUTORS.md, revert changes in Commit d2c48d3
* ❔ Adding missing card info to JSON as needed (Scheherazade bot has a similar JSON card info file which may be more up to date and may need to be merged accordingly)
* ❔Integrate hosted overlay backend files in [sse_data] into Django/FoWsim proper

## Operational Demo Video:
* Coming Soon!

## Extra installation and configuration for stream overlay components:
1. Upload contents of [sse_data] folder to a PHP capable publically accessible host. The system relies on EventSource functionality so ensure your web server supports this.
    * _Currently this cannot run as part of the Django platform FoWsim runs on and must be hosted externally._
2. Update `SSE_BASE_URL` in settings.py to reflect the hosted location of the [sse_data] contents.
3. Add `http://url.to.fowsim/card_overlay_start/` to your streaming software of choice as a browser source
    * _Staff/admin accounts are required for both the 'push' tasks as well as the stream overlay. The first load of the overlay will show a login screen for this._

## Credits:
* Force of Wind devs for the upstream project base: https://github.com/Force-of-Wind/fowsim
* SWUP library for overlay animations: https://swup.js.org/

---

# Running the Server Locally

1. Create a python3 virtual environment (3.9.6):
`python -m venv /path/to/make/venv`

2. Use that virtual environment (must activate every time you open a new prompt)
    - Windows: `/path/to/venv/Scripts/activate` 
    - Linux/MacOS: `. /path/to/venv/bin/activate`

3. Install requirements (If you add packages with pip, add them to requirements.txt using "pip freeze > requirements.txt"). If running on linux or mac, remove the line for Twisted from the requirements.txt file (dont commit this change)
> pip install -r requirements.txt

4. Install PostgreSQL and set up a local database.

5. Create a .env file in the root directory of the repository and populate it with the following, filling in as necessary with information from your Postgres install. Set `DJANGO_SECRET_KEY` as anything, since it doesn't matter for local development, but if you want to generate one properly execute the python code below the example .env file:
```
DJANGO_SECRET_KEY=
DB_USER=
DB_NAME=
DB_PASS=
DB_HOST=
DB_PORT=
```

```sh
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

6. Apply the schema to the database:
`python manage.py migrate`

7. Create a superuser account to use on your local development server:
`python manage.py createsuperuser`

8. Run the server:
`python manage.py runserver`

You can now access all the pages at localhost e.g. http://127.0.0.1:8000/search/

# Docker Setup

1. Edit `docker-compose.yml` to setup the database

2. Ensure `.env` is setup.
```
DJANGO_SECRET_KEY=(Run the command above to get this)
DB_USER=fowsim
DB_NAME=fowsim
DB_PASS=CHANGEME
DB_HOST=db
DB_PORT=5432
```

3. Run `docker-compose up -d --build`

4. Setup database running this command:
`docker-compose exec web python manage.py migrate --noinput`

5. Create the superuser:
`docker-compose exec web python manage.py createsuperuser`

6. Head to `http://localhost:1337` to enjoy the docker setup :D

# How to Contribute
Join us on [Discord](https://discord.com/invite/8S5XW6pUEF) and let us know about your interest in helping develop Force of Wind!

For approved contributors, see [here](/CONTRIBUTORS.md) for info on specific info on how to contribute.

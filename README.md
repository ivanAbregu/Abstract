# Abstract programming assignment
## Relevant Technologies:
* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/) 
* [Python 3.8](https://docs.python.org/3/)
* [Poetry](https://python-poetry.org/)
* [Django 3.0](https://docs.djangoproject.com/en/3.1/releases/3.0/)
* [Django REST framework](https://www.django-rest-framework.org/)
* [PostgreSQL](https://www.postgresql.org/)
* [React.js](https://reactjs.org/)
* [React Hooks](https://reactjs.org/docs/hooks-overview.html)
* [hubSpot](https://www.hubspot.com)


## Run on local machine
Create an .env file on docker/ there is a template.env as example.
Run the next command to run the projects on your local machine.

* docker-compose up

* Then you could consume the api on http://0.0.0.0:8000
Also you could play on the react implementation http://0.0.0.0:3000


Backend:
● Language: Python
● Framework: Django
● Web server: allowed to use development server, no need for uwsgi or any other
WSGI server integration
● Database: MySQL, PostgreSQL, or SQLite
● Any library that you consider necessary can be used
Problem statement
1. The goal of this assignment is to build a simple integration for Hubspot APIs.
2. Hubspot APIs are documented at https://developers.hubspot.com/docs/api/overview
3. There are 5 parts to this assignment:
a. Set up a Django project.
b. Schema modeling. Model needed to store OAuth tokens and user data.
c. Build Hubspot OAuth integration. Build APIs that are able to complete the OAuth
flow and persist the access token, refresh token, and user email. Follow
instructions at https://developers.hubspot.com/docs/api/oauth-quickstart-guide
d. Build Hubspot Owner API integration. Implement an endpoint to retrieve the list of
owners. Documentation: https://developers.hubspot.com/docs/api/crm/owners
e. Build Hubspot Deal API integration. Implement 2 endpoints to create basic deals
and retrieve the list of deals. Documentation:
https://developers.hubspot.com/docs/api/crm/deals
4. The delivery at the end of this assignment can be a zip file that contains the project or a
GitHub repository.
5. Bonus: implement the project using Docker.
Criteria for evaluation
1. Correctness - does the code do what it is supposed to do?
2. Code aesthetics - code structure, cleanness of code, documentation, ease of
understanding
3. Appropriate error handling
4. Does the project contain unit tests?
Frontend:
● Tools, frameworks, and libraries:
○ React
○ Bootstrap, or Tailwind (Tailwind is a plus)
○ Any library that you consider necessary can be used (like Axios, etc)
Problem statement
1. The goal of this assignment is to build a simple UI that integrates the endpoints created
on the backend project.
2. There are 4 parts to this assignment:
a. Setup a React project.
b. Integrate the OAuth flow.
c. Implement the UI that shows the list of deals (a simple table view) and integrate it
with the endpoint created previously in the backend project to retrieve the list of
deals.
d. Implement the UI for creating deals (a simple form) and integrate it with the
endpoint created previously in the backend project to create deals.
3. The delivery at the end of this assignment can be a zip file that contains the project or a
GitHub repository.
Criteria for evaluation
5. Correctness - does the UI do what it is supposed to do?
6. Code aesthetics - code structure, cleanness of code, ease of understanding.
7. Appropriate error handling
8. Does the project contain unit tests?


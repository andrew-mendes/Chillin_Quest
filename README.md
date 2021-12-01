
# Chillin' Quest <img src="README.assets/logo.png" alt="MarineGEO circle logo" style="float: right; height: 60px; width:auto;"/>
RPG-like quest maker for life
___

<a href='https://www.edx.org' target="_blank"><img alt='EDX' src='https://img.shields.io/badge/edX®-100000?style=flat&logo=EDX&logoColor=FFFFFF&labelColor=77202E&color=8B8D90'/></a> <a href='https://python.org' target="_blank"><img alt='Python' src='https://img.shields.io/badge/Made_with Python-100000?style=flat&logo=Python&logoColor=ffde57&labelColor=4584b6&color=646464'/></a> <a href='https://developer.mozilla.org/pt-BR/docs/Web/JavaScript' target="_blank"><img alt='JavaScript' src='https://img.shields.io/badge/Made_with JavaScript-100000?style=flat&logo=JavaScript&logoColor=f7df1e&labelColor=000000&color=2F2F2F'/></a> <a href='https://flask.palletsprojects.com/en/2.0.x/' target="_blank"><img alt='Flask' src='https://img.shields.io/badge/Made_with Flask-100000?style=flat&logo=Flask&logoColor=000000&labelColor=FFFFFF&color=2F2F2F'/></a> <a href='https://jquery.com' target="_blank"><img alt='JQuery' src='https://img.shields.io/badge/JQuery-100000?style=flat&logo=JQuery&logoColor=7acef4&labelColor=0769ad&color=FFFFFF'/></a> <a href='https://getbootstrap.com' target="_blank"><img alt='Bootstrap' src='https://img.shields.io/badge/Bootstrap-100000?style=flat&logo=Bootstrap&logoColor=563d7c&labelColor=FFFFFF&color=563d7c'/></a>

Video Demo: <URL HERE>

## Description

  A web application that allows users to create, manage and customize their real life objectives as RPG-like quests.

## Table of  Contents

<!--ts-->
  - [Objective](#objective)
  - [Project Status](#project-status)
  - [Features](#features)
  - [Tech Stack](#tech-stack)
  - [Installation](#installation)
  - [Setup](#setup)
    - [Requirements](#requirements)
  - [Backend](#backend)
    - [application.py](#application)
    - [helpers.py](#helpers.py)
    - [chillinquest.db](#chillinquest.db)
  - [Frontend](#frontend)
    - [Starting and Register Screens](#starting-and-register-screens)
    - [Home](#home)
    - [Profile & Account](#profile-account)
  - [Development Changes](#development-changes)
  - [Acknowledgements](#acknowledgements)
  - [About the author](#about)

<!--te-->

## Objective

​Built as a Final Project for my commitment to ***Harvard's CS50x - Introduction to Computer Science - 2021***  (<https://cs50.harvard.edu/x/>).

[return to top](#table-of-contents) :arrow_up_small:

## Project Status

As a final project commitment for the course it is completed. However I do intend to develop a new possible mobile version of it in the future with some other features and ideas that were cutout from this version.

[return to top](#table-of-contents) :arrow_up_small:

## Features

- Friendly and intuitive UI for users to add, manage, filter and customize their quests.
- Responsive to screen size and different types of actions, such as mouseover, selection, etc.
- Customizable character (as any RPG must be).

[return to top](#table-of-contents) :arrow_up_small:

## Tech Stack

- [Python](https://python.org)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/)
- [WTForms](https://wtforms.readthedocs.io/en/3.0.x/)
- [JavaScript](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript)
- [JQuery](https://jquery.com)
- [Bootstrap](https://getbootstrap.com)
- [SQLite](https://www.sqlite.org/index.html) - through CS50's [python module](https://cs50.readthedocs.io/libraries/cs50/python/)

[return to top](#table-of-contents) :arrow_up_small:

## Setup

### Requirements

All included in */templates/requirements.txt*:
  - cs50
  - Flask
  - flask_session
  - werkzeug
  - flask_wtf
  - wtforms
  - requests

[return to top](#table-of-contents) :arrow_up_small:

## Installation

**To run locally:**

**On Windows**
1. From command prompt, once in the /chillinquest folder run:<br>
    In order to create the virtual environment:
    `py -3 -m venv venv` <br>
    To activate the virtual environment:
    `& ./venv/Scripts/Activate.bat` <br>
    To install all requirements at once:
    `pip install -r requirements.txt`
    <br>
2. Run the following Flask commands in order to start the server:<br>
    To set a development server:
    `$env:FLASK_ENV="development"`<br>
    Export the python application
    `$ export FLASK_APP="application.py"`<br>
    Run the application
    `$ flask run`<br>
      Open the local link:
     ​ `* Running on http://127.0.0.1:5000/`

[return to top](#table-of-contents) :arrow_up_small:

## Backend

#### application.py
The main application file. Handles module imports, flask server and datababase deployment as well as redirects to all the webpages and loading of resources.

#### helpers.<area>py
Additional support file containing 3 additional functions required for the application to run.

#### chillinquest.<area>db
The database, containing two tables:
Users and Quests, where all of the user's information are stored.

[return to top](#table-of-contents) :arrow_up_small:

#### **/templates**
##### Folder containning the following html and txt templates:
- **account.html** - User Profile & Account management.
- **all.html** - Renders all quests list in the homepage.
- **deletequest.html** - Renders delete quest confirmation popup.
- **done.html** - Renders done quests in the homepage filter.
- **editquest.html** - Renders edit quest page.
- **error.html** - Renders comic error messages
- **farewell.html** - Renders account deletion confirmation popup.
- **firststeps.txt** - Contains tutorial first quest text.
- **index.html** - Renders homepage
- **layout.html** - Main structure of the whole web interface. All other templates are attached to this via flask and jinja syntax.
- **login.html** - Renders login page
- **newquest.html** - Renders new quest UI element.
- **open.html** - Renders open quests in the homepage filter.
- **quest.html** - Renders quests bodies in the homepage. Attached to *queststatus.html*.
- **queststatus.html** - Renders different style button and header for quests depending on completion status. Attached to *all.html*, *done.html* and *open.html*.
- **register.html** - Renders registration page.

#### /static
##### Folder containning the following files:

- **styles.css** - Contains all UI elements' styles
- **multiple images for all the UI** - Logo, icons, default avatar and background.

[return to top](#table-of-contents) :arrow_up_small:

## Frontend

#### Starting and Register Screens

At the main screen the user has the option to register a new account or log in if they already have one.

<img src="README.assets\startandregister.jpg" alt="starting" style="zoom: 100%;" />

[return to top](#table-of-contents) :arrow_up_small:

#### Home

**User card**
A user card with a default picture, name and title will be shown on the left. All of these can be changed at the Profile & Account page, accessible at the top right of the screen.

**Quests summary**
Just below the user will find a small box with its open and completed quests summary.

**Quests bar**
On the right panel the user will have access to a quests bar that provides options to create new quests, search for quests and apply filters. Below is the quest list.

**Tutorial**
The user will be greeted with a quick starting quest showing how to use the application. It's pretty straight-forward.

**Quests**
Quests clicked expand a box with its description, reward, as well as completion, delete and edit buttons at the bottom.

Once marked as completed, the title bar turns gold and completion date and time will be shown.

<img src="README.assets\home.jpg" alt="home" style="zoom: 100%;"/>

[return to top](#table-of-contents) :arrow_up_small:

#### Profile & Account
On this page the user can change their picture, profile information and password, all separately.

A "Bid Farewell" button at the bottom will give the option to delete their account along with all the user's quests and information.

<img src="README.assets\account.jpg" alt="account" style="zoom: 100%;"/>

#### About deletion:
Irreversible changes such as deletion of quests and the user's account will pop up a message requesting the user to confirm their decision.

[return to top](#table-of-contents) :arrow_up_small:

## Development Changes

​ During development, as predicted I had to face some difficulties that made me cutout some of its features with the aim of delivering a solid final product even without them.

[return to top](#table-of-contents) :arrow_up_small:

**Removed features:**

  At start I intended to store user information locally and have cloud save and synchronization options. I moved on to implement it as a server sided DB as it was already within my current knowledge to do it this

  A tree-like UI with quests parenting others as a requirement to unlock the next (e.g. "Play Hotel California", which could only be unlocked after one completed "Learn to play the guitar"). This would probably be a very cool feature but the complexity involved in the current scope of the project was out of reach for me at the time.

[return to top](#table-of-contents) :arrow_up_small:

## Acknowledgements

## About the Author


[return to top](#table-of-contents) :arrow_up_small: 



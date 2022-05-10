
<img src="README.assets/logo.png" alt="MarineGEO circle logo" style="height: 60px; width:auto;"/>

Chillin' Quest is an RPG-like quest maker for life

___

<a href='https://www.edx.org' target="_blank"><img alt='EDX' src='https://img.shields.io/badge/edX®-100000?style=flat&logo=EDX&logoColor=FFFFFF&labelColor=77202E&color=8B8D90'/></a> <a href='https://python.org' target="_blank"><img alt='Python' src='https://img.shields.io/badge/Made_with Python-100000?style=flat&logo=Python&logoColor=ffde57&labelColor=4584b6&color=646464'/></a> <a href='https://developer.mozilla.org/pt-BR/docs/Web/JavaScript' target="_blank"><img alt='JavaScript' src='https://img.shields.io/badge/Made_with JavaScript-100000?style=flat&logo=JavaScript&logoColor=f7df1e&labelColor=000000&color=2F2F2F'/></a> <a href='https://flask.palletsprojects.com/en/2.0.x/' target="_blank"><img alt='Flask' src='https://img.shields.io/badge/Made_with Flask-100000?style=flat&logo=Flask&logoColor=000000&labelColor=FFFFFF&color=2F2F2F'/></a> <a href='https://jquery.com' target="_blank"><img alt='JQuery' src='https://img.shields.io/badge/JQuery-100000?style=flat&logo=JQuery&logoColor=7acef4&labelColor=0769ad&color=FFFFFF'/></a> <a href='https://getbootstrap.com' target="_blank"><img alt='Bootstrap' src='https://img.shields.io/badge/Bootstrap-100000?style=flat&logo=Bootstrap&logoColor=563d7c&labelColor=FFFFFF&color=563d7c'/></a>

## 🎞️ [Video Demo](https://youtu.be/in0qF2AU-YU)

## ✏️ Description

  A web application that allows users to create, manage and customize their real life objectives as RPG-like quests.

## 📜 Table of Contents

<!--ts-->
  - [Objective](#objective)
  - [Project Status](#project-status)
  - [Features](#features)
  - [Tech Stack](#tech-stack)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Project files](#project-files)
    - [application.py](#application)
    - [helpers.py](#helpers)
    - [chillinquest.db](#chillinquest)
  - [UI](#ui)
    - [Starting and Register Screens](#starting-and-register-screens)
    - [Home](#home)
    - [Profile & Account](#profile-account)
  - [Development Changes](#development-changes)
  - [Tests and Compatibility](#tests-and-compatibility)
  - [Acknowledgements](#acknowledgements)
  - [About the Author](#about-the-author)
  - [License](#license)

<!--te-->

## 🎯 Objective

​Built as a Final Project for my commitment to [***Harvard's CS50x - Introduction to Computer Science***](https://cs50.harvard.edu/x/) ***- 2021***.

🔼 [return to top](#table-of-contents)

## 📝 Project Status

As a final project commitment for the course it is completed. However I do intend to develop a new improved mobile version of it in the future with some other cool features and ideas that were cutout from this version and maybe even more.

🔼 [return to top](#table-of-contents)

## ⭐ Features

- Friendly and intuitive UI for users to add, manage, filter and customize their quests.
- Customizable character (as any RPG must be).
- Responsive to screen size and different types of actions, such as mouseover, selection, etc.
- Cool adventurous soundtrack.

🔼 [return to top](#table-of-contents)

## 🧩 Tech Stack

- [Python](https://python.org)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/)
- [WTForms](https://wtforms.readthedocs.io/en/3.0.x/)
- [JavaScript](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript)
- [JQuery](https://jquery.com)
- [Bootstrap](https://getbootstrap.com)
- [SQLite](https://www.sqlite.org/index.html) - through CS50's [python module](https://cs50.readthedocs.io/libraries/cs50/python/)

🔼 [return to top](#table-of-contents)

### 🔩 Requirements

- Python 3.1+

All below modules included in */templates/requirements.txt* for quick installation:
  - cs50
  - Flask
  - flask_session
  - werkzeug
  - flask_wtf
  - wtforms
  - requests
  - python-dotenv*
  
  *This will export the environment variables in the *.flaskenv* file, deploying the server in development mode, which is not suitable for production.

🔼 [return to top](#table-of-contents)

## 📀 Installation

**To run local on Windows:**
1. From command prompt, once in the /chillinquest folder run:<br>
    In order to create the virtual environment:
    `py -3 -m venv venv` <br>
    To activate the virtual environment:
    `& ./venv/Scripts/Activate.bat` <br>
    To install all requirements at once:
    `pip install -r requirements.txt`
    <br>
2. Run the following Flask commands in order to start the server:<br>
    Run the application
    `$ flask run`<br>
      Open the local link:
     ​ `* Running on http://127.0.0.1:5000/`

🔼 [return to top](#table-of-contents)

## 📁 Project Files

#### application
application.&#8203;py - The main application file. Handles module imports, flask server and database deployment as well as redirects to all the webpages and loading of resources.

Important: A unique Secret Key should be provided on line 50 before deploying the server for production. This guarantees the user sessions safety:

`app.config["SECRET_KEY"] = "secret"`


#### helpers
helpers.&#8203;py - Support file containing 4 additional functions required for the application to run.

#### chillinquest
chillinquest.&#8203;db - The database, containing two tables:

 - Users: Where name, ID and title are stored.
 - Quests: Linked through foreign ID to users, where quests and their data are stored.

#### .flaskenv
Configuration file containing the forementioned environment variables required to run the flask application, set to development as default.

NOTE: Should be modified before usage if launching for production.

🔼 [return to top](#table-of-contents)

#### **/templates**
##### Folder containing the following html and txt templates:
- **account.html** - User Profile & Account management.
- **all.html** - Renders all quests list in the homepage right column.
- **deletequest.html** - Renders delete quest confirmation popup.
- **done.html** - Renders completed quests in the right column homepage filter.
- **editquest.html** - Renders edit quest page.
- **error.html** - Renders comic error messages (and maybe easter eggs).
- **farewell.html** - Renders account deletion confirmation popup.
- **firststeps.txt** - Contains the text for first quest tutorial.
- **index.html** - Renders the homepage.
- **layout.html** - Main structure of the whole web interface. All other templates are attached to this via flask and jinja syntax.
- **login.html** - Renders the login page.
- **newquest.html** - Renders new quest UI element.
- **open.html** - Renders open quests in the right column homepage filter.
- **quest.html** - Renders quests bodies in the homepage right column. Attached to *queststatus.html*.
- **queststatus.html** - Renders different style button and header for quests depending on completion status. Attached to *all.html*, *done.html* and *open.html*.
- **register.html** - Renders registration page.

#### /static
##### Folder containning the following files:

- **styles.css** - Contains all UI elements' styles.
- **multiple images for all the UI** - Logo, icons, soundtrack, default avatar and background.

🔼 [return to top](#table-of-contents)

## 💻 UI

#### Starting and Register Screens

<img src="README.assets\startandregister.jpg" alt="starting" style="zoom: 100%;" />

At the main screen the user has the option to register a new account or log in if they already have one.

🔼 [return to top](#table-of-contents)

#### Soundtrack Player

At the top left of all screens the user will find a button to play the Chillin' Quest main theme, _Feet on the Road_, which will play _on loop*_ despite of the screen until clicked again to cancel. Buttons to increase and decrease volume are there as well.

And no, it will **not** play automatically! Don't worry.

_*Due to some current browsers' limitations concerning media autoplay, upon returning to previous pages or receiving an error message of any type the soundtrack may stop playing, returning automatically if the user refreshes or clicks on any internal links. This is something I plan to study and solve in future versions, maybe built on React. I will have to research further._

#### Home

<img src="README.assets\home.jpg" alt="home" style="zoom: 100%;"/>

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

Once marked as completed, the title bar turns gold and the completion date and time captured from the user's system will be shown.

🔼 [return to top](#table-of-contents)

#### Profile & Account

<img src="README.assets\account.jpg" alt="account" style="zoom: 100%;"/>

On this page the user can change their picture, profile information and password, all separately.

A "Bid Farewell" button at the bottom will give the option to delete their account along with all the user's quests and information.

#### About deletion
Irreversible changes such as deletion of quests and the user's account will pop up a message requesting the user to confirm their decision.

🔼 [return to top](#table-of-contents)

## 🔨 Development Changes

During development as predicted I had to face some difficulties that made me cutout some of its features with the aim of delivering a solid final product even without them.

All of these features should be on future any future releases of this project when I work on it:

#### Scrapped features

**Icons Gallery**

I planed on it but decided to leave it open to the user to decide whatever image they want as icons for quest. There's also a default one that comes along if none is chosen.

**Local Storage**

At start I intended to store user information locally and have cloud save and synchronization options. I moved on to implement it as a server sided DB as it was already within my current knowledge to do it this way.

**Tree-like quests UI**

A tree-like UI with quests parenting others as a requirement to unlock the next (e.g. "Play Hotel California", which could only be unlocked after one completed "Learn to play the guitar"). This would probably be a very cool feature but nonetheless very advanced for the front-end. 

**Dynamic quest search tool**

I had not thought about this at the start of the project, and after some research I noticed that to have quests shown dynamically it would require me to change the whole way I implemented the quests through Flask and add some JavaScript to show them or maybe do it all on React, which I still intend to learn. So maybe (probably) on version 2.0.


🔼 [return to top](#table-of-contents)

## 🧪 Tests and compatibility

All tests were run in a Windows Desktop environment.

On browser tests the UI scaling responded well to most of the common mobile devices, such as Moto G, Galaxy, iPhone and iPad:

<img src="README.assets\mobilesok.png" alt="account" style="zoom: 20%;"/>

However there are some exceptions:

On Nest Hub, Galaxy Fold, iPad Pro and Surface Duo the UI is still usable but needs to be dragged to some areas because it does not scale well with these devices yet.  

🔼 [return to top](#table-of-contents) 

## 🏅 Acknowledgements

I wouldn't be able to reach the end of this project without the support of my dear friends. :heart:

I would also like to congratulate and give my sincere thanks Professor David J. Malan, Bryan Yu, Doug Lloyd and all the CS50's staff for such an inspiring and dedicated course. I'm thrilled to start the next one!

🔼 [return to top](#table-of-contents) 

## 🖖 About the Author

 <img style="border-radius: 50%;" src="README.assets/andrew.jpg" width="100px;" alt=""/>

 <b>Andrew Mendes</b>
 Former IT professional getting back to coding
 
 Macaé, RJ - Brazil

[![Github Badge](https://img.shields.io/badge/-AndrewMendes-black?style=flat-square&logo=Github&logoColor=white&link=https://github.com/andrew-mendes)](https://github.com/andrew-mendes) [![Linkedin Badge](https://img.shields.io/badge/-AndrewMendes-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/andrew-mendes-73805720b/)](https://www.linkedin.com/in/andrew-mendes-73805720b/) [![Gmail Badge](https://img.shields.io/badge/-andrewmendes@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:andrewmendes@gmail.com)](mailto:tgmarinho@gmail.com)

## 🔑 License

Chillin' Quest is licensed under the
[Creative Commons Zero v1.0 Universal](https://github.com/andrew-mendes/Chillin-Quest/blob/master/LICENSE.md)


🔼 [return to top](#table-of-contents) 


# Chillin' Quest <img src="README.assets/logo.png" alt="MarineGEO circle logo" style="float: right; height: 60px; width:auto;"/>
RPG-like quest maker for life
___

<a href='https://www.edx.org' target="_blank"><img alt='EDX' src='https://img.shields.io/badge/edX®-100000?style=flat&logo=EDX&logoColor=FFFFFF&labelColor=77202E&color=8B8D90'/></a> <a href='https://python.org' target="_blank"><img alt='Python' src='https://img.shields.io/badge/Made_with Python-100000?style=flat&logo=Python&logoColor=ffde57&labelColor=4584b6&color=646464'/></a> <a href='https://developer.mozilla.org/pt-BR/docs/Web/JavaScript' target="_blank"><img alt='JavaScript' src='https://img.shields.io/badge/Made_with JavaScript-100000?style=flat&logo=JavaScript&logoColor=f7df1e&labelColor=000000&color=2F2F2F'/></a> <a href='flask.palletsprojects.com/en/2.0.x/' target="_blank"><img alt='Flask' src='https://img.shields.io/badge/Made_with Flask-100000?style=flat&logo=Flask&logoColor=000000&labelColor=FFFFFF&color=2F2F2F'/></a> <a href='https://jquery.com' target="_blank"><img alt='JQuery' src='https://img.shields.io/badge/JQuery-100000?style=flat&logo=JQuery&logoColor=7acef4&labelColor=0769ad&color=FFFFFF'/></a> <a href='https://getbootstrap.com' target="_blank"><img alt='Bootstrap' src='https://img.shields.io/badge/Bootstrap-100000?style=flat&logo=Bootstrap&logoColor=563d7c&labelColor=FFFFFF&color=563d7c'/></a>

Video Demo: <URL HERE>

## Description

  A web application that allows users to create, manage and customize their real life objectives as RPG-like quests.

## Table of  Contents

<!--ts-->
  - [Objective](#objective)
  - [Project Status](#project-status)
  - [Features](#features)
  - [Used  Technologies](#used-technologies)
  - [Installation](#installation)
  - [Setup](#setup)
    - [Requirements](#requirements)
  - [Usage](#usage)
    - [Starting and Register Screens](#starting-and-register-screens)
    - [Home](#home)
    - [Profile & Account](#profile-account)
  - [Development Changes](#development-changes)
  - [Acknowledgements](#acknowledgements)
  - [About the author](#about)

<!--te-->

## Objective

​It was built as a Final Project for my commitment to ***Harvard's CS50x - Introduction to Computer Science - 2021***  (<https://cs50.harvard.edu/x/>)

## Project Status

As a final project commitment for the course it is completed. However I do intend to develop a new possible mobile version of it in the future with some other features and ideas that were cutout from this version.

## Features

- Friendly and intuitive UI for users to add, manage, filter and customize their quests.
- Responsive to screen size and different types of actions, such as mouseover, selection, etc.
- Customizable character (as any RPG must be).

## Used  Technologies

​ Chillin' Quest was built as a Python application taking advantage of Pallets Project's Flask, JavaScript to generate HTML templates for its pages and their elements.

​ Most of the CSS used was created over customized Bootstrap elements. There's a bit of JQuery too.

​ It also uses the own course's SQL module just for convenience.

​ Pallets Projects' Werkzeug modules provide additional safety to password storage and WTForms were also used in some small portion to enable inputs according to the website's style.

## Installation

​  TODO

## Setup

### Requirements

cs50
Flask
flask_session
werkzeug
flask_wtf
wtforms
requests

  **To run locally:**

  Inside a Python environment:

  1. From the terminal, once in the same folder path of the file `...\chillinquest\`  you can install all of them at once running the following command in the terminal:

     `pip install -r requirements.txt`
<br>
  2. Run the Flask commands in order to start the server:

     `$ export FLASK_APP="application.py"`

     `$ flask run`

     ​ `* Running on http://127.0.0.1:5000/`

## Usage

#### Starting and Register Screens

At the main screen the user has the option to register a new account or log in if they already have one.

<img src="README.assets\startandregister.jpg" alt="starting" style="zoom: 100%;" />

### Home

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

<img src="README.assets\home.jpg" alt="starting" style="zoom: 100%;"/>

### Profile & Account
On this page the user can change their picture, profile information and password, all separately.

A "Bid Farewell" button at the bottom will give the option to delete their account along with all the user's quests and information.

<img src="\README.assets\account.jpg" alt="starting" style="zoom: 100%;"/>

#### About deletion:
Irreversible changes such as deletion of quests and the user's account will pop up a message requesting the user to confirm their decision.

## Development Changes

​ During development, as predicted I had to face some difficulties that made me cutout some of its features with the aim of delivering a solid final product even without them.

**Removed features:**

  Ideally users quests information would be stored locally and have cloud save and synchronization options. I moved on to implement it as a server sided DB as it was already within my current knowledge to do it this

  A tree-like UI with quests parenting others as a requirement to unlock the next (e.g. "Play Hotel California", which could only be unlocked after one completed "Learn to play the guitar"). This would probably be a very cool feature but the complexity involved in the current scope of the project was out of reach for me at the time.


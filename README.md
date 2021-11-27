# <img src="C:\Users\Andru\Desktop\chillinquest\chillinquest\static\logo.png" alt="logo" style="zoom: 50%;" />

## **Chillin' Quest**

Video Demo: <URL HERE>

## **Description**

​	Chillin' Quest is a web application that allows you take real life objectives as RPG based quests, customize them and even apply rewards to yourself if you want. Its intention is to bring to your life the flavor of being an adventurer and reminds you of your own accomplishments, often easy to forget in face of everyday hardships.

​	Do your own life quests, at your own pace and be chill about it.

## Table of  Contents

<!--ts-->

* [Features](#Features)
* [Objective](#Objetive)
* [Used Technologies](#Used Technologies)
* [Development Details](#Development Details)
* [Installation](#Installation)
* [Setup](#Setup)
  * [Requirements](#Requirements)
* [Usage](#Usage)
  * [Starting Screen](#Starting Screen)
  * [Register](#Register)
  * [Login](#Login)
  * [Home](#Home)
    * [Profile Card](#Profile Card)
    * [Quest Summary](#Quest Summary)
    * [Quests Navbar](#Quests Navbar)
    * [Quest List](#Quest List)
    * [Quest Box](#Quest Box)
      * [Contents](#Contents)
        * [Bottom Options](#Bottom Options)
        * [Mark as completed](#Mark as completed)
        * [Edit](#edit)
        * [Delete](#Delete)
  * [Profile & Account](#Profile & Account)
    * [Adventurer's Tag](#Adventurer's Tag)
    * [Profile Picture](#Profile Picture)
    * [Change Password](#Change Password)
    * [Delete Account](#Delete Account)
  * [Errors](#Errors)
* [About the Author](#About the Author)
* [References](#References)

<!--te-->

## **Features**

- Friendly interface to add and manage your quests (such adventurous).
- Customizable rewards (you should celebrate your wins!).
- Upload icons to your quests (because it's cool).
- Customizable character (yourself or whoever you want to be)

## Objective

​	It was initially made as a Final Project for my commitment to ***Harvard's CS50x - Introduction to Computer Science - 2021***  (https://cs50.harvard.edu/x/), however the purpose of this application is deeply connected to the care I have for mental health and quality of life and of course to RPG games, which made a big part of my life and development as a person. So I became fonder of it to the point that I started planning on developing a (probably) standalone mobile version of it, on which I plan to include a lot more customization resources and some different architecture details that enable a closer RPG-like immersion to it.

## Used  Technologies

​	Chillin' Quest was built as a Python application taking advantage of Pallets Project's Flask, JavaScript to generate HTML templates for its pages and their elements.

​	Most of the CSS used was built over customized Bootstrap elements. There's a bit of JQuery too.

​	It also uses the own course's SQL module just for convenience.

​	Pallets Projects' Werkzeug modules provide additional safety to password storage and WTForms were also used in some small portion to enable inputs according to the website's style.

## Development Details

​	During development, as predicted I had to face some difficulties that made me cutout some of its features with the aim of delivering a solid final product even without them.

Removed features:

- Ideally these would be stored locally and have cloud save and synchronization options.

- A tree-like UI with quests parenting others as a requirement to unlock the next (e.g. "Play Hotel California", which could only be unlocked after you complete "Learn to play the guitar").

  This would probably be a very cool feature but the complexity involved in the current scope of the project was out of reach for me at the time. 

  

  I haven't given up on both of these ideas and hope to come up with more of them for future versions of it.

## Installation

​		TODO

## Setup

### 	Requirements

​		There is an included txt file with the following list of requirements.

- cs50

- Flask

- flask_session

- werkzeug

- flask_wtf

- wtforms

- requests

  

  **To run locally:**

  Inside a Python environment:

  1. From the terminal, once in the same folder path of the file `...\chillinquest\`  you can install all of them at once running the following command in the terminal: 

     `pip install -r requirements.txt`

  2. Then run the Flask commands in order to start the server:

     `$ export FLASK_APP="application.py"`

     `$ flask run`

     ​	`* Running on http://127.0.0.1:5000/`

## Usage

### 	Starting Screen

At the starting screen TODO

<img src="C:\Users\Andru\Desktop\chillinquest\chillinquest\assets\starting.jpg" alt="starting" style="zoom: 33%;" /> 

### 	Register

### 	Login

### 	Home





## Resource references

<img src="C:\Users\Andru\Desktop\python-logo-master-v3-TM-flattened.png" alt="python-logo-master-v3-TM-flattened" style="zoom: 33%;" /> 

​	https://www.python.org

<img src="C:\Users\Andru\AppData\Roaming\Typora\typora-user-images\image-20211123211016789.png" alt="image-20211123211016789" style="zoom:25%;" /> 

​	https://palletsprojects.com/p/flask/

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/JavaScript-logo.png/600px-JavaScript-logo.png" alt="File:JavaScript-logo.png" style="zoom:15%;" /> 

​	https://developer.mozilla.org/pt-BR/docs/Web/JavaScript

<img src="https://getbootstrap.com/docs/5.0/assets/brand/bootstrap-logo.svg" alt="Bootstrap" style="zoom: 20%;" /> 

​	https://getbootstrap.com

<img src="https://werkzeug.palletsprojects.com/en/2.0.x/_static/werkzeug.png" alt="Logo" style="zoom: 67%;" /> 

​	https://werkzeug.palletsprojects.com/en/2.0.x/

<img src="C:\Users\Andru\AppData\Roaming\Typora\typora-user-images\image-20211123211829636.png" alt="image-20211123211829636" style="zoom: 50%;" /> 

​	https://wtforms.readthedocs.io/en/3.0.x/






# Blogs

## Built By [Dennis](https://github.com/oodennis20/Blogs)

## Description
An application that allows users to use that one minute wisely. The users will submit their one minute blogs and other users will view them and leave comments to give their feedback on them.

## User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I would like to:
* View the blog posts submitted.
* Comment on blog posts.
* View the most recent posts
* Alerted when a new post is made by joining a subscription.
* comment on the different blogs and leave feedback.

## Blogger Abilities
These are the behaviours/features that the application implements for use by the writter/Blogger

Bloggers would like to:
* Sign in to the blog application
* Create a blog from the application
* Delete comments that I find insulting or degrading
* Update or delete blogs I have created.

## [Specifications](SPECS.md)

## SetUp / Installation Requirements
### Prerequisites
* python3.6
* pip
* virtualenv
* Requirements.txt

### Cloning
* In your terminal:

        $ git clone https://github.com/oodennis20/Blogs/
        $ cd Blogs

## Running the Application
* Creating the virtual environment

        $ python3.6 -m venv --without-pip virtual
        $ source virtual/bin/env
        $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Flask and other Modules

        $ see Requirements.txt

* To run the application, in your terminal:

        $ chmod +x start.sh
        $ ./start.sh

## Testing the Application
* To run the tests for the class files:

        $ python3.6 manage.py test

## Technologies Used
* Python3.6
* Flask

## [License](license.txt)

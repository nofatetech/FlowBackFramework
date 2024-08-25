# FlowBack Framework

A back-to-basics and simple way of creating Backend functionality.

[This file in under construction..]

## About

This is inspired by concepts like OOP, MVC, Frontend/Backend, APIs, REST, Granularity, SOA, KISS, Old-school web technology, Low-code technology,the Godot Game Engine. 

It is not inspired by the whole mess that is the JS world. Virtual dom, infinite dependencies. There is good and bad stuff in the JS, mostly bad. Layers upon layers upon layers.. 

Easy development: this is aimed at creatives who can code a little or more. Designers who learned CSS and the needed JS, developers that want to do cool stuff without being top level Sr Software Arquitects and DevOps experts and such. The aim is to have a simple way to work with top-end tools, technologies and architecture, reliable, easy and as light as possible, and open to the developers creativity, a simple order for your creative mess.

Just a concept: Beginners, intermediates and pros can use this since it is basically just a way of working to implement to your needs. 

Any language or framework: What is important is the concepts like Models (Data), Workflows (Flows), Other sources of cool stuff (Sources), the amazing things that can be done (Views, apps, interconnetivity, etc). This started with Python because of I like it, it pretty much comes in any OS, it is easy, simple, and more, but the idea of FlowBack is to have simple concepts in mind, and do your own thing. One can port this Python version to any other framework. Here we like stuff that is as core as possible, trustworthy, little dependencies, etc, so things like Laravel or SpringBoot come to mind that could be considered to be close to this ideology, but you can use anything you like, just know that if you keep using JS frameworks you are helping make the dev world sad and slow :(

This was born as an idea to bring full "pro" web backend technology for the Godot Game Engine.

## Install and Setup

- Put the files in a folder that will hold your Backend server
- Create a .env file (copy from .end.demo) and setup your data
- Setup your Data, Flows, Sources
- Setup your main pPp Database (optional, you could technically work without your own database. We can recommend Supabase.com to start easy)
- Run the "install_and_run" file (BAT for windows, SH for Mac/Linux). This will run the http server probably in http://127.0.0.1:5000
- The test_requests.rest file has sample HTTP calls to test your framework. We use the REST Client (Huachao Mao) VSCode Extention for easy testing.
- Use migrations optionally to manage your DB.

Flask Migration commands:

flask db init
    > Initializes the migrations directory.
flask db migrate -m "message"
    > Generates a new migration script based on model changes.
flask db upgrade
    > Applies the migrations to the database.
flask db downgrade
    > Rolls back the last migration applied.
flask db current
    > Shows the current migration version applied to the database.
flask db stamp <revision>
    > Stamps the database with a specific revision without running migrations.
flask db migrate --autogenerate -m "message"
    > Automatically generates a migration script based on detected changes.
flask db downgrade <revision>
    > Rolls back the database to a specific revision.
flask db history
    > Displays the history of all applied migrations.
flask db merge <revision1> <revision2> -m "message"
    > Merges two branches in the migration history.




## Development Guide

For now, you can search for this comment "# !!!!!!!" in the sources/data/flows files that we have left in places where you need to take a look and work on.

### Data

### Flows

### Services

### Concepts

### Deployment




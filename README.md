# Hello my dear
- In the proccess of discovering my project you can notice that it doesn't fit requierements for 100%. It was done intentionally.
- What? Why?
- In case you want me to do your real task.
- How to verify the solution than?
- There is a small difference. Instead of passing randomly named fields into service, you pass properly named arguments. And based on those fields (with validation) you get your guess
- Okay. But that means you haven't done the required task?
- More or less, if you look deaply you can see that your task ALSO could be done by me, my service is not that far from what you wanted, just add checks for field name pattern and that's it. But in case of cheating I changed it a bit. And all of that means, that I have such level to work with you.
- Okay, okay, I got you. Let's see what you got for me.

## How to run this project
I higly recommend you to have ```make``` util install on your machine, but if you don't just go to Makefile and copy the requeired commands. E.g. ```make venv``` might be replaced with ```python3 -m venv venv``` and so on

- Run ```make venv``` to create virtualenv, don't forget to activate it
- Run ```make install``` to install all dependencies
- Run ```make dmongo``` to run mongoDB container.
- Run ```make migrate``` to apply all migrations
- Run ```make loaddata``` to load all test forms and fields
- Run ```make run``` to run the development server

You may want to access the admin panel, run ```make createsuperuser``` to create admin user

## Docs
There is docs for all endpoints, located on ```http://127.0.0.1:8000/api/docs```

## Admin
You can access admin panel on ```http://127.0.0.1:8000/admin```

## Tests
You can run ```make test``` to run tests

## MongoDB
If you will ever need to connect to MongoDB container, you can run ```make connect_mongo```

## For empoyers
You may be interested in those files:
- models.py, it has kinda huge struct, it was made as the base for grow of the project
- views.py
- utils.py, main guessing logic (not perfect)
- tests.py, please read the docstring
- validators.py
- Makefile, all the required commands

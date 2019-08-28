# Gousto Backend API challenge

## Installation

### Python

This project has been developed and tested using Python 3.7.4.
To install it, please follow the instructions on the 
[Python website](https://www.python.org/downloads/).

### Dependencies

This project requires some specific dependencies, 
please run the following command to install them:

```bash
pip install -r requirements.txt
```


## Usage

### Run the API

Simply run the following command to run the webserver:

```bash
python main.py
```

This will instantiate a webserver running locally on port `8080`.
There is no parametrization for the port at the moment but this 
can be easily changed in the `main.py` file.

### API Documentation

The API documentation can easily be accessible at `http://localhost:8080/docs`.
It provides a nice interface to explore the different endpoints 
and consume them.

### Tests

To run the tests run the following command:
```bash
pytest tests
```


## Notes

### Technology choices

To complete this project I've decided to use 
[FastApi framework](https://fastapi.tiangolo.com/). 
The reasons being that it provides all the routing logic, and middlewares 
that I needed to complete this challenge.
Another reason for this choice is also that I've never used this framework
but was interested in it, so I've decided to give it a go and play around.


The `pytest` framework was used rather the default `unittest` module, 
the reason is that I have more experience with it and personally like it's
fixture concepts and mocking mechanisms.


### Improvements

* This project can easily be improved as I have taken some shortcuts.
First we can definitely parametrize the http port by either passing it
as a command argument or a environment variable.

* We can also potentially do the same for the recipe csv as it is currently 
hardcoded.

* The automated documentation needs lots of love, it currently only displays
the available endpoints without any proper description of them.
This can easily be improved via the `FastApi` features.

* Finally if we were using a database or calls to external endpoints I would 
have build a docker image and write some integrations tests to make sure 
that all the components were able to communicate with each other.

* Re-Finally, before sending the completed challenge I've just realised that
I was supposed to put it on GitHub, so I only have an init commit,
and the most recent one to edit this file. I'm sorry you can't have a full
proper history of all the changes.


### Impressions

I liked working on this challenge, I think it was nice to work on some recipes.
However you're missing some French recipes in it!!!

Anyway thank you for the fun ;)

# Shopping Hackathon
Applitools Holiday Shopping Hackathon

## Overview

Holiday Shopping Hackathon and Applitools AI with Ultrafast Grid 
Using Pytest and Selenium

## Prerequisites
Python 3 and pip

## Installation

Clone the repo:

```
  $ git clone https://github.com/cauvery/ShoppingHackathon.git
```

Install `pip` the python package installer, if you don't already have it:

```
  $ sudo easy_install pip
```

Next, install the required dependencies:

```
  $ pip install -r requirements.txt 
```

## Usage

Using pytest:

To execute all tests 
```
  $ pytest --env=v1 -s tests
```
Default executes on version v1 if no env is provided (-s to print console output)
```
  $ pytest -s tests
```

To execute Hackathon tests 
```
  $ pytest --env=v1 -s tests/HackathonTests
```

To Execute the tests on different version, change --env=v2 as below
```
  $ pytest --env=v2 -s tests/HackathonTests
```

To generate html report use --html command line option
```
  $ pytest --env=v2 -s tests/HackathonTests  --hmtl report.html
```
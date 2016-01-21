# random-cat

random-cat is a amazing modul to get cat images. This Project won't be
posible without the great Cat API (http://thecatapi.com).

## Big Thanks to the great Cat API

Go and visit [http://thecatapi.com](http://thecatapi.com)

![alt text](http://thecatapi.com/api/images/get?type=gif "See? amazing!")

## Installation

Install through **pip**.

```
$ pip install random-cat
```

or get from source

```
$ git clone https://github.com/gravmatt/random-cat
$ cd random-cat
$ python setup.py install
```

## Usage

The cat module has just one function **getCat()** with three optional arguments.

### Arguments

**directory** - default is the current directory

**filename** - default is a unique id

**format** - default is _png_. optional _png_, _jpg_ and _gif_ is available

```
import cat

# cat.getCat(directory=None, filename=None, format='png')

cat.getCat(directory='/users/tor', filename='cat', format='gif')

# /users/tor/cat.gif
```

The function return the image name (absolute path if directory is specified) of the image.

### Command Line

You can also request an image on the terminal.

```
$ randomcat [format] [file]

# Example:

$ randomcat gif /users/tor/cat.gif
```

The two arguments _format_ and _file_ are optional.

You can select the formats _png_, _jpg_ or _gif_.

The command return the filename/absolute path of the image to the standard output (stdout).

### Licence

The MIT License (MIT)

# [poetry-hivarun-com](poetry.hivarun.com)

###### _A Poetry Collection._

#

A site featuring a collection of poems fetched from a google document

-   `Update collection from a google doc`
-   `Minimalistic UI with parallax`
-   `Index, all poems, random pick pages`

#

## Features

#

-   Google docs api to authorie reading document and updating on site
-   Minimalist Django server with a small collection of poems stores in a json file
-   Clean and minimalist UI with vibrant colors, parallax
-   Plain html and css in django templates
-   Site functionality like index, all poems view, single poem view and random pick.

#

## Tech and Dependencies

#

A tiny, minimalist single page django server that needs python to run

-   [Python 3](https://www.python.org/download/releases/3.0/)
-   [Django 3](https://www.djangoproject.com/)
-   [Virtualenvwrapper](pypi.org/project/virtualenvwrapper)

#

Some google fonts

-   [Caveat](https://fonts.google.com/specimen/Caveat)
-   [Chilanka](https://fonts.google.com/specimen/Chilank)
-   [Montserrat Italic](https://fonts.google.com/specimen/Montserrat?query=Mont)

#

## Installation

Requires [Python 3](python.org) to run.

#

Create virtual environment

```sh
mkvirtualenv <env_name>
```

List all virtualenvwrappers in system

```sh
lsvirtualenv
```

Start virtual environment

```sh
workon <env_name>
```

Install dependencies in virtual environment

```sh
pip install -r requirements.txt
```

Run django server on port 8000

```sh
py tiny_django.py runserver 8000
```

Close virtual environment when done with running the program

```sh
deactivate
```

#

## To Do

-   Fix 'tittleArray' key to 'title' as it's not an array
-   Fix randon quoates(") trailing lines
-   Store alreday opened poems through random and don't open them again
-   Categories feature
-   Poem view count feature
-   Other favourites features to features other poets
-   Advance search with suggestions
-   Add SEO optimised meta tags
-   Update latest entries
-   Add scroll to top button
-   Store krivate keys in .env file
-   Use the following for pixlatted background-image svg while scalling
    [option 1 stack overflow](https://stackoverflow.com/questions/11856161/using-svg-as-css3-background-image-with-scaling)

```
<div class="btn"></div>
<div class="z">
<div class="btn"></div>
</div>
.btn {
    width: 100px;
    height: 100px;
    background: url(http://upload.wikimedia.org/wikipedia/en/c/ce/SVG-logo.svg) no-repeat;
}
.z {
    zoom: 300%;
    -moz-transform: 0 0;
    -moz-transform: scale(3);
}
```

[option 2 stack overflow](https://stackoverflow.com/questions/50209072/svg-background-image-scaling-issue)
Do not add width and height to the SVG Element, or background-size:cover in CSS. The SVG way of positioning and sizing works via attribute preserveAspectRatio:

```
<svg xmlns="http://www.w3.org/2000/svg"
     viewBox="0 0 347 385" preserveAspectRatio="xMaxYMax slice">
```

Option 3: exposrt svg at larger size

#

#

**Hope you like it! Start the repo if you do. :)**

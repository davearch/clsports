SportsCommand

Hack Arizona Hackathon 2015

download it from this repository:
git clone git@github.com/davearch/clsports


install the python packages from the root of tbe directory:
python setup.py install


I have only tested this program on Slackware Linux,
so I'm not sure how it will work out on other platforms.

the program spits out an interactive script and
calling "which clsportsClient" should give you:
/usr/bin/clsportsClient


simply typing the command clsportsClient should bring up the program

right now it's not very good.

the api i was using for statistics is a paid service but since I
only signed up for the trial version, i've already ran out of http
requests.

the text user interface has limited functionality. you can basically
either view nfl teams or popular players. that, coupled with the
broken update mechanism, makes this program pretty worthless. i have a few hardcoded players and there is only names but no stats.

Originally i wanted to query for information just once, place the data
into a database, and only query again if the information was not present.
the database.py file was giving me a bunch of runtime errors that was
simply taking too long, so i stopped working on it.

I'm definitely going to keep working on this. I envision a program interface similar to emacs or vim, and I want to give the user the ability to customize her commands and see personalized fantasy football stuff, as well as get 
updates by email or text.

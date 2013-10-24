#!/bin/bash

# Credits: Adopted from http://community.webfaction.com/questions/12718/installing-flask

# Step 1 - fill in these variables with your Application Name and URL Path:
APPNAME="basic_app"
URLPATH="/basic"

rm -r $HOME/webapps/$APPNAME/htdocs

# Step 2 - create virtual env
cd $HOME/webapps/$APPNAME/$APPNAME/
virtualenv-2.7 env
echo "run - source env/bin/activate from main folder"
echo "run - pip install -r requirements.txt after you are in virtual env"

# Step 3 - configure the apache wsgi.py to point to our app
sed -i "s^WSGILazyInitialization On^WSGILazyInitialization On\nWSGIScriptAlias / $HOME/webapps/$APPNAME/$APPNAME/wsgi.py^" $HOME/webapps/$APPNAME/apache2/conf/httpd.conf
sed -i "s^AddHandler wsgi-script .py^AddHandler wsgi-script .py\n    RewriteEngine on\n    RewriteBase /\n    WSGIScriptReloading On^" $HOME/webapps/$APPNAME/apache2/conf/httpd.conf
sed -i "s/htdocs/$APPNAME/g" $HOME/webapps/$APPNAME/apache2/conf/httpd.conf

# Step 4 - Restart Apache server
$HOME/webapps/$APPNAME/apache2/bin/restart

FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt update
RUN apt install apache2 php -y

ADD prob/index.php /var/www/html/index.php
ADD prob/textarea.css /var/www/html/textarea.css
ADD prob/alert.js /var/www/html/alert.js
ADD prob/Is_this_the_flag/index.php /var/www/html/Is_this_the_flag/index.php

RUN rm /var/www/html/index.html

EXPOSE 80

CMD ["apachectl", "-D", "FOREGROUND"]
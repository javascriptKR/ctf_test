FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt update
RUN apt install apache2 php -y

ADD prob/index.php /var/www/html/index.php
ADD prob/robots.txt /var/www/html/robots.txt
ADD prob/robot.png /var/www/html/robot.png
ADD prob/nobody_robot_flag/index.php /var/www/html/nobody_robot_flag/index.php

RUN rm /var/www/html/index.html

EXPOSE 80

CMD ["apachectl", "-D", "FOREGROUND"]
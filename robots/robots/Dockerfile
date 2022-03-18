FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt update
RUN apt install apache2 php -y

ADD robots/index.php /var/www/html/index.php
ADD robots/nobody_robot_flag/index.php /var/www/html/nobody_robot_flag/index.php

RUN rm /var/www/html/index.html

EXPOSE 80

CMD ["apachectl", "-D", "FOREGROUND"]
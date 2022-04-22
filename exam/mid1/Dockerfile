FROM ubuntu:bionic
RUN apt-get -y update
RUN apt-get -y install apt-utils
RUN apt-get -y install openssh-server
RUN apt-get -y install gcc
RUN apt-get -y install python3.8
RUN apt-get -y install python3-flask
RUN apt-get -y install python3-jwcrypto
RUN sed -E 's/^#(PermitRootLogin )prohibit-password/\1yes/' /etc/ssh/sshd_config -i
RUN echo 'root:toor' | chpasswd
RUN service ssh start
RUN mkdir /var/log/python
RUN mkdir /var/log/python/flask
RUN touch /var/log/python/flask/app.log
COPY src/ /home/src/
COPY confusers/git /usr/local/sbin/
COPY confusers/mongodb /usr/local/bin
COPY confusers/nginx /usr/sbin
COPY confusers/node /usr/bin
COPY confusers/postgres /sbin
COPY confusers/redis /bin
COPY confusers/webhooks /tmp
WORKDIR /home/src/
RUN python3 migrations.py
RUN chmod 777 run.sh
EXPOSE 5000
EXPOSE 22
CMD ["./run.sh"]

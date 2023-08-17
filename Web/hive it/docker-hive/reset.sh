sleep 40 && while true;
do
/opt/hive/bin/beeline -u jdbc:hive2://localhost:10000 -f /usr/local/start.hql && echo "$(date) - Reset done" >> /tmp/reset.log && sleep 300;
done

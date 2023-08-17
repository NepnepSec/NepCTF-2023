FROM bde2020/hive:2.3.2-postgresql-metastore

COPY reset.sh start.hql flag /tmp/

RUN echo -n "#!" > /usr/local/bin/reset.sh && echo "/bin/bash" >> /usr/local/bin/reset.sh \
	&& mv /tmp/start.hql /usr/local/start.hql && chmod 444 /usr/local/start.hql \
	&& echo -n "#!" > /usr/local/bin/new_entry.sh \
	&& echo "/bin/sh" >> /usr/local/bin/new_entry.sh \
	&& echo "/usr/local/bin/reset.sh &" >> /usr/local/bin/new_entry.sh \
	&& echo "entrypoint.sh startup.sh" >> /usr/local/bin/new_entry.sh \
	&& sed -i 's/\r//' /tmp/reset.sh && cat /tmp/reset.sh >> /usr/local/bin/reset.sh \
	&& chmod 500 /usr/local/bin/new_entry.sh && chmod 500 /usr/local/bin/reset.sh \
	&& rm /tmp/reset.sh \
	&& mv /tmp/flag /flag && chmod 444 /flag

ENTRYPOINT ["/usr/local/bin/new_entry.sh"]

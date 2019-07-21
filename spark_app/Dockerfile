# spark app

FROM bde2020/spark-submit:2.4.1-hadoop2.7

MAINTAINER Cecile Tonglet <cecile.tonglet@tenforce.com>

COPY template.sh /

# Copy the requirements.txt first, for separate dependency resolving and downloading
ONBUILD COPY requirements.txt /app/
ONBUILD RUN cd /app && \
            pip3 install -r requirements.txt

CMD ["/bin/bash", "/template.sh"]


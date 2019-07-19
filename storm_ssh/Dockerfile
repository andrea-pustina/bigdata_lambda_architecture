FROM storm

RUN apt update && \
    apt install openssh-server -y

RUN echo 'root:qwerty' | chpasswd

RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    service ssh stop && \
    service ssh start

RUN apt install apt-utils python3 python3-pip -y && \
    pip3 install virtualenv

RUN pip3 install streamparse

RUN mkdir -p /var/log/storm/streamparse

RUN pip3 install pykafka

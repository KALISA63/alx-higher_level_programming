# 0x0F. Python - Object-relational mapping dockerfile

FROM jupyter/scipy-notebook
LABEL maintainer="Patrick DeYoreo <pdeyoreo@gmail.com>"

USER root

RUN ln -sf /opt/conda/bin/python3 /usr/bin/python3

RUN apt-get update && apt-get install -y \
    libmysqlclient-dev \
    libssl-dev \
    mysql-client \
    mysql-server \
    zlib1g-dev && apt-get clean

RUN HOME=/root pip install mysqlclient SQLAlchemy

COPY mysql-configure mysql-populate /tmp/build/

RUN /tmp/build/mysql-populate
RUN /tmp/build/mysql-configure
RUN rm -rf /tmp/build

RUN sed -i 's/^#%sudo\t.*/%sudo\tALL=(ALL:ALL) NOPASSWD: ALL/' /etc/sudoers
RUN usermod -aG sudo $NB_USER

COPY entrypoint /usr/local/lib/

USER $NB_UID

CMD ["/usr/local/lib/entrypoint"]

FROM quay.io/ansible/ansible-runner:latest
ARG ANSIBLE_GALAXY_CLI_COLLECTION_OPTS=
USER root
ADD . /runner/project
WORKDIR /runner/project
ENV PIP_NO_BINARY=jpy
RUN dnf install -y java-17-openjdk-devel maven
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk
RUN dnf install -y gcc python38-devel
RUN pip3 install --upgrade pip setuptools
RUN ansible-galaxy role install -r requirements.yml --roles-path /usr/share/ansible/roles
RUN ansible-galaxy collection install $ANSIBLE_GALAXY_CLI_COLLECTION_OPTS -r requirements.yml --collections-path /usr/share/ansible/collections
RUN pip3 install -r requirements.txt


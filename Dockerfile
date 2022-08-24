FROM quay.io/ansible/ansible-runner:latest
ARG ANSIBLE_GALAXY_CLI_COLLECTION_OPTS=
USER root
ADD . /build
WORKDIR /build
RUN dnf install -y gcc python38-devel
RUN pip3 install --upgrade pip setuptools
RUN ansible-galaxy role install -r requirements.yml --roles-path /usr/share/ansible/roles
RUN ansible-galaxy collection install $ANSIBLE_GALAXY_CLI_COLLECTION_OPTS -r requirements.yml --collections-path /usr/share/ansible/collections
RUN pip3 install -r requirements.txt


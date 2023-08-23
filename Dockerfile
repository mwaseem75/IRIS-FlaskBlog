ARG IMAGE=intersystemsdc/iris-community:preview
FROM $IMAGE

USER root

# Update package and install sudo
RUN apt-get update && apt-get install -y \
	nano \
	python3-pip \
	python3-venv \
	sudo && \
	/bin/echo -e ${ISC_PACKAGE_MGRUSER}\\tALL=\(ALL\)\\tNOPASSWD: ALL >> /etc/sudoers && \
	sudo -u ${ISC_PACKAGE_MGRUSER} sudo echo enabled passwordless sudo-ing for ${ISC_PACKAGE_MGRUSER}

# create dev directory
WORKDIR /opt/irisapp
RUN chown ${ISC_PACKAGE_MGRUSER}:${ISC_PACKAGE_IRISGROUP} /opt/irisapp
USER ${ISC_PACKAGE_MGRUSER}

# Copy source files to image
COPY . /opt/irisapp

ENV SRC_PATH=/opt/irisapp
# Requirement for embedded python
RUN pip3 install -r ${SRC_PATH}/src/Python/requirements.txt

RUN iris start IRIS \
	&& iris session IRIS < /opt/irisapp/iris.script && iris stop IRIS quietly

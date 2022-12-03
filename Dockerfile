FROM python:3
USER root

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt-get install -y vim less
RUN pip install --upgrade pip
RUN pip install numpy
RUN pip install --upgrade setuptools
RUN pip install pandas
RUN pip install slackweb
#boto3だけpipで入らないからpip3使う
RUN pip3 install boto3
#googleapiを使用するときに使う
RUN pip install Request
RUN pip install google-auth-oauthlib
RUN pip install google-auth-httplib2
RUN pip install google-api-python-client
RUN pip install docopt
RUN pip install lxml

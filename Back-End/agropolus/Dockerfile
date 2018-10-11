 FROM python:3
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /back_end
 WORKDIR /back_end
 ADD requirements.txt /back_end/
 RUN pip install -r requirements.txt
 ADD . /back_end/

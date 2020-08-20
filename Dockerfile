FROM python:3.8.5-alpine3.12

MAINTAINER Alexander Mollison-Ball <AlexHBall.github.io>

EXPOSE 8000

RUN apk add --no-cache gcc python3-dev musl-dev

ADD . /django_ec2

WORKDIR /django_ec2

RUN pip install -r requirements.txt

# RUN python django_ec2_project/manage.py makemigrations

# RUN python django_ec2_project/manage.py migrate

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
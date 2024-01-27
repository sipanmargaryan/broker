FROM python:3.10.0

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV TF_ENABLE_ONEDNN_OPTS 3


WORKDIR /app
COPY requirements.txt pyproject.toml ./

RUN pip install --upgrade pip
RUN pip3 --no-cache-dir install -r requirements.txt
RUN poetry config virtualenvs.create false
RUN poetry install

ADD . /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


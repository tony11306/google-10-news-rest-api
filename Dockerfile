FROM python:3.9.0
WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN locale-gen zh_TW.UTF-8

EXPOSE 5000-5000
ENV PYTHONIOENCODING=utf-8
ENV FLASK_APP=main.py
ENV LANG zh_TW.UTF-8
COPY . /app

ENTRYPOINT [ "flask"]
CMD [ "run", "--host", "0.0.0.0" ]



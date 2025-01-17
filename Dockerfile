FROM python

WORKDIR . .

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD bash start.sh
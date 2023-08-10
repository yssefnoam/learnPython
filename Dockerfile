FROM python:3.8.2


COPY ./ /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD streamlit run /app/main.py
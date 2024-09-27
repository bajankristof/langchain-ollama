FROM python:3.12

ARG MODEL=llama3.2
ENV MODEL="$MODEL"

RUN pip install langchain-openai

WORKDIR /

COPY app app

CMD ["python", "-B", "-m", "app"]

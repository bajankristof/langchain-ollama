FROM ollama/ollama

ARG MODEL=llama3.2
ENV MODEL="$MODEL"

WORKDIR /app
COPY . .
RUN chmod +x *.sh
RUN ./install.sh

ENTRYPOINT ["bash", "-c"]

CMD ["/app/serve.sh"]

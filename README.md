# Sample Langchain / Ollama Server

# Usage

## Start the server

```bash
docker compose up -d
```

## Send prompts to the LLM

```bash
curl -X GET -d 'Show the failed tasks yesterday' http://localhost:8080
curl -X GET -d 'Show the closed tasks two days ago' http://localhost:8080
curl -X GET -d 'Show the open tasks today' http://localhost:8080
curl -X GET -d 'Show the last successful task of the QuickTime app' http://localhost:8080
curl -X GET -d 'Show the last task of the Why Not app' http://localhost:8080
```

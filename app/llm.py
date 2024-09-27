import os

from enum import Enum
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

class TaskStatus(Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    SUCCESS = "success"
    FAILURE = "failure"

@tool(parse_docstring=True)
def fallback() -> str:
    """
    Fallback tool for the chatbot.
    This should be called when the prompt is ambiguous or the model is unsure of the response.
    """
    return "I'm sorry, I don't understand."

@tool(parse_docstring=True)
def search_tasks(date_from: None | int = None, date_to: None | int = None, statuses: None | list[TaskStatus] = None) -> bool:
    """
    Search for tasks based on the date range and status.

    Args:
        date_from: The start date of the search range in unix milliseconds.
        date_to: The end date of the search range in unix milliseconds.
        statuses: The list of status values that the searched tasks should be in.
            The possible values are "pending", "processing", "success", and "failure".
            Only "success" and "failure" is considered as closed statuses.
    """
    return True

@tool(parse_docstring=True)
def show_last_task_of_app(app: str, status: None | TaskStatus = None) -> bool:
    """
    Show the last task of the specified app.

    Args:
        app: The app ID or name.
        status: The status of the task.
            The possible values are "pending", "processing", "success", and "failure".
    """
    return True

llm = ChatOpenAI(
    api_key="ollama",
    model=os.environ["MODEL"],
    base_url=os.environ["OLLAMA_URL"],
).bind_tools([fallback, search_tasks, show_last_task_of_app])

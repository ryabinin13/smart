from langchain_core.tools import tool
from ddgs import DDGS
from langgraph.prebuilt import ToolNode

import serial
import time


@tool
def web_search(query: str) -> str:
    """Искать информацию в интернете. Используй для свежих фактов,
    новостей и всего, чего ты не знаешь наверняка.
    query: короткий поисковый запрос."""
    results = DDGS(timeout=20).text(query, max_results=5)
    return "\n\n".join(
        f"{r['title']}\n{r['href']}\n{r['body']}" for r in results
    )



import time
import serial
from langchain_core.tools import tool

@tool
def light_on() -> bool:
    """
        Включает светодиод на Arduino.
    """

    byte_to_send = b'1'

    try:
        with serial.Serial('/dev/ttyUSB0', 9600, timeout=1) as sp:
            time.sleep(2)              # Arduino перезагружается при открытии
            sp.write(byte_to_send)
            time.sleep(0.2)
        return f"Светодиод: {True}"
    except serial.SerialException as e:
        return f"Ошибка порта: {e}"
    

@tool
def light_off() -> bool:
    """
        Выключает светодиод на Arduino.
    """

    byte_to_send = b'0'

    try:
        with serial.Serial('/dev/ttyUSB0', 9600, timeout=1) as sp:
            time.sleep(2)              # Arduino перезагружается при открытии
            sp.write(byte_to_send)
            time.sleep(0.2)
        return f"Светодиод: {False}"
    except serial.SerialException as e:
        return f"Ошибка порта: {e}"


tools = [light_on, light_off]

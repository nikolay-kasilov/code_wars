import json

from fastapi import FastAPI, Request

PATH = "notes.json"
app = FastAPI()
def read_notes(path=PATH) -> list[dict[str, str]]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


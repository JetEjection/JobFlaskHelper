import json
import os
import base64
from dotenv import load_dotenv


load_dotenv()

APP_SECRET_KEY = os.getenv("APP_SECRET_KEY")

DECODED_KEYS = json.loads(base64.b64decode(str(os.getenv("SERVICE_ACCOUNT_KEY"))[2:-1]).decode("utf-8"))

INTERNAL_PATH = "TemplateFiles"

SHEET_NAME = "TESTJ"
SHEET_TITLE = "РАПОРТ ОРИТ1"

DOCTORS_LIST = [
    ("Шлыкова В.Д.", "Шлыкова В.Д."),
    ("Дроздович Е.А.", "Дроздович Е.А."),
    ("Саид Т.Ш.", "Саид Т.Ш."),
    ("Савенков Н.А.", "Савенков Н.А."),
    ("Газизова Г.М.", "Газизова Г.М."),
]

DEPARTMENTS_LIST = [
    ("ЧЛХ", "ЧЛХ"),
    ("ХО", "ХО"),
    ("УРО", "УРО"),
    ("ТЕРАП", "ТЕРАП"),
    ("ОНКО", "ОНКО"),
    ("НХО", "НХО")
]

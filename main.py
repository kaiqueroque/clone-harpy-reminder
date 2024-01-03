from datetime import date
import pandas as pd
from emailer import send_email

#Goggle Sheets - Planilha não segura. Apenas que tem o link acessa
# SHEET_ID = "1y8Htf6aSTiDaTYnsf_PfNZpUuQJERU2JM8tPmN482HQ/"
# SHEET_NAME = "Harpy Automata Tech Demo"
URL = 'https://docs.google.com/spreadsheets/d/1y8Htf6aSTiDaTYnsf_PfNZpUuQJERU2JM8tPmN482HQ/edit#gid=320603766'

def load_df(url):
    parse_dates = ["due_date", "reminder_date"]
    df = pd.read_excel(url, parse_dates = parse_dates)
    return df


print(load_df(URL))
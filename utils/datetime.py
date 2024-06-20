from datetime import datetime

def format_date(iso_date):
    dt = datetime.fromisoformat(iso_date)
    formatted_date = dt.strftime("%d/%m/%Y às %H:%M")
    return formatted_date
from datetime import datetime

def format_date(iso_date, type="datetime"):
    dt = datetime.fromisoformat(iso_date)
    formatted_date = ""

    if type == "date":
        formatted_date = dt.strftime("%d/%m/%Y")
    else:
        formatted_date = dt.strftime("%d/%m/%Y às %H:%M")
    return formatted_date
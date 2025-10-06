def number_to_month(month):
    meses = [
        "error", "enero", "febrero", "marzo", "abril", "mayo", "junio",
        "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
    ]
    if 1 <= month <= 12:
        return meses[month]
    else:
        return "error"
def exec(start_date_str, end_date_str):
    start_date = parse_date(start_date_str)
    end_date = parse_date(end_date_str)
    return True


# yyyy-MM-ddと言う形式の文字列を分解する
def parse_date(date):
    year = date[:4]
    month = date[5:7]
    day = date[8:10]
    return {
        "year": int(year),
        "month": int(month),
        "day": int(day),
    }

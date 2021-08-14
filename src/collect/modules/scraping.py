import datetime
from collect.models import RaceInfo


# yyyy-MM-ddと言う形式の文字列をdatetime型に変換する
def parse_date(date):
    year = int(date[:4])
    month = int(date[5:7])
    day = int(date[8:10])
    return datetime.date(year, month, day)


# スクレイピング
def scrape(date):
    # TODO:実装
    pass

# 実行


def exec(start_date_str, end_date_str):
    current_date = parse_date(start_date_str)
    end_date = parse_date(end_date_str)
    while current_date <= end_date:
        contains = RaceInfo.objects.filter(date__exact=current_date)
        if contains.exists():
            scrape(current_date)

        current_date += datetime.timedelta(days=1)

    return True

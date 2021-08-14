from collect.models import RaceInfo, CourseInfo
import datetime


# レースＩＤリストを構築する
def configure_race_id_list():
    id_list = []

    # 過去５年間分に遡って取得する
    # 参考：https://qiita.com/dijzpeb/items/434b259e473cc8646e91
    year = datetime.date.today().year - 5
    for current in range(year, year + 6):
        for course_id in range(1, 11):
            for kai in range(1, 6):
                for day in range(1, 9):
                    for round in range(1, 13):
                        id = str(current) + str(course_id).zfill(2) + \
                            str(kai).zfill(2) + str(day).zfill(2) + \
                            str(round).zfill(2)
                        id_list.append(id)

    return id_list


# 実行
def exec():
    id_list = configure_race_id_list()
    return True

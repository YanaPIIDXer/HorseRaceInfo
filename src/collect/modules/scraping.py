from collect.models import RaceInfo, CourseInfo
import datetime
import requests
import time


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
                        id_list.append(int(id))

    return id_list


# 実行
def exec():
    id_list = configure_race_id_list()
    for id in id_list:
        try:
            RaceInfo.objects.get(pk=id)
        except:
            pass
        else:
            # 既に情報収集済みのレースは飛ばす
            continue

        url = "https://race.netkeiba.com/race/result.html?race_id=" + str(id)
        res = requests.get(url)

        time.sleep(3.0)

    return True

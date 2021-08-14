from collect.models import RaceInfo, CourseInfo
import datetime
import requests
import time
from bs4 import BeautifulSoup


# レースＩＤリストを構築する
def configure_race_id_list():
    id_list = []

    # 過去５年間分に遡って取得する
    # 参考：https://qiita.com/dijzpeb/items/434b259e473cc8646e91
    year_range = 1  # 時間がかかりすぎるので一時的に１年分としている
    start_year = datetime.date.today().year - year_range
    end_year = start_year + year_range
    for year in range(start_year, end_year + 1):
        # ↓各ループの終端から色々減算してるのは、本来の数値だと時間がかかりすぎて作業に支障が出るため
        for course_id in range(1, 11 - 9):
            for kai in range(1, 6 - 4):
                for day in range(1, 9 - 7):
                    for round in range(1, 13 - 11):
                        id = str(year) + str(course_id).zfill(2) + \
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
        if res.status_code != 200:
            continue
        res.encoding = res.apparent_encoding

        soup = BeautifulSoup(res.text, 'html.parser')
        item = soup.find(class_="RaceList_Item02")
        item = item.find(class_="RaceName")
        race_name = item.text.replace("\n", "").replace(" ", "")
        race = RaceInfo(id=id, name=race_name)
        race.save()

        time.sleep(3.0)

    return True

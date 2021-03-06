import requests as re
import json
import datetime


URL = 'https://api.registratuur.ee/service-times/service-id/232/all'
PERSON_NAME = 'Jevgeni Rubinstein'


if __name__ == '__main__':
    resp = re.get(URL)
    print(resp.status_code)

    # with open('all.json', 'w', encoding='utf-8') as f:
    #     json.dump(resp.json(), f)

    if 200 == resp.status_code:
        num = 0
        for i in resp.json():
            if PERSON_NAME == i['PersonName'] and 0 == i['Price']:
                date = datetime.datetime.strptime(i['Date'], '%Y-%m-%dT%H:%M:%S')
                date = "{:02}.{:02}.{}".format(date.day, date.month, date.year)

                time_from = datetime.datetime.strptime(i['TimeFrom'], '%H:%M:%S')
                time_from = "{:02}:{:02}".format(time_from.hour, time_from.minute)

                time_upto = datetime.datetime.strptime(i['TimeUpto'], '%H:%M:%S')
                time_upto = "{:02}:{:02}".format(time_upto.hour, time_upto.minute)

                free_place = date + ' ' + time_from + ' - ' + time_upto
                print(free_place)
                num += 1
        print(num)

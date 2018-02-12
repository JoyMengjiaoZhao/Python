"""命令行火车票查看器
Usage:
    tickets [-gdtkz] <from> <to> <date>
    tickets -h | --help
Options:
    -h,--help   显示帮助菜单
    -g          高铁
    -d          动车
    -t          特快
    -k          快速
    -z          直达
"""

from docopt import docopt
from stations import stations
import requests

if __name__ == '__main__':
    #arguments = docopt(__doc__, version='Naval Fate 2.0')
    arguments = docopt(__doc__)
    print(stations.get(arguments['<from>']))
    from_station = stations.get(arguments['<from>'])
    to_station = stations.get(arguments['<to>'])
    date = arguments['<date>']
    url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(date, from_station, to_station)
    r = requests.get(url, verify=False)
    #r=r.text
    print(r.json()['data']['result'])
    print('\n',r.json()['data']['map'])
    options = ''.join([key for key, value in arguments.items() if value is True])
    print(options)

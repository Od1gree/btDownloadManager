"""
This script is created by Sam

It tries to clear the banned IP list in qBittorrent

"""

from urllib import request
import json
import sys
import time
import argparse
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
#Disable certificate verification

def _get_url(url) -> str:
    """
    send HTTP GET request to server
    :param url: the domain name + port number + api path
    :return: result in a string.
    """
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) ' \
                 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'

    headers = {'X-Request': 'JSON',
               'User-Agent': user_agent,
               'X-Requested-With': 'XMLHttpRequest',
               'Accept': '*/*'}

    req = request.Request(url, headers=headers)
    resp = None
    try:
        resp = request.urlopen(req)
    except Exception as e:
        print(str(e) + '\nFailed: Wrong URL or qBittorrent Web UI server not started.')
        exit(0)

    test = resp.read()
    return test.decode('ascii', 'ignore')

def _post_url(url, content):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) ' \
                 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'

    headers = {'User-Agent': user_agent,
               'X-Requested-With': 'XMLHttpRequest',
               'Accept': '*/*'}

    request.urlopen(request.Request(url, str.encode(content)))


class ClearBannedIPsList:

    def __init__(self, url='localhost', port=8080, file=None, https=False):
        if https:
            self.url_port = "https://" + url + ":" + str(port)
        else:
            self.url_port = "http://" + url + ":" + str(port)
        self.string_list = []
        self.config_json = None
        try:
            if file is not None:
                filter_file = open(file, "rt")
                for line in filter_file:
                    self.string_list.append(line)
        except Exception as e:
            print(str(e) + "\n input File error")
            exit(0)
        else:
            self.string_list = ['XL0012', 'Xunlei', 'dandan']

    def run(self):
        print('connecting to server ' + self.url_port)
        self.config_json = json.loads(_get_url(self.url_port + "/api/v2/app/preferences"))
        banned_ip_str = ''
        self.config_json['banned_IPs'] = banned_ip_str
        _post_url(self.url_port + "/api/v2/app/setPreferences", 'json=' + json.dumps(self.config_json))

        print('Cleared all banned IPs from qBittorrent.')

if __name__ == '__main__':

    if __name__ == '__main__':
        parser = argparse.ArgumentParser(description='Clears qbittorrent banned IP list.',
                                         epilog='eg: python3 filter.py -u localhost -p 8080')
        parser.add_argument('-u', default='localhost',
                            help='url of the service without \'http://\' or \'https://\'')
        parser.add_argument('-p', default=8080, type=int,
                            help='port number. Default=8080')
        parser.add_argument('-s', default=False, action="store_true",
                            help='use https protocol. Default=http')
        parser.add_argument('-t', default=300, type=int,
                            help='This flag has no meaning for this utility')
        parser.add_argument('-f', default=None, type=str,
                            help='This flag has no meaning for this utility')
        parser.add_argument('-c', default=None, type=float,
                            help='This flag has no meaning for this utility')
        parser.add_argument('-x', default=None, type=float,
                            help='This flag has no meaning for this utility')

        config = parser.parse_args()
        f = ClearBannedIPsList(url=config.u, port=config.p, https=config.s)
        f.run()






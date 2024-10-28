from urllib.parse import urlparse
import os.path
import requests
import time
from datetime import datetime
import colored
from colored import stylize
import sys


class Main():
    def formatConsoleDate(date):
        return '[' + date.strftime('%Y-%m-%d-%H:%M:%S') + ']'
        pass

    def GetArgs():
        return sys.argv
        pass


class Resolver:
    def SolveLink():
        global target

        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
            "sec-ch-ua": '"Chromium";v="96", "Opera GX";v="82", ";Not A Brand";v="99"',
	    "origin": "https://servers.redm.net/",
	    "referer": "https://servers.redm.net//",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 OPR/82.0.4227.25"
        }

        data = requests.get(f"https://servers-frontend.fivem.net/api/servers/single/{target['id']}", headers=headers)
        return {
        	"ip": data.json()["Data"]["connectEndPoints"][0],
        	"hostname": data.json()["Data"]["hostname"]
        }
        pass


if __name__ == '__main__':
    ################################################################################
    # This script is used for resolving a cfx.re url like this url                 #
    # (https://cfx.re/join/6sf4xa). You will get the ip of the server in the input #
    ################################################################################
    global target

    target = {}
    target['link'] = Main.GetArgs()[1]
    target['id'] = os.path.basename(Main.GetArgs()[1])

    print(stylize('''
      ╔╦╗╔═╗╦═╗╦╔═    ╦ ╦╔╦╗╦╦  ╦╔╦╗╦╔═╗╔═╗
       ║║╠═╣╠╦╝╠╩╗    ║ ║ ║ ║║  ║ ║ ║║╣ ╚═╗
      ═╩╝╩ ╩╩╚═╩ ╩    ╚═╝ ╩ ╩╩═╝╩ ╩ ╩╚═╝╚═╝
           simple attacks, simple programs
    ''', colored.fg('red')))

    if len(sys.argv) < 1:
        print(stylize("""
    [ERROR]""", colored.fg('red'),
                      colored.attr('underlined'))
              + """ bad command usage
            """ + stylize("Usage Sheme:", colored.fg('#ffe900'),
                          colored.attr('underlined')) + """
                - user@some_name:~# python3 main.py <cfx.re-link>
        """)
        sys.exit()

    target['data'] = Resolver.SolveLink()
    print(stylize(Main.formatConsoleDate(datetime.today()), colored.fg('yellow')) +
        stylize(" Target info :", colored.fg('green')))
    print(stylize(f"""		
+-----------------------------------------------------+
|                  Target Info                        |
+-----------------------------------------------------+
|  Server IP: {target['data']['ip']}
+-----------------------------------------------------+
""",colored.fg('yellow')))

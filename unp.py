'''http://www.novixys.com/blog/parsing-xml-in-python/'''

import requests
from xml.dom import minidom
import xml.etree.ElementTree as ET
url = 'http://www.portal.nalog.gov.by/grp/getData?unp=690389921&charset=UTF-8'
#unp = int(input("Введите унп : "))

def get_html(url):
    r = requests.get(url)
    return r.text

def parse_xml(xml):

    tree = ET.fromstring(xml)
    for child in tree:
        unp = child.findtext('VUNP')
        polnoe_nazvanie_organizacii = child.findtext('VNAIMP')
        print('Ваше УНП ' + unp )
        print('Полное наименование: ' + polnoe_nazvanie_organizacii )
        





#

new_get_html = get_html(url)
new_parse = parse_xml(new_get_html)

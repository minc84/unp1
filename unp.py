'''http://www.novixys.com/blog/parsing-xml-in-python/
унп описание http://www.nalog.gov.by/ru/Information_about_the_business_partner/
https://bankrot.gov.by/Help/Help
https://minjust.gov.by/directions/enforcement/debtors/
https://www.cci.by
/justbel.info/
http://egr.gov.by/
http://court.gov.by/ru/ekonomicheskij/sud/goroda/minska/prikaznoe/proizvodstvo/882dae3ac505440c.html
http://court.gov.by/ru/online-help/bankr_inf/

'''

import requests
from xml.dom import minidom
import xml.etree.ElementTree as ET
import json
url = 'http://www.portal.nalog.gov.by/grp/getData?unp=690389921&charset=UTF-8'
url_egr = 'http://egr.gov.by/egrn/API.jsp?NM=690389921'
#unp = int(input("Введите унп : "))

def get_html(url):
    r = requests.get(url)
    return r.text

def get_html_egr (url_egr):
    r = requests.get(url_egr)
    return r.json()

def parse_xml(xml):

    tree = ET.fromstring(xml)
    for child in tree:
        unp = child.findtext('VUNP')
        polnoe_nazvanie_organizacii = child.findtext('VNAIMP')
        korotkoe_zanyatie = child.findtext('VNAIMK')
        adress = child.findtext('VPADRES')
        kod_inspekcii = child.findtext('NMNS')
        naimenovanie_inspekcii = child.findtext('VMNS')
        data_postanovki = child.findtext('DREG')
        sostoyanie = child.findtext('VKODS')


        print('Ваше УНП ' + unp )
        print('Полное наименование: ' + polnoe_nazvanie_organizacii )
        print('Краткое название: ' + korotkoe_zanyatie )
        print('Адрес организации: ' + adress )
        print('Код инспеции: ' + kod_inspekcii )
        print('Наименование инспекции МНС: ' + naimenovanie_inspekcii )
        print('Дата постановки на учет: ' +data_postanovki )
        print('Состояние: ' + sostoyanie )

def parse_json_egr(json):
    result = json.loads(url)



new_get_html = get_html(url)
#new_get_egr = get_html_egr(url_egr)
new_parse = parse_xml(new_get_html)
#new_parse = parse_json_egr(new_get_egr)


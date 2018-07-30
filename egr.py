
import requests


url = 'http://egr.gov.by/egrn/API.jsp?NM=690389921'
result = requests.get(url)
data_osnovaniya = result.json()[0]['DC']
zapret = result.json()[0]['Z']
likvid = result.json()[0]['DD']
print('Дата основания: ' + data_osnovaniya)
print('дата исключения из ЕГР (прекращения деятельности в связи с реорганизацией) субъекта хозяйствования: ' + str(likvid))
print('наличие запрета на отчуждение доли участника в уставном фонде коммерческой организации.: ' + str(zapret))


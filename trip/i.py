import requests
import json
latitude = '52.170799255371094'
longitude ='20.973920822143555'
checkin = '20141019'
checkout = str(int(checkin) + 1);
price = []
hotelName = []
hotelId = []
url = "http://www.priceline.com/api/hotelretail/listing/v3/" + latitude + "," + longitude + "/" + checkin + "/" + checkout + "/1/20"
data = requests.get(url).json()
for hotel in  data['priceSorted']:
	hotelId.append(hotel)
	hotelName.append(data['hotels'][hotel]['hotelName'])
	# price.append(int(data['hotels'][hotel])
for a in hotelId:
	print(a)
for b in hotelName:
	print (b)
url = "http://www.priceline.com/pws/v0/stay/retail/listing/detail/" + hotelId[0] + "?check-in=" + checkin + "&check-out=" + checkout
data = requests.get(url).json()
print(data['hotel']['rooms'][0]['displayableRates'][0]['originalRates'][0]['nativeTotalPriceIncludingTaxesAndFeePerStay'])

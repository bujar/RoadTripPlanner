import requests
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def getHotels(request):
	total_distance = 0.0
	price = []
	hotelName = []
	hotelId = []
	encoded_json = request.body.decode(encoding='UTF-8')
	data = json.loads(encoded_json)
	print(data)
	for location in data['data']:
		total_distance = total_distance + int(location['distance'])
		print(total_distance)
		latitude = str(location['coordinates'][0])
		longitude = str(location['coordinates'][1])

		url = "http://www.priceline.com/api/hotelretail/listing/v3/" + latitude + "," + longitude + "/" + checkin + "/" + checkout + "/1/20"
		data = requests.get(url).json()
		for hotel in  data['priceSorted']:
			hotelId.append(hotel)
			hotelName.append(data['hotels'][hotel]['hotelName'])
		url = "http://www.priceline.com/pws/v0/stay/retail/listing/detail/" + hotelId[0] + "?check-in=" + checkin + "&check-out=" + checkout
		data = requests.get(url).json()

		price.append(data['hotel']['rooms'][0]['displayableRates'][0]['originalRates'][0]['nativeTotalPriceIncludingTaxesAndFeePerStay'])
	for p in price:
		print(p)
	context = {'price': price, 'name': hotelName[0]}
	return render(request, 'itinerary.html', context)

def results(request):
	start = request.POST['start']
	destination = request.POST['destination']
	context = {'start': start, 'destination': destination}
	return render(request, 'result.html', context)
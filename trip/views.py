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
	starRating = []
	names = []
	city = []
	dates = []
	encoded_json = request.body.decode(encoding='UTF-8')
	json_data = json.loads(encoded_json)
	checkin = int(json_data['date'].replace("-", "")) + 1
	for location in json_data['data'][1:]:
		total_distance = total_distance + int(location['distance'])

		latitude = str(location['coordinates'][0])
		longitude = str(location['coordinates'][1])

		url = "http://www.priceline.com/api/hotelretail/listing/v3/" + latitude + "," + longitude + "/" + str(checkin) + "/" + str(checkin+1) + "/1/20"
		data = requests.get(url).json()
		for hotel in  data['priceSorted']:
			url = "http://www.priceline.com/pws/v0/stay/retail/listing/detail/" + hotel + "?check-in=" + str(checkin) + "&check-out=" + str(checkin+1)
			data = requests.get(url).json()
			try:
				price.append(data['hotel']['rooms'][0]['displayableRates'][0]['originalRates'][0]['nativeTotalPriceIncludingTaxesAndFeePerStay'])
				names.append(data['hotel']['name'])
				starRating.append(data['hotel']['starRating'])
				city.append(data['hotel']['location']['address']['cityName'])
				dates.append(checkin)
				break
			except KeyError:
				continue
		checkin = checkin+1

	zipped = zip(names, price, city, starRating, dates)
	context = {'zipped': zipped}
	return render(request, 'itinerary.html', context)

def results(request):
	start = request.POST['start']
	destination = request.POST['destination']
	context = {'start': start, 'destination': destination}
	return render(request, 'result.html', context)
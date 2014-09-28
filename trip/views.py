import requests
from django.shortcuts import render, redirect, render_to_response
import json
from django.views.decorators.csrf import csrf_exempt

def getHotels(request):
	total_distance = 0.0
	price = []
	hotelName = []
	hotelId = []
	starRating = []
	names = []
	city = []
	dates = []
	images = []
	encoded_json = request.POST['data']
	json_data = json.loads(encoded_json)
	checkin = int(json_data['date'].replace("-",""))
	start = json_data['start']

	destination = json_data['destination']
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
				price.append(float(data['hotel']['rooms'][0]['displayableRates'][0]['originalRates'][0]['nativeTotalPriceIncludingTaxesAndFeePerStay']))
				names.append(data['hotel']['name'])
				starRating.append(data['hotel']['starRating'])
				city.append(data['hotel']['location']['address']['cityName'])
				images.append(data['hotel']['images'][0]['imageUrl'])
				dates.append(checkin)
				break
			except KeyError:
				continue
		checkin = checkin+1
	totalPrice = sum(price)

	zipped = zip(names, price, city, starRating, dates, images)
	context = {'zipped': zipped, 'start': start, 'destination': destination, 'totalPrice': totalPrice}
	return render(request, 'final.html', context)


# def getHotels(request):
# 	start = request.POST['start']
# 	end = request.POST['end']
# 	context = {"start": start, "end": end}
# 	return render(request, "a.html", context)

def results(request):
	start = request.POST['start']
	destination = request.POST['destination']
	context = {'start': start, 'destination': destination}
	return render(request, 'result.html', context)
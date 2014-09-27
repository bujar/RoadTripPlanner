import requests
from django.shortcuts import render
import json
def getHotels(request):
	latitude = request.POST['latitude']
	longitude = request.POST['longitude']
	checkin = request.POST['checkin']
	checkout = str(int(checkin) + 1);
	price = []
	hotelName = []
	hotelId = []
	url = "http://www.priceline.com/api/hotelretail/listing/v3/" + latitude + "," + longitude + "/" + checkin + "/" + checkout + "/1/20"
	data = requests.get(url).json()
	for hotel in  data['priceSorted']:
		hotelId.append(hotel)
		hotelName.append(data['hotels'][hotel]['hotelName'])
	url = "http://www.priceline.com/pws/v0/stay/retail/listing/detail/" + hotelId[0] + "?check-in=" + checkin + "&check-out=" + checkout
	data = requests.get(url).json()

	price = data['hotel']['rooms'][0]['displayableRates'][0]['originalRates'][0]['nativeTotalPriceIncludingTaxesAndFeePerStay']
	context = {'price': price, 'name': hotelName[0]}
	return render(request, 'itinerary.html', context)
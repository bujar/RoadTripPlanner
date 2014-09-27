import requests

def getHotels(request)
	lattitude = request.POST['lattitude']
	longitude = request.POST['longitude']

	do processing to find hotels
	hotel_name="marriot"
	hotel_price = 32
	context = {'hotel': hotel], 'price': hotel_price}

	return render(request, 'itinerary.html', context)





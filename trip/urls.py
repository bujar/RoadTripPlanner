from django.conf.urls import patterns, url, include


urlpatterns = patterns('',
    url(r'^results$', 'trip.views.results'),
    url(r'^itinerary$', 'trip.views.getHotels'),

)

from timezonefinder import TimezoneFinder

# object creation
obj = TimezoneFinder()

# pass the longitude and latitude
# in timezone_at and
# it return time zone

def timzone(lat=25.6093239, lng = 85.1235252):
    time_zone = obj.timezone_at(lng=lng, lat=lat)
    return f"The time zone at lat: {lat} and lng: {lng} is {time_zone}"



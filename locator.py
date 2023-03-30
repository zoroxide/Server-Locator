from geoip import geolite2
import socket

hostname = input("Enter the Website URL(www.site.com): ")

ip = socket.gethostbyname(hostname)
locator = geolite2.lookup(ip)
country = locator.country
timezone = locator.timezone
continent = locator.continent
location = locator.location

print("------------------------------------------")
print(f"The website ip address: {ip}")
print(f"Server Country: {country}")
print(f"Server continent: {continent}")
print(f"Server Timezone: {timezone}")
print(f"Server Location on Map: {location}")
print("------------------------------------------")

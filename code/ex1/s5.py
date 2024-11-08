import csv
from dataclasses import dataclass
from math import radians, sin, cos, sqrt, atan2

@dataclass
class Port:
    name: str
    country: str
    latitude: float
    longitude: float
    has_airport: bool


def haversine(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """ Calculate the distance between two geographical points. Returns distance in kilometers """
    R = 6371  # Radius of the Earth in km
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c


# Step 3: Load data from the CSV file
ports = []
with open('Dataset_WorldPortIndex.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        port = Port(
            name=row['Port Name'],
            country=row['Country'],
            latitude=float(row['Latitude']),
            longitude=float(row['Longitude']),
            has_airport=row['Airport'].strip().lower() == 'yes'
        )
        ports.append(port)


def find_nearest_port_with_airport(lat: float, lon: float) -> Port | None:
    """ Finds nearest Port to coordinates  """
    nearest_port: Port = None
    min_distance: float = float('inf')
    for port in ports:
        if port.has_airport:
            distance = haversine(lat, lon, port.latitude, port.longitude)
            if distance < min_distance:
                min_distance = distance
                nearest_port = port
    return nearest_port


current_location = (52.2297, 21.0122)  # Warsaw, Poland
nearest_port = find_nearest_port_with_airport(*current_location)

print(f"Nearest port with an airport: {nearest_port.name}, {nearest_port.country}")

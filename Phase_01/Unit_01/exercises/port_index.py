import csv
from math import radians, sin, cos, sqrt, atan2

from dataclasses import dataclass
from typing import List


@dataclass
class Port:
    name: str
    country: str
    lat: float
    lon: float
    has_airport: bool


def read_dataset() -> List[Port]:
    with open('Dataset_WorldPortIndex.csv') as csv_file:
        ports = []
        reader = csv.DictReader(csv_file)
    
        for row in reader:
            has_airport = True if row['Communications - Airport'] == 'Yes' else False
            port = Port(
                row['Main Port Name'],
                row['Country Code'],
                float(row['Latitude']),
                float(row['Longitude']),
                has_airport,
            )

            ports.append(port)
    
    return ports


def haversine(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c


def get_current_location() -> List[float]:
    # connect with plane's GPS tracker
    return [2.03711, 45.34375]


def find_nearest_port_with_airport() -> Port:
    my_lat, my_lon = get_current_location()
    ports = read_dataset()
    nearest_port: Port = None
    nearest_distance: float = float('inf')

    for port in ports:
        if port.has_airport:
            distance = haversine(my_lat, my_lon, port.lat, port.lon)
            if distance < nearest_distance:
                nearest_port = port
                nearest_distance = distance

    return nearest_port


if __name__ == '__main__':
    nearest_port = find_nearest_port_with_airport()
    print(nearest_port.name)

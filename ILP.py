import numpy as np
import matplotlib.pyplot as plt

NUM_TAXIS = 1000
NUM_AREAS = 1000
DELAY_MAX = 10
time_matrix = np.array((NUM_AREAS, NUM_AREAS), dtype = 'int8')
global_time = 0

class Request:
    def __init__(self, id, original, destination, request_time, num_passengers):
        self.id = id
        self.original = original
        self.destination = destination
        self.request_time = request_time
        self.num_passengers = num_passengers

    is_assigned = False
    taxi_id = -1
    pickup_time = -1
    earliest_dropoff_time = request_time + time_matrix[original][destination]


class Taxi:
    def __init__(self, id, initial_loc, capacity):
        self.id = id
        self.capacity = capacity
        self.curr_loc = initial_loc
        self.capacity_remain = capacity
    is_pickup = False
    time_remain = -1
    req_list = []
    route = []
    dest_set = set()


class Area:
    def __init__(self, id, initial_loc, capacity):
        self.id = id
    taxi_list = []



def check_available(taxi, area, request):
    if taxi.capacity_remain < request.num_passengers:
        return False

    time_to_come = time_matrix[taxi.route[1]][area.id] + taxi.time_remain

    for r in taxi.req_list:
        time_to_destination = time_matrix[area.id][r.destination]
        recheduled_time = time_to_come + time_to_destination + global_time
        if (recheduled_time - r.earliest_dropoff_time) > DELAY_MAX:
            return False
    return True

def rechedule(taxi, area, request):
    if check_available(taxi, area, request):


def get_route(original, destination):


def update_taxi(taxi, request, is_pickup):
    if is_pickup:
        taxi.req_list.append(request)
        taxi.capacity_remain = taxi.capacity_remain - request.num_passengers

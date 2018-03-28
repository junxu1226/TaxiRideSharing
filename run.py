import numpy as np
from ILP.py import *

all_steps = 1000  ## in mins
BIG_NUM = 100000

running_taxis = set()

cost = []
req_idx = 0
all_requests = []  # (all_steps, list) according to time, every min, pre-made, Request object

all_trips = np.array(shape=[all_steps, all_areas, destinations], dtype=object)

### 2 hashmaps for taxis and requests in each area
taxi_lists = dict()
request_lists = dict()

for i in range(num_areas):
    taxi_lists[i] = set()
    request_lists[i] = set()

###  taxi_lists = {all_areas, Taxi[]}
###  request_lists = [all_areas, Request[]]

def get_cost(request_set, step):
    if len(request_set) == 0:
        return 0
    new_seats = 0
    for r in request_set:
        arr = np.array([r.request_time, r.pickup_time, step])
        cost.append(arr)
        new_seats += r.num_passengers
    return new_seats

def update_taxi():
    idles = set()
    for t in running_taxis:
        if t.time_remain > 0:
            t.time_remain = t.time_remain - 1
        else:
            if len(route) == 0:
                s.add(t)
            else:
                d = route.pop(0)
                taxi_lists[d].add(t)
                if d in t.requests.keys():
                    new_seats = get_cost(t.requests.pop(d))
                    t.capacity_remain += new_seats
    for t in idles:
        running_taxis.remove(t)


def add_requests(step):
    if len(all_requests[step]) == 0:
        continue
    else:
        for r in all_requests[step]:
            request_lists[r.original].add(r)


def requests_assign(step):   # raw_requests shape is (all_steps, all_areas, num_requests)
    for area in xrange(len(request_lists)):
        if len(request_lists[area]) == 0:
            continue
        else:
            optimize(area)  ## for each area, optimize() with a list of taxis, and a list of requests


def optimize(area):
    pass  # solve by ILP
    taxi_lists[area], request_lists[area]
    assigned = []
    remaining = []

def check_match(taxi_list, request_list):
    match_matrix = np.array(shape=[len(request_list), len(taxi_list)])

    for i, r in enumerate(request_list):
        for j, t in enumerate(taxi_list):
            if t.capacity_remain < r.num_passengers:
                match_matrix[i][j] = BIG_NUM

    return match_matrix




for step in xrange(all_steps):

    update_taxi()  ## including cost calculation
    add_requests(step)
    requests_assign(step)

    if step % 5 == 0:  ##
        dispatch()

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


def add_requests(step, all_requests, request_lists):
    if len(all_requests[step]) == 0:
        continue
    else:
        for r in all_requests_curr:
            request_lists[r.original].add(r)


def update_taxi():
    for t in running_taxis:
        if t.time_remain > 0:
            t.time_remain = t.time_remain - 1
        else:
            d = route.pop(0)

            if d in t.requests.keys():
                get_cost(t.requests[d])
                t.capacity_remain = t.capacity_remain + t.requests[d].num_passengers
                t.requests.pop(d)

            taxi_lists[d].add(t)

def requests_assign(request_lists, step):   # raw_requests shape is (all_steps, all_areas, num_requests)
    for area in xrange(len(request_lists)):
        if len(request_lists[area]) == 0:
            continue
        else:
            match_matrix = check_match(taxi_lists[area], all_trips[step, area])
            assigned, remaining = optimize(match_matrix)
            request_lists[area].add(remaining)


def optimize(match_matrix):  # shape of match_matrix is (requests, taxis)
    pass  # solve by ILP
    list = []
    remaining = []
    return list, remaining

def check_match(taxi_list, request_list):
    match_matrix = np.array(shape=[len(request_list), len(taxi_list)])

    for i, r in enumerate(request_list):
        for j, t in enumerate(taxi_list):
            if t.capacity_remain < r.num_passengers:
                match_matrix[i][j] = BIG_NUM

    return match_matrix




for step in xrange(all_steps):

    update_taxi()  ## including cost calculation
    add_requests(step, all_requests, request_lists)

    requests_assign()
    if step % 5 == 0:  ##
        dispatch()

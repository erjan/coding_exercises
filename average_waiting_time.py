'''
There is a restaurant with a single chef. You are given an array customers, where customers[i] = [arrivali, timei]:

arrivali is the arrival time of the ith customer. The arrival times are sorted in non-decreasing order.
timei is the time needed to prepare the order of the ith customer.
When a customer arrives, he gives the chef his order, and the chef starts preparing it once he is idle. The customer waits till the chef finishes preparing his order. The chef does not prepare food for more than one customer at a time. The chef prepares food for customers in the order they were given in the input.

Return the average waiting time of all customers. Solutions within 10-5 from the actual answer are considered accepted.
'''

def f(customers):

    total_c = len(customers)

    prev_start = 0

    waits = list()

    for start, cook in customers:
        print('---------------------')

        if prev_start > start:
            start_time = prev_start
        else:
            start_time = start

        finish_time = cook + start_time

        print('start time %d' % start_time)
        print('finish time %d' % finish_time)

        wait_time = finish_time - start
        waits.append(wait_time)

        prev_start = finish_time

    w = sum(waits)

    res = float(w / len(customers))
    print(res)
    return res
  

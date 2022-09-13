import time
def random(min_number, max_number):
    t_data = '%.9f' % time.time()
    interval = max_number - min_number
    razrad = len(str(interval)) * -1
    smech = int(t_data[razrad:])

    while smech > interval:
        smech = int(smech / 2)

    rnd = min_number + smech
    return rnd

print(random(20,50))
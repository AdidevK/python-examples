import itertools
from itertools  import islice
import collections

# itertoolscounter = itertools.count()
# print(next(counter))
# print(next(counter))

# data = [1, 5, 10, 15]
# daily_data = list(itertools.zip_longest(range(10), data))
# print(daily_data)

def consume(days_desc, starting_day_desc):
    index_num = [index for index in range(len(days_desc)) if days_desc[index] == starting_day_desc]
    if len(index_num)>0:
        index_num = index_num.pop()
    else:
        index_num=None
    days_desc_cycle = itertools.cycle(days_desc)
    "Advance the iterator n-steps ahead. If n is None, consume entirely."
    # Use functions that consume iterators at C speed.
    if index_num is None:
        # # feed the entire iterator into a zero-length deque
        # collections.deque(days_desc_cycle, maxlen=0)
        days_desc_cycle_adjusted = days_desc_cycle
    else:
        # advance to the empty slice starting at position n
        days_desc_cycle_adjusted = islice(days_desc_cycle, index_num, None)

    return days_desc_cycle_adjusted

def days_tuple(daysInMonth):
    daysInMonth = daysInMonth
    days = [1,2,3,4,5,6,7]
    days_desc = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    starting_day_desc= 'saturday'

    days_desc_adjsuted = consume(days_desc, starting_day_desc)
    days_data = list(zip(range(1, daysInMonth+1), days_desc_adjsuted))
    for day_details in days_data:
        print(day_details)
# # calendar_days
# days_tuple(30)

# print(list(map(pow, range(1,11), itertools.repeat(2))))

list = [1,0,2,3,0,4]

for item in list:
    if item==0:
        list.remove(item)
        list.append(item)
print(list)
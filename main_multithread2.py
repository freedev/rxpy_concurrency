import multiprocessing
import random
import time
from threading import current_thread
import rx
from rx.scheduler import ThreadPoolScheduler
from rx import operators as ops

# calculate cpu count, using which will create a ThreadPoolScheduler
thread_count = multiprocessing.cpu_count()
thread_pool_scheduler = ThreadPoolScheduler(thread_count)

print("From Main: {0} Cpu count is : {1}".format(current_thread(), thread_count))

def to_value(value):
   print("From to_value: {0} Value: {1}".format(current_thread(), value))
   return value

def adding_delay(value):
   delay = random.randint(5, 20) * 0.2
   time.sleep(delay)
   print("From adding_delay: {0} Value : {1} {2}".format(current_thread(), value, delay))
   return (value[0], value[1]+ " processed")

my_dict={'A':'url1', 'B':'url2', 'C':'url3'}

new_dict = rx.from_iterable(my_dict.items()).pipe(
   ops.flat_map(lambda a: rx.of(a).pipe(
        ops.map(lambda a: adding_delay(a)),
        ops.subscribe_on(thread_pool_scheduler)
   )),
#    ops.observe_on(thread_pool_scheduler),
   ops.to_dict(lambda x: x[0], to_value)
).run()

print("From Main: {0}".format(current_thread()))
print(str(new_dict))
# input("Press any key to exit\n")
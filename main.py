import random
import time
import rx
from rx import operators as ops

def adding_delay(value):
   time.sleep(random.randint(5, 20) * 0.1)
   return value

# Task 1
rx.of(1,2,3,4,5).pipe(
   ops.map(lambda a: adding_delay(a))
).subscribe(
   lambda s: print("From Task 1: {0}".format(s)),
   lambda e: print(e),
   lambda: print("Task 1 complete")
)

# Task 2
rx.range(1, 5).pipe(
   ops.map(lambda a: adding_delay(a))
).subscribe(
   lambda s: print("From Task 2: {0}".format(s)),
   lambda e: print(e),
   lambda: print("Task 2 complete")
) 
input("Press any key to exit\n")
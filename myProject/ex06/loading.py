import time
import sys

def ft_progress(iterable):
    total = len(iterable)
    start_time = time.time()

    for i, item in enumerate(iterable):
        elapsed_time = time.time() - start_time
        progress = (i + 1) / total
        bar_length = 40
        filled_length = int(bar_length * progress)
        bar = '=' * filled_length + ' ' * (bar_length - filled_length)
        eta = (elapsed_time / (i + 1)) * (total - (i + 1)) if i > 0 else 0

        sys.stdout.write(f"\r[{bar}] {progress * 100:.2f}% ETA: {eta:.2f}s")
        sys.stdout.flush()
        yield item
    
    print()  # Newline after completion

# ✅ **Usage Example**
from time import sleep

listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    sleep(0.01)  # Simulate processing time

print("\n")
print(ret)

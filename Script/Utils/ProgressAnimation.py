import sys
import time

# ReusableAsset_COE00079
# Function to create a rolling progress bar
def rolling_progress_bar(stop_event, message):
    while not stop_event.is_set():
        for char in '|/-\\':  # Rolling animation
            sys.stdout.write(f'\r{char} {message}....')
            sys.stdout.flush()
            time.sleep(0.1)
        if stop_event.is_set():
            break

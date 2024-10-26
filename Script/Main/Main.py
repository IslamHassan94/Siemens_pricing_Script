import logging
import os
import sys
import threading

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Script.Utils import ProgressAnimation
from Script.Config import Logger, Config_Setup
from Script.Cases import Handle_Pricing

#################### Logging #############################
Logger.init_Logger()
logger = logging.getLogger("Siemens Script")
logging.getLogger("imported_module").setLevel(logging.WARNING)
#################################################################


stop_events = {}


def start_loading(message, case):
    global stop_events
    stop_events[case] = threading.Event()
    progress_thread = threading.Thread(target=ProgressAnimation.rolling_progress_bar, args=(stop_events[case], message))
    progress_thread.start()
    return progress_thread


def stop_loading(case):
    stop_events[case].set()
    stop_events[case].wait()


if __name__ == '__main__':
    logger.debug('_______________ PROCESS STARTED _________________________')
    logger.debug('Release Date: 26-10-2024 3:31 pm')

    logger.debug("Siemens process Started")
    progress_thread1 = start_loading('Siemens process in Progress...', 1)
    if Config_Setup.handle_all == "true":
        Handle_Pricing.handle_pricing_for_all_customers()
    if Config_Setup.handle_all == "both":
        Handle_Pricing.handle_pricing_for_customer()
        Handle_Pricing.handle_pricing_for_all_customers()
    else:
        Handle_Pricing.handle_pricing_for_customer()
    stop_loading(1)
    progress_thread1.join()
    logger.debug("\nSiemens process DONE.")

    logger.debug('_______________ PROCESS FINISHED _________________________')

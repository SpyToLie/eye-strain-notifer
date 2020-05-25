from win10toast import ToastNotifier
from idle_time import IdleMonitor
import time


def monitor_idle_time():
	monitor = IdleMonitor.get_monitor()
	idle_time = monitor.get_idle_time()
	return idle_time


def notify():
	notification = ToastNotifier()
	notification.show_toast("Reminder to look away from the screen for 20 seconds!",
	                        duration=3, msg="If possible, look at something that is at least 20 meters away.")


if __name__ == '__main__':
	proceed = True
	while proceed:
		time.sleep(1200)
		if monitor_idle_time() > 60:
			notify()

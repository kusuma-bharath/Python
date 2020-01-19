import threading

class BharathMessenger(threading.Thread):
    def run(self):
        for _ in range(100):
            print(threading.current_thread().getName() + "\n")


x = BharathMessenger(name='send message')
y = BharathMessenger(name='receive message')

x.start()
y.start()

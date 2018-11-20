import signal

def handler(signum, frame):
    print(signum, frame)
    raise OSError('interrupt user')

signal.signal(signal.SIGINT, handler)
while True:
    pass

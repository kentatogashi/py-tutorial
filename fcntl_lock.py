import optparse
import fcntl
import time

def my_parser():
    parser = optparse.OptionParser()
    parser.add_option('-e', '--exlock', dest='exlock')
    parser.add_option('-s', '--sharedlock', dest='sharedlock')
    return parser

def my_lock(lock_type):
    fp = open('test.lock', 'r')
    fcntl.flock(fp.fileno(), lock_type)
    print('get lock')
    time.sleep(5)
    print('sleep 5 sec')
    fcntl.flock(fp.fileno(), fcntl.LOCK_UN)
    print('unlock')

parser = my_parser()
parser.parse_args()
if parser.values.exlock:
    print("exlock demo")
    my_lock(fcntl.LOCK_EX)
if parser.values.sharedlock:
    print('sharedlock demo')
    my_lock(fcntl.LOCK_SH)

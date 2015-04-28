#  Read the documentation about the `select` module
#  (http://docs.python.org/2/library/select.html) and attempt to write a second
#  version of the echo server that can handle multiple client connections in
#  "parallel".  You do not need to invoke threading of any kind to do this.
#

import socket
import sys
import select


def server(log_buffer=sys.stderr):
    address = ('127.0.0.1', 10000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    print >>log_buffer, "making a server on {0}:{1}".format(*address)

    sock.bind(address)
    sock.listen(5)

    try:
        while True:
            print >>log_buffer, 'waiting for a connections'

            conn, addr = sock.accept()
            # http://ilab.cs.byu.edu/python/select/echoserver.html
            # read up on this tomorrow
            try:
                print >>log_buffer, 'connection - {0}:{1}'.format(*addr)

                while True:
                    data = conn.recv(16)
                    if len(data) != 0:
                        conn.send(data)
                        print >>log_buffer, 'received "{0}"'.format(data)
                    else:
                        break
            finally:
                conn.close()

    except KeyboardInterrupt:
        conn.close()
        sys.exit(0)

if __name__ == '__main__':
    server()
    sys.exit(0)

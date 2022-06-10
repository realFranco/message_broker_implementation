# ref https://zguide.zeromq.org/docs/chapter2/#Pub-Sub-Message-Envelopes

import sys

import zmq


# topic: [A, B]
def main(topic: str):
    """ main method """

    # Prepare our context and publisher
    context = zmq.Context()
    subscriber = context.socket(zmq.SUB)
    subscriber.connect("tcp://localhost:5563")
    subscriber.setsockopt(zmq.SUBSCRIBE, topic.encode())

    # while True:
    if True:
        # Read envelope with address
        [address, contents] = subscriber.recv_multipart()
        print(f"[{address}] {contents}")

    # We never get here but clean up anyhow
    subscriber.close()
    context.term()


if __name__ == "__main__":
    topic = str(sys.argv[1])
    main(topic=topic)

# ref https://zguide.zeromq.org/docs/chapter2/#Pub-Sub-Message-Envelopes

import time
import zmq


def main():
    """main method"""

    # Prepare our context and publisher
    context = zmq.Context()
    publisher = context.socket(zmq.PUB)
    publisher.bind("tcp://*:5563")

    while True:
        # Write two messages, each with an envelope and content
        publisher.send_multipart([b"A", b"Topic A"])
        publisher.send_multipart([b"B", b"Topic B"])
        time.sleep(1)

    # We never get here but clean up anyhow
    publisher.close()
    context.term()


if __name__ == "__main__":
    main()
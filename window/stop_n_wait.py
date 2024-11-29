import random
import time

def stop_and_wait_arq(frames, timeout):
    for frame in range(1, frames + 1):
        print(f"Sending frame {frame}...")
        ack = random.randint(0, 1)
        start_time = time.time()
        while True:
            if ack == 1:
                print(f"Frame {frame} acknowledged.\n")
                break
            else:
                elapsed_time = time.time() - start_time
                if elapsed_time > timeout:
                    print(f"Timeout! Retransmitting frame {frame}...")
                    ack = random.randint(0, 1)
                    start_time = time.time()
    print("All frames sent and acknowledged successfully!")

stop_and_wait_arq(frames=5, timeout=2)
import random
import time

def go_back_n_arq(frames, window_size, timeout):
    base = 1
    next_frame = 1
    while base <= frames:
        print(f"Window [{base} to {min(base + window_size - 1, frames)}]")
        for i in range(next_frame, min(base + window_size, frames + 1)):
            print(f"Sending frame {i}")
            ack = random.randint(0, 1)
            start_time = time.time()
            if ack == 1:
                print(f"Acknowledgment received for frame {base}")
                base += 1
                next_frame = base
            else:
                elapsed_time = time.time() - start_time
                if elapsed_time > timeout:
                    print(f"Timeout! Retransmitting from frame {base}...")
                    next_frame = base
        print()
    print("All frames sent and acknowledged successfully!")

go_back_n_arq(frames=7, window_size=3, timeout=2)
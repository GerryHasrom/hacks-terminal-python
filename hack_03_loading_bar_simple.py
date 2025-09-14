import time
import sys

def loading_bar(total=30, duration=3):
    
    for i in range(total + 1):
        percent = (i / total) * 100
        bar = '█' * i + '-' * (total - i)
        sys.stdout.write(f'\r[{bar}] {percent:6.2f}%')
        sys.stdout.flush()
        time.sleep(duration / total)
    print()  

if __name__ == "__main__":
    print("Memulai proses...")
    loading_bar(total=40, duration=4)
    print("Selesai!")

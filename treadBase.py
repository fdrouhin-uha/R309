import sys, time, threading
def task(i):
    print(f"Task {i} starts")
    time.sleep(1)
    print(f"Task {i} ends")

def main():
    start = time.perf_counter()
    t1 = threading.Thread(target=task, args=[1]) # création de la thread
    t1.start() # je démarre la thread
    t1.join() # j'attends la fin de la thread
    end = time.perf_counter()
    print(f"Tasks ended in {round(end - start, 2)} second(s)")

if __name__=="__main__":
    sys.exit(main())
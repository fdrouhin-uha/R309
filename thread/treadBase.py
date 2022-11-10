import sys, time, threading
def task(i):
    print(f"Task {i} starts")
    time.sleep(1)
    print(f"Task {i} ends")
'''start = time.perf_counter()
t1 = threading.Thread(target=task, args=[1]) # création de la thread
t1.start() # je démarre la thread
t2 = threading.Thread(target=task, args=[2])
t2.start()
t1.join()  # j'attends la fin de la thread
t2.join()  # j'attends la fin de la thread
end = time.perf_counter()
print(f"Tasks ended in {round(end - start, 2)} second(s)")'''
def main():
    start = time.perf_counter()
    T = []
    for i in range(100):
        T.append(threading.Thread(target=task, args=[i]))
    for i in range(len(T)):
        T[i].start()
    for i in range(len(T)):
        T[i].join()
    end = time.perf_counter()
    print(f"Tasks ended in {round(end - start, 2)} second(s)")
if __name__=="__main__":
    sys.exit(main())
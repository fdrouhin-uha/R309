import time
import multiprocessing
import sys,requests
img_urls = [
    'https://cdn.pixabay.com/photo/2018/01/14/23/12/nature-3082832_960_720.jpg',
    'https://cdn.pixabay.com/photo/2017/02/01/22/02/mountain-landscape-2031539_960_720.jpg'
]


def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[-1]
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded")
def main():
    #start = time.perf_counter()
    p1 = multiprocessing.Process(target=download_image, args=[img_urls[0]])
    p2 = multiprocessing.Process(target=download_image,args=[img_urls[1]])
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    #end = time.perf_counter()
    #print(f"Tasks ended in {round(end - start, 2)} second(s)")

if __name__ == '__main__':
    sys.exit(main())
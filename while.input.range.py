from tracemalloc import start


start_n = int(input('start number : '))

end_n   = int(input('end number : '))


if start_n <= end_n :
    while start_n <= end_n :
        print (start_n)
        start_n += 1
else:
    while start_n >= end_n : 
     print (start_n)
     start_n -= 1

    
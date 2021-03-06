# -*- coding: cp1254 -*-
from multiprocessing import Pool
from math import sqrt, floor
import time
start = time.time()

 # 7.244999885559082

def asal_mi(sayi):
	"sayı asal mı?"
	if sayi < 2:
		raise ValueError("Sayi ikiden buyuk olmalidir.")

	if sayi == 2:
		return True

	if sayi % 2 == 0:
		return False

	bolunecekler = range(3, int(sqrt(sayi)),2)

	for b in bolunecekler:
		if sayi % b == 0:
			return False

	return True


def sayilar_asal_mi(sayilar):
	"Bir liste içindeki asalları döndür"
	return [x for x in sayilar if asal_mi(x)]


if __name__ == "__main__": # Bunu yapmanız şart, şimdilik niye diye sormayın.
	p = Pool(processes=4) # 4 işlemden oluşan işlemci havuzu oluştur

	# İşleri işlemler arasında dağıt
	sonuclar = p.map(sayilar_asal_mi, [ range(500000, 625000),
								   range(625000, 750000),
								   range(750000, 875000),
								   range(875000, 1000000) ] )

	alt_toplamlar = map(sum, sonuclar) # Her listenin kendi toplamını al
	print alt_toplamlar
	print sum(alt_toplamlar) # tümünü topla
	print 'sure: ',time.time()-start

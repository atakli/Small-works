# from matplotlib import style
import psutil,time
# style.use('fivethirtyeight')
while True:
	upload = psutil.net_io_counters(pernic=True)['Kablosuz Ağ Bağlantısı'][0]
	download = psutil.net_io_counters(pernic=True)['Kablosuz Ağ Bağlantısı'][1]
	print('upload: '+str(round(upload/1024/1024,2))+' MB'+'\n'+'download: '+str(round(download/1024/1024,2))+' MB\n')
	time.sleep(1)

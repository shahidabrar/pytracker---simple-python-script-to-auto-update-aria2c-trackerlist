import xmlrpc.client as xc,urllib.request as urllib2,shutil
from pprint import pprint
response = urllib2.urlopen('https://trackerslist.com/all_aria2.txt')
tracker_list = response.read().decode('utf-8')
c = "dir=/storage/emulated/0/IDMP/Torrents\ncheck-certificate=false\nfile-allocation=none\ndisk-cache=0\ncontinue=true\nmax-concurrent-downloads=3\nmax-connection-per-server=16\nmin-split-size=1M\nsplit=16\nmax-overall-download-limit=0\nmax-download-limit=0\nmax-overall-upload-limit=0\ndisable-ipv6=false\nsave-session=/storage/emulated/0/IDMP/Torrents/aria2.session\n#input-file=/storage/emulated/0/IDMP/Torrents/aria2.session\nsave-session-interval=0\nfollow-torrent=mem\nlisten-port=51413\nbt-max-peers=0\nenable-dht=true\nenable-dht6=true\ndht-listen-port=6881-6999\nbt-enable-lpd=true\nenable-peer-exchange=true\npeer-id-prefix=-TR3000-\nuser-agent=Transmission/3.00\npeer-agent=Transmission/3.00\nseed-time=0\nenable-rpc=true\nrpc-allow-origin-all=true\nrpc-listen-all=true\nrpc-listen-port=6800\n#rpc-secret=shahidsx831\n#rpc-user=shahid\n#rpc-passwd=01925066654\nbt-seed-unverified=true\nbt-save-metadata=true\nmax-file-not-found=50\nmax-tries=100\nretry-wait=3\nbt-max-open-files=100000\nconsole-log-level=notice\ndownload-result=full\nbt-tracker="
with open ("/storage/emulated/0/.config/aria2/aria2.conf" , "w+" ) as f:
	f.write(f'{c}{tracker_list}')
shutil.copyfile('/storage/emulated/0/.config/aria2/aria2.conf','/data/data/com.termux/files/home/.config/aria2/aria2.conf')
s = xc.ServerProxy('http://localhost:6800/rpc')	
x = input("enter the http link  without quotation mark :")
r = s.aria2.addUri([x])
pprint(r)
 

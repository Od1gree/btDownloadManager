中文往下翻

# btDownloadManager
A python script to manage qBittorrent.

## Feature
* Anti-leech

This script ban peers according to client name if the torrent has leechers, or unconditionally.
> It is widely known that some torrent managers such as '-XL0012-' and 'Xunlei 0.0.x.x' are bad leechers. 
They only download files and never contribute to torrent network.

## Requirements
* `python 3.6`
* `qBittorrent 4.2.1` (GUI version and non-GUI version are both fine)

## Configuration and run
1. Open the qBittorrent Web UI in settings.
2. Set *IP Address* and *Port*. My configuration is `localhost` and `8080`.
3. Set your own *Username* and *Password*.
4. Check the config box "Bypass authentication for clients on localhost" to let the script work without a password.
5. Download the `filter.py` to the computer running qBittorrent.
6. Run the script `filter.py' with required flags -u, -p, and -t`.  For example `python3 filter.py -u localhost -p 8080 -t 10`.

## Params
* `-u`: url of service, default=`localhost`
* `-p`: port of service, default=`8080`
* `-f`: path to a customized filter list, with each line containing a string. Default=`None`, i.e. use default filter list.
* `-t`: time interval between filter checks, default =`10`
* `-c`: optional time interval to clear "Banned IP Addresses", in hours, default=`None`
* `-s`: use https to connect webui.
* `-x`: ban clients in the filter list always, regardless of leeching status

## Clearing "Banned IP Addresses"
Over time `filter.py` will add more and more entries to "Banned IP Addresses". If it is very long it might slow down your seeding.  You can choose to clear the list through btDownloadManager. Note that the script will unconditionally clean up the list, including anything that may have been manually added before!

You can set `-c` the optional time interval between clearing to any numberof hours: `-c 24` will clear it once a day

If you want to clear the list just once, run the script `clear_once.py`.  It needs only flags `-u` and `-p`

## Using your own list of clients to the filter
Create a file with a string on each line that contains part of the name of the client you want to filter.  Or edit the sample file `my_clients_to_filter.txt` and use it. 
_________________________________

# btDownloadManager
一个管理qBittorrent的脚本

## 特性
* 反吸血

这个脚本目前用于封禁迅雷种子下载请求
> 众所周知，迅雷下载BT种子时只下载不上传，无益于种子社区的活性，因此给迅雷客户端提供上传不仅没有意义而且占用自己的带宽。
>迅雷的标识符为'-XL0012-' 和 'Xunlei 0.0.x.x'.

## 运行要求
* `python 3.6`
* `qBittorrent 4.2.1` (图形界面版本和纯Web UI版本都可以)

## 设置
1. 打开qBittorrent的设置，进入Web UI设置.
2. 设置 *IP 地址* 和 *端口*. 我的设置分别为 `localhost` 和 `8080`.
3. 自定义 *用户名* 和 *密码*.
4. 勾选 _对本地主机上的客户端跳过身份验证_ 让脚本在本机无需密码即可访问WebUI.
5. 下载 `filter.py` 到你运行qBittorrent的电脑里.
6. 打开命令行,运行 `python3 filter.py -u localhost -p 8080 -t 10`。

## 参数解释
* `-u`: 自定义ip地址, 默认=`localhost`
* `-p`: 自定义端口, 默认=`8080`
* `-f`: 使用自定义的过滤列表,每行一个字符串,不填的话使用内置默认过滤列表. 默认=`None`.
* `-t`: 获取种子列表的时间间隔,单位秒, 默认=`10`
* `-s`: 使用https连接webui, 不添加该参数默认使用http
* `-c`: optional time interval to clear "Banned IP Addresses", in hours, default=`None`
* `-x`: ban clients in the filter list always, regardless of leech status

Need translation to Chinese:
## Clearing "Banned IP Addresses"
Over time `filter.py` will add more and more entries to "Banned IP Addresses". If it is very long it might slow down your seeding.  You can choose to clear the list through btDownloadManager. Note that the script will unconditionally clean up the list, including anything that may have been manually added before!

You can set `-c` the optional time interval between clearing to any numberof hours: `-c 24` will clear it once a day

If you want to clear the list just once, run the script `clear_once.py`.  It needs only flags `-u` and `-p`

## Using your own list of clients to the filter
Create a file with a string on each line that contains part of the name of the client you want to filter.  Or edit the sample file `my_clients_to_filter.txt` and use it. 


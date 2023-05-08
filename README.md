中文往下翻

# btDownloadManager
A python script to manage qBittorrent.

## Feature
* Anti-leech

Currently the script is able to ban peers according to client name.
> It is widely known that '-XL0012-' and 'Xunlei 0.0.x.x' are bad leecher. 
They only download files and never contribute to torrent network.

## Requirements
* `python 3.6`
* `qBittorrent 4.2.1` (GUI version and non-GUI version are both fine)

## Configuration
1. Open the qBittorrent Web UI in settings.
2. Set *IP Address* and *Port*. My configuration is `localhost` and `8080`.
3. Set your own *Username* and *Password*.
4. Check the config _Bypass authentication for clients on localhost_ to let the script work without password.
5. Download the `filter.py` to your computer which running qBittorrent.
6. Run the script `python3 filter.py -u localhost -p 8080 -a 300 -b 10`.

## Params
* `-u`: url of service, default=`localhost`
* `-p`: port of service, default=`8080`
* `-f`: customize filter list, each line contains a string. Defaule=`None`, i.e. use default filter list.
* `-a`: time interval to Get the torrent list in seconds, default=`300`
* `-b`: time interval to Get the peers list in seconds, default=`10`
* `-s`: use https to connect webui.

The frequency of changing the torrent list is low, so we can set longer time interval to get torrent list.
I suggest the `-a` value is N times of `-b` value, N is an integer bigger than 2.

## Another python to clean up the "Banned IP Addresses" list

Over time the `filter.py` will keep populating the "Banned IP Addresses" list with more and more entires.
`clear_qbittorrent.py` helps with over-populating by simply emptying the list.

NOTE:  Running the script will unconditionally clean up the list, including anything thay may have been manually added before !

Run the script by doing `python3 clear_qbittorrent.py -u localhost -p 8080`.

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
6. 打开命令行,运行 `python3 filter.py -u localhost -p 8080 -a 300 -b 10`。

## 参数解释
* `-u`: 自定义ip地址, 默认=`localhost`
* `-p`: 自定义端口, 默认=`8080`
* `-f`: 使用自定义的过滤列表,每行一个字符串,不填的话使用内置默认过滤列表. 默认=`None`.
* `-a`: 获取种子列表的时间间隔,单位秒, 默认=`300`
* `-b`: 获取peers的时间间隔,单位秒, 默认=`10`
* `-s`: 使用https连接webui, 不添加该参数默认使用http

由于种子的列表不经常改变，所以可以适当增加获取间隔.
建议 `-a` 的值是 `-b` 值的整数倍，且整数大于2.

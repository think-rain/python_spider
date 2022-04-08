import urllib.request
import urllib.parse

# urlopen(url, data, timeout)方法用于打开一个URL地址，函数有三个参数：
# url：表示打开的URL地址
# data：表示发送的数据，可以为空
# timeout：表示打开URL的最大等待时间，如果超过这个时间，就会抛出一个URLError异常
# 返回值：表示打开的URL的内容，返回的是一个HTTPResponse对象

response = urllib.request.urlopen('http://www.baidu.com')
print(response.read().decode('utf-8'))

# Request(url, data, headers, method)方法用于构造一个Request对象
# url：表示打开的URL地址
# data：表示发送的数据，可以为空
# headers：表示HTTP的请求头，可以为空
# method：表示HTTP的请求方法，可以为空
# 返回值：同上

urllib.request.Request()
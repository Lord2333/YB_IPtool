import time
import requests
import json
import random

UA_DB = [
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36',
	'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; chromeframe/11.0.696.57)',
	'Opera/12.0(Windows NT 5.1;U;en)Presto/22.9.168 Version/12.00']


def Check_update(Ver):
	Url = 'https://oh.urjj.ml/IPupdate'
	version = float(requests.get(Url).text)
	if version > Ver:
		Info = requests.get('https://ur.daj8.ml/Up_info').text.replace('[/n]', '\n')
		return Info
	else:
		return False


def check_zm():
	# 获取五个代理，结构形如[{ip:'123.123.123.123',port:'456'}]
	IP_API = 'http://webapi.http.zhimacangku.com/getip?num=5&type=2&pro=&city=0&yys=0&port=1&pack=234772&ts=0&ys=0&cs=0&lb=4&sb=0&pb=4&mr=1&regions='
	res = json.loads(requests.get(IP_API).text)
	code = res['code']
	if code == 0:
		return 1, res['data']
	return 0, res['msg']


def Deal_IP():
	flag, data = check_zm()
	IPS = []
	if flag:
		for ips in data:
			proxymeta = str(ips["ip"]) + ':' + str(ips["port"])
			IP = {"http": proxymeta}
			IPS.append(IP)
		return IPS


def Run(App_id, IP):
	url = 'https://q.yiban.cn/app/index/appid/' + App_id
	try:
		res1 = requests.get(url, proxies=IP, headers={'UA': random.choice(UA_DB)})
		return 1
	except requests.exceptions.SSLError:  # 易班接口出错
		return 0


def main():
	Ver = 0.2
	if Check_update(Ver):
		print(Check_update(Ver))
	flag, msg = check_zm()
	if flag:
		Appid = input('请输入轻应用ID：')
		run_time = int(input('请输入运行次数：'))
		if run_time <= 5:
			run_time = 1
		else:
			run_time = int(run_time / 5)
		cnt = 0
		while run_time:
			run_time -= 1
			IPS = Deal_IP()
			for ip in IPS:
				cnt += 1
				Run(Appid, ip)
				print('\r当前请求%d次' % cnt, end='')
				time.sleep(1)
		print('\n任务完成！')
	else:
		print(msg)
		print("芝麻代理官网：https://www.zmhttp.com/")
		i = input('按回车重试')
		main()


if __name__ == '__main__':
	main()

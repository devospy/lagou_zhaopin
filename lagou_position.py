# @Time   :2019/6/22 11:36
# @Author :YTL
# @File   :lagou_position.py

import requests

from lagou_zhaopin import user_agent
import random
import time
from lagou_zhaopin.info import Info
from lxml import etree
import datetime
from urllib.request import quote

_user_agent = random.choice(user_agent.user)

cookie = None
headers = None
url_1 = None
url_2 = None
def data_preprocess(city, job):
	global url_1, url_2,headers
	url_city = quote(city)
	url_job = quote(job)
	
	#url_1 进入拉勾的页面，但是无法获取数据，数据是通过Ajax异步加载的
	url_1 = r'https://www.lagou.com/jobs/list_{job}?city={city}&cl=false&fromSearch=true&labelWords=&suginput='.format(job=url_job, city=url_city)
	#获取数据的网址
	url_2 = r'https://www.lagou.com/jobs/positionAjax.json?city={city}&needAddtionalResult=false'.format(city=url_city)
	#print(url_1)
	#print(url_2)
	headers={
		'Accept': 'application/json, text/javascript, */*; q=0.01',
		'Accept-Encoding': 'gzip, deflate, br',
		'Accept-Language': 'zh-CN,zh;q=0.9',
		'Cache-Control': 'no-cache',
		'Connection': 'keep-alive',
		'Content - Length': '55',
		'Content - Type': 'application / x - www - form - urlencoded; charset = UTF - 8',
		'Host': 'www.lagou.com',
		'Origin': 'https: // www.lagou.com',
		'Pragma': 'no-cache',
		'Referer': url_1,
		'User-Agent': str(_user_agent),
		'X - Anit - Forge - Code': '0',
		'X - Anit - Forge - Token': 'None',
		'X - Requested - With': 'XMLHttpRequest'
	}

zhaopin_url = r'https://www.lagou.com/jobs/'

def get_zhaopin_info(pages=None,):
	global cookie,url_1, url_2,headers
	if pages is None:
		pages = 2
	for page in range(1, pages):
		print("="*20 + 'Start print {0} page zhaopin info.'.format(page) + "="*20)
		if page == 0:
			data = {
				'first': 'true',
				'pn': page,
				'kd': "软件测试"
			}
		else:
			data = {
				'first': 'false',
				'pn': page,
				'kd': "软件测试"
			}
		s = requests.session()
		s.get(url=url_1, headers=headers, timeout=3)
		cookie = s.cookies.get_dict()
		#print(cookie)
		now = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d%H%M%S")
		t = cookie['user_trace_token'].split("-")
		t[0] = now
		cookie['user_trace_token'] = '-'.join(t)
		print(cookie) #主页面cookie
		rep = s.post(url=url_2, headers=headers, data=data, cookies=cookie, timeout=5)
		time.sleep(5)
		content = rep.json()['content']['positionResult']['result']

		parse_zhaopin_info(content)

def parse_zhaopin_info(rep: list):
	global cookie,url_1,url_2,headers
	res_info = []
	for num in range(0,len(rep)):
		print('-'*10 + 'Start print {0}th zhaopin info.'.format(num+1) + '-'*10)
		temp_res: dict = rep[num]  #temp_res: dict
		res = Info()
		res.position_id = temp_res['positionId']
		res._company_name = temp_res['companyFullName']
		res.position_name = temp_res['positionName']
		res.money = temp_res['salary']
		res.work_year = temp_res['workYear']
		res.education = temp_res['education']
		res.job_advantage = temp_res['positionAdvantage']
		res.company_size = temp_res['companySize']
		#res.job_description = temp_res['']  在另一个页面
		#res.job_address = temp_res[''] 在另一个页面
		#res.job_publisher = temp_res[''] 在另一个页面
		job_description_url = zhaopin_url + str(res.position_id) + '.html'
		print(job_description_url)
		now = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d%H%M%S")
		t = cookie['user_trace_token'].split("-")
		t[0] = now
		cookie['user_trace_token'] = '-'.join(t)
		#print(cookie)
		temp_rep = requests.get(job_description_url, headers=headers, cookies=cookie, timeout=5)
		#print("#"*30 + str(temp_rep.content.decode(encoding='utf-8')) + "#"*30)
		html = etree.HTML(temp_rep.content)
		res.job_description = str(html.xpath("//div[@class='job-detail']//text()"))
		res.job_address = str(html.xpath("//div[@class='work_addr']//text()")).replace('-\\n', "").replace('\\n', "").replace(" ", "")
		res.job_publisher = str(html.xpath("//a/span[@class='name']/text()"))
		res_info.append(res)
		write_info(res)
		time.sleep(10)
		
	return res_info

def write_info(res: Info):
	print(res.company_name)
	line = "position_id: " + str(res.position_id) + '\n' +\
	       "company_name: " + str(res.company_name) + '\n' +\
	       "position_name: " + str(res.position_name) + '\n' +\
		   "money: " + str(res.money) + '\n' +\
		   "work_year: " + str(res.work_year) + '\n' +\
		   "education: " + str(res.education) + '\n' +\
		   "job_advantage: " + str(res.job_advantage) + '\n' +\
		   "job_description: " + str(res.job_description) + '\n' +\
		   "job_address: " + str(res.job_address) + '\n' +\
		   "job_publisher: " + str(res.job_publisher) + '\n' +\
		   "company_size: " + str(res.company_size) + '\n'
	    
	with open('zhaopin.txt', 'a+', encoding='utf-8') as f:
		f.write(line)
		f.write("=" * 30 + '\n')


if __name__ == "__main__":
	city = '上海'
	job = '软件测试'
	data_preprocess(city, job)
	get_zhaopin_info(31)

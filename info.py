# coding:UTF-8

# @Time   :2019/6/22 12:47
# @Author :YTL
# @File   :info.py


class Info():
	'''获取招聘公司的信息'''
	
	def __init__(self):
		self._position_id = None #id标识
		self._company_name = None  # 公司名称
		self._position_name = None  # 职位名称信息
		self._money = None  # 薪水
		self._work_year = None  # 工作经验要求
		self._education = None  # 教育程度要求
		self._job_advantage = None  # 职位诱惑
		self._job_description = None  # 职位描述
		self._job_address = None  # 工作地址
		self._job_publisher = None  # 职位发布者
		self._company_size = None #公司规模大小
		
	@property
	def position_id(self):
		return self._position_id
	
	@position_id.setter
	def position_id(self, position_id):
		self._position_id = position_id
		
	@property
	def company_name(self):
		return self._company_name
	
	@company_name.setter
	def company_name(self, name):
		self._company_name = name
	
	@property
	def position_name(self):
		return self._position_name
	
	@position_name.setter
	def position_name(self, position_name):
		self._position_name = position_name
	
	@property
	def money(self):
		return self._money
	
	@money.setter
	def money(self, money):
		self._money = money
	
	@property
	def work_year(self):
		return self._work_year
	
	@work_year.setter
	def work_year(self, work_year):
		self._work_year = work_year
	
	@property
	def education(self):
		return self._education
	
	@education.setter
	def education(self, education):
		self._education = education
		
	@property
	def job_advantage(self):
		return self._job_advantage
	
	@job_advantage.setter
	def job_advantage(self, job_advantage):
		self._job_advantage = job_advantage
	
	@property
	def job_description(self):
		return self._job_description
	
	@job_description.setter
	def job_description(self, job_description):
		self._job_description = job_description
		
	@property
	def job_address(self):
		return self._job_address
	
	@job_address.setter
	def job_address(self, job_address):
		self._job_address = job_address

	@property
	def job_publisher(self):
		return self._job_publisher
	
	@job_publisher.setter
	def job_publisher(self, job_publisher):
		self._job_publisher = job_publisher
	
	@property
	def company_size(self):
		return self._company_size
	
	@company_size.setter
	def company_size(self, company_size):
		self._company_size = company_size
	
if __name__ == "__main__":
	pass
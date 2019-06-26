# coding=utf-8  #或# -*- coding: UTF-8 -*-

# @Time   :2019/6/25 22:19
# @Author :YTL
# @File   :ciyun.py

import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re

word = ['工作职责', '岗位职责', '岗位要求', '任职资格', '职位要求', '任职要求', '职位亮点', '职位描述', '工作内容', '职位诱惑','职责描述',"【【","】"]

def read_txt(file_name):
	res_data = []
	with open(file_name, 'r', encoding='utf-8') as f:
		for line in f.readlines():
			if "job_description" in line:
				line = line.split("[")[1][0:-2]
				for s in word:
					line = line.replace(s, "")
				res_data.append(line)
	print(res_data)
	return res_data

def read_txt2(file_name):
	res_data = []
	with open(file_name, 'r', encoding='utf-8') as f:
		lines = f.readlines()
		lines = ''.join(lines)
		desc = re.findall("job_description: \[(.*?)\]", lines)
		if desc:
			for line in desc:
				line = line.replace("\\n","")
				line = "".join(line.split(","))
				line = line.replace("xa0","").replace("'","").replace(" ","")
				line = line.strip(",").replace(",,", "").replace("\\","")
				for w in word:
					line = line.replace(w,"")
				line = line.replace("：", "").replace(":","")
				#print(line)
				res_data.append(line)
	return res_data

def word_cloud(file_name, image_path):
	bg_pic = plt.imread(image_path)
	text_data = ''.join(read_txt2(file_name))
	wordcloud = WordCloud(mask=bg_pic, background_color='white', scale=2.5,min_font_size=6).generate(text_data)
	plt.imshow(wordcloud)
	plt.axis('off')
	plt.show()
	

if __name__ == "__main__":
	file_name = "zhaopin.txt"
	image_name = "background2.jpg"
	word_cloud(file_name, image_name)
	#read_txt2(file_name)
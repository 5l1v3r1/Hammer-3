#!/usr/bin/python2.7
#coding:utf-8
   
import json
import requests
import time
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
class WebInterface(object):
	"""docstring for webInterface"""
	def __init__(self,server,token):
		super(WebInterface, self).__init__()
		self.server = server
		self.token = token
		self.startTime = 0
		self.endTime = 0
		self.id = None

	def task_start(self,taskurl,args=''):
		try:
			serverurl = 'http://' + self.server +'/scans_add.php'
			# cookies = {'PHPSESSID':self.token}
			postdata = {'type':'start','token':self.token,'url':taskurl,'args':args}

			r = requests.post(serverurl,data=postdata)
			# print r.status_code,r.text
			if r.status_code == 200 and r.text != '':
				# print r.request.headers
				# print r.request.body
				# print r.text
				# self.startTime = json.loads(r.text)['startTime']
				self.id = json.loads(r.text)['id']
			else:
				print 'return error, please check token and server'
			pass
		except requests.HTTPError,e:
			print 'requests.HTTPError', e

	def task_end(self):
		try:
			serverurl = 'http://' + self.server +'/scans_add.php'
			# cookies = {'PHPSESSID':self.token}
			# print retinfo
			postdata = {'type':'end','token':self.token,'id':self.id}

			r = requests.post(serverurl,data=postdata)
			# print r.request.headers
			# print r.request.body
			print r.text
			if r.status_code == 200:
				# print r.text
				pass
			else:
				print 'return error, please check token and server'
		except requests.HTTPError,e:
			print 'requests.HTTPError', e

	def task_end_old(self,taskurl,retinfo):
		try:
			serverurl = 'http://' + self.server +'/scans_add.php'
			# cookies = {'PHPSESSID':self.token}
			retinfo = json.dumps(retinfo)
			# print retinfo
			postdata = {'type':'end','token':self.token,'ipurl':taskurl,'id':self.id,'retinfo':retinfo}

			r = requests.post(serverurl,data=postdata)
			# print r.request.headers
			print r.request.body
			print r.text
			if r.status_code == 200:
				# print r.text
				pass
			else:
				print 'return error, please check token and server'
		except requests.HTTPError,e:
			print 'requests.HTTPError', e
	

	
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	server = 'www.hammer.org'
	token = 'uuppgj43ig9hc0tgcjeqo88t50'
	taskurl = 'http://www.eguan.cn'
	wi = WebInterface(server,token)
	wi.task_start(taskurl)
	print wi.id
	time.sleep(2)
	retinfo=[{'content': {u'HTTPServer': {u'string': [u'Microsoft-IIS/6.0']}, u'X-Powered-By': {u'string': [u'ASP.NET']}}, 'type': 'Web Application Recognition', 'level': 'info'}, {'content': 'http://www.eguan.cn/aspnet_client/\tcode:403\nhttp://www.eguan.cn/images/\tcode:403\nhttp://www.eguan.cn/aspnet_client/system_web/2_0_50727/\tcode:403\nhttp://www.eguan.cn/images\tcode:403\nhttp://www.eguan.cn/aspnet_client/FreeTextBox/\tcode:403\nhttp://www.eguan.cn/upload\tcode:403\nhttp://www.eguan.cn/aspnet_client/system_web/2_0_50727\tcode:403\nhttp://www.eguan.cn/aspnet_client/system_web/\tcode:403\n', 'type': 'Sensitive File/Directory Discover', 'level': 'low'}, {'content': 'OPTIONS, TRACE, GET, HEAD', 'type': 'IIS PUT Vulnerability', 'level': 'high'}]
	wi.task_end_old(taskurl,retinfo)
	taskurl = 'http://eguan.cn'
	retinfo=[{'content': {u'HTTPServer': {u'string': [u'Microsoft-IIS/6.0']}, u'X-Powered-By': {u'string': [u'ASP.NET']}}, 'type': 'Web Application Recognition', 'level': 'info'}, {'content': 'http://www.eguan.cn/aspnet_client/\tcode:403\nhttp://www.eguan.cn/images/\tcode:403\nhttp://www.eguan.cn/aspnet_client/system_web/2_0_50727/\tcode:403\nhttp://www.eguan.cn/images\tcode:403\nhttp://www.eguan.cn/aspnet_client/FreeTextBox/\tcode:403\nhttp://www.eguan.cn/upload\tcode:403\nhttp://www.eguan.cn/aspnet_client/system_web/2_0_50727\tcode:403\nhttp://www.eguan.cn/aspnet_client/system_web/\tcode:403\n', 'type': 'Sensitive File/Directory Discover', 'level': 'low'}, {'content': 'OPTIONS, TRACE, GET, HEAD', 'type': 'IIS PUT Vulnerability', 'level': 'info'}]
	wi.task_end_old(taskurl,retinfo)
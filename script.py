
import requests
from bs4 import BeautifulSoup

class User:
	"""User Class """
	def __init__(self,usrname):
		""" scrap and initialise details """
		url = 'https://github.com/'
		repo_li = '?tab=repositories'

		soup = BeautifulSoup(requests.get(url+usrname).content,'html.parser') # main user page

		self.name = soup.find('h1',{'class':'vcard-names'}).find_all('span')[0].text # user name		

		try:
			self.bio = soup.find('div',{'class','user-profile-bio'}).text # bio 
		except:
			self.bio = 'None' # some users do not add bio
		self.contributions = soup.find('div',{'class':'js-contribution-graph'}).h2.text.strip().split('\n')[0] # user's contributions

		repos = BeautifulSoup(requests.get(url+usrname+repo_li).content,'html.parser')
		self.rep_list = [] # list of repositories

		all_repos = repos.find('div',{'id':'user-repositories-list'}).ul.find_all('li')

		for rep in all_repos:
			project_name = rep.find('a',{'itemprop':'name codeRepository'}).text.strip() # project name
			try:
				project_description = rep.find('p',{'itemprop':'description'}).text.strip() # project description
			except:
				project_description = 'None'
			try:
				project_lang = rep.find('div',{'class':'f6'}).find_all('span')[1].text.strip() # language used
			except:
				project_lang = 'None' # if no files were added and thus language used must be none
			self.rep_list.append({'name':project_name,'desc':project_description,'lang':project_lang}) # appending data as dictionary

	def user_details(self):
		"""Display user details"""
		print('\n\nName : {}\nBio : {}\nContributions : {} in last year'.format(self.name,self.bio,self.contributions))

	def user_repos(self):
		"""Display reposiory details"""
		for repo in self.rep_list:
			print('\n\n')
			print('Project Name : '+repo['name'])
			print('Description : '+repo['desc'])
			print('Language : '+repo['lang'])




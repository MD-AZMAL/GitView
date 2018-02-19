
import requests
from bs4 import BeautifulSoup

class User:
	"""User Class """
	def __init__(self,usrname):
		""" scrap and initialise details """
		url = 'https://github.com/'
		repo_li = '?tab=repositories'

		soup = BeautifulSoup(requests.get(url+usrname).content,'html.parser') # main user page

		names = soup.find('h1',{'class':'vcard-names'}).find_all('span') 	# span containing deatails for names
		name = names[0].text			
		nick_name = names[1].text
		bio = soup.find('div',{'class','user-profile-bio'}).text # bio 
		contributions = soup.find('div',{'class':'js-contribution-graph'}).h2.text.strip().split('\n')[0] # user's contributions

		repos = BeautifulSoup(requests.get(url+usrname+repo_li).content,'html.parser')
		rep_list = [] # list of repositories

		all_repos = repos.find('div',{'id':'user-repositories-list'}).ul.find_all('li')

		for rep in all_repos:
			project_name = rep.find('a',{'itemprop':'name codeRepository'}).text.strip() # project name
			project_description = rep.find('p',{'itemprop':'description'}).text.strip() # project description
			try:
				project_lang = rep.find('div',{'class':'f6'}).find_all('span')[1].text.strip() # language used
			except:
				project_lang = 'None' # if no files were added and thus language used must be none
			rep_list.append({'name':project_name,'desc':project_description,'lang':project_lang}) # appending data as dictionary
		self.name = name
		self.nick_name = nick_name
		self.bio = bio
		self.contributions = contributions
		self.repos = rep_list

	def user_details(self):
		"""Display user details"""
		print('Name : {}\nNick Name : {}\nBio : {}\nContributions : {} in last year'.format(self.name,self.nick_name,self.bio,self.contributions))

	def user_repos(self):
		"""Display reposiory details"""
		for repo in self.repos:
			print('\n\n')
			print('Project Name : '+repo['name'])
			print('Description : '+repo['desc'])
			print('Language : '+repo['lang'])
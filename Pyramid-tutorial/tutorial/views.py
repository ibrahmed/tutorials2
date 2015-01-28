from pyramid.view import (
    view_config,
    view_defaults
    )

from BeautifulSoup import BeautifulSoup
from lxml import html
import requests

@view_defaults(route_name='form')
class TutorialViews(object):
    def __init__(self, request):
        self.request = request
      
    @view_config(route_name='home', renderer='home.pt')
    def home(self):
        return {}

    # Retrieving /howdy/first/last the first time
    @view_config(renderer='form.pt')
    def Form(self):
        return {}

    # Posting to /howdy/first/last via the "Edit" submit button
    @view_config(request_method='POST', renderer='edit.pt')
    def edit(self):
		main_list = [] 
		page = requests.get(self.request.params['new_url'])
		html = page.text
		soup = BeautifulSoup(html)
		h2_list = soup.findAll('h2')
		for item in h2_list:
			if item.contents[0]=='Contents':
        			#if item.a.get('href')=='#contents':
                		content_list = item.findNext('ul').findAll('li')
                     		for i in content_list:
					main_list.append(i.contents[0].text)
				
        	return {'page_title': 'Edit View', 'main_list':main_list}





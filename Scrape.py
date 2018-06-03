
# coding: utf-8

# In[3]:

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


# In[4]:

from bs4 import BeautifulSoup


# In[5]:

soup = BeautifulSoup(html_doc,'html.parser')


# In[6]:

print(soup.prettify())


# In[7]:

soup.title


# In[8]:

title = soup.title


# In[10]:

title.text


# In[11]:

soup.title.name


# In[12]:

soup.title.string  ##same as title.text here


# In[13]:

soup.title.parent.name


# In[19]:

soup.p


# In[23]:

soup.p['class']


# In[24]:

soup.a


# In[27]:

soup.a


# In[26]:

soup.find_all('a')


# In[30]:

soup.find(id="link2")


# In[31]:

soup.find(href="http://example.com/lacie")


# In[32]:

for link in soup.find_all('a'):
    print(link.get('href'))


# In[33]:

print(soup.get_text)


# In[34]:

"""Parser             	Typical usage                        	Advantages                                       	Disadvantages
Python’s html.parser	BeautifulSoup(markup, "html.parser")	Batteries included,Decent speedLenient (as of Python 2.7.3 and 3.2.)Not very lenient (before Python 2.7.3 or 3.2.2)
lxml’s HTML parser	BeautifulSoup(markup, "lxml")	Very fast,LenientExternal C dependencylxml’s 
XML parser	BeautifulSoup(markup, "lxml-xml") 
BeautifulSoup(markup, "xml")	
Very fast
The only currently supported XML parser
External C dependency
html5lib	BeautifulSoup(markup, "html5lib")	
Extremely lenient
Parses pages the same way a web browser does
Creates valid HTML5
Very slow
External Python dependency"""


# In[38]:

soup = BeautifulSoup('<b class="boldest">Extremely bold</b>',"lxml")
tag = soup.b


# In[40]:

type(tag)


# In[41]:

tag.name


# In[42]:

tag.name = "blockquote"
tag
# <>


# In[ ]:




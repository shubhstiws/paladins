
# coding: utf-8

# # Paladins API python implementation

# MIT License
# 
# Copyright (c) [2018] [Shubhankar Tiwari]
# 
# <!-- Place this tag where you want the button to render. -->
# <a class="github-button" href="https://github.com/shubhstiws" aria-label="Follow @shubhstiws on GitHub">Follow @shubhstiws</a>
# <!-- Place this tag in your head or just before your close body tag. -->
# <script async defer src="https://buttons.github.io/buttons.js"></script>
# 
# [Paladins API Documentation](https://docs.google.com/document/d/1OFS-3ocSx-1Rvg4afAnEHlT3917MAK_6eJTR6rzr-BM/edit) 

# #### Load libraries

# In[87]:


import requests
import time
import datetime
import json
import calendar
import hashlib


# #### Create Atlanta, Georgia timestamp

# In[217]:


def tsgen():
    ts = datetime.datetime.fromtimestamp(time.time()) #get current time
    ts_temp = ts + datetime.timedelta(days=1)

    #add 5 hours to get Georgia time (change this to time in your region)
    if ts.hour > 18:
        temp_hr = (ts.hour+5)-24
        temp_day = ts_temp.day
    else: 
        temp_hr = ts.hour+5
        temp_day = ts.day

    ts = datetime.datetime(ts.year,ts.month,temp_day,temp_hr,ts.minute,ts.second).strftime('%Y%m%d%H%M%S') 
    return ts


# #### Setup Keys and api

# In[301]:


devId = '****'
authKey = '*'
pal='http://api.paladins.com/paladinsapi.svc'
smite = 'http://api.smitegame.com/smiteapi.svc'
temp = tsgen()


# #### Create Signature

# In[197]:


def signature_id(method):
    signature = str(devId)+str(method)+str(authKey)+str(temp)
    signature = hashlib.md5(signature.encode('utf-8')).hexdigest()
    return signature


# #### Create session

# In[262]:


def session_id(urlPrefix):
    
    signature = signature_id('createsession')

    url = str(urlPrefix)+'/'+'createsessionJson'+'/'+str(devId)+'/'+str(signature)+'/'+str(temp)
    sess = loadUrl(url)['session_id']
    return sess


# #### Generate timestamp and session id

# In[291]:


def refresh():
    temp = tsgen()
    session = session_id(pal)
    return temp,session
temp,session=refresh()


# #### Generate URL

# In[247]:


def genUrl(method):
    return pal+'/'+str(method)+'json'+'/'+devId+'/'+signature_id(method)+'/'+session+'/'+temp


# #### Load url()

# In[213]:


def loadUrl(url):
    return json.loads(requests.get(url).content)


# ### If you get timestamp exception run <font color='red'> refresh() </font>

# ### APIs Connectivity:

# #### <font color='red'>Python ping</font>

# In[215]:


def ping():
    method = 'pingjson'
    url = pal+'/'+method
    return loadUrl(url)


# #### <font color='red'>Python testsession</font>

# In[232]:


def testsession():
    url=genUrl('testsession')
    return loadUrl(url)


# #### <font color='red'>Python getplayer()</font>

# In[238]:


def getplayer(ign):
    url = genUrl('getplayer')+'/'+str(ign)
    return loadUrl(url)


# #### <font color='red'> Python gethirezserverstatus() </font>

# In[240]:


def gethirezserverstatus():
    url=genUrl('gethirezserverstatus')
    return loadUrl(url)


# ### APIs

# #### <font color = 'red' > Python getdataused() </font>

# In[242]:


def getdataused():
    url=genUrl('getdataused')
    return loadUrl(url)


# #### <font color = 'red' > Python getdemodetails() </font>

# In[252]:


def getdemodetails(matchid):
    url=genUrl('getdemodetails')+'/'+str(matchid)
    return loadUrl(url)


# #### <font color = 'red' > Python getesportsproleaguedetails() </font> 

# In[253]:


def getesportsproleaguedetails():
    url=genUrl('getesportsproleaguedetails')
    return loadUrl(url)


# #### <font color = 'red' > Python getfriends() </font> 

# In[275]:


def getfriends(ign):
    url=genUrl('getfriends')+'/'+str(ign)
    return loadUrl(url)


# #### <font color = 'red' > Python getchampionranks() </font> 

# In[280]:


def getchampionranks(ign):
    url=genUrl('getchampionranks')+'/'+str(ign)
    return loadUrl(url)


# #### <font color = 'red' > Python getmatchhistory() </font> 

# In[282]:


def getmatchhistory(ign):
    url=genUrl('getmatchhistory')+'/'+str(ign)
    return loadUrl(url)


# #### <font color = 'red' > Python getplayerachievements() </font> 

# In[299]:


def getplayerachievements(ign):
    id = getplayer(ign)[0]['Id']
    url=genUrl('getplayerachievements')+'/'+str(id)
    return loadUrl(url)


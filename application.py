''' The application programs interface for likes by genix shop
Please download this file ready too.
'''

import requests as XMLHttpRequest

def Likers(cookies,target):
	OnReady = XMLHttpRequest.post("https://az-like.com/likes",headers={"cookie": f"__gads=ID=e7afc2688ac82e35-22abbe80f1db0044:T=1678352964:RT=1678352964:S=ALNI_MbLbU3pcFSslRZGAIzTJQ7TD6zZpw;_gid=GA1.2.627146000.1682435051;__gpi=UID=00000bd4dc223ab2:T=1678352964:RT=1682435052:S=ALNI_Mb8_Py3rv5RW-PuTrPjU-J-M56rTQ;{cookies};_gat_gtag_UA_175303241_1=1;_ga_Q6G7B4WRCL=GS1.1.1682435049.5.1.1682437560.0.0.0;_ga=GA1.1.606891092.1678352956","user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36"},json={"fbid":target,"type":"1"})
	print(OnReady.json())
	
def ReadyLogin(tokens):
	cookies = XMLHttpRequest.post("https://az-like.com/loginWithToken_v2",headers={"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","cookie": "__gads=ID=e7afc2688ac82e35-22abbe80f1db0044:T=1678352964:RT=1678352964:S=ALNI_MbLbU3pcFSslRZGAIzTJQ7TD6zZpw;_gid=GA1.2.627146000.1682435051;__gpi=UID=00000bd4dc223ab2:T=1678352964:RT=1682471433:S=ALNI_Mb8_Py3rv5RW-PuTrPjU-J-M56rTQ;_ga_Q6G7B4WRCL=GS1.1.1682471432.6.1.1682471482.0.0.0;_ga=GA1.2.606891092.1678352956;az_likecom_session=eyJpdiI6InhRRnZaakp0eVlZclZrR3RkOHVBWUE9PSIsInZhbHVlIjoiRXdWUm9FQU5IWGhyUks1Z3Q4R25Bc0lNOFZkcFdmdnE0ZEVGblU5ajdJcEhjdWIrVnFScFZ2TkdIT3BkMTh1TkpjOFQ5K3gvaEJPRlhZOWVpUStIMnBFZFBQeDdmcnpuUG1XRzFaUXpjcjFmRnVLWEhCM0JFTC9WQUYvWWJodUUiLCJtYWMiOiJhMDM5ZTFhYTBjMDI1NjM5MWY5NGZlMzEwNjIwZjM5MTU3ZjgxOGQ2N2Q5ZTk3OThkZDA2NzcwYzNkNmNhYjBhIn0%3D"},json={"access_token": tokens})
	cookie = cookies.headers['set-cookie'][:349]

"""
Application Programs Interface List Normal [GENIX SHOP]
"""
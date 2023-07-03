from pyfacebook import GraphAPI
# import pyfacebook as fb
api = GraphAPI(access_token ='EAANZBowEVZATsBAIu7sRl78Y8PhkMCBb2ezEhJ1ZBXDjanqR4pWypi9geelerr3MGseOSvBWJ5TXIyM869ahJFuZCh8xaWCIzpyRTEU9yRpwHYDoRv80kAzyGJNaDg2BZBiZBbE32UZBKkdOXn1AWYtWwEFgdw4CHPwFm58nwU63HTusNGUWcRi')
# fb.page.get_info(page_id="310621318958658")
# Page(id='310621318958658', name='Rappler')
api.get_object(object_id="310621318958658")

import urllib
import http.cookiejar

URL = 'https://www.google.ca/'

def extract_cookies():
    cookie_jar = http.cookiejar.CookieJar()

    url_opener = urllib.request.build_opener(urllib.request.HTTPCookieprocessor(cookie_jar))
    url_opener.open(URL)
    for cookie in cookie_jar:
        print("[Cookie Name = %s] -- [cookie_value = %s]" % (cookie.Name, cookie.value))
        if __name__ == '__main__':
            extract_cookies()

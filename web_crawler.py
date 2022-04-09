'''
Given a url startUrl and an interface HtmlParser, implement a web crawler to crawl all links that are under the same hostname as startUrl. 

Return all urls obtained by your web crawler in any order.

Your crawler should:

Start from the page: startUrl
Call HtmlParser.getUrls(url) to get all urls from a webpage of given url.
Do not crawl the same link twice.
Explore only the links that are under the same hostname as startUrl.
'''


def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        hostname, grab = '', False
        # get hostname
        for index, char in enumerate(startUrl):
            if grab:
                if char == '/':
                    break
                hostname += char
            if char == '/' and startUrl[index-1] == '/':
                grab = True
        hostname = 'http://' + hostname
		# process stack
        result, stack = set([startUrl]), [startUrl]
        while stack:
            q = stack.pop()
            urls = htmlParser.getUrls(q)
            for url in urls:
                if url.find(hostname) != -1:
                    if url not in result:
                        result.add(url)
                        stack.append(url)
        return result
      
      
-------------------------

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        self.ans = set()
        hostname = self.parse(startUrl)
        self.helper(hostname, startUrl, htmlParser)  
        
        return list(self.ans)
        
    def helper(self, start_host, url, htmlParser):
        host = self.parse(url)
        if start_host == host and url not in self.ans:
            self.ans.add(url)
            
            next_urls = htmlParser.getUrls(url)
            for nu in next_urls:
                self.helper(start_host, nu, htmlParser)
        return
        
        
    def parse(self, url):
        res = re.match(r"http:\/\/([a-zA-Z0-9\.\-]+)", url)
        if res:
            hostname = res.group(1)
            return hostname
        return ""

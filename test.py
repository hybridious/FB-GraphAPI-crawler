# coding=utf-8

import GraphCrawler as GC


if __name__ == '__main__':
    crawler = GC.GraphCrawler(page_name='littlelifer')
    print crawler.get_access_token()
    # posts = crawler.get_posts(since="2016-06-20", until="2016-06-25")

    # print posts.text
    # print posts["data"]
    # for post in posts["data"]:
    #     print post['id']
    # print post['data']
    # for post in posts.text['data']:
    #     print post.data.id

    posts = crawler.save_posts(since="2016-06-20", until="2016-06-25")


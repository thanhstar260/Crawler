# from facebook_scraper import get_posts

# postIDs = []
# for post in get_posts('nintendo', pages=5):
#     postIDs.append(post['post_id'])
#     print(postIDs)

from facebook_scraper import get_posts
import pandas as pd
import csv
FANPAGE_LINK ="neuconfessions"
FOLDER_PATH = r"D:/UIT/Năm 2/Kỳ 4/Tính toán đa phương tiện/Lab/Lab01/comments_crawl"
PAGES_NUMBER = 5
post_list = []
for post in get_posts(FANPAGE_LINK, 
                    options={"comments": True, "reactions": False, "allow_extra_requests": False}, 
                    extra_info=False, pages=10):
    post_list.append(post)
    
fields_list = ['post_id', 'text', 'likes', 'comments', 'shares', 'post_url', 'link', 'username']
result_list = []
for post in post_list:
    my_obj = {}
    for field in fields_list:
        my_obj[field] = post[field]
    ## Manipulate Comments
    if len(post['comments_full']) > 0:
        my_obj['comments_content'] = '\n'.join([comment['comment_text'] for comment in post['comments_full']])
    result_list.append(my_obj)

df = pd.DataFrame(result_list)
df.to_csv(FOLDER_PATH + FANPAGE_LINK + "4.csv", index=True, encoding='utf-8-sig', quoting=csv.QUOTE_ALL, line_terminator='\r\n')


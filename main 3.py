import requests
import time
import json

# 人气popularity
# 点赞total_upvote_num
url = "https://u5pyq.webapp.163.com/apps/u5/house/get_house_data?avatar_id=ZDk%2BNgYrcxAaCF4K"
headers = {
  "Host": "u5pyq.webapp.163.com",
  "Connection": "keep-alive",
  "content-type": "application/json",
  "Accept-Encoding": "gzip,compress,br,deflate",
  "User-Agent": "Mozilla/5.0 (iPad; CPU OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.49(0x18003137) NetType/WIFI Language/zh_CN",
  "Referer": "http"
}
response = requests.get(url, headers=headers).json()
response = response['data']['house']
print(response)
old_popularity = json.loads(response)['popularity']
old_total_upvote_num = json.loads(response)['total_upvote_num']
print('初始化完成...')
while True:
    url = "https://u5pyq.webapp.163.com/apps/u5/house/get_house_data?avatar_id=ZDk%2BNgYrcxAaCF4K"
    headers = {
        "Host": "u5pyq.webapp.163.com",
        "Connection": "keep-alive",
        "content-type": "application/json",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPad; CPU OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.49(0x18003137) NetType/WIFI Language/zh_CN",
        "Referer": "http"
    }

    res = requests.get(url, headers=headers).json()
    res = res['data']['house']
    popularity = json.loads(res)['popularity']
    total_upvote_num = json.loads(res)['total_upvote_num']
    if popularity != old_popularity or total_upvote_num != old_total_upvote_num:
        new_popularity = popularity
        new_total_upvote_num = total_upvote_num
        requests.post('http://localhost:3113/send_group_msg', json={
            'user_id': 980811231,
            'group_id': 980811231,
            'message': [{
                'type': 'text',
                'data': {
                    'text': f'庄园数据变动通知\n人气值：\n\t·{old_popularity} -> {new_popularity}\n点赞量：\n\t·{old_total_upvote_num} -> {new_total_upvote_num}'
                }
            }]
        })
        old_popularity = popularity
        old_total_upvote_num = total_upvote_num
        print("数据变动通知已发送")
    else:
        print(f"{old_popularity} -> {popularity}\n{old_total_upvote_num} -> {total_upvote_num}")
    time.sleep(10)
    
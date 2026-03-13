from operator import itemgetter

import requests

# make an API call, and store the response

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# prosses info about each submision
submission_ids = r.json()
submission_dict = []
submission_dicts = sorted(submission_dict, key=itemgetter('comments'), 
                          reverse=True)
for submission_id in submission_ids[:30]:
    # make a new api for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # build a dictoinary for each article
    submission_dict = {
        'title': response_dict['title'],
        'hm_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)


for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discution link: {submission_dict['hm_link']}")
    print(f"Comments: {submission_dict['comments']}")

import requests


def count_words(subreddit, word_list, after=None, count_dic=None):
    """Recursively queries the Reddit API and prints a sorted count of given keywords."""
    if count_dic is None:
        count_dic = {}

    headers = {'User-Agent': 'xica369'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}

    response = requests.get(url, headers=headers, params=parameters, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get('data')
    if not data:
        return

    after = data.get('after')
    posts = data.get('children')

    for post in posts:
        title = post.get('data').get('title')
        for word in word_list:
            count = title.lower().split().count(word.lower())
            if count:
                count_dic[word.lower()] = count_dic.get(word.lower(), 0) + count

    if after is not None:
        count_words(subreddit, word_list, after=after, count_dic=count_dic)
    else:
        count_list = sorted(count_dic.items(), key=lambda x: (-x[1], x[0]))
        for word, count in count_list:
            print("{}: {}".format(word, count))


if __name__ == '__main__':
    subreddit = input("Enter subreddit: ")
    word_list = input("Enter list of keywords separated by spaces: ").lower().split()
    count_words(subreddit, word_list)


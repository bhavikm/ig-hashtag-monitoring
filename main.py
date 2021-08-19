"""
Name: main.py
Description: This script would allow to search for the popular IG Hastags
Date: Aug-18-2021

"""

def get_hashtags_to_monitor():
    return ['#photostreamdemo', '#trent100']


def main():
    hashtags_to_monitor = get_hashtags_to_monitor()

    # get hashtag IDs - https://developers.facebook.com/docs/instagram-api/reference/ig-hashtag

    # every x minutes loop:

    # for each hashtag

    # get latest posts from hashtag - https://developers.facebook.com/docs/instagram-api/reference/ig-user/recently_searched_hashtags

    # if post ID not in cache (Redis or advise otherwise)

    # process the post and post to URL
    # process_post(ig_post_data)

    # save processed post IDs to cache
    pass


def process_post(ig_post_data):
    # once we have some sample responses from the API lets discuss the processing steps
    return {}


if __name__ == '__main__':
    main()

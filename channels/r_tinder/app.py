#encoding:utf-8

t_channel = '@rtinder'
subreddit = 'Tinder'


def send_post(submission, r2t):
    return r2t.send_simple(submission)

Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import praw
... 
... 
... # Create a Reddit instance
... reddit = praw.Reddit(client_id='eOEg0PHcT1Lsljyh30YM0A',
...                      client_secret='E5PJgAZuzDShPFqaRk2YrZ13TYpi8Q',
...                      user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')
... 
... # Specify the search query
... search_query = 'nsfw'
... 
... # Search for NSFW subreddits that allow crossposting
... crosspostable_nsfw_subreddits = []
... for subreddit in reddit.subreddits.search(search_query, limit=None):
...     if subreddit.allow_crosspost and subreddit.over18:
...         crosspostable_nsfw_subreddits.append(subreddit)
... 
... # Save the crosspostable NSFW subreddits in a text file
... file_path = 'crosspostable_nsfw_subreddits.txt'
... with open(file_path, 'w') as file:
...     for subreddit in crosspostable_nsfw_subreddits:
...         file.write('Subreddit: ' + subreddit.display_name + '\n')
...         file.write('Description: ' + subreddit.public_description + '\n')
...         file.write('---\n')
... 
... print('Crosspostable NSFW subreddits saved in', file_path)

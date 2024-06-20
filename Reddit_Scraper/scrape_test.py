import praw
import csv

from credentials import p_id, p_agent, p_secret, p_pass

post_search_limit = 10
sub_name = 'Stocks'
csv_file = 'reddit_posts.csv'

#reddit = praw.Reddit(client_id=p_id,
                     #client_secret=p_secret,
                     #user_agent=p_agent)


reddit = praw.Reddit(
    client_id=p_id,
    client_secret=p_secret,
    password=p_pass,
    user_agent='testscript',
    username=p_agent,
)

print(reddit.read_only)
print(reddit.user.me())


# Subreddit to search
subreddit = reddit.subreddit(sub_name) 

# Keywords to search for in post titles or selftexts
keywords = ['TSLA'] 
print("Keyword Query = {}".format(' '.join(keywords)))






with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Text', 'URL', 'Author', 'Score', 'Upvote Ratio', 'Comments'])


    for submission in subreddit.search(query=' '.join(keywords), sort='new', limit=post_search_limit):

        # Filter by keywords in title or selftext
        if any(keyword.lower() in submission.title.lower() or 
               (submission.selftext and keyword.lower() in submission.selftext.lower())
               for keyword in keywords):
            
            # Write relevant data to CSV
            writer.writerow([submission.title,
                             submission.selftext,
                             submission.url,
                             submission.author,
                             submission.score,
                             submission.upvote_ratio,
                             submission.num_comments])

            print(f"Post '{submission.title}' saved to CSV.")

print("CSV file generation complete.")




'''
# Open CSV file for writing with headers
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Text', 'URL', 'Author', 'Score', 'Upvote Ratio', 'Comments'])

    # Iterate through posts in the subreddit
    for submission in subreddit.search(query=' '.join(keywords), sort='new', limit=post_search_limit):
            continue

        # Filter by keywords in title or selftext
        #if any(keyword.lower() in submission.title.lower() or 
               #(submission.selftext and keyword.lower() in submission.selftext.lower())
               #for keyword in keywords):
            
            # Write relevant data to CSV
            writer.writerow([submission.title,
                             submission.selftext,
                             submission.url,
                             submission.author,
                             submission.score,
                             submission.upvote_ratio,
                             submission.num_comments])

            #print(f"Post '{submission.title}' saved to CSV.")

#print("CSV file generation complete.")'''


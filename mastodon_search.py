import pandas as pd
directory = pd.read_csv('mastodon_directory.csv') #Read the directory
print(f"Unique instances: {directory['instance'].unique()}") #Print the unique instances I'm pulling from
search_for = ['Machine Learning', 'MachineLearning'] #Search for these terms
matches = directory[directory['note'].str.contains('|'.join(search_for), case=False, na=False)|directory['fields'].str.contains('|'.join(search_for), case=False, na=False)]
matches = matches.sort_values(by=['followers_count'], ascending=False) #Sort by followers
usernames = matches['username'].tolist() #Get the usernames
instances = matches['instance'].tolist() #Get the instances
followers = matches['followers_count'].tolist() #Get the follower counts
print(f"{len(usernames)} matches found:") #Print the number of matches
for i in range(len(usernames)):
    print(f"{usernames[i]}@{instances[i]} (Followers: {int(followers[i])})") #Print the matches
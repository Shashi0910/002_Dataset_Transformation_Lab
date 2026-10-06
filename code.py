import pandas as pd
import numpy as np

df = pd.read_csv("day02_usage.csv")
chat = df["Chat"].to_numpy()
video = df["Video"].to_numpy()
study = df["Study"].to_numpy()
games = df["Games"].to_numpy()

# print(chat.shape," ", video.shape, " ", study.shape, " ", games.shape)

# total minutes over the thirty days
print("Total Time Spent on each app over 30 days : ")
print("Chat : ",chat.sum())
print("Video : ",video.sum())
print("Study : ",study.sum())
print("Games : ",games.sum())

# average minutes per day, rounded to one decimal
print("Average minutes spent per day on each app : ")
print("Chat : ",round(chat.mean(),1))
print("Video : ",round(video.mean(),1))
print("Study : ",round(study.mean(),1))
print("Games : ",round(games.mean(),1))

#Create a new array holding Study minutes minus Games minutes for every day
diff = study - games
print(diff)

#Print the day number of your best value and the day number of your worst value.
print(f"""The best (Study - Games) day : Day{int(diff.argmax())+1} with {int(diff.max())}
The worst (Study - Games) day : Day{int(diff.argmin())+1} with {int(diff.min())}""")

#D1. Which app won each day?
app_won = []
for i in range(len(chat)):
    if (chat[i] > games[i] and chat[i] > study[i] and chat[i] > video[i]):
        app_won.append("Chat")
    elif(chat[i] < games[i] and games[i] > study[i] and games[i] > video[i]):
        app_won.append("Games")
    elif(chat[i] <study[i] and games[i] < study[i] and study[i] > video[i]):
        app_won.append("Study")
    else :
        app_won.append("Video")
print("App that won day wise : ",app_won)

#D2. What share of each day did each app take?
total = study + games + video + chat
print("Share of each day a app took : ")
print("Chat Share : ",(chat/total)*100)
print("\nVideo Share : ",(video/total)*100)
print("\nStudy Share : ",(study/total)*100)
print("\nGames Share : ",(games/total)*100)

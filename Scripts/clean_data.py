import pandas as pd
import mysql.connector as sql

df = pd.read_csv("../Data/ufc-master.csv")

df["RedWinsByDecision"] = df["RedWinsByDecisionUnanimous"] + df["RedWinsByDecisionMajority"] + df["RedWinsByDecisionSplit"]
df["BlueWinsByDecision"] = df["BlueWinsByDecisionUnanimous"] + df["BlueWinsByDecisionMajority"] + df["BlueWinsByDecisionSplit"]
df["WinnerName"] = df.apply(lambda row: row["RedFighter"] if row["Winner"] == "Red" else row["BlueFighter"], axis=1)
df["FinishDetails"] = df["FinishDetails"].fillna("No Finish")
df["BlueStance"] = df["BlueStance"].fillna("Unknown")
df["Finish"] = df["Finish"].fillna("Unknown")

data_points = ["RedFighter", "BlueFighter", "RedOdds", "BlueOdds", "Winner", "WinnerName", "Finish", "FinishDetails",
          "Date", "Location", "TitleBout", "RedWins", "RedWinsByKO", "RedWinsBySubmission", "RedWinsByDecision", "RedLosses", "BlueWins",
          "BlueWinsByKO", "BlueWinsBySubmission", "BlueWinsByDecision", "BlueLosses", "RedHeightCms", "BlueHeightCms", "RedReachCms", 
          "BlueReachCms", "WeightClass", "RedAvgSigStrLanded", "RedAvgTDLanded", "RedAvgSigStrPct", "RedAvgSubAtt",
          "BlueAvgSigStrLanded", "BlueAvgTDLanded", "BlueAvgSigStrPct", "BlueAvgSubAtt", "RedStance", "BlueStance"]

for d in data_points:
    if df[d].isnull().sum() > 0:
        df[d] = df[d].fillna(df[d].mean())
df = df[data_points]
df.to_csv("../Data/ufc-cleaned.csv")
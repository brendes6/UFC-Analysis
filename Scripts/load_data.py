import pandas as pd
import mysql.connector as sql

df = pd.read_csv("../Data/ufc-cleaned.csv")

connection = sql.connect(host="localhost", user="root", password="Daisydog1200$", 
                         database="ufc_matchup_database", connection_timeout=300)
cursor = connection.cursor()

vals = [(row["RedFighter"], row["BlueFighter"], row["RedOdds"], row["BlueOdds"], row["Winner"], row["WinnerName"], row["Finish"], row["FinishDetails"],
          row["Date"], row["Location"], row["TitleBout"], row["RedWins"], row["RedWinsByKO"], row["RedWinsBySubmission"], row["RedWinsByDecision"], row["RedLosses"], row["BlueWins"],
          row["BlueWinsByKO"], row["BlueWinsBySubmission"], row["BlueWinsByDecision"], row["BlueLosses"], row["RedHeightCms"], row["BlueHeightCms"], row["RedReachCms"], row["BlueReachCms"], 
          row["WeightClass"], row["RedAvgSigStrLanded"], row["RedAvgTDLanded"], row["RedAvgSigStrPct"], row["RedAvgSubAtt"],
          row["BlueAvgSigStrLanded"], row["BlueAvgTDLanded"], row["BlueAvgSigStrPct"], row["BlueAvgSubAtt"],row["RedStance"], row["BlueStance"]) for n, row in df.iterrows()]


cursor.executemany("""
    INSERT INTO ufc_fights (red_fighter, blue_fighter, red_odds, 
    blue_odds, winner, winner_name, finish, finish_details, event_date, location, title_bout, red_wins, red_wins_ko, 
    red_wins_sub, red_wins_dec, red_losses, blue_wins, blue_wins_ko, blue_wins_sub, blue_wins_dec, blue_losses, red_height_cm, blue_height_cm, red_reach_cm, blue_reach_cm, weight_class, 
    red_avg_str, red_avg_td, red_avg_str_pct, red_avg_sub_att, blue_avg_str, blue_avg_td, blue_avg_str_pct, blue_avg_sub_att, red_stance, blue_stance) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, vals)

connection.commit()
connection.close()
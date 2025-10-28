import os

def log(predictions):
    if os.path.exists("logger.txt"):
        os.remove("logger.txt")
    
    with open("logger.txt", "a") as o:
        for team in predictions:
            o.write(team + ",")
        
        o.write("\n")

def getYesterday():
    if not os.path.exists("logger.txt"):
        return []

    with open("logger.txt", "r") as i:
        predictions = i.readline()
        predictions = predictions.strip().split(",")
    
    predictions.pop()

    return predictions

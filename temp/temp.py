sql_text = ["CREAT", "SELECT", "INSERT INTO", "UPDATE"]
sql_0 = "CREAT"
sql_1 = "SELECT"
sql_2 = "INSERT INTO"
sql_3 = "UPDATE"


def SqlCheck(sql_text):
    for val in sql_text:
        if val.startswith("CREAT"):
            print("CREAT TUT")
    # return val.startswith()


SqlCheck(sql_text)

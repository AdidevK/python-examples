import pandas as pd

# person = {
#     "first": "Adidev",
#     "last" : "kundurthi",
#     "email": "adi2dev@gmail.com"
# }
#
# people = {
#     "first": ["Aadya", "Adidev"],
#     "last" : ["kartika", "Kundurthi"],
#     "email": ["cutieaadya@gmail.com", "adi2dev@gmail.com"]
# }
#
# df = pd.DataFrame(people)
# print(df.iloc[0])
# print(type(df.iloc[0]))
#
# print(df.loc[0])
# print(type(df.loc[0]))
input_file = "/Users/adidevkundurthi/pythonProject/firtSpark/data/bookings.csv"
df = pd.read_csv(input_file, nrows=10000)
# print(df.loc[[0,1,2],['dep_port','arr_port']])
# print(type(df.loc[[0,1,2],['dep_port','arr_port']]))
# print(df["dep_port"].value_counts())
print(df.loc[0:2,"arr_port"])
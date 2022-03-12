import pandas as pd

#
# column=["chinuu", "siv", "sivnandana"]
# a=pd.DataFrame(column)
# style={"names":column,
#        "agents":['reyna','phoenix','sage'],
#        "age":[17,18,19]
#        }
# updated_data=pd.DataFrame(style)
# print(updated_data)
# select_row=updated_data.iloc[0]["agents"]
# print(select_row)
data_crush = {"names": ["siv", "sivnandana", "chinnuuu"],
              "height": [1.25, 1.55, 1.69],
              "weight": [56, 55, 60]

              }
a = pd.DataFrame(data_crush)
# bmi=weight/height**2
BMI = []  # empty
for i in range(len(data_crush)):
    new = (data_crush["weight"][i]) / (data_crush["height"][i] ** 2)
    BMI.append(format(new,".2f"))


a["bmi"]=BMI
print(a)
a.to_csv("bmi.txt",sep="\t")

# BMI=pd.DataFrame(data_crush)
# print(BMI)
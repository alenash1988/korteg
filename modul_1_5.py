immutable_var = 3, 4, "milk", True
print(immutable_var)
#immutable_var[0] = 5 (потому что кортеж это не изменняемый обьект, если мы нажмем Run, программа даст ошибку)
mutable_list = ["agg", "milk", "bred"]
mutable_list[0] = "meat"
print(mutable_list)
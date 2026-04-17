# class Kitob:
#     def __init__(self, name, author, price, nashriyot):
#         self.name = name
#         self.author = author
#         self.price = price
#         self.nashriyot = nashriyot
#     def info(self):
#         return self.name, self.author, self.price, self.nashriyot
    
# lst = [Kitob(input("kitob nomi: "), (input("kitob muallifi: ")), int(input("kitob narxi: ")), input("kitob nashriyoti: ")) for i in range(5)]

# for i in lst:
#     if 'A' <= i.nashriyot[0].upper() <= 'H':
#         print(i.info())

# --------------------------------

# class Kompyuter:
#     def __init__(self, name, rami, narxi, protsessori):
#         self.name = name
#         self.rami = rami
#         self.narxi = narxi
#         self.protsessori = protsessori
#     def info(self):
#         return self.name, self.rami, self.narxi, self.protsessori
    
# lst = [Kompyuter(input("kompyuter nomi: "), int((input("kompyuter rami: "))), int(input("kompyuter narxi: ")), input("kompyuter protsessori: ")) for i in range(4)]

# for i in lst:
#     if 4 < i.rami < 16:
#         print(i.info())

# -----------------------------------

# class user:
#     def __init__(self, u_name, name, email):
#         self.name = name
#         self.u_name = u_name
#         self.email = email
#     def info(self):
#         return f"Foydalanuvchi: {self.u_name}, ismi: {self.name}, email: {self.email}"

# u1 = user("ali1994", "Ali Valiyev", "ali1994@gmail.com")
# u2 = user("vali144", "jilm Doe", "doe22@gmail.com")

# print(u1.info())
# print(u2.info())
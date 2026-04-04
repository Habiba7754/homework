data = {
  "center": "IT Academy",
  "branches": [
    {
      "name": "Chilonzor",
      "teachers": 
      [
        { "id": 1, "name": "Ali", "subject": "Python", "experience": 5 },
        { "id": 2, "name": "Vali", "subject": "JavaScript", "experience": 3 }
      ],
      "students": 
      [
        { "id": 101, "name": "Hasan", "course": "Python", "payment": 600000 },
        { "id": 102, "name": "Husan", "course": "JavaScript", "payment": 500000 }
      ]
    },
    {
      "name": "Yunusobod",
      "teachers": 
      [
        { "id": 3, "name": "Aziza", "subject": "Python", "experience": 6 }
      ],
      "students": 
      [
        { "id": 103, "name": "Malika", "course": "Python", "payment": 650000 }
      ]
    }
  ]
}

# --------------------------------------------------------
# 1

# for i in data['branches']:
#     print(i['name'])

# ---------------------------------------------------------
# 2

# for i in data["branches"]:
#     for x in i['teachers']:
#         if x['subject'] == "Python":
#             print(f"{x['id']} {x['name']} {x['subject']} {x['experience']}\n")

# ---------------------------------------------------------
# 3

# for i in data['branches']:
#     p_count= 0
#     j_count = 0
#     for x in i['students']:
#         if x['course'] == "Python":
#             p_count += 1
#         elif x['course'] == "JavaScript":
#             j_count += 1
#     print(f"Python : {p_count} \n JavaScript : {j_count}")

# ----------------------------------------------------------
# 4

# m_p = 0
# m_n = ""
# for i in data["branches"]:
#     for x in i['students']:
#         if x['payment'] > m_p:
#             m_p = x['payment']
#             m_n = x['name']
# print(m_n, m_p)

# ----------------------------------------------------------
# 5

# for i in data["branches"]:
#     natija = sum(x['payment'] for x in i['students'])
#     print(i["name"], natija)

# -----------------------------------------------------------
# 6

# for i in data["branches"]:
#     for x in i['teachers']:
#         if x['experience'] > 5:
#             print(x["name"])

# ------------------------------------------------------------
# 7

# for i in data["branches"]:
#     for x in i["students"]:
#         if x["course"] == "Python":
#             print(i["name"])
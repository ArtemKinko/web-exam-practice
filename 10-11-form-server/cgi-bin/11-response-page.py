#!C:\Users\Nika_Lis\AppData\Local\Programs\Python\Python37\python.exe
# 11. Написать серверный сценарий, который принимает одно значение, введеное пользователем в форму,
# и создает страницу, содержащую фразу: "было введено ..." (вставить введенное значение)
import cgi
print("Content-Type: text/html")

form = cgi.FieldStorage()

# header
html_header = """
<head>
    <meta charset="UTF-8">
    <title>Server response</title>
</head>
<body>
    <p>User input: <b>
"""
print(html_header)

# body
bodystr = str(form["user-input"].value) + "</b><p></body>"
print(bodystr)

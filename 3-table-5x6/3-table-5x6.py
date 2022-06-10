#!C:\Users\Nika_Lis\AppData\Local\Programs\Python\Python37\python.exe

print("Content-Type: text/html")

# header
html_header = """
<head>
    <meta charset="UTF-8">
    <title>Formed table 5x6</title>
    <style>
        table, tr, th {border: black solid 2px}
    </style>
</head>
<body>
    <table>
"""
print(html_header)

# body
bodystr = ""
# цикл по строкам
for _ in range(5):
    bodystr += "<tr>"
    # цикл по столбцам
    for _ in range(6):
        bodystr += "<th>Sample Text</th>"
    bodystr += "</tr>"
bodystr += "</table>" \
           "</body>"

print(bodystr)

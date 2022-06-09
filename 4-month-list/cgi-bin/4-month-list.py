#!C:\Users\Nika_Lis\AppData\Local\Programs\Python\Python37\python.exe

print("Content-Type: text/html")

# header
html_header = """
<head>
    <meta charset="UTF-8">
    <title>Formed list of months</title>
</head>
<body>
    <ol>
"""
print(html_header)

seasons = ["Winter", "Spring", "Summer", "Autumn"]
months = ["Dec", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov"]

bodystr = ""
# цикл по сезонам
for i in range(4):
    bodystr += "<li>" + seasons[i] + "</li>" + "<ul>"
    # цикл по трем месяцам
    for j in range(3):
        bodystr += "<li>" + months[i * 3 + j] + "</li>"
    bodystr += "</ul>"
bodystr += "</ol>" \
           "</body>"

print(bodystr)

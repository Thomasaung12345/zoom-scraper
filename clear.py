with open("ids.html", 'w') as f:
    f.truncate(0)
    f.write('''<title>Saved Zoom Links</title>
    <meta http-equiv="refresh" content="5">
    <link href="style.css" rel="stylesheet">
    <body style="background-color:black;">
    <h2> Zoom Links!</h2>''')

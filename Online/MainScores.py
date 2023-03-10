from flask import Flask
from Utils import Utils

app = Flask(__name__)
@app.route("/")
def score_server():
    try:
        score = open("Scores/Scores.txt", mode='r')
        score = score.read()
        print(score)
        return_html = f'''<html>
	<head>
		<title>Scores Game</title>
	</head>
	<body>
		<h1>The score is <div id="score">{score}</div></h1>
	</body>
</html>'''
    except:
        return_html = f'''<html>
	<head>
		<title>Scores Game</title>
	</head>
	<body>
		<h1><div id="score" style="color:red">{Utils.BAD_RETURN_CODE}</div></h1>
	</body>
</html>'''
    return return_html

app.run(debug=True, host="0.0.0.0", port=4000)

# -*- utf-8 -*-

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
        return render_template('index.html')

if __name__ == "__main__": #Mais si le script est le script principal, alors __name__ ne contient pas le nom du script, il contient la chaine __main__ (oui, cest bizarre avec deux underscores, mais cest une chaine normale).
	print(__name__)
	app.run()



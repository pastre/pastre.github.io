from flask import Flask, request


app = Flask(__name__)

@app.route('/vem')
def vem():
	data = request.form
	print("Recebi", data)

	return str(data)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
    
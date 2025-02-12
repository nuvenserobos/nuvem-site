from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/enviar', methods=['POST'])
def enviar_contato():
    nome = request.form['nome']
    email = request.form['email']
    mensagem = request.form['mensagem']
    
    print(f"📩 Mensagem recebida de {nome} ({email}): {mensagem}")

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

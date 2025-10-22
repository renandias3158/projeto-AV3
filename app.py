from flask import Flask, render_template, request, jsonify, url_for
from modelo import prever

app = Flask(__name__)


@app.route('/')
def menu():
    return render_template('front/fungos.html')

@app.route('/form')
def form():
    return render_template('front/formulario.html')

@app.route('/processar', methods = ['POST'])
def processar():
    try:
        valores = [
            request.form.get('pergunta1'),
            request.form.get('pergunta2'),
            request.form.get('pergunta3'),
            request.form.get('pergunta4'),
            request.form.get('pergunta5'),
            request.form.get('pergunta6'),
            request.form.get('pergunta7'),
            request.form.get('pergunta8'),
            request.form.get('pergunta9'),
            request.form.get('pergunta10'),
        ]
        resultado = prever(valores)
        mensagem = 'Esse cogumelo é venenoso(P)' if resultado == 'p' else 'Esse cogumelo é comestivel (E)'
        return jsonify({'mensagem': mensagem})


    except Exception as e:
        return jsonify({'mensagem': f"erro: {str(e)}"})

if __name__ == '__main__':
    app.run(debug= True)
# Trabalho UniSENAI
# Disciplina de Algoritmos e Programação de Computadores
# Alunos: Darlan Rodrigues Schmeller, Danilo Domingues


# main.py (main file)
from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)

app.secret_key = 'your_unique_secret_key'

quiz_data = [
    [
        {
            "question": "1. Qual dos seguintes componentes é considerado hardware?",
            "options": ["Teclado (✔️)", "Photoshop", "Google Chrome", "Linux"],
            "answer": "Teclado (✔️)"
        },
        {
            "question": "2. O que é um sistema operacional?",
            "options": ["Um software que gerencia o hardware do computador (✔️)", 
                        "Um dispositivo físico para armazenar dados",
                        "Uma ferramenta para editar imagens",
                        "Um tipo de cabo de rede"],
            "answer": "Um software que gerencia o hardware do computador (✔️)"
        },
        {
            "question": "3. Qual dos seguintes é um exemplo de software de sistema?",
            "options": ["Microsoft Word", "Linux (✔️)", "Adobe Photoshop", "Google Drive"],
            "answer": "Linux (✔️)"
        },
        {
            "question": "4. Qual é a função principal da memória RAM?",
            "options": ["Executar instruções de CPU temporariamente (✔️)", 
                        "Armazenar dados permanentemente",
                        "Proteger o sistema contra vírus",
                        "Controlar a velocidade do processador"],
            "answer": "Executar instruções de CPU temporariamente (✔️)"
        },
        {
            "question": "5. O que é um disco rígido (HDD)?",
            "options": ["Um tipo de memória volátil", 
                        "Um dispositivo de armazenamento permanente (✔️)", 
                        "Um componente da CPU", 
                        "Um software de segurança"],
            "answer": "Um dispositivo de armazenamento permanente (✔️)"
        },
        {
            "question": "6. Qual é a principal diferença entre hardware e software?",
            "options": ["Hardware é físico, software é digital (✔️)", 
                        "Hardware é programável, software não é", 
                        "Hardware consome mais energia", 
                        "Não há diferença"],
            "answer": "Hardware é físico, software é digital (✔️)"
        },
        {
            "question": "7. O que é um driver de dispositivo?",
            "options": ["Um tipo de software que gerencia hardware (✔️)", 
                        "Um protocolo de rede", 
                        "Um componente da CPU", 
                        "Um tipo de arquivo"],
            "answer": "Um tipo de software que gerencia hardware (✔️)"
        },
        {
            "question": "8. Qual das opções a seguir é um sistema operacional de código aberto?",
            "options": ["Windows", "macOS", "Ubuntu (✔️)", "iOS"],
            "answer": "Ubuntu (✔️)"
        },
        {
            "question": "9. O que é firmware?",
            "options": ["Um software de aplicativo", 
                        "Um software que controla hardware específico (✔️)", 
                        "Um sistema operacional completo", 
                        "Um tipo de memória RAM"],
            "answer": "Um software que controla hardware específico (✔️)"
        },
        {
            "question": "10. Qual é a função de um aplicativo?",
            "options": ["Gerenciar hardware", 
                        "Executar tarefas específicas para o usuário (✔️)", 
                        "Armazenar dados", 
                        "Proteger o sistema contra malware"],
            "answer": "Executar tarefas específicas para o usuário (✔️)"
        }
    ],
    [
        {
            "question": "1. O que é um protocolo de rede?",
            "options": ["Um tipo de software", 
                        "Um conjunto de regras para comunicação entre dispositivos (✔️)", 
                        "Um tipo de hardware", 
                        "Um formato de arquivo"],
            "answer": "Um conjunto de regras para comunicação entre dispositivos (✔️)"
        },
        {
            "question": "2. Qual dos seguintes é um exemplo de protocolo da camada de transporte?",
            "options": ["HTTP", "IP", "TCP (✔️)", "DNS"],
            "answer": "TCP (✔️)"
        },
        {
            "question": "3. O que é um endereço IP?",
            "options": ["Um tipo de software", 
                        "Uma forma de criptografia", 
                        "Um identificador único para um dispositivo em uma rede (✔️)", 
                        "Um protocolo de segurança"],
            "answer": "Um identificador único para um dispositivo em uma rede (✔️)"
        },
        {
            "question": "4. Qual é a função do roteador em uma rede?",
            "options": ["Armazenar dados", 
                        "Encaminhar pacotes entre redes (✔️)", 
                        "Proteger contra vírus", 
                        "Executar aplicativos"],
            "answer": "Encaminhar pacotes entre redes (✔️)"
        },
        {
            "question": "5. O que significa a sigla DNS?",
            "options": ["Domain Name System (✔️)", 
                        "Digital Network Service", 
                        "Data Network System", 
                        "Domain Name Security"],
            "answer": "Domain Name System (✔️)"
        },
        {
            "question": "6. O que é uma VPN?",
            "options": ["Um tipo de protocolo de rede", 
                        "Uma rede privada virtual que garante segurança na comunicação (✔️)", 
                        "Um software de edição de vídeos", 
                        "Um tipo de firewall"],
            "answer": "Uma rede privada virtual que garante segurança na comunicação (✔️)"
        },
        {
            "question": "7. O que é um switch em redes de computadores?",
            "options": ["Um dispositivo que conecta redes diferentes", 
                        "Um dispositivo que conecta dispositivos dentro da mesma rede (✔️)", 
                        "Um tipo de malware", 
                        "Um software de proteção"],
            "answer": "Um dispositivo que conecta dispositivos dentro da mesma rede (✔️)"
        },
        {
            "question": "8. O que caracteriza uma rede LAN?",
            "options": ["Conexão de longa distância", 
                        "Conexão de dispositivos em uma área geográfica limitada (✔️)", 
                        "Conexão global", 
                        "Conexão sem fio apenas"],
            "answer": "Conexão de dispositivos em uma área geográfica limitada (✔️)"
        },
        {
            "question": "9. Qual das seguintes opções é um serviço da camada de aplicação?",
            "options": ["IP", "TCP", "FTP (✔️)", "Ethernet"],
            "answer": "FTP (✔️)"
        },
        {
            "question": "10. O que é o modelo OSI?",
            "options": ["Um tipo de software", 
                        "Um modelo de arquitetura de rede com 7 camadas (✔️)", 
                        "Um protocolo de segurança", 
                        "Um sistema de arquivos"],
            "answer": "Um modelo de arquitetura de rede com 7 camadas (✔️)"
        }
    ],
    [
        {
            "question": "1. O que é criptografia?",
            "options": ["O processo de tornar dados ilegíveis para proteger a informação (✔️)", 
                        "O ato de enviar dados pela internet", 
                        "Um tipo de software de segurança", 
                        "Uma técnica de backup"],
            "answer": "O processo de tornar dados ilegíveis para proteger a informação (✔️)"
        },
        {
            "question": "2. Qual é o propósito de um firewall?",
            "options": ["Monitorar o desempenho do computador", 
                        "Proteger a rede contra acessos não autorizados (✔️)", 
                        "Aumentar a velocidade da internet", 
                        "Armazenar dados de forma segura"],
            "answer": "Proteger a rede contra acessos não autorizados (✔️)"
        },
        {
            "question": "3. O que é autenticação multifator?",
            "options": ["Um método de backup de dados", 
                        "Um processo de verificação que utiliza mais de um método de autenticação (✔️)", 
                        "Um tipo de criptografia", 
                        "Um sistema de arquivos"],
            "answer": "Um processo de verificação que utiliza mais de um método de autenticação (✔️)"
        },
        {
            "question": "4. O que caracteriza um ataque de phishing?",
            "options": ["Acesso físico não autorizado", 
                        "Envio de e-mails fraudulentos para roubar informações pessoais (✔️)", 
                        "Invasão de redes por meio de malware", 
                        "Uso de força bruta para adivinhar senhas"],
            "answer": "Envio de e-mails fraudulentos para roubar informações pessoais (✔️)"
        },
        {
            "question": "5. O que é um malware?",
            "options": ["Um software projetado para proteger o sistema", 
                        "Um software malicioso que causa danos ou rouba informações (✔️)", 
                        "Um tipo de firewall", 
                        "Um protocolo de rede"],
            "answer": "Um software malicioso que causa danos ou rouba informações (✔️)"
        },
        {
            "question": "6. O que é um certificado digital?",
            "options": ["Um tipo de hardware de segurança", 
                        "Uma forma de autenticação que verifica a identidade de um usuário (✔️)", 
                        "Um software de edição de textos", 
                        "Um protocolo de rede"],
            "answer": "Uma forma de autenticação que verifica a identidade de um usuário (✔️)"
        },
        {
            "question": "7. O que significa 'backups regulares'?",
            "options": ["Armazenar dados para recuperação futura (✔️)", 
                        "Excluir dados antigos", 
                        "Criar um novo tipo de criptografia", 
                        "Segurança de rede"],
            "answer": "Armazenar dados para recuperação futura (✔️)"
        },
        {
            "question": "8. O que é um ataque de DDoS?",
            "options": ["Roubo de informações confidenciais", 
                        "Ataque a um site ou rede com tráfego excessivo para derrubá-lo (✔️)", 
                        "Invasão de dispositivos móveis", 
                        "Interceptação de senhas"],
            "answer": "Ataque a um site ou rede com tráfego excessivo para derrubá-lo (✔️)"
        },
        {
            "question": "9. O que é a 'segurança em profundidade'?",
            "options": ["Um único sistema de proteção", 
                        "Várias camadas de proteção para garantir a segurança (✔️)", 
                        "Proteção contra vírus", 
                        "Métodos para otimizar o desempenho do sistema"],
            "answer": "Várias camadas de proteção para garantir a segurança (✔️)"
        },
        {
            "question": "10. O que é 'criptografia de ponta a ponta'?",
            "options": ["Criptografia de dados durante o envio e recebimento (✔️)", 
                        "Criptografia de dados enquanto estão armazenados", 
                        "Desenvolvimento de novos protocolos de segurança", 
                        "Método de backup de dados"],
            "answer": "Criptografia de dados durante o envio e recebimento (✔️)"
        }
    ]

]



@app.route('/')
def index():
    session['score'] = 0
    session['level'] = 0
    return redirect(url_for('quiz'))


@app.route('/quiz')
def quiz():
    level = session.get('level', 0)
    if level < len(quiz_data):
        return render_template('quiz.html', quiz_data=quiz_data[level], level=level, enumerate=enumerate)
    else:
        return redirect(url_for('result'))


@app.route('/submit', methods=['POST'])
def submit():
    level = session.get('level', 0)
    score = session.get('score', 0)

    for i, question in enumerate(quiz_data[level]):
        user_answer = request.form.get(f'question-{i}')
        if user_answer == question['answer']:
            score += 1

    session['score'] = score
    session['level'] = level + 1  # Avança para o próximo nível
    return redirect(url_for('quiz'))


@app.route('/result')
def result():
    score = session.get('score', 0)
    total = sum(len(level) for level in quiz_data)  # Total de perguntas
    return render_template('result.html', score=score, total=total)


if __name__ == '__main__':
    app.run(debug=True)

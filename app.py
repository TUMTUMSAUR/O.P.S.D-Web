from flask import Flask
from threading import Thread

app = Flask('')

html_code = """
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>O.P.S.D - Proteggi il tuo Server Discord</title>
    <link rel="icon" href="logo.jpg" type="image/jpg">
    <style>
        body {
            margin: 0;
            font-family: 'Arial', sans-serif;
            background-color: #1e1e2f;
            color: #ffffff;
            line-height: 1.6;
        }
        
        header {
            background-color: #2c2c3e;
            padding: 1rem 0;
            position: sticky;
            top: 0;
            z-index: 1000;
        }
        
        header .container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 1rem;
        }
        
        header h1 {
            font-size: 1.8rem;
            color: #ffffff;
        }
        
        header nav ul {
            list-style: none;
            display: flex;
            gap: 1.5rem;
            margin: 0;
            padding: 0;
        }
        
        header nav ul li a {
            text-decoration: none;
            color: #ffffff;
            font-weight: bold;
            transition: color 0.3s ease;
        }
        
        header nav ul li a:hover {
            color: #7f5af0;
        }
        
        .hero {
            text-align: center;
            padding: 3rem 1rem;
            background: linear-gradient(135deg, #2c2c3e, #1e1e2f);
        }
        
        .hero h2 {
            font-size: 2.4rem;
            color: #d4b5ff;
        }
        
        .hero p {
            font-size: 1rem;
            margin: 0.8rem 0;
        }
        
        .buttons {
            margin-top: 2rem;
        }
        
        .buttons .btn {
            text-decoration: none;
            padding: 0.6rem 1.2rem;
            border-radius: 5px;
            font-weight: bold;
            font-size: 0.9rem;
            transition: background-color 0.3s ease, color 0.3s ease;
        }
        
        .buttons .btn.primary {
            background-color: #7f5af0;
            color: #ffffff;
        }
        
        .buttons .btn.primary:hover {
            background-color: #6842c2;
        }
        
        .buttons .btn.secondary {
            background-color: #2c2c3e;
            color: #7f5af0;
            border: 2px solid #7f5af0;
        }
        
        .buttons .btn.secondary:hover {
            background-color: #3a3a4e;
        }
        
        .features {
            padding: 4rem 1rem;
            background-color: #2c2c3e;
            text-align: center;
        }
        
        .features h2 {
            font-size: 2rem;
            margin-bottom: 1.5rem;
            color: #d4b5ff;
        }
        
        .feature-list {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 2rem;
        }
        
        .feature-item {
            background-color: #1e1e2f;
            padding: 1rem;
            border-radius: 8px;
            max-width: 280px;
            text-align: left;
        }
        
        .feature-item h3 {
            color: #7f5af0;
            margin-bottom: 1rem;
        }
        
        .bot-info,
        .server-info {
            padding: 4rem 1rem;
            text-align: center;
        }
        
        .bot-logo {
            display: block;
            max-width: 100px;
            height: auto;
            margin: 1.5rem auto 0 auto;
            border-radius: 50%;
            box-shadow: 0 3px 6px rgba(0, 0, 0, 0.15);
        }
        
        footer {
            background-color: #2c2c3e;
            text-align: center;
            padding: 0.8rem 0;
            margin-top: 2rem;
        }
        
        footer p {
            margin: 0;
            color: #7f5af0;
            font-size: 0.9rem;
        }
        
        .coming-soon {
            font-size: 1.2rem;
            color: #ffcc00;
            font-weight: bold;
            margin-top: 1rem;
            animation: pulse 1.5s infinite;
        }
        
        @keyframes pulse {
            0%,
            100% {
                opacity: 1;
            }
            50% {
                opacity: 0.5;
            }
        }
    </style>
</head>

<body>
    <header>
        <div class="container">
            <h1>O.P.S.D</h1>
            <nav>
                <ul>
                    <li><a href="#home">Home</a></li>
                    <li><a href="#features">Caratteristiche</a></li>
                    <li><a href="#bot">Il Nostro Bot</a></li>
                    <li><a href="#server">Server</a></li>
                </ul>
            </nav>
        </div>
    </header>
    <main>
        <section id="home" class="hero">
            <div class="container">
                <h2>Proteggi il Tuo Server Discord</h2>
                <p>Con O.P.S.D, la sicurezza della tua community è la nostra priorità.</p>
                <div class="buttons">
                    <a href="#features" class="btn primary">Scopri di Più</a>
                    <a href="#bot" class="btn secondary">Il Nostro Bot</a>
                </div>
            </div>
        </section>
        <section id="features" class="features">
            <div class="container">
                <h2>Caratteristiche Principali</h2>
                <div class="feature-list">
                    <div class="feature-item">
                        <h3>Protezione Avanzata</h3>
                        <p>Blocca spam, raid e comportamenti tossici con il nostro sistema di moderazione automatica.</p>
                    </div>
                    <div class="feature-item">
                        <h3>Comandi Personalizzati</h3>
                        <p>Crea comandi personalizzati per adattare il bot alle esigenze del tuo server.</p>
                    </div>
                    <div class="feature-item">
                        <h3>Supporto 24/7</h3>
                        <p>Il nostro team è sempre disponibile per aiutarti con qualsiasi problema.</p>
                    </div>
                </div>
            </div>
        </section>
        <section id="bot" class="bot-info">
            <div class="container">
                <h2>Il Nostro Bot</h2>
                <p>O.P.S.D è progettato per garantire la massima sicurezza e personalizzazione per il tuo server Discord.</p>
                <p class="coming-soon">🚀 Il bot non è ancora disponibile. Resta sintonizzato per il lancio ufficiale!</p>
                <img src="logo.jpg" alt="Logo O.P.S.D" class="bot-logo">
            </div>
        </section>
        <section id="server" class="server-info">
            <div class="container">
                <h2>Unisciti al Nostro Server</h2>
                <p>Entra nella nostra community per ricevere supporto, aggiornamenti e suggerimenti.</p>
                <a href="https://discord.gg/yJryuZNT" class="btn primary">Unisciti Ora</a>
            </div>
        </section>
    </main>
    <footer>
        <div class="container">
            <p>&copy; 2025 O.P.S.D. Tutti i diritti riservati.</p>
        </div>
    </footer>
</body>

</html>
"""

@app.route('/')
def home():
    return html_code

@app.route('/status')
def status():
    return "Il bot è attivo!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

keep_alive()
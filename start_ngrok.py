from pyngrok import ngrok

# Указываем порт, на котором работает сервер Django
public_url = ngrok.connect(8000)

print(f"Ваш публичный URL: {public_url}")

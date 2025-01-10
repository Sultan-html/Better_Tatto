from pyngrok import ngrok

ngrok.set_auth_token("2rRlFAfAGBMpwtj4vWJRztpA5S0_2uXThQn3fGX9jtjHdVjKC")
public_url = ngrok.connect(8000)
print("Ngrok URL:", public_url)

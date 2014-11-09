from flask import request, current_app
import hashlib, hmac
    
def genSecrets():
    access_token = request.args.get('access_token')
    app_secret = current_app.config['FB_APP_SECRET']
    appsecret_proof = hmac.new(app_secret, access_token, hashlib.sha256).hexdigest()
    return access_token, appsecret_proof
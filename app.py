# -*- coding: utf-8 -*-
"""
Created on Fri May 23 20:09:14 2025

@author: PDFIGUEROA
"""

from flask import Flask, request

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Webhook recibido:", data)
    return "OK", 200

@app.route("/")
def home():
    return "¡Webhook activo!"

if __name__ == "__main__":
    app.run()

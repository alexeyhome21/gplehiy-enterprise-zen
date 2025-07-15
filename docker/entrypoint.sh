#!/bin/sh
echo "GpLehiy готов! Панель на http://$HOSTNAME:8080"
echo "Логин: admin | Пароль: admin"
echo "Подкинули кожаного — добро пожаловать 🧘"
set -e
python /app/generate_config.py

if [ ! -f /usr/local/bin/xray ]; then
    echo "Downloading Xray core..."
    curl -L -o /usr/local/bin/xray https://github.com/XTLS/Xray-core/releases/latest/download/Xray-linux-64.zip || true
    chmod +x /usr/local/bin/xray || true
fi


# start xray in background if exists
if [ -f /usr/local/bin/xray ]; then
    /usr/local/bin/xray -config /app/config.json &
fi

uvicorn main:app --host 0.0.0.0 --port 8080 --reload

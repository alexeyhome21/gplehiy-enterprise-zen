# GpLehiy Enterprise Zen Edition™

Веб-панель для управления Xray-core. Запускается одной командой через Docker.

## Установка

```bash
sudo apt install -y docker.io docker-compose
git clone https://github.com/alexeyhome21/gplehiy-enterprise-zen.git
cd gplehiy-enterprise-zen
docker-compose up -d
```

После запуска появится сообщение:

```
GpLehiy готов! Панель на http://<ip>:8080
Логин: admin | Пароль: admin
Подкинули кожаного — добро пожаловать 🧘
```

Панель доступна по адресу `http://<ip>:8080`.

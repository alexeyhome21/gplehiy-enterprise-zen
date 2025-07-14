import json

with open("users.json") as f:
    users = json.load(f)

with open("config_template.json") as f:
    template = json.load(f)

# логика вставки пользователей в шаблон
# сохраняем как config.json
with open("/etc/xray/config.json", "w") as f:
    json.dump(template, f)
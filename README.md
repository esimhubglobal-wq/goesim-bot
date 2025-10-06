# Go_ESIM Hunter Bot

Telegram bot that watches group chats for travelers asking about **SIM/eSIM/internet**,
then sends a helpful reply + your affiliate link. Also works in DMs as a quick helper.

## Render deploy (Background Worker)

1. Create a new repository on GitHub (e.g. `goesim-bot`).
2. Upload the files from this archive to that repo.
3. On https://render.com → New → **Background Worker** → connect the repo.
4. Build Command: `pip install -r requirements.txt`
5. Start Command: `python bot.py`
6. Environment Variables:
   - `TG_TOKEN` – your BotFather token
   - `ADMIN_ID` – your Telegram numeric ID (owner)
   - `SIMO_URL` – your affiliate URL
   - `CHANNEL_URL` – `https://t.me/Go_ESIM`
   - `AUTO_REPLY` – `true` / `false`
   - `COOLDOWN_CHAT` – seconds per chat
   - `COOLDOWN_USER` – seconds per user
7. In @BotFather: **Group Privacy → Turn OFF (Disable)**.
8. Add the bot to groups.

Local run:
```
pip install -r requirements.txt
cp .env.example .env
# edit .env with your values
python bot.py
```

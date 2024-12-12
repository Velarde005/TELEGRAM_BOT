from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import BOT_TOKEN  # Importa el token desde config.py

# Comando /start
async def start(update: Update, context):
    await update.message.reply_text('¡Hola! Soy un bot de echo. Envíame cualquier mensaje y lo repetiré.')

# Función que maneja mensajes de texto
async def echo(update: Update, context):
    text_received = update.message.text
    await update.message.reply_text(text_received)

# Función principal que inicializa el bot
def main():
    # Crea la aplicación de Telegram
    application = Application.builder().token(BOT_TOKEN).build()

    # Agregar handlers para comandos y mensajes
    application.add_handler(CommandHandler("start", start))  # Handler para /start
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))  # Echo handler

    # Inicia el bot
    application.run_polling()

# Punto de entrada
if __name__ == '__main__':
    main()

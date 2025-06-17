import os
from dotenv import load_dotenv
import chainlit as cl
from openai import OpenAI

# Load environment variables
load_dotenv()

# Configure OpenAI via OpenRouter
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url=os.getenv("BASE_URL")
)

model_name = os.getenv("MODEL", "gpt-4o")

# Study tip function
def get_tip():
    return "🎓 Study Smart Tip:\nUse *spaced repetition*! Break your study sessions into small intervals and repeat over time to boost memory retention."

# Summary function
def summarize(text):
    if len(text.strip()) < 30:
        return "⚠️ Please provide a longer paragraph for a useful summary."
    return f"📄 Here's a quick summary:\n{text.strip()[:60]}..."

# Chat start event
@cl.on_chat_start
async def start():
    await cl.Message("👋 Hello! I'm your **Smart Student Assistant**.").send()

# Chat message handler
@cl.on_message
async def handle_message(msg: cl.Message):
    user_input = msg.content.lower()

    try:
        # First-time interaction or confused input
        if user_input in ["hi", "hello", "hey"]:
            await cl.Message(
                "I'm here to support your learning journey! 🚀\n"
                "✨ Type `tip` for a quick study hack.\n"
                "✍️ Need a summary? Use `summarize: your paragraph...`\n"
                "🔍 Got a question? Ask me anything academic. I'll do my best to explain!"
            ).send()

        elif "summarize:" in user_input:
            passage = user_input.split("summarize:")[1].strip()
            await cl.Message(summarize(passage)).send()

        elif "tip" in user_input:
            await cl.Message(get_tip()).send()

        else:
            completion = client.chat.completions.create(
                model=model_name,
                messages=[
                    {"role": "system", "content": "You are a supportive and knowledgeable Smart Student Assistant helping students learn, summarize, and stay motivated."},
                    {"role": "user", "content": user_input}
                ],
                max_tokens=1024
            )
            await cl.Message(completion.choices[0].message.content).send()

    except Exception as e:
        await cl.Message(f"❌ Error:\n{str(e)}").send()

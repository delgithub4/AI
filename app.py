from chatbot import AIChatbot

bot = AIChatbot()

print("=" * 40)
print("      AI PERSONAL ASSISTANT")
print("=" * 40)

while True:
    question = input("\nYou: ")

    if question.lower() in ["exit", "quit", "bye"]:
        print("AI: Goodbye!")
        break

    answer = bot.respond(question)
    print("AI:", answer)

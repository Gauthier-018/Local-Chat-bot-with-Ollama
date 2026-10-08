from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question based on the context below.

Here is the conversation history: {context}

Question: {question}

Answer:

"""

model = OllamaLLM(model="qwen2.5:1.5b")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context = ""
    print("Welcome to the LUNATIC BOT! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        context += f"You: {user_input}\n"
        result = chain.invoke({"context": context, "question": user_input})
        print(f"LunaticBot: {result}")
        context += f"\nUser: {user_input}\nLunaticBot: {result}\n"
if __name__ == "__main__":
    handle_conversation()

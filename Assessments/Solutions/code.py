# import ollama library for LLM integration
import ollama

# empty variable for init
LLMmodel = 'None'

# choosing between LLM models
choice = input("What LLM Model do you want to use?\n\nChoices:\n1. Qwen [Q] - 500M parameters\n2. Dolphin-Phi [D] - 3B parameters\n3. TERMINAL [T] - 3B parameters\n\nNOTE: The more parameters, the slower the generation\n\n> ")
if choice == 'Q':
    LLMmodel = "qwen:0.5b"
elif choice == 'D':
    LLMmodel = "dolphin-phi:latest"
elif choice == 'T':
    LLMmodel = "terminal:latest"

while True:

    s = input("\n> ")

    # implement streaming to increase speed on this low-spec device
    stream = ollama.chat(
        model=LLMmodel, # a very lightweight model
        messages=[{'role': 'user', 'content': str(s)}], # user says {s}
        stream=True, # streaming for live printing of LLM
    )

    for chunk in stream:
        # print in chunks as they're being generated
        print(chunk['message']['content'], end='', flush=True)
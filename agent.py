print("AI Agent started")

while True:
    user = input("You: ")
    
    if user.lower() == "exit":
        print("Agent stopped")
        break
    
    print("Agent:", user)

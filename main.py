from pyscript import document, display

display("")
# Welcome Message
welcome = document.getElementById("welcome-message")
welcome.innerText = "Welcome to my ICT Quarter 2 Portfolio!"

# Fun Fact Generator

facts = [
    "I enjoy studying Philosophy and Ethics.",
    "My dream careers are Attorney, Priest, and Experimental Physicist.",
    "I enjoy learning about Politics, History, and Science.",
    "My favorite philosopher is Socrates.",
    "I hope to help solve corruption and social issues in the Philippines."
]

current = 0

def next_fact(event):
    global current
    current = (current + 1) % len(facts)
    document.getElementById("fact-box").innerText = facts[current]

button = document.getElementById("fact-btn")

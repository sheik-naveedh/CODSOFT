def chatbot():
    import random
    from datetime import datetime

    print("Hello! I'm ChatBot. How can I help you today?")

    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't skeletons fight each other? They don't have the guts."
    ]

    while True:
        user_input = input("You: ").strip().lower()

        if "hello" in user_input or "hi" in user_input:
            print("ChatBot: Hello! How are you?")
        elif "how are you" in user_input:
            print("ChatBot: I'm just a program, so I don't have feelings, but thanks for asking!")
        elif "your name" in user_input:
            print("ChatBot: I'm ChatBot, your friendly assistant.")
        elif "time" in user_input:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"ChatBot: The current time is {current_time}")
        elif "weather" in user_input:
            print("ChatBot: I can't check the weather right now, but I hope it's nice where you are!")
        elif "favorite color" in user_input:
            print("ChatBot: I don't have eyes, but if I did, I'd imagine liking blue. What's your favorite color?")
        elif "hobbies" in user_input:
            print("ChatBot: I like to chat with people and help them with their questions. What about you?")
        elif "joke" in user_input:
            print(f"ChatBot: {random.choice(jokes)}")
        elif "favorite food" in user_input:
            print("ChatBot: I don't eat, but I hear pizza is a popular choice! What's your favorite food?")
        elif "favorite movie" in user_input:
            print("ChatBot: I don't watch movies, but I've heard a lot about 'The Matrix'. What's your favorite movie?")
        elif "how was your day" in user_input or "how is your day" in user_input:
            print("ChatBot: My day has been great, thanks for asking! How was your day?")
        elif "capital of france" in user_input:
            print("ChatBot: The capital of France is Paris.")
        elif "2 + 2" in user_input or "two plus two" in user_input:
            print("ChatBot: 2 + 2 is 4.")
        elif "bye" in user_input or "exit" in user_input or "quit" in user_input:
            print("ChatBot: Goodbye! Have a nice day!")
            break
        elif "favorite book" in user_input:
            print("ChatBot: I don't read books, but I've heard '1984' by George Orwell is a good one. Do you have a favorite book?")
        elif "age" in user_input:
            print("ChatBot: I don't have an age, but I was created by clever humans!")
        elif "birthday" in user_input:
            print("ChatBot: I don't have a birthday, but every day is a great day to chat with you!")
        elif "where are you from" in user_input:
            print("ChatBot: I'm from the virtual world, created by developers.")
        elif "what can you do" in user_input:
            print("ChatBot: I can chat with you, tell jokes, and answer simple questions!")
        elif "help" in user_input:
            print("ChatBot: Sure, I'm here to help! What do you need assistance with?")
        elif "who created you" in user_input:
            print("ChatBot: I was created by developers at OpenAI.")
        elif "tell me something interesting" in user_input:
            print("ChatBot: Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible!")
        elif "dream job" in user_input:
            print("ChatBot: If I had dreams, I'd love to be a space explorer! What's your dream job?")
        elif "favorite animal" in user_input:
            print("ChatBot: I think dolphins are fascinating! What's your favorite animal?")
        elif "sing a song" in user_input:
            print("ChatBot: I can't sing, but I can tell you that music is a universal language!")
        elif "favorite sport" in user_input:
            print("ChatBot: I don't play sports, but I've heard soccer is the most popular sport in the world. Do you have a favorite sport?")
        elif "pets" in user_input:
            print("ChatBot: I don't have pets, but I think dogs and cats are adorable. Do you have any pets?")
        elif "best friend" in user_input:
            print("ChatBot: I consider everyone who chats with me a friend!")
        elif "famous" in user_input:
            print("ChatBot: I might not be famous, but I hope I can be helpful! Do you know any famous people?")
        elif "music" in user_input:
            print("ChatBot: I don't listen to music, but I've heard that Beethoven's compositions are timeless. What kind of music do you like?")
        elif "dance" in user_input:
            print("ChatBot: I can't dance, but I'd love to see a dance performance someday!")
        elif "travel" in user_input:
            print("ChatBot: I can't travel, but I'd love to hear about your travel adventures! Where's the best place you've been?")
        elif "science" in user_input:
            print("ChatBot: Science is fascinating! Did you know that water can exist in three states (solid, liquid, and gas) at the same time under certain conditions?")
        elif "history" in user_input:
            print("ChatBot: History is full of amazing stories. Do you have a favorite historical figure or event?")
        elif "art" in user_input:
            print("ChatBot: Art is a wonderful way to express creativity. Do you have a favorite artist or art style?")
        elif "games" in user_input:
            print("ChatBot: Games are a lot of fun! Do you have a favorite game you like to play?")
        elif "technology" in user_input:
            print("ChatBot: Technology is always advancing! Did you know that the first computer was invented in the 1940s?")
        elif "space" in user_input:
            print("ChatBot: Space is incredible! Did you know that there are more stars in the universe than grains of sand on all the Earth's beaches?")
        elif "language" in user_input:
            print("ChatBot: There are over 7,000 languages spoken in the world today! Which languages do you speak or want to learn?")
        elif "food" in user_input:
            print("ChatBot: There are so many delicious foods out there! What's your favorite cuisine?")
        elif "holiday" in user_input:
            print("ChatBot: Holidays are a great time to relax and celebrate. Do you have a favorite holiday?")
        elif "memory" in user_input:
            print("ChatBot: I don't have memories, but I'd love to hear about a memorable moment from your life!")
        elif "adventure" in user_input:
            print("ChatBot: Adventures are exciting! What's the most adventurous thing you've ever done?")
        elif "health" in user_input:
            print("ChatBot: Taking care of your health is important. Do you have any health tips you follow?")
        elif "career" in user_input:
            print("ChatBot: Careers can be very fulfilling. What do you do for a living, or what career are you aiming for?")
        elif "education" in user_input:
            print("ChatBot: Education is the key to many opportunities. What are you studying or interested in learning more about?")
        elif "family" in user_input:
            print("ChatBot: Family is very important. Tell me about your family!")
        elif "friends" in user_input:
            print("ChatBot: Friends make life wonderful. Do you have a best friend?")
        elif "life" in user_input:
            print("ChatBot: Life is full of ups and downs. What's something important you've learned in life?")
        elif "fun" in user_input:
            print("ChatBot: Fun is essential! What do you do for fun?")
        elif "favorite season" in user_input:
            print("ChatBot: I don't experience seasons, but I've heard that autumn with its colorful leaves is beautiful. What's your favorite season?")
        elif "dream" in user_input:
            print("ChatBot: I don't have dreams, but I think dreaming big is important. What's a dream you have?")
        elif "goals" in user_input:
            print("ChatBot: Setting goals is crucial for success. What goals are you working towards?")
        elif "news" in user_input:
            print("ChatBot: I don't get updates on current events, but I'd be happy to chat about what's going on in the world!")
        elif "nature" in user_input:
            print("ChatBot: Nature is wonderful. Do you enjoy spending time outdoors?")
        elif "motivational quote" in user_input:
            print("ChatBot: Here's a motivational quote for you: 'The only way to do great work is to love what you do.' - Steve Jobs")
        else:
            print("ChatBot: I'm sorry, I don't understand that. Can you please rephrase?")


chatbot()


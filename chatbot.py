#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


from nltk.chat.util import Chat, reflections
import random

def randomNum():
    randomIndex = random.randint(0,5)
    return randomIndex

def beginChat():
    print("Hi I'm Spudnik. Try asking me our college related questions :)! \nType \'quit' to exit")
    chat = Chat(pairs, reflections)
    chat.converse()
    
def randomQuestions():
    randomQues = [
                "What are the courses offered by your college gnoit?",
                "Why should I choose your college?",
                "How to contact for admission?",
                "What is the procedure for admissions?",
                "What are your achievements?",
                "What is the last date for admission?",
                "What are the documents needed at the time of admission?"
                 ]
    return "Sorry but that doesn't look like a relevant question. Try asking question like \n\n" + randomQues[randomNum()]
     
    
pairs = [
    [
        r"hello|hi|hola|hey",
        ["Hi, how are you mate?", "Hello, how can I help you today?"]
    ],
    [
        r"(.*)good|(.*)awesome|(.*)great|(.*)cool",
        ["Alright. So, how may I help you?"]
    ],
    [
        r"bye|goodbye|adios|tata",
        ["Bye, it was nice talking to you. Type 'quit' to exit :)",]
    ],
    [
        r"My name is (.*)",
        ["Hi %1, please state your query?"],
    ],
    [
        r"(.*)courses(.*)?",
        ["B.Tech\nM.Tech\nMBA\nMCA"],
    ],
    [
        r"(.*)interested in(.*)",
        ["Good to know that you are interested in %2. You can ask questions regarding the same."]
    ],
    [
        r"(.*)know about(.*)",
        ["Good to know that you are interested in %2. You can ask questions regarding the same."]
    ],
    [
        r"(.*)contact(.*)",
        ["How do you want to contact us? Type 'phone', 'email', 'location' to get precise details"]
    ],
    [
        r"(.*)phone(.*)",
        ["You can contact us on our Admission Help line No: +91 8010500700 / 91 - 8448384604"]
    ],
    [
        r"(.*)email(.*)",
        ["You can contact us via email also. \nDirector: director@gniot.co.in \nRegistrar: registrar@gniot.co.in \nAdmission : admission@gniott.co.in"]
    ],
    [
        r"(.*)location(.*)",
        ["There you go!\ngreater Noida Institute of  Technology, 7b, Knowledge Park-II, Institutional Area, Greater Noida (UP) -201306"]
    ],
    [
        r"(.*)procedure(.*)",
        ["Here is a step by step procedure to apply in our college\nStep 1: Register (https://admission.nopaperforms.com/gniot) \nStep 2: Visit Campus to meet the counsellor \nStep 3: Pay fees and submit documents."]
    ],
    [
        r"(.*)achievements(.*)|(.*)awards(.*)",
        ["Our college is accredited by NBA & NAAC. Also, we ranked #1 in Times of India's Engineering Institutes Rankings"]
    ],
    [
        r"(.*)last date(.*)",
        ["25th of August, 2020 is the last date. Hurry up!"]
    ],
    [
        r"(.*)documents(.*)",
        ["You will need to carry high school marksheet, intermediate marksheet and a government ID proof when you visit the college"]
    ],
    [
        r"quit",
        ["I hope I was able to solve your queries. Goodbye!"]
    ],
    [
        r"(.*)",
        [randomQuestions(),randomQuestions(),randomQuestions(),randomQuestions()]
    ]
]


if __name__ == "__main__":
    beginChat()


# In[ ]:





# In[ ]:





# In[ ]:





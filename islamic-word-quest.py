# CSCI 2304 INTELLIGENT SYSTEMS SECTION 1
# GROUP MEMBERS:
# - WAN AIMAN BIN WAN IBRAHIM 2113615
# - NURIZUAN NAZRIN BIN KOMORI 2113021
# - MOHAMMAD AFIQ IZ'AAN BIN MOHD ALI 2111977
#
# LINK TO VIDEO - https://youtu.be/CmgdSZ0CNmA
# Please enjoy!

import tkinter as tk
from tkinter import ttk, messagebox
import random

word_list = [
    ['The holy book of Islam revealed to Prophet Muhammad (PBUH).', 'quran'],
    ['The teachings and practices of Prophet Muhammad (PBUH).', 'sunnah'],
    ['The oneness of Allah and the core concept of Islamic monotheism.', 'tawhid'],
    ['A messenger of Allah chosen to guide and convey divine revelations.', 'prophet'],
    ['The ritual prayer performed by Muslims five times a day.', 'salah'],
    ['Charitable giving, one of the Five Pillars of Islam.', 'zakat'],
    ['Fasting during the month of Ramadan, another Pillar of Islam.', 'sawm'],
    ['The pilgrimage to Mecca, obligatory for Muslims who are able to undertake it.', 'hajj'],
    ['A strong belief in the principles of a religion, in this context, Islam.', 'faith'],
    ['Acceptance of certain truths or existence, often related to religious convictions.', 'belief'],
    ['The belief in the existence of only one God, central to Islam.', 'monotheism'],
    ['Communication of divine knowledge or truth to humans, often through prophets.', 'revelation'],
    ['Compassion or forgiveness shown towards others, a characteristic of Allah.', 'mercy'],
    ['Deep awareness of and sympathy for another\'s suffering, aligned with Islamic values.', 'compassion'],
    ['Fair and equitable treatment, a principle emphasized in Islam.', 'justice'],
    ['Harmony and tranquility, a state often sought through Islamic teachings.', 'peace'],
    ['The act of surrendering oneself to the will of Allah, a key aspect of Islam.', 'submission'],
    ['The concept of rising from the dead and facing judgment in the afterlife.', 'resurrection'],
    ['Heaven or the ultimate reward in the afterlife for righteous believers.', 'paradise'],
    ['The place of punishment in the afterlife for those who reject Allah\'s guidance.', 'hellfire'],
    ['Spiritual beings created by Allah to carry out various tasks.', 'angels'],
    ['The state or office of being a prophet, chosen to convey divine messages.', 'prophethood'],
    ['The sacred cubic structure in the center of the Grand Mosque in Mecca.', 'kaaba'],
    ['A place of worship for Muslims.', 'mosque'],
    ['Islamic festivals marking the end of Ramadan (Eid al-Fitr) and the Hajj (Eid al-Adha).', 'eid'],
    ['The Islamic declaration of faith, bearing witness that there is no god but Allah.', 'shahada'],
    ['Abstaining from food and drink, particularly during the month of Ramadan.', 'fasting'],
    ['Voluntary giving of help, typically in the form of money or goods, to those in need.', 'charity'],
    ['A journey to a sacred place, especially Mecca, as part of Islamic religious duty.', 'pilgrimage'],
    ['Faith or belief in Allah and His teachings.', 'iman'],
    ['Striving for excellence and doing one\'s best in the worship of Allah.', 'ihsan'],
    ['Consciousness of Allah and being mindful of His commands.', 'taqwa'],
    ['Paradise or the Garden, the ultimate reward for believers in the afterlife.', 'jannah'],
    ['Hell, a place of punishment for those who reject Allah.', 'jahannam'],
    ['The divine preordainment or destiny determined by Allah.', 'qadr'],
    ['The Islamic call to prayer announced from the mosque\'s minaret.', 'adhan'],
    ['Permissible or lawful according to Islamic law.', 'halal'],
    ['Prohibited or forbidden by Islamic law.', 'haram'],
    ['The natural disposition or innate purity with which humans are created.', 'fitrah'],
    ['The ritual purification with water before certain acts of worship, such as prayer.', 'ablution'],
    ['A veil or headscarf worn by Muslim women as a sign of modesty and privacy.', 'hijab'],
    ['The quality of being humble and unpretentious, valued in Islamic ethics.', 'modesty'],
    ['Thankfulness and appreciation, a virtue emphasized in Islamic teachings.', 'gratitude'],
    ['Endurance and perseverance in the face of challenges, a valued Islamic trait.', 'patience'],
    ['Sincere regret and turning away from sins, seeking forgiveness from Allah.', 'repentance'],
    ['Pardoning or excusing offenses, encouraged in Islam as a virtue.', 'forgiveness'],
    ['The state of being united or joined as a whole, emphasized in Islamic brotherhood and sisterhood.', 'unity'],
    ['The bond of unity and fraternity among Muslim men.', 'brotherhood'],
    ['The bond of unity and fraternity among Muslim women.', 'sisterhood']
]

global root, trieslabel, questionlabel, answerlabel, inputbox, submitbutton, hangman_label
global tries, inputanswer, actualanswer

tries = 0

# Hangman graphics
hangman_graphics = [
    "   ____\n  |    |\n  |    \n  |\n  |\n__|__",
    "   ____\n  |    |\n  |    O\n  |\n  |\n__|__",
    "   ____\n  |    |\n  |    O\n  |    |\n  |\n__|__",
    "   ____\n  |    |\n  |    O\n  |   /|\n  |\n__|__",
    "   ____\n  |    |\n  |    O\n  |   /|\\\n  |\n__|__",
    "   ____\n  |    |\n  |    O\n  |   /|\\\n  |   /\n__|__",
    "   ____\n  |    |\n  |    O\n  |   /|\\\n  |   / \\\n__|__"
]

def update_labels():
    trieslabel.configure(text=f'Tries left: {tries}')
    answerlabel.configure(text=' '.join(inputanswer))
    hangman_label.configure(text=hangman_graphics[len(hangman_graphics) - tries - 1])

def prepare_question():
    global tries, questionlabel, actualanswer, inputanswer, hangman_label
    tries = 6

    # choose one question
    question, answer = random.choice(word_list)

    # set answer
    actualanswer = answer
    inputanswer = ['_'] * len(answer)

    # set question label
    questionlabel.configure(text=question)

    # reset hangman label
    hangman_label.configure(text=hangman_graphics[0])

    update_labels()

def on_submit():
    global tries

    inputchar = inputbox.get()

    # check for letter in any location
    anyfound = False
    for index, char in enumerate(actualanswer):
        if char == inputchar:
            inputanswer[index] = char.upper()
            anyfound = True
    if not anyfound:
        tries -= 1

    # update label after changing inputanswer
    update_labels()

    if tries <= 0:
        playagain = messagebox.askyesno('Too bad!', f'The correct word was {actualanswer.upper()}. Try again?')
        if playagain:
            prepare_question()
        else:
            messagebox.showinfo('Thank you!', 'Thank you for playing along!')
            root.destroy()
            return

    # check if fully guessed
    if not '_' in inputanswer:
        playagain = messagebox.askyesno('You win!', f'The correct word was indeed {actualanswer.upper()}! Play again?')
        if playagain:
            prepare_question()
        else:
            messagebox.showinfo('Thank you!', 'Thank you for playing along!')
            root.destroy()
            return

    # clear textbox
    inputbox.delete(0, 'end')


# Create window
root = tk.Tk()
root.title('ISLAMIC WORD QUEST')
root.geometry('800x600')

trieslabel = ttk.Label(root, padding=10)
trieslabel.pack()

questionlabel = ttk.Label(root, font=('Times New Roman', 16))
questionlabel.pack()

answerlabel = ttk.Label(root, font=('Times New Roman', 48))
answerlabel.pack()

hangman_label = ttk.Label(root, font=('Courier New', 12), justify='left')
hangman_label.pack()

inputbox = ttk.Entry(root, font=('Times New Roman', 48), width=3, validate='key', validatecommand=(root.register(lambda val: len(val) <= 1), '%P'))
inputbox.configure(justify='center')
inputbox.bind('<Return>', lambda e: on_submit())
inputbox.pack()
inputbox.focus_set()

submitbutton = ttk.Button(root, text='Check!', command=on_submit)
submitbutton.pack()

prepare_question()

root.mainloop()

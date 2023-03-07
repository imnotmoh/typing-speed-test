from tkinter import *
from tkinter import messagebox
import time
import random
from tkinter.simpledialog import askstring

import sqlalchemy
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session

# creating a data base for the scores
engine = sqlalchemy.create_engine("sqlite:///highscore.db", echo=True)


class Base(DeclarativeBase):
    pass


class HighScore(Base):
    __tablename__ = "highscore"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=False)
    score = Column(Integer, nullable=False)


# Base.metadata.create_all(engine)

# new_score = HighScore(name="Moh", score=5)


word_list = ['a', 'ability', 'able', 'about', 'above', 'accept', 'according', 'account', 'across', 'act', 'action',
             'activity', 'actually', 'add', 'address', 'administration', 'admit', 'adult', 'affect', 'after', 'again',
             'against', 'age', 'agency', 'agent', 'ago', 'agree', 'agreement', 'ahead', 'air', 'all', 'allow', 'almost',
             'alone', 'along', 'already', 'also', 'although', 'always', 'American', 'among', 'amount', 'analysis',
             'and', 'animal', 'another', 'answer', 'any', 'anyone', 'anything', 'appear', 'apply', 'approach', 'area',
             'argue', 'arm', 'around', 'arrive', 'art', 'article', 'artist', 'as', 'ask', 'assume', 'at', 'attack',
             'attention', 'attorney', 'audience', 'author', 'authority', 'available', 'avoid', 'away', 'baby', 'back',
             'bad', 'bag', 'ball', 'bank', 'bar', 'base', 'be', 'beat', 'beautiful', 'because', 'become', 'bed',
             'before', 'begin', 'behavior', 'behind', 'believe', 'benefit', 'best', 'better', 'between', 'beyond',
             'big', 'bill', 'billion', 'bit', 'black', 'blood', 'blue', 'board', 'body', 'book', 'born', 'both', 'box',
             'boy', 'break', 'bring', 'brother', 'budget', 'build', 'building', 'business', 'but', 'buy', 'by', 'call',
             'camera', 'campaign', 'can', 'cancer', 'candidate', 'capital', 'car', 'card', 'care', 'career', 'carry',
             'case', 'catch', 'cause', 'cell', 'center', 'central', 'century', 'certain', 'certainly', 'chair',
             'challenge', 'chance', 'change', 'character', 'charge', 'check', 'child', 'choice', 'choose', 'church',
             'citizen', 'city', 'civil', 'claim', 'class', 'clear', 'clearly', 'close', 'coach', 'cold', 'collection',
             'college', 'color', 'come', 'commercial', 'common', 'community', 'company', 'compare', 'computer',
             'concern', 'condition', 'conference', 'Congress', 'consider', 'consumer', 'contain', 'continue', 'control',
             'cost', 'could', 'country', 'couple', 'course', 'court', 'cover', 'create', 'crime', 'cultural', 'culture',
             'cup', 'current', 'customer', 'cut', 'dark', 'data', 'daughter', 'day', 'dead', 'deal', 'death', 'debate',
             'decade', 'decide', 'decision', 'deep', 'defense', 'degree', 'Democrat', 'democratic', 'describe',
             'design', 'despite', 'detail', 'determine', 'develop', 'development', 'die', 'difference', 'different',
             'difficult', 'dinner', 'direction', 'director', 'discover', 'discuss', 'discussion', 'disease', 'do',
             'doctor', 'dog', 'door', 'down', 'draw', 'dream', 'drive', 'drop', 'drug', 'during', 'each', 'early',
             'east', 'easy', 'eat', 'economic', 'economy', 'edge', 'education', 'effect', 'effort', 'eight', 'either',
             'election', 'else', 'employee', 'end', 'energy', 'enjoy', 'enough', 'enter', 'entire', 'environment',
             'environmental', 'especially', 'establish', 'even', 'evening', 'event', 'ever', 'every', 'everybody',
             'everyone', 'everything', 'evidence', 'exactly', 'example', 'executive', 'exist', 'expect', 'experience',
             'expert', 'explain', 'eye', 'face', 'fact', 'factor', 'fail', 'fall', 'family', 'far', 'fast', 'father',
             'fear', 'federal', 'feel', 'feeling', 'few', 'field', 'fight', 'figure', 'fill', 'film', 'final',
             'finally', 'financial', 'find', 'fine', 'finger', 'finish', 'fire', 'firm', 'first', 'fish', 'five',
             'floor', 'fly', 'focus', 'follow', 'food', 'foot', 'for', 'force', 'foreign', 'forget', 'form', 'former',
             'forward', 'four', 'free', 'friend', 'from', 'front', 'full', 'fund', 'future', 'game', 'garden', 'gas',
             'general', 'generation', 'get', 'girl', 'give', 'glass', 'go', 'goal', 'good', 'government', 'great',
             'green', 'ground', 'group', 'grow', 'growth', 'guess', 'gun', 'guy', 'hair', 'half', 'hand', 'hang',
             'happen', 'happy', 'hard', 'have', 'he', 'head', 'health', 'hear', 'heart', 'heat', 'heavy', 'help', 'her',
             'here', 'herself', 'high', 'him', 'himself', 'his', 'history', 'hit', 'hold', 'home', 'hope', 'hospital',
             'hot', 'hotel', 'hour', 'house', 'how', 'however', 'huge', 'human', 'hundred', 'husband', 'I', 'idea',
             'identify', 'if', 'image', 'imagine', 'impact', 'important', 'improve', 'in', 'include', 'including',
             'increase', 'indeed', 'indicate', 'individual', 'industry', 'information', 'inside', 'instead',
             'institution', 'interest', 'interesting', 'international', 'interview', 'into', 'investment', 'involve',
             'issue', 'it', 'item', 'its', 'itself', 'job', 'join', 'just', 'keep', 'key', 'kid', 'kill', 'kind',
             'kitchen', 'know', 'knowledge', 'land', 'language', 'large', 'last', 'late', 'later', 'laugh', 'law',
             'lawyer', 'lay', 'lead', 'leader', 'learn', 'least', 'leave', 'left', 'leg', 'legal', 'less', 'let',
             'letter', 'level', 'lie', 'life', 'light', 'like', 'likely', 'line', 'list', 'listen', 'little', 'live',
             'local', 'long', 'look', 'lose', 'loss', 'lot', 'love', 'low', 'machine', 'magazine', 'main', 'maintain',
             'major', 'majority', 'make', 'man', 'manage', 'management', 'manager', 'many', 'market', 'marriage',
             'material', 'matter', 'may', 'maybe', 'me', 'mean', 'measure', 'media', 'medical', 'meet', 'meeting',
             'member', 'memory', 'mention', 'message', 'method', 'middle', 'might', 'military', 'million', 'mind',
             'minute', 'miss', 'mission', 'model', 'modern', 'moment', 'money', 'month', 'more', 'morning', 'most',
             'mother', 'mouth', 'move', 'movement', 'movie', 'Mr', 'Mrs', 'much', 'music', 'must', 'my', 'myself',
             'name', 'nation', 'national', 'natural', 'nature', 'near', 'nearly', 'necessary', 'need', 'network',
             'never', 'new', 'news', 'newspaper', 'next', 'nice', 'night', 'no', 'none', 'nor', 'north', 'not', 'note',
             'nothing', 'notice', 'now', "n't", 'number', 'occur', 'of', 'off', 'offer', 'office', 'officer',
             'official', 'often', 'oh', 'oil', 'ok', 'old', 'on', 'once', 'one', 'only', 'onto', 'open', 'operation',
             'opportunity', 'option', 'or', 'order', 'organization', 'other', 'others', 'our', 'out', 'outside', 'over',
             'own', 'owner', 'page', 'pain', 'painting', 'paper', 'parent', 'part', 'participant', 'particular',
             'particularly', 'partner', 'party', 'pass', 'past', 'patient', 'pattern', 'pay', 'peace', 'people', 'per',
             'perform', 'performance', 'perhaps', 'period', 'person', 'personal', 'phone', 'physical', 'pick',
             'picture', 'piece', 'place', 'plan', 'plant', 'play', 'player', 'PM', 'point', 'police', 'policy',
             'political', 'politics', 'poor', 'popular', 'population', 'position', 'positive', 'possible', 'power',
             'practice', 'prepare', 'present', 'president', 'pressure', 'pretty', 'prevent', 'price', 'private',
             'probably', 'problem', 'process', 'produce', 'product', 'production', 'professional', 'professor',
             'program', 'project', 'property', 'protect', 'prove', 'provide', 'public', 'pull', 'purpose', 'push',
             'put', 'quality', 'question', 'quickly', 'quite', 'race', 'radio', 'raise', 'range', 'rate', 'rather',
             'reach', 'read', 'ready', 'real', 'reality', 'realize', 'really', 'reason', 'receive', 'recent',
             'recently', 'recognize', 'record', 'red', 'reduce', 'reflect', 'region', 'relate', 'relationship',
             'religious', 'remain', 'remember', 'remove', 'report', 'represent', 'Republican', 'require', 'research',
             'resource', 'respond', 'response', 'responsibility', 'rest', 'result', 'return', 'reveal', 'rich', 'right',
             'rise', 'risk', 'road', 'rock', 'role', 'room', 'rule', 'run', 'safe', 'same', 'save', 'say', 'scene',
             'school', 'science', 'scientist', 'score', 'sea', 'season', 'seat', 'second', 'section', 'security', 'see',
             'seek', 'seem', 'sell', 'send', 'senior', 'sense', 'series', 'serious', 'serve', 'service', 'set', 'seven',
             'several', 'sex', 'sexual', 'shake', 'share', 'she', 'shoot', 'short', 'shot', 'should', 'shoulder',
             'show', 'side', 'sign', 'significant', 'similar', 'simple', 'simply', 'since', 'sing', 'single', 'sister',
             'sit', 'site', 'situation', 'six', 'size', 'skill', 'skin', 'small', 'smile', 'so', 'social', 'society',
             'soldier', 'some', 'somebody', 'someone', 'something', 'sometimes', 'son', 'song', 'soon', 'sort', 'sound',
             'source', 'south', 'southern', 'space', 'speak', 'special', 'specific', 'speech', 'spend', 'sport',
             'spring', 'staff', 'stage', 'stand', 'standard', 'star', 'start', 'state', 'statement', 'station', 'stay',
             'step', 'still', 'stock', 'stop', 'store', 'story', 'strategy', 'street', 'strong', 'structure', 'student',
             'study', 'stuff', 'style', 'subject', 'success', 'successful', 'such', 'suddenly', 'suffer', 'suggest',
             'summer', 'support', 'sure', 'surface', 'system', 'table', 'take', 'talk', 'task', 'tax', 'teach',
             'teacher', 'team', 'technology', 'television', 'tell', 'ten', 'tend', 'term', 'test', 'than', 'thank',
             'that', 'the', 'their', 'them', 'themselves', 'then', 'theory', 'there', 'these', 'they', 'thing', 'think',
             'third', 'this', 'those', 'though', 'thought', 'thousand', 'threat', 'three', 'through', 'throughout',
             'throw', 'thus', 'time', 'to', 'today', 'together', 'tonight', 'too', 'top', 'total', 'tough', 'toward',
             'town', 'trade', 'traditional', 'training', 'travel', 'treat', 'treatment', 'tree', 'trial', 'trip',
             'trouble', 'true', 'truth', 'try', 'turn', 'TV', 'two', 'type', 'under', 'understand', 'unit', 'until',
             'up', 'upon', 'us', 'use', 'usually', 'value', 'various', 'very', 'victim', 'view', 'violence', 'visit',
             'voice', 'vote', 'wait', 'walk', 'wall', 'want', 'war', 'watch', 'water', 'way', 'we', 'weapon', 'wear',
             'week', 'weight', 'well', 'west', 'western', 'what', 'whatever', 'when', 'where', 'whether', 'which',
             'while', 'white', 'who', 'whole', 'whom', 'whose', 'why', 'wide', 'wife', 'will', 'win', 'wind', 'window',
             'wish', 'with', 'within', 'without', 'woman', 'wonder', 'word', 'work', 'worker', 'world', 'worry',
             'would', 'write', 'writer', 'wrong', 'yard', 'yeah', 'year', 'yes', 'yet', 'you', 'young', 'your',

             'yourself']
# timers
start_time = None
live_caltimer = None
count_down_timer = None
refresh = None
count_down_time = None
# declared because it's a global variable
test_words = None
speed = 0
# to track the current word to be typed
word_track = 0
# track countdown
counting_down = False
# to contain typed words
typed_words_list_correct = []
typed_words_list_wrong = []
# to contain each word object
canva_text_obj_list = []

# Tkinter ui

window = Tk()
window.title("Moh's type speed calculator")
window.config(pady=30, padx=30)

canva = Canvas(background="white", width=500, height=300)
canva.grid(row=1, column=0, columnspan=5, padx=20)
label = Label(text="type in here", pady=50)
label.grid(column=0, row=2)
text_input = Entry(width=40)
text_input.grid(column=1, row=2, columnspan=3, pady=50)
speed_label = Label(text=f"speed:{speed} cps")
speed_label.grid(row=3, column=2)
timer_label = Label()
timer_label.grid(row=0, column=3)
with Session(engine) as session:
    all_data = session.query(HighScore).all()
    high_score = all_data[-1].score
high_score_label = Label(text=f"highcore:{high_score}")
high_score_label.grid(row=0, column=0)

# algorithm to place each word
def fetch_words():
    global test_words
    # selects random 50 words
    test_words = random.choices(word_list, k=50)
    x = 0
    y = 30
    for i in test_words:
        x += (13 * len(i)) / 2
        if x > 470:
            x = (13 * len(i)) / 2
            y += 30
        canva_text_obj_list.append(canva.create_text(x, y, text=f"{i}", font=("Ariel", 20, "bold"), fill="black"))
        x += (15 * len(i) - (len(i))) / 2


# calculates the speed automatically
def cal_speed(inp):
    global count_down_time
    global refresh
    global counting_down
    global start_time
    global speed
    global word_track
    global test_words
    canva.itemconfig(canva_text_obj_list[word_track], fill="Blue")
    if " " in inp:
        if inp.strip() == test_words[word_track]:
            text_input.delete(0, END)
            canva.itemconfig(canva_text_obj_list[word_track], fill="green")
            if word_track < len(canva_text_obj_list):
                word_track += 1
            else:
                wpm = (len(typed_words_list_correct)/(30 - count_down_time)) * 2
                window.after_cancel(refresh)
                messagebox.showinfo(title="type speed", message=f"type speed:{wpm} words per minute\n"
                                                                f"the words typed wrong are not included in the score\n"
                                                                f"The typed wrong words are\n"
                                                                + "\n".join(typed_words_list_wrong))
                with Session(engine) as session:
                    all_data = session.query(HighScore).all()
                    if wpm > all_data[-1].score:
                        name = askstring('New highscore', 'please enter your name?')
                        if name != "":
                            new_score = HighScore(name=name,score=wpm)
                            session.add(new_score)
                            session.commit()
                    reset()

            typed_words_list_correct.append(inp)
        else:
            text_input.delete(0, END)
            canva.itemconfig(canva_text_obj_list[word_track], fill="red")
            typed_words_list_wrong.append(test_words[word_track])
            word_track += 1
    refresh = window.after(50, cal_speed, text_input.get())


# count down function
def count_down(time):
    global count_down_time
    global count_down_timer
    global counting_down
    counting_down = True
    count_down_time = time
    if count_down_time < 0:
        wpm = len(typed_words_list_correct) * 2
        window.after_cancel(refresh)
        messagebox.showinfo(title="type speed", message=f"type speed:{wpm} words per minute\n"
                                                        f"the words typed wrong are not included in the score\n"
                                                        f"The typed wrong words are\n"
                                                        + "\n".join(typed_words_list_wrong)
                            )
        with Session(engine) as session:
            all_data = session.query(HighScore).all()
            if wpm > all_data[-1].score:

                name = askstring('New highscore', 'please enter your name?')
                if name != "" :
                    new_score = HighScore(name=name,score=wpm)
                    session.add(new_score)
                    session.commit()
            reset()




        return

    str_count_down = f"{count_down_time}"
    if count_down_time < 10:
        str_count_down = f"0{count_down_time}"
    timer_label.config(text=f"00:{str_count_down}")
    count_down_time -= 1
    count_down_timer = window.after(1000, count_down, count_down_time)


# to caalculate the live characters entered per second
def live_calculator(inp):
    global counting_down
    global start_time
    global speed
    global live_caltimer
    global word_track
    global test_words
    # to dectect if a text has been entered
    if inp != "" or len(typed_words_list_correct) > 0 or len(typed_words_list_wrong) > 0:
        if not counting_down:
            count_down(30)
        if start_time == None:
            start_time = time.time()
        time_now = time.time()
        typing_time = time_now - start_time
        # bug fix
        if typing_time != 0:
            speed = round(len("".join(typed_words_list_correct)) / typing_time, 2)
        speed_label.config(text=f"speed:{speed} cps")
    live_caltimer = window.after(500, live_calculator, text_input.get())


# resets the app variables
def reset():
    global typed_words_list_correct
    global typed_words_list_wrong
    global count_down_timer
    global canva_text_obj_list
    global live_caltimer
    global start_time
    global speed
    global word_track
    global counting_down

    word_track = 0
    speed = 00
    start_time = None
    text_input.delete(0, END)
    window.after_cancel(refresh)
    window.after_cancel(live_caltimer)
    window.after_cancel(count_down_timer)
    speed_label.config(text=f"speed:{speed} cps")
    timer_label.config(text="")
    typed_words_list_wrong = []
    typed_words_list_correct = []
    cal_speed(text_input.get())
    live_calculator(text_input.get())

    counting_down = False
    for i in canva_text_obj_list:
        canva.delete(i)
    canva_text_obj_list = []
    with Session(engine) as session:
        all_data = session.query(HighScore).all()
        high_score = all_data[-1].score
    high_score_label.config(text=f"highscore:{high_score}")

    fetch_words()


fetch_words()
reset_button = Button(text="reset", command=reset)
reset_button.grid(row=4, column=2)
live_calculator(text_input.get())
cal_speed(text_input.get())
window.mainloop()
# The words_list used in this code are scraped from ef.com and was intended for personal purpose

#!/usr/bin/python3

"""
starleader: Michael Adams; unquietwiki.com; December 2020
Organized entry of STAR Response Method into Amazon(TM) Leadership Practices
Not official Amazon software; written as a tool to help myself with interviews.

* https://www.aboutamazon.com/about-us/leadership-principles
* https://www.thebalancecareers.com/what-is-the-star-interview-response-technique-2061629
* https://pysimplegui.readthedocs.io/
* https://pynative.com/
"""

import PySimpleGUI as sg
import json
from json import JSONEncoder

# === Define data to collect ===


class LeadershipPractice:
    def __init__(self, name, description, situation="", task="", actions="", result=""):
        self.name = name
        self.description = description
        self.situation = situation
        self.task = task
        self.actions = actions
        self.result = result

    def setSituation(self, value):
        self.situation = value

    def setTask(self, value):
        self.task = value

    def setActions(self, value):
        self.actions = value

    def setResult(self, value):
        self.result = value

    def getSituation(self):
        return self.situation

    def getTask(self):
        return self.task

    def getActions(self):
        return self.actions

    def getResult(self):
        return self.result

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)


# === Aggregate the Leadership Principles ===


def getLeadershipPrinciples():
    lps = []
    lps.append(LeadershipPractice(
        "Customer Obsession", "Leaders start with the customer and work backwards. They work vigorously to earn and keep customer trust. Although leaders pay attention to competitors, they obsess over customers."))
    lps.append(LeadershipPractice(
        "Ownership", "Leaders are owners. They think long term and don’t sacrifice long-term value for short-term results. They act on behalf of the entire company, beyond just their own team. They never say \"that’s not my job.\""))
    lps.append(LeadershipPractice(
        "Invent and Simplify", "Leaders expect and require innovation and invention from their teams and always find ways to simplify. They are externally aware, look for new ideas from everywhere, and are not limited by \"not invented here.\" As we do new things, we accept that we may be misunderstood for long periods of time."))
    lps.append(LeadershipPractice(
        "Are Right, A Lot", "Leaders are right a lot. They have strong business judgment and good instincts. They seek diverse perspectives and work to disconfirm their beliefs."))
    lps.append(LeadershipPractice(
        "Learn and Be Curious", "Leaders are never done learning and always seek to improve themselves. They are curious about new possibilities and act to explore them."))
    lps.append(LeadershipPractice(
        "Hire and Develop the Best", "Leaders raise the performance bar with every hire and promotion. They recognize exceptional talent, and willingly move them throughout the organization. Leaders develop leaders and take seriously their role in coaching others. We work on behalf of our people to invent mechanisms for development like Career Choice."))
    lps.append(LeadershipPractice(
        "Insist on the Highest Standards", "Leaders have relentlessly high standards—many people may think these standards are unreasonably high. Leaders are continually raising the bar and driving their teams to deliver high-quality products, services, and processes. Leaders ensure that defects do not get sent down the line and that problems are fixed so they stay fixed."))
    lps.append(LeadershipPractice(
        "Think Big", "Thinking small is a self-fulfilling prophecy. Leaders create and communicate a bold direction that inspires results. They think differently and look around corners for ways to serve customers."))
    lps.append(LeadershipPractice(
        "Bias for Action", "Speed matters in business. Many decisions and actions are reversible and do not need extensive study. We value calculated risk taking."))
    lps.append(LeadershipPractice(
        "Frugality", "Accomplish more with less. Constraints breed resourcefulness, self-sufficiency and invention. There are no extra points for growing headcount, budget size, or fixed expense."))
    lps.append(LeadershipPractice(
        "Earn Trust", "Leaders listen attentively, speak candidly, and treat others respectfully. They are vocally self-critical, even when doing so is awkward or embarrassing. Leaders do not believe their or their team’s body odor smells of perfume. They benchmark themselves and their teams against the best."))
    lps.append(LeadershipPractice(
        "Dive Deep", "Leaders operate at all levels, stay connected to the details, audit frequently, and are skeptical when metrics and anecdote differ. No task is beneath them."))
    lps.append(LeadershipPractice(
        "Have Backbone; Disagree and Commit", "Leaders are obligated to respectfully challenge decisions when they disagree, even when doing so is uncomfortable or exhausting. Leaders have conviction and are tenacious. They do not compromise for the sake of social cohesion. Once a decision is determined, they commit wholly."))
    lps.append(LeadershipPractice(
        "Deliver Results", "Leaders focus on the key inputs for their business and deliver them with the right quality and in a timely fashion. Despite setbacks, they rise to the occasion and never settle."))
    return lps


# === Data handler ===


class DataHandler:
    def __init__(self):
        self.fileName = "starleader.json"

    # Attempt to load JSON file
    def load(self):
        try:
            dataBlobs = []
            with open(self.fileName, 'r') as jsonFile:
                jsonData = json.load(jsonFile)
                # The "properly formatted JSON" likes having a master block, so we need to account for that
                for blob in jsonData["LeadershipPractice"]:
                    dataBlobs.append(LeadershipPractice(
                        blob['name'],blob['description'],blob['situation'],blob['task'],blob['actions'],blob['result']))
            return dataBlobs
        except:
            return getLeadershipPrinciples()

    # Attempt to format & save JSON file
    def save(self, sourceData):
        try:
            fileToSave = []
            for s in sourceData:
                fileToSave.append(s.toJSON())
            with open(self.fileName, 'w') as jsonFile:
                jsonFile.write("{\"LeadershipPractice\":["+'\n')
                curRow = 0
                for dataString in fileToSave:
                    curRow = curRow + 1
                    if curRow != len(fileToSave):
                        jsonFile.write('   '+dataString+',\n')
                    else:
                        jsonFile.write('   '+dataString+'\n')
                jsonFile.write("]}"+'\n')
        except:
            sg.popup("JSON couldn't save")


# === GUI program ===


sg.theme('Material2')
standardFont = 'Arial 12'
# leadershipPrinciples = getLeadershipPrinciples()
leadershipPrinciples = DataHandler().load()

for principle in leadershipPrinciples:
    # Variable fields
    situation = sg.Multiline(principle.getSituation(),
                             size=(128, 6), auto_refresh=True)
    task = sg.Multiline(principle.getTask(), size=(128, 6), auto_refresh=True)
    actions = sg.Multiline(principle.getActions(),
                           size=(128, 6), auto_refresh=True)
    result = sg.Multiline(principle.getResult(),
                          size=(128, 6), auto_refresh=True)
    # Define the window's contents
    layout = [
        [sg.Text("")],
        [sg.Text("Principle: "+principle.name, font='Arial 14')],
        [sg.Multiline(principle.description, size=(
            160, 3), disabled=True, autoscroll=True, text_color="yellow")],
        [sg.Text("")],
        [sg.Text("Describe the event or SITUATION that you were in.")],
        [situation],
        [sg.Text("Explain the TASK you had to complete.")],
        [task],
        [sg.Text("Describe the specific ACTIONS you took to complete the task.")],
        [actions],
        [sg.Text("Close with the RESULT of your efforts.")],
        [result],
        [sg.Text("")],
        [sg.Text("            "), sg.Button('Next'),
         sg.Text("            "), sg.Text("Saves on quitting"),
         sg.Text("            "), sg.Button('Quit'),
         sg.Text("            "),
         sg.Text(
             "Reference: https://www.aboutamazon.com/about-us/leadership-principles")
         ],
        [sg.Text("")],
    ]
    # Create the window
    window = sg.Window(
        'Amazon(TM) Leadership Principles in STAR format ; NOT AN OFFICIAL TOOL',
        layout,
        size=(1152, 832),
        font=standardFont)
    event, values = window.read()
    # Event handlers
    principle.setSituation(situation.get())
    principle.setTask(task.get())
    principle.setActions(actions.get())
    principle.setResult(result.get())
    window.close()
    if event == 'Next':
        next
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

DataHandler().save(leadershipPrinciples)

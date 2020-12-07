"""
starleader: Michael Adams; unquietwiki.com; December 2020
Organized entry of STAR Response Method into Amazon(TM) Leadership Practices
Not official Amazon software; written as a tool to help myself with an interview.
* https://www.aboutamazon.com/about-us/leadership-principles
* https://www.thebalancecareers.com/what-is-the-star-interview-response-technique-2061629
* https://pysimplegui.readthedocs.io/
"""

import PySimpleGUI as sg

# === Define data to collect ===


class LeadershipPractice:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def setSituation(self, value):
        self.situation = value

    def setTask(self, value):
        self.task = value

    def setActions(self, value):
        self.actions = value

    def setResult(self, value):
        self.result = value


# === Aggregate the Leadership Principles ===


leadershipPrinciples = []
leadershipPrinciples.append(LeadershipPractice(
    "Customer Obsession", "Leaders start with the customer and work backwards. They work vigorously to earn and keep customer trust. Although leaders pay attention to competitors, they obsess over customers."))
leadershipPrinciples.append(LeadershipPractice(
    "Ownership", "Leaders are owners. They think long term and don’t sacrifice long-term value for short-term results. They act on behalf of the entire company, beyond just their own team. They never say \"that’s not my job.\""))
leadershipPrinciples.append(LeadershipPractice(
    "Invent and Simplify", "Leaders expect and require innovation and invention from their teams and always find ways to simplify. They are externally aware, look for new ideas from everywhere, and are not limited by \"not invented here.\" As we do new things, we accept that we may be misunderstood for long periods of time."))
leadershipPrinciples.append(LeadershipPractice(
    "Are Right, A Lot", "Leaders are right a lot. They have strong business judgment and good instincts. They seek diverse perspectives and work to disconfirm their beliefs."))
leadershipPrinciples.append(LeadershipPractice(
    "Learn and Be Curious", "Leaders are never done learning and always seek to improve themselves. They are curious about new possibilities and act to explore them."))
leadershipPrinciples.append(LeadershipPractice(
    "Hire and Develop the Best", "Leaders raise the performance bar with every hire and promotion. They recognize exceptional talent, and willingly move them throughout the organization. Leaders develop leaders and take seriously their role in coaching others. We work on behalf of our people to invent mechanisms for development like Career Choice."))
leadershipPrinciples.append(LeadershipPractice(
    "Insist on the Highest Standards", "Leaders have relentlessly high standards—many people may think these standards are unreasonably high. Leaders are continually raising the bar and driving their teams to deliver high-quality products, services, and processes. Leaders ensure that defects do not get sent down the line and that problems are fixed so they stay fixed."))
leadershipPrinciples.append(LeadershipPractice(
    "Think Big", "Thinking small is a self-fulfilling prophecy. Leaders create and communicate a bold direction that inspires results. They think differently and look around corners for ways to serve customers."))
leadershipPrinciples.append(LeadershipPractice(
    "Bias for Action", "Speed matters in business. Many decisions and actions are reversible and do not need extensive study. We value calculated risk taking."))
leadershipPrinciples.append(LeadershipPractice(
    "Frugality", "Accomplish more with less. Constraints breed resourcefulness, self-sufficiency and invention. There are no extra points for growing headcount, budget size, or fixed expense."))
leadershipPrinciples.append(LeadershipPractice(
    "Earn Trust", "Leaders listen attentively, speak candidly, and treat others respectfully. They are vocally self-critical, even when doing so is awkward or embarrassing. Leaders do not believe their or their team’s body odor smells of perfume. They benchmark themselves and their teams against the best."))
leadershipPrinciples.append(LeadershipPractice(
    "Dive Deep", "Leaders operate at all levels, stay connected to the details, audit frequently, and are skeptical when metrics and anecdote differ. No task is beneath them."))
leadershipPrinciples.append(LeadershipPractice(
    "Have Backbone; Disagree and Commit", "Leaders are obligated to respectfully challenge decisions when they disagree, even when doing so is uncomfortable or exhausting. Leaders have conviction and are tenacious. They do not compromise for the sake of social cohesion. Once a decision is determined, they commit wholly."))
leadershipPrinciples.append(LeadershipPractice(
    "Deliver Results", "Leaders focus on the key inputs for their business and deliver them with the right quality and in a timely fashion. Despite setbacks, they rise to the occasion and never settle."))


# === Define the GUI ===

sg.theme('Dark Grey 3')
standardFont = 'Arial 12'

for principle in leadershipPrinciples:
    # Define the window's contents
    layout = [
        [sg.Text("")],
        [sg.Text("Principle: "+principle.name, font='Arial 14')],
        [sg.Multiline(principle.description, size=(
            160, 3), text_color='white', background_color='blue', disabled=True)],
        [sg.Text("")],
        [sg.Text("Describe the event or SITUATION that you were in.")],
        [sg.Multiline(size=(128, 6), key=principle.setSituation)],
        [sg.Text("Explain the TASK you had to complete.")],
        [sg.Multiline(size=(128, 6), key=principle.setTask)],
        [sg.Text("Describe the specific ACTIONS you took to complete the task.")],
        [sg.Multiline(size=(128, 6), key=principle.setActions)],
        [sg.Text("Close with the RESULT of your efforts.")],
        [sg.Multiline(size=(128, 6), key=principle.setResult)],
        [sg.Text("")],
        [sg.Text("            "), sg.Button('Next'),
         sg.Text("            "), sg.Text("Saves on quitting"),
         sg.Text("            "), sg.Button('Quit'),
         sg.Text("            "),
         sg.Text("Reference: https://www.aboutamazon.com/about-us/leadership-principles")
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
    if event == 'Next':
        window.close()
        next
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        window.close()
        break

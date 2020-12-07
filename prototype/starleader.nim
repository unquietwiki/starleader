#[

starleader: Michael Adams; unquietwiki.com; December 2020

Organized entry of STAR Response Method into Amazon(TM) Leadership Practices
* https://www.aboutamazon.com/about-us/leadership-principles
* https://www.thebalancecareers.com/what-is-the-star-interview-response-technique-2061629
* https://nim-by-example.github.io/
* https://stackoverflow.com/questions/26191114/how-to-convert-object-to-json-in-nim
* https://github.com/yglukhov/nimx

]#

import json
import nimx / [ window, button, layout, text_field, scroll_view ]

# === Define data to collect ===

type LeadershipPractice = object 
    name: string
    description: string
    situation: string
    task: string
    actions: string
    result: string

var practices: seq[LeadershipPractice] = @[]
practices.add(LeadershipPractice(name: "Customer Obsession", description: "Leaders start with the customer and work backwards. They work vigorously to earn and keep customer trust. Although leaders pay attention to competitors, they obsess over customers."))
practices.add(LeadershipPractice(name: "Ownership", description: "Leaders are owners. They think long term and don’t sacrifice long-term value for short-term results. They act on behalf of the entire company, beyond just their own team. They never say \"that’s not my job.\""))
practices.add(LeadershipPractice(name: "Invent and Simplify", description: "Leaders expect and require innovation and invention from their teams and always find ways to simplify. They are externally aware, look for new ideas from everywhere, and are not limited by \"not invented here.\" As we do new things, we accept that we may be misunderstood for long periods of time."))
practices.add(LeadershipPractice(name: "Are Right, A Lot", description: "Leaders are right a lot. They have strong business judgment and good instincts. They seek diverse perspectives and work to disconfirm their beliefs."))
practices.add(LeadershipPractice(name: "Learn and Be Curious", description: "Leaders are never done learning and always seek to improve themselves. They are curious about new possibilities and act to explore them."))
practices.add(LeadershipPractice(name: "Hire and Develop the Best", description: "Leaders raise the performance bar with every hire and promotion. They recognize exceptional talent, and willingly move them throughout the organization. Leaders develop leaders and take seriously their role in coaching others. We work on behalf of our people to invent mechanisms for development like Career Choice."))
practices.add(LeadershipPractice(name: "Insist on the Highest Standards", description: "Leaders have relentlessly high standards—many people may think these standards are unreasonably high. Leaders are continually raising the bar and driving their teams to deliver high-quality products, services, and processes. Leaders ensure that defects do not get sent down the line and that problems are fixed so they stay fixed."))
practices.add(LeadershipPractice(name: "Think Big", description: "Thinking small is a self-fulfilling prophecy. Leaders create and communicate a bold direction that inspires results. They think differently and look around corners for ways to serve customers."))
practices.add(LeadershipPractice(name: "Bias for Action", description: "Speed matters in business. Many decisions and actions are reversible and do not need extensive study. We value calculated risk taking."))
practices.add(LeadershipPractice(name: "Frugality", description: "Accomplish more with less. Constraints breed resourcefulness, self-sufficiency and invention. There are no extra points for growing headcount, budget size, or fixed expense."))
practices.add(LeadershipPractice(name: "Earn Trust", description: "Leaders listen attentively, speak candidly, and treat others respectfully. They are vocally self-critical, even when doing so is awkward or embarrassing. Leaders do not believe their or their team’s body odor smells of perfume. They benchmark themselves and their teams against the best."))
practices.add(LeadershipPractice(name: "Dive Deep", description: "Leaders operate at all levels, stay connected to the details, audit frequently, and are skeptical when metrics and anecdote differ. No task is beneath them."))
practices.add(LeadershipPractice(name: "Have Backbone; Disagree and Commit", description: "Leaders are obligated to respectfully challenge decisions when they disagree, even when doing so is uncomfortable or exhausting. Leaders have conviction and are tenacious. They do not compromise for the sake of social cohesion. Once a decision is determined, they commit wholly."))
practices.add(LeadershipPractice(name: "Deliver Results", description: "Leaders focus on the key inputs for their business and deliver them with the right quality and in a timely fashion. Despite setbacks, they rise to the occasion and never settle."))


# === GUI definition ===

const GUI_width = 1280
const GUI_height = 896

runApplication:
    let root = newWindow(newRect(32, 32, GUI_width, GUI_height))
    root.makeLayout:
        - ScrollView:
            size >= [256, 1279]
            left == 0
            - Label:
                text: "Questions"
                top == 128          
        - Button:
            left == 256 + 1
            width == 128
            height == 48
            title: "Situation"
            onAction:
                echo "S"
        - Button:
            left == 256 + 129
            width == 128
            height == 48
            title: "Task"
            onAction:
                echo "T"
        - Button:
            left == 256 + 257
            width == 128
            height == 48
            title: "Actions"
            onAction:
                echo "A"
        - Button:
            left == 256 + 385
            width == 128
            height == 48
            title: "Result"
            onAction:
                echo "R"
        - Button:
            left == 256 + 513
            width == 128
            height == 48
            title: "SAVE"
            onAction:
                echo "SAVED"

#[
# Interview Process

for p in practices:
    echo '\n' & "===== " & p.name & " =====" & '\n'
    echo p.description
    echo '\n'
    # SITUATION
    echo "Describe the event or SITUATION that you were in."
    # TASK
    echo "Explain the TASK you had to complete."
    # ACTIONS
    echo "Describe the specific ACTIONS you took to complete the task."
    # RESULT
    echo "Close with the RESULT of your efforts."

# Export JSON

echo(%practices)
]#
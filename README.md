# My ProLearning Recommendation API (Option B)


## Disclamer & Tools
Before I start I want to preface that I used AI to assist me to write the code, create the data base and to even start out tell me how & where I could research information in order to be able to do this on my own. I will say I don't think I would've given this same quality of work without AI

I also used FASTAPI & PYDANTIC to have most of my error handling and the hosting set up.

##  Introduction: What I built and focused on
Hi! I'm a student at granite bay high school, and for my internship project, I chose **Option B: Backend / API**. 

I chose option B because I was interested in the backend development side of things. The brief mentioned avoiding hallucinations and making sure things were source-grounded, so I built an API that relies on a clean, curated internal dataset based off a ai generated placeholder dataset that would be later replace with a system that can revcieve manual data/courses and gets courses from onlune websites that offer these services, like coursera that you mentioned in your doc that was sent out. It filters learning opportunities, scores them based on how well they match, and tells the user  why it was recommended, complete with a link and a "data confidence" rating.

## What currently works vs. What is incomplete
**What works:**
* **Smart Filtering:** You can filter by budget, topic, modality (online/in-person), and activity type.
* **Custom Scoring:** I wrote an algorithm that gives bonus points if an activity is completely free or if it has been recently verified.
* **Honest Explanations:** Every result generates a custom sentence explaining why it was picked, plus a "confidence rating" based on the last time the data was verified.
* **Safe Errors:** If you search for something I don't have, it returns a friendly 404 message suggesting what to do next.

**What is incomplete (My Boundaries):**
* **Database:** I don't have a live database running. Instead, I used a seeded, hardcoded Python list of 12 diverse activities to simulate what the database would return. 
* **Live Ingestion:** I am not scraping external sites in real-time. I assumed that part of the pipeline happens somewhere else.

## Time Spent
Appromently I spent around 1-2 hours brainstorming. 2-3 hours learning about apis(not directly on this project). And 4-5 hours on the project itself. 

In total I would say I spent 5-7 hours directly on this project.

## Setup and Review Instructions
I built this using Python and FastAPI. So it runs locally!

**1. Install the required libraries:**
Open your terminal and run:
`pip install fastapi uvicorn pydantic`

**2. Start the API server:**
Make sure you are in the same folder as `main.py`, then run:
`uvicorn main:app --reload`

**3. Test the API:**
Once it's running, the absolute best way to review my project is to use the automatic interactive docs. Open your browser and go to:
**http://127.0.0.1:8000/docs**

**Example Input to try:**
Go to the `POST /recommendations` endpoint, click "Try it out", and paste this in:
```json
{
  "topic": "python",
  "max_budget": 50,
  "modality": "online",
  "activity_type": "course"
}

```json

Here is a list of all the possible inputs.
**Note you can also just leave some of them empty if you dont want to write anything for the ("").**
1. topic (Primary Topics & Tags) you can enter either one

    Primary Topics: python, machine learning, web development, project management, data science, networking, cybersecurity, consulting, engineering, artificial intelligence

    Searchable Tags: programming, coding, beginner, ai, tensorflow, html, css, javascript, automation, scripting, pmp, leadership, business, google, sql, ibm, community, meetup, women in tech, diversity, career, security, hacking, tech, volunteering, nonprofits, electrical engineering, research, ieee, government

2. activity_type

    Course

    Textbook

    Certificate

    Meetup

    Workshop

    Volunteering

    Professional Association

    Community of Practice

3. modality

    Online

    In-Person

    Hybrid

4. preferred_format

    Online Course

    Textbook (Free Online)

    Online Certificate Program

    Local Meetup

    Live Online Workshop

    Volunteer Project

    Professional Association

    Online Community
# Imports required libraries for building the API and defining data models.
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

# Acts as a simulated, normalized database.
LEARNING_DATABASE = [
    {
        "id": 1,
        "title": "Python for Everybody",
        "topic": "python",
        "activity_type": "Course",
        "cost": 49,
        "modality": "Online",
        "location": "Online (U.S.)",
        "audience": "High School, University, Professional",
        "format": "Online Course",
        "tags": ["python", "programming", "coding", "beginner"],
        "source_name": "Coursera",
        "source_link": "https://www.coursera.org/specializations/python",
        "description": "A beginner-friendly specialization covering Python fundamentals.",
        "is_verified": True,
        "last_verified": "2026-03",
    },
    {
        "id": 2,
        "title": "Machine Learning Crash Course",
        "topic": "machine learning",
        "activity_type": "Course",
        "cost": 0,
        "modality": "Online",
        "location": "Online (U.S.)",
        "audience": "University, Professional",
        "format": "Online Course",
        "tags": ["machine learning", "ai", "data science", "python", "tensorflow"],
        "source_name": "Google Developers",
        "source_link": "https://developers.google.com/machine-learning/crash-course",
        "description": "Google's fast-paced intro to machine learning using TensorFlow.",
        "is_verified": True,
        "last_verified": "2026-03",
    },
    {
        "id": 3,
        "title": "The Complete Web Developer Bootcamp",
        "topic": "web development",
        "activity_type": "Course",
        "cost": 15,
        "modality": "Online",
        "location": "Online (U.S.)",
        "audience": "High School, University, Professional",
        "format": "Online Course",
        "tags": ["web development", "html", "css", "javascript", "coding"],
        "source_name": "Udemy",
        "source_link": "https://www.udemy.com/course/the-complete-web-development-bootcamp/",
        "description": "Covers HTML, CSS, JavaScript, and backend development from scratch.",
        "is_verified": True,
        "last_verified": "2026-02",
    },
    {
        "id": 4,
        "title": "Automate the Boring Stuff with Python",
        "topic": "python",
        "activity_type": "Textbook",
        "cost": 0,
        "modality": "Online",
        "location": "Online (U.S.)",
        "audience": "High School, University, Professional",
        "format": "Textbook (Free Online)",
        "tags": ["python", "automation", "scripting", "beginner", "coding"],
        "source_name": "AutomateTheBoringStuff.com",
        "source_link": "https://automatetheboringstuff.com",
        "description": "A free, practical book for writing Python scripts to automate real tasks.",
        "is_verified": True,
        "last_verified": "2026-03",
    },
    {
        "id": 5,
        "title": "Google Project Management Certificate",
        "topic": "project management",
        "activity_type": "Certificate",
        "cost": 49,
        "modality": "Online",
        "location": "Online (U.S.)",
        "audience": "University, Professional",
        "format": "Online Certificate Program",
        "tags": ["project management", "pmp", "leadership", "business", "google"],
        "source_name": "Coursera (Google)",
        "source_link": "https://www.coursera.org/professional-certificates/google-project-management",
        "description": "A 6-course certificate program from Google. No prior experience required.",
        "is_verified": True,
        "last_verified": "2026-03",
    },
    {
        "id": 6,
        "title": "IBM Data Science Professional Certificate",
        "topic": "data science",
        "activity_type": "Certificate",
        "cost": 49,
        "modality": "Online",
        "location": "Online (U.S.)",
        "audience": "University, Professional",
        "format": "Online Certificate Program",
        "tags": ["data science", "python", "machine learning", "sql", "ibm"],
        "source_name": "Coursera (IBM)",
        "source_link": "https://www.coursera.org/professional-certificates/ibm-data-science",
        "description": "10-course IBM certificate covering data science, Python, SQL, and ML.",
        "is_verified": True,
        "last_verified": "2026-02",
    },
    {
        "id": 7,
        "title": "Sacramento Python Users Group Monthly Meetup",
        "topic": "python",
        "activity_type": "Meetup",
        "cost": 0,
        "modality": "In-Person",
        "location": "Sacramento, CA",
        "audience": "High School, University, Professional",
        "format": "Local Meetup",
        "tags": ["python", "networking", "community", "programming", "meetup"],
        "source_name": "Meetup.com",
        "source_link": "https://www.meetup.com/sacramento-python-user-group/",
        "description": "A free local meetup for Python developers of all skill levels.",
        "is_verified": True,
        "last_verified": "2026-01",
    },
    {
        "id": 8,
        "title": "Women in Tech Los Angeles Networking Night",
        "topic": "networking",
        "activity_type": "Meetup",
        "cost": 0,
        "modality": "In-Person",
        "location": "Los Angeles, CA",
        "audience": "High School, University, Professional",
        "format": "Local Meetup",
        "tags": ["networking", "women in tech", "diversity", "community", "career"],
        "source_name": "Meetup.com",
        "source_link": "https://www.meetup.com/women-in-tech-los-angeles/",
        "description": "Monthly networking event for women and allies in the tech industry.",
        "is_verified": False,
        "last_verified": "2025-11",
    },
    {
        "id": 9,
        "title": "Intro to Cybersecurity Workshop",
        "topic": "cybersecurity",
        "activity_type": "Workshop",
        "cost": 25,
        "modality": "Online",
        "location": "Online (U.S.)",
        "audience": "High School, University",
        "format": "Live Online Workshop",
        "tags": ["cybersecurity", "security", "hacking", "networking", "tech"],
        "source_name": "SANS Cyber Aces",
        "source_link": "https://www.cyberaces.org/",
        "description": "Free and low-cost cybersecurity workshops designed for beginners.",
        "is_verified": True,
        "last_verified": "2026-02",
    },
    {
        "id": 10,
        "title": "Taproot Plus — Pro Bono Tech Consulting",
        "topic": "consulting",
        "activity_type": "Volunteering",
        "cost": 0,
        "modality": "Hybrid",
        "location": "Online (U.S.) + Select Cities",
        "audience": "University, Professional",
        "format": "Volunteer Project",
        "tags": ["volunteering", "consulting", "nonprofits", "project management", "leadership"],
        "source_name": "Taproot Foundation",
        "source_link": "https://taprootplus.org/",
        "description": "Match your professional skills with nonprofits that need pro bono help.",
        "is_verified": True,
        "last_verified": "2026-01",
    },
    {
        "id": 11,
        "title": "IEEE Student Membership",
        "topic": "engineering",
        "activity_type": "Professional Association",
        "cost": 32,
        "modality": "Hybrid",
        "location": "Online (U.S.) + Local Chapters",
        "audience": "High School, University",
        "format": "Professional Association",
        "tags": ["engineering", "electrical engineering", "networking", "research", "ieee"],
        "source_name": "IEEE",
        "source_link": "https://www.ieee.org/membership/students/index.html",
        "description": "Global tech professional organization with student rates, events, and publications.",
        "is_verified": True,
        "last_verified": "2026-03",
    },
    {
        "id": 12,
        "title": "AI Community of Practice — U.S. Digital Service",
        "topic": "artificial intelligence",
        "activity_type": "Community of Practice",
        "cost": 0,
        "modality": "Online",
        "location": "Online (U.S.)",
        "audience": "University, Professional",
        "format": "Online Community",
        "tags": ["ai", "artificial intelligence", "machine learning", "government", "community"],
        "source_name": "U.S. Digital Service / Digital.gov",
        "source_link": "https://digital.gov/communities/artificial-intelligence/",
        "description": "A U.S. government-affiliated community for AI practitioners and enthusiasts.",
        "is_verified": True,
        "last_verified": "2026-02",
    },
]

# Defines the strict data structures for incoming requests and outgoing API responses.
class SearchQuery(BaseModel):
    topic: str
    max_budget: int
    preferred_format: Optional[str] = None
    modality: Optional[str] = None
    activity_type: Optional[str] = None

class Recommendation(BaseModel):
    id: int
    title: str
    topic: str
    activity_type: str
    cost: int
    modality: str
    location: str
    audience: str
    format: str
    source_name: str
    source_link: str
    is_verified: bool
    last_verified: str
    data_confidence: str
    relevance_score: int
    explanation: str

class RecommendationResponse(BaseModel):
    query_topic: str
    query_budget: int
    results_found: int
    recommendations: List[Recommendation]

class CatalogItem(BaseModel):
    id: int
    title: str
    topic: str
    activity_type: str
    cost: int
    modality: str
    source_name: str
    source_link: str
    is_verified: bool

# Calculates a basic relevance score to rank search results based on topic, cost, and verification.
def calculate_relevance_score(item: dict, query: SearchQuery, search_topic: str) -> int:
    score = 0
    if search_topic == item["topic"].lower():
        score += 40
    else:
        score += 20
    if item["cost"] == 0:
        score += 25
    if item["is_verified"]:
        score += 20
    if query.preferred_format:
        if query.preferred_format.lower() in item["format"].lower():
            score += 15
    return score

# Generates a plain-English label explaining the trustworthiness and freshness of the data.
def get_data_confidence(item: dict) -> str:
    if item["is_verified"] and item["last_verified"] >= "2026":
        return "High — manually verified in 2026. Details are likely current."
    elif item["is_verified"]:
        return "Medium — verified in a prior period. Some details may have changed."
    else:
        return "Low — not recently verified. Please confirm details at the source link."

# Initializes the FastAPI application with metadata for the documentation.
app = FastAPI(
    title="ProLearning Recommendation API",
    description=(
        "A prototype API that recommends ProLearning opportunities "
        "(courses, workshops, meetups, volunteering, and more) "
        "based on topic, budget, modality, and activity type. "
        "Built for LearnHaus AI — Option B: Backend/API. "
        "Data is source-grounded with honesty about verification status."
    ),
    version="2.0.0",
)

# Provides a basic health check endpoint to confirm the API is running.
@app.get("/", summary="Health Check")
def read_root():
    return {
        "message": "ProLearning Recommendation API is live.",
        "version": "2.0.0",
        "docs": "Visit /docs to explore and test all endpoints.",
    }

# Returns a deduplicated list of all available topics and tags in the database.
@app.get("/topics", summary="List All Available Topics")
def get_topics():
    all_topics = set()
    all_tags = set()
    for item in LEARNING_DATABASE:
        all_topics.add(item["topic"])
        for tag in item["tags"]:
            all_tags.add(tag)
    return {
        "primary_topics": sorted(list(all_topics)),
        "searchable_tags": sorted(list(all_tags)),
        "tip": "You can search for any primary topic or any tag in the /recommendations endpoint.",
    }

# Allows users to browse the entire activity database with an optional filter for activity type.
@app.get("/catalog", response_model=List[CatalogItem], summary="Browse Full Activity Catalog")
def get_catalog(activity_type: Optional[str] = None):
    results = []
    for item in LEARNING_DATABASE:
        if activity_type:
            if activity_type.lower() not in item["activity_type"].lower():
                continue
        results.append(CatalogItem(
            id=item["id"],
            title=item["title"],
            topic=item["topic"],
            activity_type=item["activity_type"],
            cost=item["cost"],
            modality=item["modality"],
            source_name=item["source_name"],
            source_link=item["source_link"],
            is_verified=item["is_verified"],
        ))
    if not results:
        raise HTTPException(
            status_code=404,
            detail=f"No activities found with type '{activity_type}'. Try: Course, Meetup, Workshop, Volunteering, Certificate, Textbook.",
        )
    return results

# Processes user search queries, filters the database, ranks matches, and returns personalized recommendations.
@app.post("/recommendations", response_model=RecommendationResponse, summary="Get Personalized Recommendations")
def get_recommendations(query: SearchQuery) -> RecommendationResponse:
    search_topic = query.topic.lower().strip()
    matches = []

    for item in LEARNING_DATABASE:
        topic_matches = (
            search_topic in item["topic"].lower()
            or any(search_topic in tag.lower() for tag in item["tags"])
        )
        budget_matches = item["cost"] <= query.max_budget
        
        if query.modality:
            modality_matches = query.modality.lower() in item["modality"].lower()
        else:
            modality_matches = True

        if query.activity_type:
            type_matches = query.activity_type.lower() in item["activity_type"].lower()
        else:
            type_matches = True

        if query.preferred_format:
            format_matches = query.preferred_format.lower() in item["format"].lower()
        else:
            format_matches = True

        if topic_matches and budget_matches and modality_matches and type_matches and format_matches:
            score = calculate_relevance_score(item, query, search_topic)
            confidence = get_data_confidence(item)

            explanation = (
                f"Recommended because it matches your topic of '{query.topic}' "
                f"and fits your ${query.max_budget} budget "
                f"(this resource costs ${item['cost']})."
            )
            explanation += f" Available {item['modality'].lower()} — {item['location']}."
            explanation += f" Suitable for: {item['audience']}."
            if query.preferred_format and format_matches:
                explanation += f" Matches your preferred format: '{item['format']}'."
            if item["cost"] == 0:
                explanation += " Bonus: this resource is completely FREE!"
            if item["is_verified"]:
                explanation += f" Verified as of {item['last_verified']}."
            else:
                explanation += f" Not recently verified — please confirm details at the source."

            recommendation = Recommendation(
                id=item["id"],
                title=item["title"],
                topic=item["topic"],
                activity_type=item["activity_type"],
                cost=item["cost"],
                modality=item["modality"],
                location=item["location"],
                audience=item["audience"],
                format=item["format"],
                source_name=item["source_name"],
                source_link=item["source_link"],
                is_verified=item["is_verified"],
                last_verified=item["last_verified"],
                data_confidence=confidence,
                relevance_score=score,
                explanation=explanation,
            )
            matches.append(recommendation)

    matches.sort(key=lambda rec: rec.relevance_score, reverse=True)

    if len(matches) == 0:
        raise HTTPException(
            status_code=404,
            detail=(
                f"No ProLearning opportunities found for topic '{query.topic}' "
                f"within a ${query.max_budget} budget. "
                f"Try visiting /topics to see all searchable topics, "
                f"or try removing optional filters like modality or activity_type."
            ),
        )

    return RecommendationResponse(
        query_topic=query.topic,
        query_budget=query.max_budget,
        results_found=len(matches),
        recommendations=matches,
    )
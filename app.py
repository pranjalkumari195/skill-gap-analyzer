import streamlit as st
# Page Configuration

st.set_page_config(
    page_title="AI Skill Gap Analyzer",
    page_icon="🎯",
    layout="centered"
)

# Role → Skill Mapping (Updated & Industry-Aligned)

ROLE_SKILLS = {
    "Machine Learning Engineer": {
        "Python": "critical",
        "Statistics": "critical",
        "Data Preprocessing": "critical",
        "EDA": "important",
        "Machine Learning": "critical",
        "Model Evaluation": "important",
        "Model Deployment": "important"
    },
    "Data Analyst": {
        "Python": "critical",
        "SQL": "critical",
        "Statistics": "important",
        "EDA": "critical",
        "Data Visualization": "important"
    },
    "Backend Developer": {
        "Python": "critical",
        "Databases": "critical",
        "APIs": "critical",
        "Authentication": "important",
        "System Design": "important"
    }
}

# Learning Recommendations

RECOMMENDATIONS = {
    "Python": "Practice data structures, functions, OOP, and real-world projects",
    "Statistics": "Revise probability, distributions, hypothesis testing",
    "Data Preprocessing": "Work on missing values, encoding, scaling techniques",
    "EDA": "Practice data visualization and pattern discovery",
    "Machine Learning": "Implement ML models using scikit-learn",
    "Model Evaluation": "Learn metrics like accuracy, precision, recall, RMSE",
    "Model Deployment": "Learn Streamlit, Flask, and basic cloud deployment",
    "SQL": "Practice joins, subqueries, window functions",
    "Data Visualization": "Build dashboards using Streamlit or Power BI",
    "Databases": "Learn schema design and indexing",
    "APIs": "Build REST APIs using FastAPI or Flask",
    "Authentication": "Understand JWT, OAuth basics",
    "System Design": "Learn scalability, caching, load balancing"
}

# App Title

st.title(" AI Skill Gap Analyzer")
st.caption("Evaluate your skills • Identify gaps • Get a personalized roadmap")

st.markdown("---")

# STEP 1: Role & Skill Selection

st.header("  Select Target Role & Skills")

target_role = st.selectbox(
    "Choose your target job role",
    list(ROLE_SKILLS.keys())
)

all_skills = list(ROLE_SKILLS[target_role].keys())

selected_skills = st.multiselect(
    "Select skills to evaluate",
    all_skills,
    default=all_skills
)

st.markdown("---")

# STEP 2: Interactive Skill Assessment

st.header(" Skill Assessment")

score_map = {
    "No knowledge": 0,
    "Basic understanding": 1,
    "Can apply practically": 2,
    "Advanced / real-world experience": 3
}

skill_scores = {}

for skill in selected_skills:
    st.subheader(skill)

    response = st.radio(
        f"Your level in {skill}:",
        list(score_map.keys()),
        key=skill
    )

    skill_scores[skill] = score_map[response]

st.markdown("---")


# STEP 3: Skill Proficiency Overview (Modern UI)

st.header(" Skill Proficiency Overview")

for skill, score in skill_scores.items():
    percent = int((score / 3) * 100)

    if score >= 2:
        label = "🟢 Strong"
    elif score == 1:
        label = "🟡 Needs Improvement"
    else:
        label = "🔴 Critical Gap"

    st.markdown(f"**{skill}** — {label}")
    st.progress(percent)

st.markdown("---")

# STEP 4: Skill Gap Analysis

st.header(" Skill Gap Analysis")

strengths = []
gaps = []
high_priority = []

for skill, score in skill_scores.items():
    importance = ROLE_SKILLS[target_role][skill]

    if score >= 2:
        strengths.append(skill)
    else:
        gaps.append(skill)
        if importance == "critical":
            high_priority.append(skill)

col1, col2 = st.columns(2)

with col1:
    st.subheader(" Strengths")
    if strengths:
        for s in strengths:
            st.success(s)
    else:
        st.info("No strong skills yet")

with col2:
    st.subheader(" Skill Gaps")
    if gaps:
        for g in gaps:
            st.error(g)
    else:
        st.success("No major gaps")

st.markdown("---")

# STEP 5: High Priority Focus

st.header(" High Priority Focus Areas")

if high_priority:
    for hp in high_priority:
        st.warning(f"{hp} (Critical for {target_role})")
else:
    st.success("You are strong in all critical skills ")

st.markdown("---")

# STEP 6: Personalized Learning Roadmap

st.header(" Personalized Learning Roadmap")

if gaps:
    for skill in gaps:
        if skill in RECOMMENDATIONS:
            st.markdown(
                f"""
                 **{skill}**  
                 {RECOMMENDATIONS[skill]}
                """
            )
else:
    st.success("You are job-ready! Focus on advanced projects.")

st.markdown("---")

# STEP 7: Career Readiness Score

st.header(" Career Readiness Score")

readiness_score = int(
    (sum(skill_scores.values()) / (len(skill_scores) * 3)) * 100
)

st.metric(
    label="Overall Readiness",
    value=f"{readiness_score}%",
    delta="Industry Aligned"
)

if readiness_score >= 75:
    st.success("You are close to being job-ready!")
elif readiness_score >= 50:
    st.warning("You are on the right path. Strengthen weak areas.")
else:
    st.error("Focused upskilling is required.")

st.caption("📌 This report dynamically adapts as your skills improve.")

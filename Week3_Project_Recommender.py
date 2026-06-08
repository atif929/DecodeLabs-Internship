from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


# Job roles and their associated skills
JOB_ROLES = [
    {
        "title": "Data Scientist",
        "tags": "python sql machine learning data analysis statistics numpy pandas "
                "scikit-learn tensorflow keras deep learning visualization jupyter "
                "data structures algorithms probability modeling regression classification"
    },
    {
        "title": "Machine Learning Engineer",
        "tags": "python machine learning deep learning tensorflow pytorch scikit-learn "
                "model deployment mlops docker kubernetes cloud apis data pipelines "
                "feature engineering neural networks optimization algorithms cuda"
    },
    {
        "title": "Data Engineer",
        "tags": "python sql spark hadoop etl data pipelines kafka airflow cloud aws "
                "azure gcp databases postgresql mongodb data warehousing big data "
                "data structures scala java linux bash automation"
    },
    {
        "title": "Backend Developer",
        "tags": "python java node javascript sql rest apis docker databases postgresql "
                "mongodb microservices git linux server authentication cloud aws "
                "data structures algorithms software development backend frameworks"
    },
    {
        "title": "Frontend Developer",
        "tags": "javascript html css react angular vue node typescript git "
                "responsive design ui ux rest apis web development frontend "
                "redux webpack figma accessibility browser optimization"
    },
    {
        "title": "Full Stack Developer",
        "tags": "python javascript html css react node sql rest apis docker git "
                "databases mongodb postgresql cloud aws linux backend frontend "
                "microservices authentication software development deployment"
    },
    {
        "title": "DevOps Engineer",
        "tags": "docker kubernetes linux bash aws azure gcp ci cd jenkins git "
                "automation terraform ansible monitoring cloud infrastructure "
                "networking security pipelines scripting python yaml deployment"
    },
    {
        "title": "Cloud Architect",
        "tags": "aws azure gcp cloud infrastructure docker kubernetes terraform "
                "networking security automation python linux monitoring cost "
                "optimization scalability microservices databases serverless"
    },
    {
        "title": "Cybersecurity Analyst",
        "tags": "networking security linux python penetration testing firewalls "
                "cryptography authentication risk assessment vulnerability "
                "cloud security monitoring incident response bash scripting"
    },
    {
        "title": "AI Research Engineer",
        "tags": "python machine learning deep learning pytorch tensorflow research "
                "mathematics statistics optimization neural networks nlp computer vision "
                "cuda gpu algorithms data analysis scientific computing papers"
    },
    {
        "title": "NLP Engineer",
        "tags": "python nlp natural language processing transformers huggingface "
                "machine learning deep learning text classification sentiment analysis "
                "bert gpt tokenization linguistics data analysis tensorflow pytorch"
    },
    {
        "title": "Computer Vision Engineer",
        "tags": "python computer vision opencv deep learning tensorflow pytorch "
                "image processing convolutional neural networks object detection "
                "cuda gpu data augmentation machine learning classification"
    },
    {
        "title": "Android Developer",
        "tags": "java kotlin android mobile development xml rest apis git "
                "databases sqlite firebase ui ux agile software development "
                "android studio sdk testing deployment google play"
    },
    {
        "title": "iOS Developer",
        "tags": "swift objective c ios mobile development xcode rest apis git "
                "databases core data firebase ui ux agile software development "
                "testing deployment app store apple sdk"
    },
    {
        "title": "Blockchain Developer",
        "tags": "solidity ethereum blockchain javascript python web3 smart contracts "
                "cryptography security databases decentralized applications git "
                "node react algorithms data structures"
    },
    {
        "title": "Database Administrator",
        "tags": "sql postgresql mysql mongodb databases data management python "
                "linux bash backup recovery performance optimization cloud aws "
                "data warehousing etl security replication clustering"
    },
    {
        "title": "System Administrator",
        "tags": "linux bash windows networking servers automation python scripting "
                "docker security monitoring cloud aws azure storage backups "
                "active directory virtualization troubleshooting"
    },
    {
        "title": "QA / Test Engineer",
        "tags": "python javascript testing selenium automation junit git ci cd "
                "performance testing security testing rest apis agile databases "
                "bug tracking documentation software development quality"
    },
]


def get_user_profile():
    """Collect user skills."""

    print("=" * 50)
    print("Tech Stack Career Recommender")
    print("=" * 50)

    print("\nEnter your skills one by one.")
    print("Type 'done' when finished (minimum 3 skills).\n")

    skills = []

    while True:
        skill = input(f"Skill {len(skills) + 1}: ").strip().lower()

        if skill == "done":
            if len(skills) < 3:
                print(f"Please enter at least 3 skills. ({len(skills)} entered)\n")
                continue
            break

        if not skill:
            print("Skill cannot be empty.\n")
            continue

        if skill in skills:
            print("Skill already added.\n")
            continue

        skills.append(skill)

    print("\nYour Skills:", skills)

    return " ".join(skills), skills


def build_tfidf_matrix(job_roles):
    """Create TF-IDF vectors for all job roles."""

    corpus = [role["tags"] for role in job_roles]

    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 1),
        max_features=500
    )

    tfidf_matrix = vectorizer.fit_transform(corpus)

    return vectorizer, tfidf_matrix


def score_and_rank(user_profile, vectorizer, tfidf_matrix, job_roles, top_n=3):
    """Calculate similarity scores and return top matches."""

    user_vector = vectorizer.transform([user_profile])

    scores = cosine_similarity(user_vector, tfidf_matrix).flatten()

    ranked_indices = np.argsort(scores)[::-1]

    results = []

    for idx in ranked_indices[:top_n]:
        results.append({
            "rank": len(results) + 1,
            "title": job_roles[idx]["title"],
            "score": round(float(scores[idx]), 4)
        })

    return results


def display_recommendations(results, user_skills):
    """Display recommendation results."""

    print("\n" + "=" * 50)
    print("Recommended Career Paths")
    print("=" * 50)

    print(f"\nSkills: {user_skills}\n")

    if not results or results[0]["score"] == 0:
        print("No matching roles found.")
        print("\nSuggested roles:")
        print("1. Data Scientist")
        print("2. Full Stack Developer")
        print("3. DevOps Engineer")
        return

    for result in results:
        percentage = int(result["score"] * 100)

        print(f"{result['rank']}. {result['title']}")
        print(f"   Match Score: {result['score']:.4f} ({percentage}%)")
        print()

    top_role = results[0]

    print("-" * 50)
    print(f"Best Match: {top_role['title']}")
    print(f"Similarity Score: {top_role['score']:.4f}")

    if len(results) > 1:
        print(f"Second Choice: {results[1]['title']}")

    if len(results) > 2:
        print(f"Third Choice: {results[2]['title']}")


def demo_mode():
    """Run recommendations for sample users."""

    print("=" * 50)
    print("Demo Mode")
    print("=" * 50)

    vectorizer, tfidf_matrix = build_tfidf_matrix(JOB_ROLES)

    sample_users = [
        {
            "name": "Data Enthusiast",
            "skills": [
                "python",
                "machine learning",
                "sql",
                "statistics",
                "tensorflow"
            ]
        },
        {
            "name": "Cloud Engineer",
            "skills": [
                "docker",
                "kubernetes",
                "aws",
                "linux",
                "automation",
                "terraform"
            ]
        },
        {
            "name": "Web Developer",
            "skills": [
                "javascript",
                "react",
                "html",
                "css",
                "node",
                "rest apis"
            ]
        }
    ]

    for user in sample_users:

        profile = " ".join(user["skills"])

        results = score_and_rank(
            profile,
            vectorizer,
            tfidf_matrix,
            JOB_ROLES
        )

        print(f"\n{user['name']}")
        print("Skills:", user["skills"])

        for result in results:
            print(
                f"{result['rank']}. "
                f"{result['title']} "
                f"({result['score']:.4f})"
            )

        print("-" * 50)


if __name__ == "__main__":
    import sys

    vectorizer, tfidf_matrix = build_tfidf_matrix(JOB_ROLES)

    if len(sys.argv) > 1 and sys.argv[1] == "demo":
        demo_mode()
    else:
        user_profile, user_skills = get_user_profile()

        results = score_and_rank(
            user_profile,
            vectorizer,
            tfidf_matrix,
            JOB_ROLES,
            top_n=3
        )

        display_recommendations(results, user_skills)
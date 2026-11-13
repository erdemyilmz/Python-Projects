import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

retriever = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

data = pd.read_csv("tickets.csv")

example_tickets = data["example_ticket"].tolist()
ticket_embeddings = retriever.encode(example_tickets)

while True:
    user_question = input("\nWhat is your problem: ").strip()

    if user_question.lower() == "exit":
        break

    if not user_question:
        continue

    user_embedding = retriever.encode([user_question])

    scores = cosine_similarity(user_embedding, ticket_embeddings)[0]
    best_index = scores.argmax()
    best_score = scores[best_index]

    if best_score < 0.45:
        print("No relevant team found.")
        print(f"Best similarity: {best_score:.3f}")
        continue

    row = data.iloc[best_index]

    print(f"Team: {row['team']}")
    print(f"Matched example: {row['example_ticket']}")
    print(f"Similarity: {best_score:.3f}")
    print(f"Reply: {row['reply']}")
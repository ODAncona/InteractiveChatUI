from exa_py import Exa
from dotenv import load_dotenv
import os
import joblib


search_schema = {
    "type": "object",
    "properties": {
        "country": {"type": "string"},
        "policy_name": {"type": "string"},
        "year": {"type": "integer"},
        "goals": {"type": "array", "items": {"type": "string"}},
        "key_measures": {
            "type": "array",
            "items": {"type": "string"},
        },
    },
}


def main():
    exa = Exa(api_key=exa_api_key)
    result = exa.search_and_contents(
        "news article about a specific climate change policy implemented by a G20 country",
        type="auto",
        category="news",
        num_results=10,
        start_published_date="2020-01-01T08:00:00.000Z",
        text={"max_characters": 500},
        summary={
            "query": "What are the main policies implemented?",
            "schema": {
                "type": "object",
                "properties": {
                    "country": {"type": "string"},
                    "policy_name": {"type": "string"},
                    "year": {"type": "integer"},
                    "goals": {"type": "array", "items": {"type": "string"}},
                    "key_measures": {
                        "type": "array",
                        "items": {"type": "string"},
                    },
                },
            },
        },
    )
    joblib.dump(result, "result.joblib")


if __name__ == "__main__":
    load_dotenv()
    exa_api_key = os.getenv("EXA_API_KEY")
    main()

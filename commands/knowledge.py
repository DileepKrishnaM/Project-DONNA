# commands/knowledge.py
import wikipedia

def get_summary(query: str):
    try:
        result = wikipedia.summary(query, sentences=2)
        return result
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Your query is ambiguous. Did you mean {e.options[0]}?"
    except wikipedia.exceptions.PageError:
        return "I could not find information on that topic."
    except Exception:
        return "Sorry, I couldn't fetch the information."

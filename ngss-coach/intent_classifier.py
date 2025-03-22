import re

def classify_intent(query):
    query = query.lower()

    if re.search(r'\b(ls[1-4]\.[a-d])\b', query):  # e.g., LS2.C
        return "find_lessons_by_dci"
    if "phenomenon" in query or "real-world example" in query:
        return "find_lessons_by_phenomenon"
    if "sep" in query or "science practice" in query:
        return "identify_seps"
    if "model" in query and "students" in query:
        return "modeling_support"
    if "assessment" in query or "how is this assessed" in query:
        return "assessment_identification"
    
    return "general_support"

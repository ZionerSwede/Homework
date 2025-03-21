import json

data = {
    "questions": [
        {
            "question": "Vad är den främsta energikällan för jorden?",
            "options": ["Månen", "Solen", "Stjärnorna", "Vinden"],
            "answer": "Solen"
        },
        {
            "question": "Vilken form av energi lagras i mat?",
            "options": ["Rörelseenergi", "Värmeenergi", "Kemisk energi", "Kärnenergi"],
            "answer": "Kemisk energi"
        },
        {
            "question": "Vilken typ av energi har en bil som rör sig?",
            "options": ["Lägesenergi", "Rörelseenergi", "Värmeenergi", "Ljudenergi"],
            "answer": "Rörelseenergi"
        },
        {
            "question": "Vilken enhet används för att mäta energi?",
            "options": ["Meter", "Kilogram", "Joule", "Liter"],
            "answer": "Joule"
        },
        {
            "question": "Vilken typ av energi används för att driva en ficklampa?",
            "options": ["Värmeenergi", "Kemisk energi", "Kärnenergi", "Ljudenergi"],
            "answer": "Kemisk energi"
        },
        {
            "question": "Vilken typ av energi produceras genom att bränna fossila bränslen?",
            "options": ["Kärnenergi", "Kemisk energi", "Värmeenergi", "Ljudenergi"],
            "answer": "Värmeenergi"
        },
        {
            "question": "Vilken typ av energi lagras i ett utsträckt gummiband?",
            "options": ["Rörelseenergi", "Värmeenergi", "Lägesenergi", "Ljudenergi"],
            "answer": "Lägesenergi"
        },
        {
            "question": "Vilken form av energi används för att laga mat i en mikrovågsugn?",
            "options": ["Värmeenergi", "Kemisk energi", "Elektrisk energi", "Strålningsenergi"],
            "answer": "Strålningsenergi"
        },
        {
            "question": "Vilken typ av energi används för att driva en cykel som åker nerför en backe?",
            "options": ["Lägesenergi", "Rörelseenergi", "Värmeenergi", "Ljudenergi"],
            "answer": "Rörelseenergi"
        }
    ]
}

with open("questions.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
import random
import json
import time


def load_questions():
    with open("questions.json", "r", encoding="utf-8") as f:
        questions = json.load(f)["questions"]
    return questions

def load_results():
    try:
        with open("results.json", "r", encoding="utf-8") as f:
            results = json.load(f)["results"]
    except FileNotFoundError:
        results = []
    return results

def save_results(results):
    with open("results.json", "w", encoding="utf-8") as f:
        json.dump({"results": results}, f, ensure_ascii=False, indent=4)

def get_random_questions(questions, num_questions):
    if num_questions > len(questions):
        num_questions = len(questions)
    random_questions = random.sample(questions, num_questions)
    return random_questions

def ask_question(question):
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(str(i + 1) + ".", option)
    number = int(input("Välj rätt nummer: "))
    if number < 1 or number > len(question["options"]):
        print("Ogiltigt val, standard till fel svar.")
        return False
    correct = question["options"][number - 1] == question["answer"]
    return correct

def show_results(results):
    print("\nTidigare resultat:")
    for result in results:
        print(f"{result['person']}, Bästa poäng: {result['correct_answers']}, Bästa tid: {result['best_time']} sekunder")

def search_name(results, person_name):
    for result in results:
        if result["person"].lower() == person_name.lower():
            return result
    return None

questions = load_questions()
results = load_results()

person_name = input("Ange ditt namn: ").lower()
person_result = search_name(results, person_name)

if person_result:
    print(f"Välkommen tillbaka, {person_name}! Ditt bästa resultat är {person_result['correct_answers']} och din bästa tid är {person_result['best_time']} sekunder.")
else:
    print(f"Välkommen, {person_name}! Det här verkar vara din första gång.")

total_questions = int(input("Ange antalet frågor: "))
random_questions = get_random_questions(questions, total_questions)
correct = 0
start_time = time.time()

for question in random_questions:
    is_correct = ask_question(question)
    if is_correct:
        correct += 1
    else:
        print("Fel svar!, det korrekta svaret är: ", question["answer"])
    print("-----------------")

completed_time = time.time() - start_time
score = round((correct / total_questions) * 100, 2)

print("Sammanfattning")
print("Totalt antal frågor:", total_questions)
print("Rätt svar:", correct)
print("Poäng:", str(score) + "%")
print("Tid:", round(completed_time, 2), "sekunder")

if score == 100:
    print("Grattis! Du fick full poäng!")
    if person_result:
        if correct > person_result["correct_answers"]:
            print("Du slog ditt tidigare rekord!")
            person_result["correct_answers"] = correct
            person_result["best_time"] = round(completed_time, 2)
            save_results(results)
    elif not person_result:
        print("Du fick ditt första rekord!")
        results.append({
        "person": person_name,
        "correct_answers": correct,
        "best_time": round(completed_time, 2)
        })
        save_results(results)    
else:
    print("Bättre lycka nästa gång!")



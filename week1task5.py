events = {
    "Night of Museums Dortmund": "19 September 2026",
    "Dortmund Autumn Festival": "20 September 2026",
    "Dortmund Concert": "19 September 2026",
    "City Art Exhibition": "18 September 2026",
    "Food Festival Dortmund": "21 September 2026"
}


date = "19 September 2026"

print("Events running during Night of Museums in Dortmund:")
print()

for event, event_date in events.items():
    if event_date == date:
        print(event)
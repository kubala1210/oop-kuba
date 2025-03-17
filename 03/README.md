> :white_check_mark: *Jeśli będziesz mieć problem z rozwiązaniem tego zadania, poproś o pomoc na odpowiednim kanale na Slacku, tj. `s8e02-python-basics` (dotyczy [mentee](https://devmentor.pl/mentoring-javascript/)) lub na ogólnodostępnej i bezpłatnej [społeczności na Discordzie](https://devmentor.pl/discord). Pamiętaj, aby treść Twojego wpisu spełniała [odpowiednie kryteria](https://devmentor.pl/jak-prosic-o-pomoc/).*

&nbsp;

# `#03` Python: Podstawy


## Magiczne metody – Reprezentacja obiektu użytkownika

Twoim zadaniem jest **nadpisać metodę `__str__`**, aby obiekt klasy `User` był czytelnie reprezentowany w postaci tekstowej.  

📌 **Instrukcja:**  
1. Otwórz plik `user_management.py` i edytuj wcześniej stworzoną klasę `User`.  
2. Dodaj metodę `__str__`, aby `print(user)` zwracało:  
   ```
   "Profil użytkownika: {username} ({email})"
   ```  
3. Przetestuj działanie `print(user1)` i `print(user2)`.  

> **⭐ Podpowiedź:** Metoda `__str__` powinna zwracać wartość (`return`), a nie ją wypisywać (`print`).  

📌 **Przykładowe wywołanie:**  
```python
print(user1)  # Oczekiwany wynik: "Profil użytkownika: jan_kowalski (jan@example.com)"
print(user2)  # Oczekiwany wynik: "Profil użytkownika: anna_nowak (anna@example.com)"
```  


&nbsp;
> :no_entry: *Jeśli nie posiadasz materiałów do tego zadania tj. **PDF, projekt + Code Review**, znajdziesz je na stronie [devmentor.pl](https://devmentor.pl/workshop-python-basics)*

> :arrow_left: [*poprzednie zadanie*](./../02) | [*następne zadanie*](./../04) :arrow_right:

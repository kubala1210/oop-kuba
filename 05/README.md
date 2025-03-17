> :white_check_mark: *Jeśli będziesz mieć problem z rozwiązaniem tego zadania, poproś o pomoc na odpowiednim kanale na Slacku, tj. `s8e03-python-oop` (dotyczy [mentee](https://devmentor.pl/mentoring-javascript/)) lub na ogólnodostępnej i bezpłatnej [społeczności na Discordzie](https://devmentor.pl/discord). Pamiętaj, aby treść Twojego wpisu spełniała [odpowiednie kryteria](https://devmentor.pl/jak-prosic-o-pomoc/).*

&nbsp;

# `#05` Python: Programowanie obiektowe

## Polimorfizm – Logowanie użytkowników 

Twoim zadaniem jest **nadpisać metodę `login()`**, aby różne typy użytkowników miały odmienne komunikaty logowania.  

📌 **Instrukcja:**  
1. Otwórz plik `user_management.py` i edytuj klasy `User` oraz `Admin`.  
2. Dodaj metodę `login()` do klasy `User`, która zwróci tekst:  
   ```
   "Zalogowano użytkownika: {username}"
   ```  
3. Nadpisz metodę `login()` w klasie `Admin`, aby zwracała:  
   ```
   "Zalogowano administratora: {username}"
   ```  
4. Napisz funkcję `authenticate_user(user)`, która przyjmie obiekt i wywoła jego metodę `login()`.  

> **⭐ Podpowiedź:** Upewnij się, że `authenticate_user()` działa zarówno dla `User`, jak i `Admin`.  

📌 **Przykładowe wywołanie:**  
```python
user1 = User("jan_kowalski", "jan@example.com")
admin1 = Admin("superadmin", "admin@example.com", ["manage_users"])

print(authenticate_user(user1))  # Oczekiwany wynik: "Zalogowano użytkownika: jan_kowalski"
print(authenticate_user(admin1))  # Oczekiwany wynik: "Zalogowano administratora: superadmin"
```  


&nbsp;
> :no_entry: *Jeśli nie posiadasz materiałów do tego zadania tj. **PDF, projekt + Code Review**, znajdziesz je na stronie [devmentor.pl](https://devmentor.pl/workshop-python-oop)*

> :arrow_left: [*poprzednie zadanie*](./../04) | [*następne zadanie*](./../06) :arrow_right:

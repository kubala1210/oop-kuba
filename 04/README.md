> :white_check_mark: *Jeśli będziesz mieć problem z rozwiązaniem tego zadania, poproś o pomoc na odpowiednim kanale na Slacku, tj. `s8e03-python-oop` (dotyczy [mentee](https://devmentor.pl/mentoring-javascript/)) lub na ogólnodostępnej i bezpłatnej [społeczności na Discordzie](https://devmentor.pl/discord). Pamiętaj, aby treść Twojego wpisu spełniała [odpowiednie kryteria](https://devmentor.pl/jak-prosic-o-pomoc/).*

&nbsp;

# `#04` Python: Programowanie obiektowe

## Dziedziczenie – System ról użytkowników

Twoim zadaniem jest **stworzenie klasy `Admin`**, która dziedziczy po klasie `User` i dodaje dodatkową funkcjonalność.  

📌 **Instrukcja:**  
1. Otwórz plik `user_management.py` i edytuj wcześniej stworzoną klasę `User`.  
2. Stwórz nową klasę `Admin`, która dziedziczy po `User`.  
3. Dodaj do klasy `Admin` nowy atrybut `permissions`, który będzie przechowywał listę uprawnień administratora.  
4. Utwórz obiekt `Admin`, przypisz mu nazwę użytkownika, e-mail oraz listę uprawnień.  
5. Wypisz dane administratora oraz jego uprawnienia.  

> **⭐ Podpowiedź:** Użyj `super().__init__()`, aby nie powielać kodu konstruktora z klasy `User`.  

📌 **Przykładowe wywołanie:**  
```python
admin1 = Admin("superadmin", "admin@example.com", ["manage_users", "delete_posts", "ban_users"])

print(admin1.get_info())  
# Oczekiwany wynik: "Użytkownik: superadmin, e-mail: admin@example.com"

print(admin1.permissions)  
# Oczekiwany wynik: ["manage_users", "delete_posts", "ban_users"]
```  


&nbsp;

> :no_entry: *Jeśli nie posiadasz materiałów do tego zadania tj. **PDF, projekt + Code Review**, znajdziesz je na stronie [devmentor.pl](https://devmentor.pl/workshop-python-oop)*

> :arrow_left: [*poprzednie zadanie*](./../03) | [*następne zadanie*](./../05) :arrow_right:

> :white_check_mark: *Jeśli będziesz mieć problem z rozwiązaniem tego zadania, poproś o pomoc na odpowiednim kanale na Slacku, tj. `s8e03-python-oop` (dotyczy [mentee](https://devmentor.pl/mentoring/)) lub na ogólnodostępnej i bezpłatnej [społeczności na Discordzie](https://devmentor.pl/discord). Pamiętaj, aby treść Twojego wpisu spełniała [odpowiednie kryteria](https://devmentor.pl/jak-prosic-o-pomoc/).*

&nbsp;

# `#01` Python: Programowanie obiektowe


## Klasy i obiekty – System zarządzania użytkownikami  

Twoim zadaniem jest **stworzenie klasy**, która będzie reprezentowała użytkownika systemu.  

📌 **Instrukcja:**  
1. Stwórz nowy plik `user_management.py`.  
2. Zdefiniuj klasę `User` z dwoma atrybutami:  
   - `username` (nazwa użytkownika),  
   - `email` (adres e-mail).  
3. Utwórz dwa obiekty klasy `User` z różnymi danymi i wypisz ich atrybuty.  

> **⭐ Podpowiedź:** Pamiętaj, że obiekty klasy `User` powinny być tworzone za pomocą konstruktora `__init__()`.  

📌 **Przykładowe wywołanie:**  
```python
user1 = User("jan_kowalski", "jan@example.com")
user2 = User("anna_nowak", "anna@example.com")

print(user1.username, user1.email)  # Oczekiwany wynik: jan_kowalski jan@example.com
print(user2.username, user2.email)  # Oczekiwany wynik: anna_nowak anna@example.com
```  


&nbsp;
> :no_entry: *Jeśli nie posiadasz materiałów do tego zadania tj. **PDF, projekt + Code Review**, znajdziesz je na stronie [devmentor.pl](https://devmentor.pl/workshop-python-oop)*

> :arrow_left: ~~*poprzednie zadanie*~~ | [*następne zadanie*](./../02) :arrow_right:

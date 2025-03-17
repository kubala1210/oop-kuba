> :white_check_mark: *Jeśli będziesz mieć problem z rozwiązaniem tego zadania, poproś o pomoc na odpowiednim kanale na Slacku, tj. `s8e03-python-oop` (dotyczy [mentee](https://devmentor.pl/mentoring-javascript/)) lub na ogólnodostępnej i bezpłatnej [społeczności na Discordzie](https://devmentor.pl/discord). Pamiętaj, aby treść Twojego wpisu spełniała [odpowiednie kryteria](https://devmentor.pl/jak-prosic-o-pomoc/).*

&nbsp;

# `#05` Python: Programowanie obiektowe

## Enkapsulacja – Bezpieczne przechowywanie hasła 

Twoim zadaniem jest **zabezpieczenie danych użytkownika**, poprzez ukrycie jego hasła i umożliwienie jego zmiany oraz weryfikacji.  

📌 **Instrukcja:**  
1. Otwórz plik `user_management.py` i edytuj klasę `User`.  
2. Dodaj prywatny atrybut `__password`, który będzie przechowywał hasło użytkownika.  
3. Dodaj metodę `set_password(new_password)`, która pozwoli ustawić nowe hasło.  
4. Dodaj metodę `authenticate(password)`, która sprawdzi poprawność podanego hasła i zwróci `True` lub `False`.  
5. Przetestuj, czy użytkownik może poprawnie ustawić i zweryfikować hasło.  

> **⭐ Podpowiedź:** Pamiętaj, że prywatne atrybuty (`__password`) są dostępne tylko wewnątrz klasy.  

📌 **Przykładowe wywołanie:**  
```python
user1 = User("jan_kowalski", "jan@example.com")
user1.set_password("mojeBezpieczneHaslo")

print(user1.authenticate("zleHaslo"))  # Oczekiwany wynik: False
print(user1.authenticate("mojeBezpieczneHaslo"))  # Oczekiwany wynik: True
```  


&nbsp;
> :no_entry: *Jeśli nie posiadasz materiałów do tego zadania tj. **PDF, projekt + Code Review**, znajdziesz je na stronie [devmentor.pl](https://devmentor.pl/workshop-python-oop)*

> :arrow_left: [*poprzednie zadanie*](./../05) | ~~*następne zadanie*~~ :arrow_right:

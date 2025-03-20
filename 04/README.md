> :white_check_mark: *Jeśli będziesz mieć problem z rozwiązaniem tego zadania, poproś o pomoc na odpowiednim kanale na Slacku, tj. `s8e03-python-oop` (dotyczy [mentee](https://devmentor.pl/mentoring-javascript/)) lub na ogólnodostępnej i bezpłatnej [społeczności na Discordzie](https://devmentor.pl/discord). Pamiętaj, aby treść Twojego wpisu spełniała [odpowiednie kryteria](https://devmentor.pl/jak-prosic-o-pomoc/).*

&nbsp;

# `#04` Python: Programowanie obiektowe

Twoim zadaniem jest stworzenie **klasy `Animal`**, reprezentującej ogólne zwierzę, oraz **klas `Dog` i `Cat`**, które będą dziedziczyć po `Animal`. Każde zwierzę powinno mieć metodę `make_sound()`, ale jej implementacja powinna zależeć od konkretnej klasy (**polimorfizm**).


### ✅ Wymagania

1. **Zdefiniuj klasę `Animal`**, która będzie posiadać:
   - `name` – imię zwierzęcia.

2. **Zaimplementuj metodę `make_sound(self)` w `Animal`**, która zwróci:
   ```
   Zwierzę wydaje dźwięk.
   ```

3. **Zdefiniuj klasy `Dog` i `Cat`, które dziedziczą po `Animal`**, ale każda nadpisuje metodę `make_sound()`:
   - `Dog` powinien zwrócić:
     ```
     Burek szczeka: Hau! Hau!
     ```
   - `Cat` powinien zwrócić:
     ```
     Mruczek miauczy: Miau! Miau!
     ```

4. **Stwórz listę zwierząt zawierającą zarówno psy, jak i koty, a następnie iteruj po niej, wywołując metodę `make_sound()`**.


### 💡 Podpowiedzi
- **Polimorfizm** oznacza, że możemy wywołać `make_sound()` dla każdego obiektu `Animal`, niezależnie od tego, czy to `Dog`, `Cat`, czy inna klasa.
- **Wszystkie klasy utwórz w pliku `app.py`**.
- Możesz dodać dodatkową klasę, np. `Bird`, która również nadpisuje `make_sound()`.
- Przykładowe użycie:
  ```python
  animals = [Dog("Burek"), Cat("Mruczek"), Dog("Reksio")]
  
  for animal in animals:
      print(animal.make_sound())
  ```


&nbsp;

> :no_entry: *Jeśli nie posiadasz materiałów do tego zadania tj. **PDF, projekt + Code Review**, znajdziesz je na stronie [devmentor.pl](https://devmentor.pl/workshop-python-oop)*

> :arrow_left: [*poprzednie zadanie*](./../03) | [*następne zadanie*](./../05) :arrow_right:

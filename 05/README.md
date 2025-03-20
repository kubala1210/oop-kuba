> :white_check_mark: *Jeśli będziesz mieć problem z rozwiązaniem tego zadania, poproś o pomoc na odpowiednim kanale na Slacku, tj. `s8e03-python-oop` (dotyczy [mentee](https://devmentor.pl/mentoring-javascript/)) lub na ogólnodostępnej i bezpłatnej [społeczności na Discordzie](https://devmentor.pl/discord). Pamiętaj, aby treść Twojego wpisu spełniała [odpowiednie kryteria](https://devmentor.pl/jak-prosic-o-pomoc/).*

&nbsp;

# `#05` Python: Programowanie obiektowe

Twoim zadaniem jest stworzenie **klasy `BankAccount`**, która będzie reprezentować konto bankowe. Klasa ta powinna wykorzystywać **enkapsulację**, aby chronić saldo konta przed bezpośrednią modyfikacją.

### ✅ Wymagania

1. **Zdefiniuj klasę `BankAccount`**, która będzie posiadać:
   - `owner` – nazwisko właściciela konta,
   - `__balance` – prywatny atrybut przechowujący saldo konta (nie powinien być dostępny bezpośrednio).

2. **Zaimplementuj metodę `deposit(self, amount)`**, która pozwoli na wpłatę środków, ale tylko jeśli kwota jest dodatnia.

3. **Zaimplementuj metodę `withdraw(self, amount)`**, która pozwoli na wypłatę środków, ale tylko jeśli na koncie jest wystarczająca ilość pieniędzy.

4. **Zaimplementuj metodę `get_balance(self)`, która zwróci aktualne saldo konta**.

5. **Stwórz obiekt `BankAccount`, wykonaj kilka operacji wpłat i wypłat, a następnie sprawdź saldo**.


### 💡 Podpowiedzi
- Atrybut `__balance` powinien być **prywatny**, co oznacza, że nie można go odczytać bezpośrednio.
- **Użyj metod `deposit()` i `withdraw()`**, aby zapewnić kontrolę nad operacjami finansowymi.
- **Nie pozwól na wpłatę ujemnej kwoty ani na wypłatę większej niż dostępne saldo**.
- Przykładowe użycie:
  ```python
  account = BankAccount("Jan Kowalski", 1000)

  account.deposit(500)
  account.withdraw(200)
  print(account.get_balance())  # 1300
  ```

&nbsp;
> :no_entry: *Jeśli nie posiadasz materiałów do tego zadania tj. **PDF, projekt + Code Review**, znajdziesz je na stronie [devmentor.pl](https://devmentor.pl/workshop-python-oop)*

> :arrow_left: [*poprzednie zadanie*](./../05) | ~~*następne zadanie*~~ :arrow_right:
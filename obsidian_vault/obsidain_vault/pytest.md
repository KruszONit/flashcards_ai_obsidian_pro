### **Czym jest** 

### [**pytest**](chatgpt://generic-entity?number=0)


pytest to framework testowy oparty na **konwencjach zamiast konfiguracji**. Minimalny boilerplate, silny mechanizm **fixture**, bogaty ekosystem pluginów i bardzo czytelne raportowanie błędów.

---

## **Filozofia**

- **Tests are functions** – zwykłe funkcje test_*
    
- **assert** zamiast dedykowanych matcherów
    
- **Dependency Injection przez fixtures**
    
- **Fail fast, rich output** – traceback pokazuje _dlaczego_, nie tylko _że_
    

---

## **Minimalny przykład**

```python
def add(a: int, b: int) -> int:
    return a + b

def test_add():
    assert add(2, 3) == 5
```
#pytest #uni_tests #python

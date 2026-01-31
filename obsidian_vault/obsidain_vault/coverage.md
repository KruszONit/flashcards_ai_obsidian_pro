  

**Coverage** to miara, **które fragmenty kodu zostały faktycznie wykonane podczas testów**. Najczęściej mówimy o:

- **line coverage** – czy linia została wykonana,
    
- **branch coverage** – czy wykonano wszystkie gałęzie (if/else, match),
    
- **function coverage** – czy funkcja została wywołana.
    
W Pythonie standardem jest biblioteka [**coverage.py**](chatgpt://generic-entity?number=0), najczęściej używana razem z [**pytest**](chatgpt://generic-entity?number=1).

---

## **Jak to działa (precyzyjnie)**

1. Interpreter uruchamia kod **pod kontrolą tracera** (hooki na wykonanie linii).
    
2. Każda wykonana linia/gałąź jest **zaznaczana** w raporcie.
    
3. Raport **porównuje** kod źródłowy z tym, co zostało uruchomione.
    

  

> Coverage **nie mierzy jakości testów**, tylko _zasięg wykonania_.


```python
uv add coverage pytest-cov --dev
```




#pytest #coverage 
# Nested example: keep the whole pending tree

This example begins after the user confirmed the root's criteria and selected a professional moving service. All organizations are unspecified; no real offers or measurements are claimed.

Assistant:

[1] ВЫБОР — профессиональный перевозчик

Выбран профессиональный перевозчик. Нужны отдельные решения о компании, дате и упаковке. Следующий узел после подтверждения: [1.1]. Подтверждаете переход?

Неразрешённые узлы:
- [1] переезд — ожидает подтверждения декомпозиции ◀
  - [1.1] компания
  - [1.2] дата
  - [1.3] упаковка
    - [1.3.1] хрупкие предметы
    - [1.3.2] книги

User: Продолжай

Assistant:

[1.1] КРИТЕРИИ — компания

Остаются также дата и упаковка с двумя подзадачами.
1. Итоговая стоимость — меньше при одинаковом составе услуг
2. Ответственность за повреждения — условия покрытия и исключения
3. Доступность — обязательное соответствие согласованному окну переезда

Подтверждаете критерии?

Неразрешённые узлы:
- [1] переезд — ждёт завершения подзадач
  - [1.1] компания ◀
  - [1.2] дата
  - [1.3] упаковка
    - [1.3.1] хрупкие предметы
    - [1.3.2] книги

User: Добавь отзывчивость

Assistant stays in CRITERIA, adds responsiveness, repeats the entire pending tree, and asks for confirmation again. It does not output options yet.

Once the criteria are confirmed, OPTIONS must compare at least three genuine available approaches. If actual providers and quotes are unknown, distinguish structural approaches with explicit unknown provider details, or ask for the missing scope information. Do not fabricate three businesses and score their reputation.

A later leaf COLLAPSE remains “awaiting confirmation” in the tree. The user's selection does not itself confirm that COLLAPSE. The last leaf follows this rule too; its merged plan appears only after the user's subsequent confirmation.

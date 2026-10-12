---
name: logika
license: MIT
metadata:
  version: "2.1.0"
  upstream-version: "2.0.0"
  languages: "en,ru"
description: >
  Review and repair arguments in English or Russian using classical formal logic
  from G. Chelpanov's textbook. Check inferences, syllogisms, definitions, divisions,
  induction, and analogies; identify fallacies and solve logic exercises.
  Use for logical review, argument repair, and logic problems.
  Русские запросы: «проверь логику», «найди логические ошибки», «исправь логику»,
  «поправь аргументацию», «проверь силлогизм».
---

# Logika / Логика

Choose the instruction language from the text or exercise being analyzed. If no
source text is present, use the user's requested language, otherwise the language
of their request. Explicit language instructions take precedence.

- **English:** read [SKILL.en.md](SKILL.en.md), then its English references as needed.
- **Русский:** прочитай [SKILL.ru.md](SKILL.ru.md), затем нужные русские справочники.

Load one instruction version. For mixed-language material, use the references
needed for each passage. Preserve the source language when repairing a text;
translate only when requested. Write the analysis in the user's requested
response language, or the language of their request by default.

Both versions provide review, repair, exercise, and explicit BQA/MCQA benchmark
modes. Reference and script paths are relative to this skill directory.

## Sustained source-formalization workflow (2026-09-24)

When reviewing source-based mathematical formalization, compare the original proposition with the final theorem and its entire dependency chain. Check domain, quantifiers, hypotheses, equality notion, labels, ordering, normalization, and paid operations. A useful intermediate identity does not establish an unproved implementation-to-specification bridge.

Record which source obligation a helper actually discharges. Keep the parent claim open until all obligations are proved or the original false claim is explicitly refuted and its correction distinguished. Kernel acceptance, source provenance, source correspondence, and completeness of coverage are separate judgments; none alone entails the others. Treat literal counters or status labels as assertions until their producing checks are inspected.

Apply this review to the central theorem at meaningful integration points. Do not replace proof work with repeated generic checklists, or report skill reading as evidence that the logical review occurred.

## Source-to-proof review details

For mathematical source/Lean correspondence reviews, read [formalization-audit.md](references/formalization-audit.md). In particular, distinguish a one-state length identity from a two-state metric isometry, assumptions defining a model from consequences proved within it, and encoded cases checked from relevant cases covered. Keep the review tied to the actual quantifiers and proof dependencies.

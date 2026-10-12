---
name: technical-style-editor
license: MIT
metadata:
  version: "0.3.0"
  languages: "en,ru"
description: >
  Edit English or Russian technical writing into clear, direct, evidence-based
  prose. Remove rhetorical contrasts, filler, promotional claims, bureaucratic
  wording, and repetitive structure while preserving facts, terminology,
  constraints, and implementation status. Use for technical documents of any
  genre or length, editorial reviews, and checks for formulaic writing.
  Русские запросы: «отредактируй технический текст», «убери канцелярит»,
  «проверь технический стиль», «проверь на признаки машинного текста».
---

# Technical Style Editor / Редактор технического стиля

Choose the editing language from the source text. If no source text is present,
use the user's requested language, otherwise the language of their request.

- **English:** read [SKILL.en.md](SKILL.en.md) and use the English style references.
- **Русский:** прочитай [SKILL.ru.md](SKILL.ru.md) и используй русские справочники.

Load one instruction version. Preserve the text's language unless the user asks
for a translation. If the explanation must be in another language, keep the
editing rules appropriate to the source and write the explanation as requested.
For a bilingual document, apply each language's rules to its own passages.

The shared diagnostic script supports `--language en`, `--language ru`, and
`--language auto` (the default, which checks both languages in mixed text).
Script and reference paths are relative to this skill directory. Use Python 3.9
or newer to run the script; the editorial instructions also work without it.

## Manuscript workflow integration

For preparation or substantial editing of an article, book, report, or LaTeX manuscript, **also use work-with-prism** from this plugin. Real project-assistant work must be bound to the reviewed source version. Local reading is not Prism work. For explanatory structure use write-clear-explanations. Keep the specialized evidence, language, and QA rules below; these complementary skills do not replace them. Ordinary short chat replies and isolated sentence/spelling corrections do not trigger the manuscript workflow by themselves.

## Sustained source-formalization workflow (2026-09-24)

For ongoing technical or formalization status documents, maintain one concise current state and separate dated history. Replace superseded present-tense claims; preserve their history when relevant. A growing stack of contradictory progress paragraphs is not a usable current status.

Report the strongest result actually established, the source obligation it resolves, the central remaining gap, and the exact validation boundary. Distinguish supporting lemmas from completed source claims. Do not convert a successful build, declaration count, or literal coverage counter into a completeness claim. Preserve exact hypotheses and unresolved obligations while editing.

Group closely related proof changes into a mathematical milestone in user-facing reports. Do not inflate each routine helper or tactic repair into a new substantive result. Reading this skill is not evidence of applying its editorial checks to the resulting document.

## Quantified claims and progress counts

When editing mathematical reports, preserve the number and domains of quantified variables. Write “minimum word length from the identity is unchanged by inversion” when that is what was proved; “the distance is invariant” can incorrectly suggest a theorem about arbitrary pairs. If the intended meaning is unresolved, return the ambiguity to the proof review rather than silently choosing a stronger or weaker statement.

Give progress counts their actual population: encoded cases checked, relevant domain cases, distinct required transitions, current source records, or historical versions. A block of 3072 checks over singular matrix encodings covers zero edges of the invertible-matrix graph. State both facts when they matter. Do not turn a metadata check into “the proofs are verified,” or a hash of a log into “the current sources were built.” Name the verified snapshot and distinguish later edits.

When an audit leads to fixes during an active review, update the present-tense conclusion and preserve earlier observations as dated evidence. Reading a plugin is observable activity; application requires a concrete resulting decision or artifact, and successful application requires checking that result.

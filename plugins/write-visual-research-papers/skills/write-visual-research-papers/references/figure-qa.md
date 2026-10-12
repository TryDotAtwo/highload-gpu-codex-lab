# Figure and PDF quality gate

## Design before rendering

For each figure write: the exact step it explains; inputs and outputs; source equation/claim; every symbol's meaning; what the picture does NOT establish. Give each figure one primary job. Split overloaded evidence maps into linked panels instead of shrinking labels until unreadable.

Use native TikZ/SVG for exact equations, geometry, circuit wires, graph structure, and arrows. Keep editable sources. Prefer explicit grid rows/columns and named node anchors. Route trees and DAGs through reserved gutters with parent/child anchors; use explicit intermediate bend coordinates when needed. Account for a node's actual rendered height, not only a nominal minimum height. Long labels must wrap inside their own boxes. Align nodes at the same hierarchical level to one grid row or a shared anchor (for example, all north anchors); unequal box heights are not a reason to stagger their level accidentally.

For ordinary tree/flow layouts, leave at least about 3 mm of visible boundary-to-boundary space between independent nodes at the FINAL displayed/printed scale. This is a default layout-quality threshold, not a mathematical condition on all plots. Touching boundaries of independent blocks are a defect even when no text overlaps. Intentional adjacency is permitted for semantic matrices or explicitly joined panels; record that meaning rather than treating accidental contact as intentional. Measure after any resizing.

Place arrow ports on the actual box boundary, not inside the box. Use anchored connectors such as `node.south` to `next.north`; route edges around nodes and labels. Parallel edges need separate lanes. A routing junction may be shared only when visually intentional. Edge crossings must be unambiguous and must not imply an unintended dependency. Avoid coordinates whose spacing depends on an unmeasured text box. Do not solve collisions by indiscriminate global resizing.

Keep equations typeset, baseline-aligned, and readable at final print size. Check thin lines, subscripts, bit labels, legends, caption type, and contrast. Use textual status labels so meaning survives grayscale and color-vision differences. Mark schematics that are not to scale.

## Required individual inspection

Maintain a figure inventory with:
`ID | source | final page/panel | explanatory claim | render file | inspection scale | defects/fixes | final PASS/OPEN`.

1. Compile the exact manuscript or a figure wrapper using the same fonts, styles, scale, and width
2. Render every figure/panel at its final effective size, then inspect it individually at 100–150%; zoom further for dense labels as needed
3. Check every text label against ALL edges, including edges from other branches; check text against text, edges against nodes, clipping, math glyphs, cropped arrows, line breaks, legend associations, color/status consistency, reading order, and semantic arrow direction. Check that independent block boundaries neither touch nor crowd the default separation and that nodes on the same hierarchical level share the intended alignment
4. For every tree/DAG, trace each edge from named source to named destination. Check that each port meets its actual box boundary, routing avoids unrelated boxes and labels, and all parents/children remain distinguishable
5. Fix the source, recompile, and inspect the affected figure again. Recheck neighboring pages after any size change
6. Record an actual visual judgment; do not infer PASS from an empty compile log or geometric bounding boxes alone

An image or crop whose text cannot actually be read is an unperformed check, never PASS. A crop is acceptable only when its labels and every relevant edge are legible and its surrounding context does not hide contacts or crossings. A contact sheet helps navigation but is not per-figure inspection. A successful TeX build does not detect semantic arrows, overlap, or microscopic labels. When actual image inspection is unavailable, state that visual QA is incomplete.

## Whole-PDF pass

Render and inspect EVERY page after the final changes. Check first-page metadata, equations, tables, whitespace, widows/orphans, heading placement, split/stranded captions, float order, citation links, appendix references, page numbers, and page overflow. Check that a figure is beside the argument it explains and that its caption does not overclaim evidence.

Inspect build warnings: unresolved references/citations, missing glyphs, overfull boxes, float placement, duplicate labels. Investigate and fix relevant warnings; document intentionally tolerated warnings. Recompile enough times for references and contents to settle. Record page count and final PDF hash only after the last QA pass.

## Release gate

Release as visually checked only when every inventory row passes and the whole-PDF pass matches the final source/PDF identities. If a limitation remains, name the affected figure/page and withhold a clean-QA claim. Never claim a corrected preview proves that a separately compiled or older PDF is corrected.

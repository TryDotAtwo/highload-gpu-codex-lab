# Reproducible delivery, Prism, and PDF fallback

## Identify the source of truth

Before changing a project, resolve its exact owner/project, main file, source set, and current version. Use observed links and supported tools. Record whether you are editing a live project, a fetched copy, or a proposed revision. Preserve user edits and do not overwrite unrelated artifacts. Drafting approval does not authorize submission, public sharing, publication, or acceptance of venue terms.

Keep the paper source, figure sources, data/certificates, references, and ancillary proofs under explicit identities. List exclusions and missing raw evidence. Supply enough build instructions to reproduce the delivered PDF: main file, engine/toolchain, dependencies, bibliography commands, and required passes. Never claim a build was rerun when only historical logs were inspected.

## Prism/native-editor path

When the user requests Prism or another online editor, inspect the existing project and use its available source/edit/compile operations. After saving, check that the expected source is present. After compiling, verify that the project returned a fresh successful build and that the displayed/downloaded PDF matches that version. Saving text is not compilation; compilation is not visual inspection.

If authentication, unsupported attachment types, build failure, or transport prevents completion, report the precise observed boundary. Do not treat a local build as evidence that a live project was updated. Continue with an authorized local source/PDF fallback when useful; label it clearly. Do not publish or create public hosting as an implicit fallback.

## Exact artifact identity

Use a manifest beside the deliverable with:
- Main file and every required source/figure/data/ancillary path, size, SHA-256
- Build command, engine/version, build log, build time and source snapshot/version
- Final PDF filename, size, page count, SHA-256
- Which evidence was rerun, inspected, reported, missing, or conditional
- Figure inventory and whole-PDF QA outcome, tied to this exact PDF

Freeze or copy the source set for the final build. Recompute source hashes afterward and confirm it did not change during compilation/QA. If any source changes, rebuild and recheck affected figures/pages plus final document flow. A source archive hash and PDF hash identify artifacts but do not alone prove the PDF was built from that archive; retain the actual build record binding them.

## Handoff

Deliver the current PDF plus a clean editable source bundle and required evidence attachments using the user's authorized destination. Include the main-file/build instructions and any unresolved issues in a brief handoff. Verify that links resolve to the intended versions and that the user can access them. Do not upload confidential source to an unrelated service, broaden sharing, or include internal assistant notes/tools in a deliverable.

If the live editor cannot provide a working PDF, compile the exact fetched source locally when feasible, inspect it, and deliver that PDF with its source bundle and manifest. State which live-project steps remain unverified. If local compilation or visual inspection is unavailable, supply source and exact diagnostics rather than asserting readiness.

Ask for publication/submission approval only when a final draft and destination are ready. Preserve the distinction between user approval of a writing style, approval of scientific claims, and permission to publish.

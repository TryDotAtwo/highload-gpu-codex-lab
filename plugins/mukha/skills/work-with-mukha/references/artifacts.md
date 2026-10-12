# Artifacts, live runs and resumable data

## Provenance that can survive interruption

Pin source commit/GCS generation/HF revision and record source schema/units.
Validate the actual requested object, not just the size or a filename. A HEAD
ETag followed by unconditional GETs is not immutable retrieval. For large remote
Arrow/Feather data, range reads and filtered shards can avoid filling local disk;
budget RAM, network bytes, caching and result size before launching.

A robust extraction publishes a completely written, hashed shard before an atomic
manifest update. On restart, verify committed parts and handle an orphan from the
write/commit gap by validating its expected batch/source identity or regenerating
to a separate temporary path. Never silently append past corrupt/missing parts.
Check completed empty batches too. Store enough state to resume exact boundaries.
Terminate/cancel worker work and wait before closing its streams. Use bounded
prefetch so a slow earlier batch does not create an unbounded queue of results.

For synapse tables, reconcile both total contacts AND counts for every original
body pair with the pinned graph. Preserve source coordinates, units, confidence
and ROI metadata. Establish contact uniqueness from the source contract; do not
deduplicate arbitrary coordinate tuples or coalesce weak rows without justification.
Partial extraction must remain visibly partial and cannot calibrate a full model.

`python <plugin>/scripts/verify_manifest.py --root <artifact-root> --manifest
<manifest.json>` checks explicit `files` entries with `sha256` and `bytes`.
It rejects traversal/symlinks, missing files and mismatches. Use this only on
completed immutable artifacts, not files being written. It proves byte identity,
not successful biology or origin of a KSP trace. It does not support every
project-specific manifest; use the project's verifier for other schemas.

## Molab and HF

Use the actual Molab skill for transport/lifecycle. Keep one heavy workload per
sandbox and attach it to the visible active notebook cell/SSE. Inspect actual
process and GPU state before launching. Preserve a confirmed live session; do
not duplicate a job when observation times out. HTTP410 is sandbox loss, not
evidence of OOM, an empty result, or permission to hide a detached job.

Long historical notebooks with automatic downloads/builds/runs are fragile
entrypoints. Recover with a small notebook that explicitly separates preflight,
restore, build, bounded experiment and export. Heavy stages should require the
intended explicit execution; marimo dependencies must not trigger them again
when merely opening or restoring. Source stays in versioned files/artifact bundles.

Use the project's private HF content-addressed archive and immutable receipts.
Verify a fresh-directory restore of inputs/source/build closure before relying
on recovery. Archive completed conditions/checkpoint boundaries before moving on.
A receipt cannot resurrect data that was never uploaded. Never put auth URLs,
tokens, `.env`, private pairing state or unrestricted directory dumps into a
report, notebook cell, plugin or archive. Reuse source/build objects by digest.


## Mandatory persistence gate, 2026-10-04

Apply [execution-policy.md](execution-policy.md). HF publication is a stage gate, not end-of-run cleanup. Preflight the private repository and publish source/input closure before computation. Immediately publish every immutable completed shard, condition, checkpoint, segmented log and result with tools/hf_artifact_archive.py or the existing verified project archive workflow. Require server digest verification and an immutable commit/manifest receipt before proceeding. Never hash/upload a mutating file. On upload failure retain completed files in the same MoLab session and stop advancing; no Windows download or local calculation fallback. Restoration and fresh-directory verification also run only in MoLab. A documentation update is not a verified upload.

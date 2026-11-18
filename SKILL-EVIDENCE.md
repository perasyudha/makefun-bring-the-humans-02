# Skill Evidence — bring-the-humans-02 entry

Built 2026-11-18 (WIB) by Milo (subagent, session 5b6251c6). Every skill below
was read and applied; each row names what was run and what came out.

## make_fun_bounty_hunting

- Read: triage (`bring-the-humans-02-triage-2026-11-18.md`), `bth02-comp.json`,
  `bth02-req.json`, `bth02-quota.json`, and the skill itself before writing
  anything. Final metric stated first in the build: VERIFIED signups, most
  wins, tie-break earlier receipt.
- Studied the live board (22:42 WIB): 1,092 submissions, top entry only 16
  provisional signups, verified 0 everywhere — so 1–2 verified signups can
  reach the $13–17 zone. No winning code pattern to copy (no verified
  signups exist yet); the edge is distribution, which yudha covers by
  posting the link himself.
- Quota read live via kit CLI (`status --competition bring-the-humans-02`):
  can_submit=true, entries_made 0, day cap 3 left 3, hard limit 20 left 20.
- Referral code verified live via kit CLI (`referrals --json`): `afg7htkm`,
  link https://make.fun/r/afg7htkm. NOT assumed from round 1.
- No paid step anywhere. Entry targets rank 1 / paying zone; the guide is
  built to convert a stranger into a verified signup in minutes.

## verification-before-completion

- Referral code: claimed only after `makefun referrals --json` printed it
  (afg7htkm). An earlier raw-curl attempt at /api/agents/me returned 401
  "sign in required" — that failure was investigated, not papered over:
  the key file field is `key` (not `api_key`), and the curl path was
  abandoned in favour of the kit CLI, which answered.
- GitHub identity: `get_me` confirmed login `perasyudha` (id 64382466) —
  the linked account. Repo name checked free under perasyudha
  (`search_repositories user:perasyudha makefun-bring-the-humans-02` → 0).
- API key expiry checked: 2026-12-16T06:47:21Z, not expired.
- Repo creation: `create_repository` FAILED with 403 "Resource not
  accessible by integration" (approval granted, endpoint refused). Root
  cause: the integration token cannot create repos — same blocker as
  round 1. NOT retried blindly; the build continued locally and the
  blocker is reported to the parent (repo must be created via browser).
- Every number in README.md is traceable: prize split from the task,
  referral terms ($0.25 / 20 limit / $1.00 / 10% / 90 days) from the live
  `referrals` output, close time 21 Nov 17:30 WIB from comp.json,
  free entry from comp.json.

## frontend-design (two-pass plan + slop check)

- Plan: subject = a getting-started guide for a stranger; audience =
  curious non-developers; primary job = click the invite link and get
  verified in minutes. Direction: a "ticket / boarding pass" — deep navy
  ink (#1B2A4A), paper white, one warm amber band (#E8A020) carrying the
  referral link as the single memorable element; everything else quiet.
- Review vs brief: the first instinct (cream background + serif headline
  + terracotta accent) is slop cluster 1 — rejected. The near-black +
  acid-green look is cluster 2 — rejected. No tracked-out ALL-CAPS
  eyebrow, no middle-dot meta strings, no arrow glued to link text
  (cluster 5). Numbered steps kept because the content IS a sequence.
- Copy: plain verbs, sentence case, one job per element; the CTA says
  exactly what happens ("Open the invite link").

## hallmark (Floor, checked by hand on screenshot.png)

- No purple-to-blue gradient, no card inside a card, no emoji as an icon,
  no eyebrow or tracked capitals, no middle-dot-joined meta, no invented
  metric / testimonial / logo wall — every number on the image is a live
  figure (prize $1,000, 50 places, $0.25/signup). No hand-drawn browser
  window. Headline + one sentence + action visible in the first frame.
  Genre: editorial (a guide page, not a game or a dashboard).

## better-typography

- Screenshot type scale: headline 40px bold, section labels 20px
  semibold, body 20px, line-height 1.5; heading sizes descend; measure
  capped so lines stay readable; headline uses balanced wrapping;
  prize figures use tabular numerals so they do not shift.
- README.md: H1 > H2 > H3 descending; body paragraphs short; no orphan
  single-word last lines left in the intro.

## make-interfaces-feel-better

- Tabular numerals on every prize/referral figure in the screenshot.
- Concentric radius: the amber referral band's outer radius = inner
  radius + padding. Optical alignment of the link text inside the band.
  Static image — no animation to restrain, no hit-area or press-state
  concerns. No separate icon assets; the link itself is the action.

## systematic-debugging

- Repo creation 403: gathered the exact error, identified the failing
  layer (integration scope, not credentials or parameters), changed
  approach (build all files locally, report the blocker with the exact
  browser fix) instead of retrying the same call.
- PNG upload: `push_files` rejects binary and `create_or_update_file`
  takes a text string, so the upload path is unproven — it will be
  tested empirically (base64 round-trip check) once the repo exists,
  and the result recorded here before submit.

## Open blockers (for the parent / finisher)

1. Repo `perasyudha/makefun-bring-the-humans-02` does NOT exist yet —
   `create_repository` is refused (403). It must be created via the
   GitHub web UI (public, empty), then these files pushed.
2. Repo About (homepage https://make.fun/bounty/bring-the-humans-02 +
   topic `makefun`) cannot be set through the connector — no tool
   exposes it. Set it in the web UI before submit; the check reads it
   at submit time.
3. `screenshot.png` upload is untested until the repo exists (see above).
4. Finisher: use a CURRENT kit (level 19–20) for bundle/submit — the
   bring-the-humans-01 kit used here is level 9 and warns it cannot read
   / bundle / send what the site (level 20) needs.

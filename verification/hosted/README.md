# Inspect the mathematics on GitHub

The capture utility compares equations in an exact Git revision with the mathematics actually rendered on its public GitHub pages. It records screenshots at desktop and narrow widths, the source expressions, hosted MathML, structural comparisons and a revision-bound report.

## Run a capture

Requirements are Node.js 18 or later, Python 3.10 or later, Git, Playwright and MathJax. Install browser dependencies outside the repository, then supply an exact commit and a new empty evidence directory:

```bash
npm install --prefix /tmp/purity-hosted-deps playwright@1.56.1 mathjax-full@3.2.1
/tmp/purity-hosted-deps/node_modules/.bin/playwright install chromium
NODE_PATH=/tmp/purity-hosted-deps/node_modules node verification/hosted/capture_hosted_math.cjs \
  --root . \
  --repository GoGoKo699/Collective-Purity-Advantage \
  --revision FULL_COMMIT_SHA \
  --output /tmp/purity-hosted-evidence
```

Replace `FULL_COMMIT_SHA` with the complete 40-character SHA of the source being inspected. The command reads Git objects at that commit, not uncommitted changes. Its default scope is every tracked Markdown page. Repeated `--page PATH` options select an explicitly narrower diagnostic scope; a partial capture does not verify omitted pages.

The browser is anonymous and visits commit-pinned public GitHub URLs. It does not sign in, modify hosted content or change rendering styles. The GitHub Actions workflow has read-only repository permissions, checks out the exact pull-request head and retains its evidence as a workflow artifact.

## Read the evidence

`hosted-report.json` binds the source commit and tree, required pages, expression counts, runtime versions and artifact hashes. The capture saves both a 1440-pixel and a 760-pixel viewport. Every source expression is compiled locally for comparison with its actual hosted MathML; inline, display and table mathematics are included. Missing hosts, changed expression structure, absent relations or labels, renderer errors and collapsed or overflowing display geometry cause failure.

A structural pass still needs visual inspection of the saved screenshots, including main claims, substantial proofs and learning pages. Check equation bodies and labels against their source, and inspect layout and navigation separately. Local compilation alone does not establish hosted rendering. A hosted pass does not establish scientific correctness, universal browser compatibility or future GitHub behavior.

Each attempt needs a new output directory. Preserve a failed report when diagnosing a problem, and rerun the relevant capture after source changes. Workflow artifacts expire; source code and commands support reproduction, while enduring scientific validation is documented in the [verification overview](../README.md).

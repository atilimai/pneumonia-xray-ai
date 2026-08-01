# Release Checklist (v1.0.0)

This is the working checklist for the final release (GitHub issue #14). It tracks
what is already done in the repo and what still needs a manual step from the
maintainer (things like creating a Git tag, uploading weights, or deploying a
demo, which cannot be done from inside the repo).

Status meaning:
- done - finished in the repo
- pending (you) - needs an action from the maintainer / an account
- optional - only needed if the Hugging Face model page or demo is published

## GitHub release (required path)

| Item | Status | Notes |
|---|---|---|
| Release notes with metrics, dataset, limitations | done | `CHANGELOG.md` |
| Docs reflect the real project (no draft/placeholder) | done | fixed `DEPLOYMENT_PLAN.md`, `METRICS.md` |
| README shows final model and metrics | done | Results section in `README.md` |
| Medical disclaimer prominent in README | done | top of `README.md` |
| Clean `git status` (no uncommitted/untracked) | pending (you) | commit everything before tagging |
| Git tag `v1.0.0` created and pushed | pending (you) | see steps below |
| GitHub Release created from the tag | pending (you) | paste the `CHANGELOG.md` v1.0.0 notes |

## Hugging Face model page (optional)

| Item | Status | Notes |
|---|---|---|
| Model card written | done | `MODEL_CARD.md` (ready to use as HF `README.md`) |
| Trained checkpoint available | pending (you) | no `.pt` exists in the repo yet |
| Weights uploaded to HF Hub or attached to the Release | pending (you) | see steps below |
| README links to the HF model page | pending (you) | add once the page exists |

## Gradio demo (optional)

| Item | Status | Notes |
|---|---|---|
| Demo app built (`app/`) | pending (you) | `app/` is not implemented yet |
| Demo deployed on HF Spaces with a visible disclaimer | pending (you) | needs the checkpoint first |
| Demo link added to `README.md` and `app/README.md` | pending (you) | add once the Space is live |

## Dependency checklists

| Item | Status | Notes |
|---|---|---|
| `11_reproducibility_checklist.md` items complete | mostly | `requirements.txt` is not version-pinned yet |
| `12_documentation_pass.md` items complete | done | docs reviewed in this pass |

---

## Steps for the manual parts

### 1. Clean status and commit

```bash
git status
git add .
git commit -m "Prepare v1.0.0 release"
git push
```

### 2. Tag and push the release

```bash
git tag -a v1.0.0 -m "v1.0.0 - first public release"
git push origin v1.0.0
```

Then on GitHub: Releases > Draft a new release > choose the `v1.0.0` tag >
paste the notes from `CHANGELOG.md`.

### 3. (Optional) Publish the weights on Hugging Face

Only possible once a trained `best_model.pt` exists.

```bash
pip install huggingface_hub
huggingface-cli login
huggingface-cli upload <your-username>/pneumonia-xray-resnet50 best_model.pt
huggingface-cli upload <your-username>/pneumonia-xray-resnet50 MODEL_CARD.md README.md
```

Alternatively, attach `best_model.pt` as a binary asset on the GitHub Release
(good enough if you do not want a separate HF repo).

### 4. (Optional) Deploy the Gradio demo

This needs a small `app/app.py` (Gradio) plus a `requirements.txt`, loading the
model from the HF repo or the Release. Create a Hugging Face Space (Gradio SDK),
push those files, and keep the medical disclaimer visible in the UI. After it is
live, add the Space link to `README.md` and `app/README.md`.

### 5. Update links and close the issue

Once the tag, and optionally the HF page and demo, are live, add the links to the
README, tick the remaining boxes on issue #14, and close it.

---

## Honest status summary

The GitHub release path is ready in the repo: notes, model card, cleaned docs,
and metrics are all in place. What is left are actions that only the maintainer
can do (tagging, and optionally uploading weights and deploying the demo), and
those are blocked on having a trained checkpoint file, which is not in the repo
right now.

# Title
Final release checklist for GitHub and optional Hugging Face

## Type
Task

## Summary
Complete the final release checklist to confirm all project components are in order before tagging the public GitHub release and optionally publishing a Hugging Face model page and demo. This issue is the final gate before the project is considered complete and publicly shared.

## Background
A clean public release requires that the repository is tidy, all documentation is finalized, model artifacts are accessible, the demo (if built) is live, and the medical disclaimer is prominently in place. See `docs/DEPLOYMENT_PLAN.md` for the full deployment plan.

## Deliverables
- [ ] Repository passes a clean `git status` with no untracked or uncommitted changes
- [ ] Final trained model checkpoint is uploaded to Hugging Face Hub or attached to GitHub Release
- [ ] GitHub Release tag created (e.g., `v1.0.0`) with release notes
- [ ] Release notes include: final evaluation metrics, dataset reference, and known limitations
- [ ] `README.md` contains a badge or link to the Hugging Face model page (if applicable)
- [ ] Hugging Face model card (`README.md` on the HF repo) is complete with model description, metrics, limitations, and medical disclaimer
- [ ] Gradio demo is live on Hugging Face Spaces (if built) with a visible medical disclaimer
- [ ] Demo link added to `README.md` and `app/README.md`
- [ ] All items in `docs/issues/11_reproducibility_checklist.md` are confirmed complete
- [ ] All items in `docs/issues/12_documentation_pass.md` are confirmed complete

## Acceptance Criteria
- [ ] GitHub Release `v1.0.0` is tagged and publicly visible
- [ ] Model checkpoint is accessible via GitHub Release or Hugging Face Hub
- [ ] The repository README accurately represents the completed project
- [ ] Medical disclaimer is present in `README.md`, the model card, and the demo
- [ ] The project can be fully reproduced per the reproducibility checklist
- [ ] No placeholder text, broken links, or draft sections remain in any public-facing document

## Dependencies
- `11_reproducibility_checklist.md`
- `12_documentation_pass.md`
- `10_demo_deployment_plan.md`

## Out of Scope
- Ongoing model updates after release
- Clinical validation or regulatory submission
- Automated deployment pipelines

## Suggested Labels
`release`, `docs`

## Notes
The Hugging Face model card should explicitly state the dataset used, the license, the intended use (educational and research only), and the limitations. Avoid language that implies clinical reliability. The GitHub Release should include a `CHANGELOG` or brief release notes summarising what was built, what was measured, and what limitations were identified. The optional Hugging Face Space demo should be marked as a Space under the same organization or user account as the model repository for discoverability.

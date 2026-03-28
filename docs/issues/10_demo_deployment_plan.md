# Title
Plan lightweight demo deployment path

## Type
Task

## Summary
Plan the deployment of a lightweight interactive demo for the Pneumonia Detection model. The demo should allow users to upload a chest X-ray image and receive a prediction with a Grad-CAM heatmap overlay. This issue defines the demo scope, technology choice, hosting approach, and required disclaimers before any implementation begins.

## Background
The project plans an optional demo hosted on Hugging Face Spaces using Gradio. See `docs/DEPLOYMENT_PLAN.md` for the full deployment overview. The demo is a Week 5 milestone deliverable and depends on a trained, evaluated model being available.

## Deliverables
- [ ] Demo technology agreed and documented (Gradio recommended)
- [ ] Demo hosting platform agreed (Hugging Face Spaces)
- [ ] Demo input/output interface defined: image upload → label + confidence + Grad-CAM overlay
- [ ] Medical disclaimer text agreed and committed
- [ ] Model loading strategy for the demo documented (load from Hugging Face Hub or bundled checkpoint)
- [ ] `app/README.md` updated to reflect the agreed demo plan
- [ ] Demo scope limitations documented (single image, no batch processing, no clinical claims)

## Acceptance Criteria
- [ ] Demo plan is documented and committed
- [ ] Technology stack is agreed and consistent with the project's dependencies
- [ ] Medical disclaimer is defined and will be visible on the demo interface
- [ ] Demo can be built using only dependencies already in `requirements.txt`
- [ ] The plan is achievable within Week 5 given the rest of the milestone workload

## Dependencies
- `04_baseline_model_selection.md`
- `08_gradcam_integration_plan.md`
- `13_final_release_checklist.md`

## Out of Scope
- Building the demo application (this is planning only)
- API backend or server-side deployment
- Mobile or embedded deployment
- Clinical validation of demo outputs

## Suggested Labels
`deployment`, `docs`

## Notes
Hugging Face Spaces with Gradio is a well-supported and zero-cost option for this kind of demo. The demo should be clearly labelled as a research and educational project. The disclaimer should appear prominently — not just in a footer — and should state that the tool is not a medical device and should not be used for clinical decision-making. Gradio's `Image` and `Label` components are sufficient for the planned interface.

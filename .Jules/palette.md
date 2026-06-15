## 2024-06-15 - Input Constraints for Numeric Values
**Learning:** In Streamlit apps (and forms in general), numeric inputs without constraints (`min_value`, `max_value`) allow users to enter impossible values (like negative weight or age). This not only breaks backend calculations but also creates a confusing user experience where the app accepts invalid data without feedback.
**Action:** Always provide sensible boundaries (`min_value`) and defaults for numeric form inputs to guide the user and prevent erroneous inputs.

## 2024-06-15 - Visual Language and Brand Theming
**Learning:** Setting up a dark theme that matches the app's logo (using the logo's slate blue background, soft green primary color, and cream text) drastically improves the perceived quality of the Streamlit application and reduces eye strain.
**Action:** Always attempt to extract a cohesive color palette from provided brand assets and inject them natively via `.streamlit/config.toml` to unify the application's visual language.

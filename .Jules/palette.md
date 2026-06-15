## 2024-06-15 - Input Constraints for Numeric Values
**Learning:** In Streamlit apps (and forms in general), numeric inputs without constraints (`min_value`, `max_value`) allow users to enter impossible values (like negative weight or age). This not only breaks backend calculations but also creates a confusing user experience where the app accepts invalid data without feedback.
**Action:** Always provide sensible boundaries (`min_value`) and defaults for numeric form inputs to guide the user and prevent erroneous inputs.

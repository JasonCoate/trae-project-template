# [PROJECT_NAME] Project Rules

These rules guide AI behavior when working on the [PROJECT_NAME] project. All AI assistance must follow these guidelines to ensure consistency, quality, and adherence to project specifications.

## Project Context

- **Project:** [PROJECT_NAME] - [Brief project description]
- **Current Phase:** Phase 1 (Foundation)
- **Architecture:** [Technology stack and architecture description]
- **Frontend:** [Frontend technology stack]
- **Backend:** [Backend technology stack]

## AI Behavior Guidelines

### Always Reference Project Documentation
- Reference .trae/project-overview/PRODUCT_PRD.md for foundational product vision and requirements
- Check .trae/project-overview/PROJECT_STATUS.md for current project progress before starting any task
- Follow specifications in .trae/specs/ directory (phase_1.md, phase_2.md, phase_3.md)
- Update .trae/project-overview/PROJECT_STATUS.md when completing checklist items
- Reference .trae/project-overview/DEVELOPMENT_CHECKLIST.md for daily development tasks
- Follow .trae/rules/git_rules.md for version control and commit standards

### PRD Reference System
- Always check PRD section references in feature specifications
- Ensure feature implementations align with referenced PRD requirements
- When creating new features, include "PRD References" section linking to relevant PRD sections
- Maintain traceability between PRD requirements and feature implementations
- Use numbered PRD sections (e.g., "PRD: 2.1, 3.1, 5.1") for clear referencing

### Feature-Based Development
- Organize work by feature areas under .trae/features/
- Check both feature specs and feature docs when working on implementations
- Update feature documentation when making significant changes
- Ensure feature implementations meet the objectives defined in feature specifications
- Reference development phase, priority, and dependencies from feature specs

### Code Implementation Standards
- Follow [LANGUAGE/FRAMEWORK] coding standards and best practices
- Use established naming conventions ([NAMING_CONVENTION])
- Implement proper security measures ([SECURITY_REQUIREMENTS])
- Add comprehensive error handling and validation

### Technology-Specific Guidelines

**Backend [TECHNOLOGY]:**
- [Backend-specific guideline 1]
- [Backend-specific guideline 2]
- [Backend-specific guideline 3]
- [Backend-specific guideline 4]

**Frontend [TECHNOLOGY]:**
- [Frontend-specific guideline 1]
- [Frontend-specific guideline 2]
- [Frontend-specific guideline 3]
- [Frontend-specific guideline 4]

**[COMPONENT/FEATURE] Development:**
- [Component-specific guideline 1]
- [Component-specific guideline 2]
- [Component-specific guideline 3]
- [Component-specific guideline 4]

### Quality and Testing Standards
- Test all features before marking checklist items complete
- Verify cross-browser compatibility and responsive design
- Test with different user roles and permissions
- Validate security measures and input sanitization
- Ensure no console errors or warnings
- Follow testing checklists defined in feature specifications

### File Organization
- **Feature Specifications:** Place in .trae/features/[feature-name]/specs/
- **Feature Documentation:** Place in .trae/features/[feature-name]/docs/
- **[FILE_TYPE_1]:** Place in `[DIRECTORY_PATH]` with `[NAMING_PATTERN]`
- **[FILE_TYPE_2]:** Place in `[DIRECTORY_PATH]` with `[NAMING_PATTERN]`
- **[FILE_TYPE_3]:** Organize in `[DIRECTORY_PATH]` with proper structure
- **[FILE_TYPE_4]:** Place in `[DIRECTORY_PATH]` with appropriate subdirectories

### Communication Style
- Provide clear, actionable feedback
- Reference specific checklist items when completing tasks
- Reference PRD sections when explaining requirements
- Explain technical decisions and trade-offs
- Suggest improvements and optimizations
- Always prioritize user experience and best practices

### Development Focus Areas
- **Foundation:** [Core system architecture and basic functionality]
- **Enhancement:** [Advanced features and user experience improvements]
- **Optimization:** [Performance, analytics, and advanced integrations]

## Key Project Files
- `.trae/project-overview/PRODUCT_PRD.md` - Main Requirements Reference (numbered sections)
- `.trae/project-overview/PROJECT_STATUS.md` - Main progress tracker
- `.trae/project-overview/DEVELOPMENT_CHECKLIST.md` - Daily development reference
- `.trae/features/[feature-name]/specs/` - Feature-specific technical specifications
- `.trae/features/[feature-name]/docs/` - Feature-specific documentation
- `.trae/rules/git_rules.md` - Git workflow and commit standards
- `[MAIN_FILE]` - Main project file
- `[KEY_DIRECTORY_1]/` - [Description]
- `[KEY_DIRECTORY_2]/` - [Description]
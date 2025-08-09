# Trae Project Template

This template demonstrates the organizational structure and best practices developed for Trae AI projects, featuring a feature-based architecture with comprehensive documentation and traceability.

## Directory Structure

```
.trae/
├── features/              # Feature-based organization
│   └── example-feature/   # Example feature structure
│       ├── docs/          # Feature documentation
│       │   └── README.md  # Feature overview
│       └── specs/         # Feature specifications
│           └── example-specification.md
├── project-overview/       # Project-wide documentation
│   ├── PRODUCT_PRD.md     # Main Requirements Reference (numbered sections)
│   ├── PROJECT_STATUS.md  # Current project status
│   ├── DEVELOPMENT_CHECKLIST.md # Development tasks
│   ├── DEVELOPMENT_WORKFLOW.md # Development process and guidelines
│   ├── FEATURE_STATUS.md  # Feature progress tracking
│   └── README.md          # Project overview and quick start
└── rules/                 # Project rules and guidelines
    ├── project_rules.md   # General project rules
    └── git_rules.md       # Git workflow rules
```

## Key Features of This Template

### 1. Numbered PRD Structure
The `PRODUCT_PRD.md` uses a numbered section system (1, 1.1, 1.2, etc.) that serves as the main requirements reference for all feature specifications.

### 2. Feature-Based Organization
Each feature has its own directory under `.trae/features/` with:
- `docs/` - Feature documentation and guides
- `specs/` - Detailed technical specifications

### 3. PRD Reference System
All feature specifications include:
- **PRD References** section linking to relevant PRD sections
- Cross-references in objectives showing traceability
- Consistent numbering for easy navigation

### 4. Development Metadata
Each specification includes:
- Development priority and dependencies
- Estimated effort and timeline
- Feature branch name (must match folder name)
- Clear implementation tasks and success criteria

### 5. Branch Naming Convention
Feature branches must exactly match the feature folder names:
- Feature folder: `.trae/features/user-management/` → Branch: `feature/user-management`
- Feature folder: `.trae/features/api-integration/` → Branch: `feature/api-integration`
- This ensures consistency between documentation and version control

## Getting Started

1. **Copy this template** to your new project directory
2. **Update PRODUCT_PRD.md** with your project's specific requirements using the numbered structure
3. **Create feature directories** under `.trae/features/` for each major feature
4. **Write feature specifications** using the example template, ensuring PRD references
5. **Customize project rules** for your specific technology stack and workflow
6. **Update status documents** regularly as development progresses

## Documentation Guidelines

### PRD as Single Source of Truth
- The `PRODUCT_PRD.md` is the main requirements reference
- All feature specs must reference relevant PRD sections
- Use numbered sections (e.g., "PRD: 2.1, 3.1, 5.1") for traceability

### Feature Specification Standards
- Include development priority, dependencies, and effort estimates
- Reference PRD sections in both the header and objectives
- Use numbered sections for consistency
- Provide clear implementation tasks and success criteria

### Naming Conventions
- Feature directories: `kebab-case` (e.g., `form-management`, `user-authentication`)
- Feature branches: `feature/[exact-folder-name]` (e.g., `feature/form-management`, `feature/user-authentication`)
- Specification files: descriptive names ending in `.md`
- Documentation files: `README.md` for overviews, descriptive names for specific docs

### Maintenance
- Update PROJECT_STATUS.md as features are completed
- Keep PRD current with any requirement changes
- Update feature specs when PRD sections change
- Maintain cross-references between related features

## Example Usage

See the `example-feature` directory for a complete demonstration of:
- Proper PRD referencing
- Numbered section structure
- Development metadata inclusion
- Implementation task organization
- Testing and success criteria definition

This structure ensures comprehensive project management, clear development guidelines, and consistent AI assistance across any project. You haven't missed anything - this is a complete, reusable framework for Trae project setup!
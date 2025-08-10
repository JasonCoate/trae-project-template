# Trae Project Template

This template demonstrates the organizational structure and best practices developed for Trae AI projects, featuring a feature-based architecture with comprehensive documentation, traceability, and integrated task management.

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
│   ├── PROJECT_STATUS.md  # Current project status (auto-generated)
│   ├── DEVELOPMENT_CHECKLIST.md # Development tasks
│   ├── DEVELOPMENT_WORKFLOW.md # Development process and guidelines
│   ├── FEATURE_STATUS.md  # Feature progress tracking
│   └── README.md          # Project overview and quick start
├── rules/                 # Project rules and guidelines
│   ├── project_rules.md   # General project rules
│   ├── git_rules.md       # Git workflow rules
│   └── pre-commit-hook.sh # Pre-commit validation hook
└── task-management/       # SQLite-based task tracking system
    ├── task_manager.py    # CLI for task and branch management
    ├── schema.sql         # Database schema definition
    └── seed_data.sql      # Example seed data (customize per project)
.env.example              # Environment variable template
.gitignore                # Standard ignores for .env, databases, etc.
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

### 6. Integrated Task Management (SQLite + CLI)
- Centralized project DB: `.trae/task-management/<project>.db`
- CLI: `python .trae/task-management/task_manager.py`
- Auto-generated status: `.trae/project-overview/PROJECT_STATUS.md` via `sync-markdown`
- Branch validation against `.trae/features/` via `validate-branch`
- Optional pre-commit hook to enforce workflow

## Quickstart for New Projects and AI Assistants

This template is designed to be used by humans and AI assistants to bootstrap a new project with a feature-driven structure, database-backed task tracking, and auto-synced status documentation.

- Read the step-by-step guide: `QUICKSTART.md`
- Update your PRD: `.trae/project-overview/PRODUCT_PRD.md`
- Create feature folders under `.trae/features/` matching your branch names
- Initialize the task database and generate status with the CLI

Minimal setup:
```bash
# Choose how to set the Project ID used for the task DB filename
# Option A) .env file (good default for per-project config)
echo 'TRAE_PROJECT_ID=my-project' >> .env
# Option B) Per-project file (also supported)
echo 'my-project' > .trae/project-id
# Option C) Session-only environment variable
export TRAE_PROJECT_ID=my-project

python .trae/task-management/task_manager.py init --seed
python .trae/task-management/task_manager.py sync-markdown
python .trae/task-management/task_manager.py validate-branch
```

Next, follow `QUICKSTART.md` for full project customization, rules, and daily workflows.

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
# [PROJECT_NAME] Project Rules

**MAIN COORDINATION FILE** - This file serves as the central coordination point for all project activities. All AI assistance must follow these guidelines to ensure consistency, quality, and adherence to project specifications.

## CRITICAL: Pre-Feature Development Workflow

### MANDATORY Checks Before Starting Any Feature Work
1. **Git Status Check**: ALWAYS verify current branch and working directory status
   ```bash
   git status
   git branch
   ```
2. **Previous Feature Completion**: Ensure the previous feature is FULLY completed:
   - All tasks marked as ✅ in PROJECT_STATUS.md
   - All changes committed and pushed
   - Feature branch merged to main
   - Working directory clean
3. **Branch Management**: 
   - Switch to main branch: `git checkout main`
   - Pull latest changes: `git pull origin main`
   - Create new feature branch: `git checkout -b feature/[exact-folder-name]`
4. **Documentation Update**: Update PROJECT_STATUS.md with new feature progress before making any code changes
5. **Task DB Ready**: Ensure the task DB is initialized and synced
   ```bash
   # Choose one per-project option (preferred)
   echo 'TRAE_PROJECT_ID=my-project' >> .env
   # or
   echo 'my-project' > .trae/project-id
   # or use a session-only env var
   export TRAE_PROJECT_ID=my-project

   python .trae/task-management/task_manager.py init --seed
   python .trae/task-management/task_manager.py validate-branch
   python .trae/task-management/task_manager.py sync-markdown
   ```

### NEVER Begin Feature Work Without:
- ✅ Confirming previous feature is complete and merged
- ✅ Verifying clean working directory
- ✅ Creating proper feature branch
- ✅ Updating PROJECT_STATUS.md with current task
- ✅ Initializing the task DB and generating status markdown

## Project Context

- **Project:** [PROJECT_NAME] - [Brief project description]
- **Current Phase:** Phase 1 (Foundation)
- **Architecture:** [Technology stack and architecture description]
- **Frontend:** [Frontend technology stack]
- **Backend:** [Backend technology stack]

## AI Behavior Guidelines

### Always Reference Project Documentation (In Priority Order)
1. **THIS FILE (.trae/rules/project_rules.md)** - Main coordination and workflow rules
2. **.trae/project-overview/PROJECT_STATUS.md** - Current progress and active tasks (auto-generated from DB)
3. **.trae/project-overview/PRODUCT_PRD.md** - Foundational product vision and requirements
4. **.trae/project-overview/DEVELOPMENT_WORKFLOW.md** - Development workflow guidelines
5. **.trae/rules/git_rules.md** - Version control and commit standards
6. **Feature-specific docs** - .trae/features/[feature-name]/docs/ and specs/

### Documentation Update Requirements
- ALWAYS update task status via CLI where applicable
  - Example: `python .trae/task-management/task_manager.py update-task <id> completed`
- Regenerate status after updates: `python .trae/task-management/task_manager.py sync-markdown`
- Document any blockers or architectural decisions
- Update "Current Working Files" and "Next Immediate Tasks" sections

### Branch Naming Convention
- **ALWAYS use feature folder names for branches** - Branch names MUST match the exact folder names in `.trae/features/`
- When suggesting branch creation, use: `feature/[exact-folder-name]`
- Available feature branches correspond to folders in `.trae/features/` directory
- Example: For work on user management → `feature/user-management` (matches `.trae/features/user-management/`)
- Example: For work on API integration → `feature/api-integration` (matches `.trae/features/api-integration/`)

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

### CLI and Task DB
- CLI entrypoint: `python .trae/task-management/task_manager.py`
- Set project id for DB filename via `.env`, `.trae/project-id`, or `TRAE_PROJECT_ID` env var
- Commands:
  - `init [--seed]` - Initialize DB from schema.sql (with optional seed data)
  - `status` - Print feature summaries and completion
  - `validate-branch` - Ensure current branch matches `.trae/features/`
  - `list-tasks [--feature name]` - View tasks
  - `update-task <id> <status>` - Update status (todo|in_progress|completed|blocked)
  - `sync-markdown` - Generate `.trae/project-overview/PROJECT_STATUS.md`

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
- **Task DB:** `.trae/task-management/<project>.db`
- **Schema/Seeds:** `.trae/task-management/schema.sql` and `seed_data.sql`

### Communication Style
- Provide clear, actionable feedback
- Reference specific checklist items when completing tasks
- Explain technical decisions and trade-offs
- Suggest improvements and optimizations
- Always prioritize user experience and best practices

### Development Focus Areas
- **Foundation:** [Core system architecture and basic functionality]
- **Enhancement:** [Advanced features and user experience improvements]
- **Optimization:** [Performance, analytics, and advanced integrations]

## Key Project Files
- `.trae/project-overview/PRODUCT_PRD.md` - Product Requirements Document
- `.trae/project-overview/PROJECT_STATUS.md` - Main progress tracker (auto-generated)
- `.trae/project-overview/DEVELOPMENT_WORKFLOW.md` - Development workflow guidelines
- `.trae/project-overview/README.md` - Project overview and setup
- `.trae/rules/git_rules.md` - Git workflow and commit standards
- `.trae/features/[feature-name]/docs/` - Feature-specific documentation
- `.trae/features/[feature-name]/specs/` - Feature specifications
- `[MAIN_FILE]` - Main project file
- `[KEY_DIRECTORY_1]/` - [Description]
- `[KEY_DIRECTORY_2]/` - [Description]
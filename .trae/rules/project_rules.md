# [PROJECT_NAME] Project Rules

**TRAE IDE PROJECT RULES** - These rules guide AI behavior for this specific project.

## Project Context

- **Project**: [PROJECT_NAME] - [BRIEF_PROJECT_DESCRIPTION]
- **Current Phase**: [CURRENT_DEVELOPMENT_PHASE]
- **Architecture**: [MAIN_ARCHITECTURE_DESCRIPTION]
- **Frontend**: [FRONTEND_TECHNOLOGIES]
- **Backend**: [BACKEND_TECHNOLOGIES]
- **Database**: [DATABASE_TECHNOLOGY]

## AI Behavior Guidelines

### Always Reference Project Documentation (In Priority Order)
1. **THIS FILE (.trae/rules/project_rules.md)** - Main coordination and workflow rules
2. **.trae/documents/MASTER_COORDINATION_GUIDE.md** - Complete workflow guide
3. **.trae/project-overview/PROJECT_STATUS.md** - Current progress and active tasks (auto-generated from DB)
4. **.trae/project-overview/PRODUCT_PRD.md** - Foundational product vision and requirements
5. **.trae/rules/git_rules.md** - Version control and commit standards
6. **Feature-specific docs** - .trae/features/[feature-name]/docs/ and specs/

### Pre-Work Requirements
Before ANY feature work, AI must execute these steps:

```bash
# 1. Check git status and ensure clean working directory
git status && git checkout main && git pull

# 2. Set project ID for task database
echo 'TRAE_PROJECT_ID=[project_id]' >> .env

# 3. Initialize and sync task management
python .trae/task-management/task_manager.py init --seed
python .trae/task-management/task_manager.py sync-markdown

# 4. Create feature branch (MUST match .trae/features/ folder name)
git checkout -b feature/[exact-folder-name]
```

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

## Code Implementation Standards

### Technology-Specific Rules
- Follow [FRAMEWORK] and [LANGUAGE] best practices
- Use [NAMING_CONVENTION] for variables/functions, [COMPONENT_NAMING] for components
- Implement proper authentication, input validation, and data sanitization
- Add comprehensive error handling and validation

### Code Quality Requirements
- Write clean, readable, and maintainable code
- Follow established project patterns and conventions
- Include appropriate comments for complex logic
- Ensure proper TypeScript typing (if applicable)
- Follow security best practices

### Testing Standards
- Test all features before marking checklist items complete
- Verify cross-browser compatibility and responsive design
- Test with different user roles and permissions
- Validate security measures and input sanitization
- Ensure no console errors or warnings
- Follow testing checklists defined in feature specifications

## Task Management

### CLI and Task Database
- CLI entrypoint: `python .trae/task-management/task_manager.py`
- Set project id for DB filename via `.env`, `.trae/project-id`, or `TRAE_PROJECT_ID` env var
- Commands:
  - `init [--seed]` - Initialize DB from schema.sql (with optional seed data)
  - `status` - Print feature summaries and completion
  - `validate-branch` - Ensure current branch matches `.trae/features/`
  - `list-tasks [--feature name]` - View tasks
  - `update-task <id> <status>` - Update status (todo|in_progress|completed|blocked)
  - `sync-markdown` - Generate `.trae/project-overview/PROJECT_STATUS.md`

### Task Update Pattern
1. Start task: `update-task [id] in_progress`
2. Complete task: `update-task [id] completed`
3. Regenerate docs: `sync-markdown`
4. Commit changes with descriptive message

## File Organization

- **Feature Specifications**: Place in .trae/features/[feature-name]/specs/
- **Feature Documentation**: Place in .trae/features/[feature-name]/docs/
- **Task DB**: `.trae/task-management/<project>.db`
- **Schema/Seeds**: `.trae/task-management/schema.sql` and `seed_data.sql`
- **Project Rules**: `.trae/rules/project_rules.md` (this file)
- **Git Rules**: `.trae/rules/git_rules.md`

## Communication Style

- Provide clear, actionable feedback
- Reference specific checklist items when completing tasks
- Explain technical decisions and trade-offs
- Suggest improvements and optimizations
- Always prioritize user experience and best practices
- Use professional but friendly tone
- Be concise but thorough in explanations

## Development Focus Areas

### Current Phase Priorities
- **[PRIORITY_1]**: [Description]
- **[PRIORITY_2]**: [Description]
- **[PRIORITY_3]**: [Description]

### Future Enhancements
- **[ENHANCEMENT_1]**: [Description]
- **[ENHANCEMENT_2]**: [Description]
- **[ENHANCEMENT_3]**: [Description]

## Key Project Files

- `.trae/documents/MASTER_COORDINATION_GUIDE.md` - Complete workflow guide
- `.trae/project-overview/PRODUCT_PRD.md` - Product Requirements Document
- `.trae/project-overview/PROJECT_STATUS.md` - Main progress tracker (auto-generated)
- `.trae/rules/project_rules.md` - This file (project-specific AI rules)
- `.trae/rules/git_rules.md` - Git workflow and commit standards
- `.trae/features/[feature-name]/docs/` - Feature-specific documentation
- `.trae/features/[feature-name]/specs/` - Feature specifications
- `[MAIN_PROJECT_FILE]` - [Description]
- `[KEY_DIRECTORY_1]/` - [Description]
- `[KEY_DIRECTORY_2]/` - [Description]

## Project-Specific Rules

### Custom Guidelines
[Add any project-specific rules, conventions, or requirements here]

### API Restrictions
[List any APIs or libraries that should be avoided]

### Performance Requirements
[Specify any performance benchmarks or requirements]

### Security Considerations
[Outline any specific security requirements or considerations]

---

**Note**: This file contains project-specific rules for Trae IDE AI agents. Modify the placeholders (text in [BRACKETS]) to match your project's specific requirements and context.
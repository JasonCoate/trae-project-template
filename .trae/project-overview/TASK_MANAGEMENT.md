# Task Management System

This project uses an integrated SQLite-based task management system to maintain consistency between documentation, features, and branch validation.

## Overview

The task management system provides:
- **Centralized SQLite database** for features and tasks
- **CLI interface** for database operations
- **Auto-generated status** documents from database state
- **Branch validation** against feature directory structure
- **Optional pre-commit hooks** for workflow enforcement

## Quick Setup

### 1. Set Project Identifier

You can set the project ID in any of these ways (checked in this order at runtime):
- Environment variable: TRAE_PROJECT_ID
- .trae/project-id file (per-project)
- Folder name fallback (project directory name)

We also auto-load a local .env at the project root if present.

```bash
# Option A) .env (recommended per-project)
echo 'TRAE_PROJECT_ID=my-project' >> .env

# Option B) .trae/project-id file
echo 'my-project' > .trae/project-id

# Option C) Session-only env var
export TRAE_PROJECT_ID=my-project
```

This creates/uses the database at `.trae/task-management/my-project.db`.

### 2. Initialize Database

Initialize the database with the schema:

```bash
python .trae/task-management/task_manager.py init
```

Or initialize with example seed data:

```bash
python .trae/task-management/task_manager.py init --seed
```

### 3. Validate Setup

Check that your current branch matches the feature structure:

```bash
python .trae/task-management/task_manager.py validate-branch
```

Generate the auto-updated status document:

```bash
python .trae/task-management/task_manager.py sync-markdown
```

## CLI Commands

| Command | Purpose | Example |
|---------|---------|---------|
| `init [--seed]` | Initialize database from schema | `task_manager.py init --seed` |
| `status` | Show feature summaries | `task_manager.py status` |
| `validate-branch` | Check branch against features | `task_manager.py validate-branch` |
| `list-tasks [--feature name]` | List tasks | `task_manager.py list-tasks --feature example` |
| `update-task <id> <status>` | Update task status | `task_manager.py update-task 5 completed` |
| `sync-markdown` | Generate PROJECT_STATUS.md | `task_manager.py sync-markdown` |

### Task Status Values

- `todo` - Not yet started
- `in_progress` - Currently being worked on
- `completed` - Finished successfully
- `blocked` - Cannot proceed due to dependency or issue

## Database Schema

### Features Table
Stores high-level project features with metadata:
- `name` - Feature identifier (matches folder name)
- `title` - Human-readable feature name
- `description` - Feature description
- `phase` - Development phase (1, 2, 3, etc.)
- `priority` - Priority level (low, medium, high, critical)
- `status` - Overall status (not_started, in_progress, completed, blocked)
- `branch_name` - Associated Git branch
- `prd_references` - JSON array of PRD section references

### Tasks Table
Stores individual implementation tasks:
- `feature_id` - References features table
- `title` - Task description
- `category` - Type of work (backend, frontend, testing, documentation)
- `type` - Task type (implement, verify, test, write)
- `status` - Current status (todo, in_progress, completed, blocked)
- `priority` - Numeric priority (higher = more important)
- `file_path` - Associated code file (optional)
- `checklist_items` - JSON array of sub-tasks

## Branch Validation

The system enforces that feature branches match feature directory names:

```
.trae/features/user-management/ → feature/user-management
.trae/features/api-integration/ → feature/api-integration
```

This ensures consistency between:
- Documentation structure
- Version control branches  
- Database feature records
- AI assistant behavior

## Auto-Generated Documentation

The `sync-markdown` command generates `.trae/project-overview/PROJECT_STATUS.md` from the database, including:
- Feature progress summaries
- Task completion percentages
- Current branch information
- Timestamp of last sync

## Pre-Commit Integration

Install the optional pre-commit hook to enforce the workflow:

```bash
cp .trae/rules/pre-commit-hook.sh .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

The hook validates:
- Database initialization
- Branch naming convention
- Prevents manual PROJECT_STATUS.md edits
- Basic file size and syntax checks

## Customization Per Project

### Schema Customization

Modify `.trae/task-management/schema.sql` for project-specific needs:
- Add custom task categories or types
- Include additional metadata fields
- Create project-specific views or indexes

### Seed Data

Update `.trae/task-management/seed_data.sql` with your project's features and initial tasks.

### CLI Extensions

The `task_manager.py` script can be extended with additional commands for project-specific workflows.

## Integration with AI Assistants

The task management system helps AI assistants by:
- Providing current project state through `status` command
- Enforcing consistent branch naming
- Maintaining traceability between features and documentation
- Auto-generating status documents to reduce manual updates

## Troubleshooting

### Database Not Found
```bash
# Ensure you've set the project ID and initialized
# Preferred: per-project config
echo 'TRAE_PROJECT_ID=my-project' >> .env
# Or:
echo 'my-project' > .trae/project-id
# Or (session-only):
export TRAE_PROJECT_ID=my-project

python .trae/task-management/task_manager.py init
```

### Branch Validation Fails
```bash
# Check that your feature directories exist
ls .trae/features/
# Create feature directory if needed
mkdir .trae/features/my-feature
# Switch to matching branch
git checkout -b feature/my-feature
```

### Status Document Out of Sync
```bash
# Regenerate from database
python .trae/task-management/task_manager.py sync-markdown
```

## Best Practices

1. Set project ID via .env or .trae/project-id (env var also supported)
2. **Initialize database early** in project setup
3. **Sync markdown regularly** after task updates
4. **Use validate-branch** before starting feature work
5. **Update task status** as work progresses
6. **Create feature directories** before creating branches
7. **Install pre-commit hook** for team consistency
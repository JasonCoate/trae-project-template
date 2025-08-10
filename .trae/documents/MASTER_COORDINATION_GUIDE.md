# \[PROJECT\_NAME] Master Coordination Guide

**SINGLE SOURCE OF TRUTH** - This is the only file AI assistants and developers need to follow for project coordination, task management, and development workflow.

## 🚀 Quick Start for AI Assistants

### MANDATORY Pre-Work Checklist

Before ANY feature work, execute these steps in order:

```bash
# 1. Check git status
git status
git branch

# 2. Ensure clean working directory and switch to main
git checkout main
git pull origin main

# 3. Initialize task database (choose ONE method)
echo 'TRAE_PROJECT_ID=[project_id]' >> .env  # Recommended
# OR: echo '[project_id]' > .trae/project-id
# OR: export TRAE_PROJECT_ID=[project_id]

# 4. Setup task management
python .trae/task-management/task_manager.py init --seed
python .trae/task-management/task_manager.py validate-branch
python .trae/task-management/task_manager.py sync-markdown

# 5. Create feature branch (MUST match .trae/features/ folder name)
git checkout -b feature/[exact-folder-name]
```

### ⚠️ NEVER Start Without:

* ✅ Clean working directory

* ✅ Proper feature branch created

* ✅ Task DB initialized and synced

* ✅ PROJECT\_STATUS.md updated

## 📋 Task Management Workflow

### Core Commands

```bash
# View current status
python .trae/task-management/task_manager.py status

# List tasks for a feature
python .trae/task-management/task_manager.py list-tasks --feature [feature-name]

# Update task status
python .trae/task-management/task_manager.py update-task [id] [status]
# Status options: todo | in_progress | completed | blocked

# Regenerate PROJECT_STATUS.md
python .trae/task-management/task_manager.py sync-markdown
```

### Task Update Pattern

1. Start task: `update-task [id] in_progress`
2. Complete task: `update-task [id] completed`
3. Regenerate docs: `sync-markdown`
4. Commit changes with descriptive message

## 🏗️ Feature Development Process

### Step 1: Feature Selection

1. Check `.trae/project-overview/PROJECT_STATUS.md` for priorities
2. Verify dependencies are complete
3. Review feature specs in `.trae/features/[feature-name]/specs/`

### Step 2: Branch Creation

```bash
# Branch names MUST match feature folder names exactly
git checkout -b feature/[feature-name]  # matches .trae/features/[feature-name]/
```

### Step 3: Implementation

1. **Update task status**: Mark relevant tasks as `in_progress`
2. **Follow specs**: Implement according to `.trae/features/[feature]/specs/`
3. **Test incrementally**: Verify each component works
4. **Update progress**: Use `sync-markdown` regularly
5. **Commit frequently**: Use descriptive commit messages

### Step 4: Completion

1. **Mark tasks complete**: `update-task [id] completed`
2. **Regenerate docs**: `sync-markdown`
3. **Final testing**: Ensure all acceptance criteria met
4. **Merge to main**: Create PR and merge after review

## 📁 File Organization

### Essential Files (Priority Order)

1. **THIS FILE** - Master coordination guide
2. **`.trae/project-overview/PROJECT_STATUS.md`** - Auto-generated progress (DO NOT EDIT MANUALLY)
3. **`.trae/project-overview/PRODUCT_PRD.md`** - Product requirements
4. **`.trae/features/[feature]/specs/`** - Feature specifications
5. **`.trae/features/[feature]/docs/`** - Feature documentation

### Task Database

* **Location**: `.trae/task-management/[project_id].db`

* **Schema**: `.trae/task-management/schema.sql`

* **Seeds**: `.trae/task-management/seed_data.sql`

* **CLI**: `.trae/task-management/task_manager.py`

## 🎯 Project Context

**Project**: \[PROJECT\_NAME] - \[Brief project description]
**Phase**: \[Current development phase]
**Tech Stack**: \[List main technologies]

### Current Phase Features

\[List features for current development phase]

## 📝 Spec Document Creation

### When to Create Specs

* **New features**: Always create before implementation

* **Major changes**: Update existing specs

* **Dependencies**: Document integration points

### Spec Template Structure

```markdown
# [Feature Name] Specifications

## Overview
- Priority: [High/Medium/Low]
- Phase: [1/2/3]
- Dependencies: [List other features]
- Estimated Effort: [Hours/Days]

## Technical Specifications
### Data Model
### API Endpoints
### UI Components

## Implementation Tasks
- [ ] Task 1
- [ ] Task 2

## Testing Checklist
- [ ] Unit tests
- [ ] Integration tests
- [ ] User acceptance tests

## Success Criteria
- Measurable outcomes
- Performance requirements
```

## 🔧 Development Standards

### Code Quality

* **TypeScript**: Strict mode enabled (if applicable)

* **Components**: PascalCase naming

* **Functions/Variables**: camelCase naming

* **Error Handling**: Comprehensive try-catch blocks

* **Validation**: Input sanitization and validation

### Testing Requirements

* Unit tests for all new functionality

* Integration tests for API endpoints

* Cross-browser compatibility testing (if web app)

* Security validation

* Performance testing

### Git Workflow

```bash
# Feature development
git checkout main
git pull origin main
git checkout -b feature/[feature-name]
# ... development work ...
git add .
git commit -m "feat: implement [specific functionality]"
git push origin feature/[feature-name]
# Create PR, review, merge
```

## 🚨 Common Issues & Solutions

### Database Not Found

```bash
# Ensure project ID is set
echo 'TRAE_PROJECT_ID=[project_id]' >> .env
python .trae/task-management/task_manager.py init --seed
```

### Branch Validation Fails

```bash
# Check feature directories exist
ls .trae/features/
# Create if missing
mkdir .trae/features/[feature-name]
# Switch to matching branch
git checkout -b feature/[feature-name]
```

### Status Document Out of Sync

```bash
# Regenerate from database
python .trae/task-management/task_manager.py sync-markdown
```

## 📚 Documentation Hierarchy

### For AI Assistants (Read in Order)

1. **This file** - Complete workflow guidance
2. **PROJECT\_STATUS.md** - Current progress and active tasks
3. **Feature specs** - Implementation requirements

### For Developers

1. **This file** - Start here for everything
2. <br />


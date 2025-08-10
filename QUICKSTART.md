# Trae Project Template - Quickstart Guide

**Goal:** Transform this template into a fully functional project with proper task management, documentation, and development workflow.

## Requirements
- macOS, Linux, or Windows (via WSL)
- Python 3.9+ (with standard library sqlite3 module)
- Git (for version control and branching)
- Optional: A code editor/IDE and shell access
- Optional: Pre-commit hook support (standard Git hooks)

## 🚀 Quick Setup (5 minutes)

### Step 1: Copy Template and Set Project Identity

```bash
# Copy template to your new project location
cp -r trae-project-template/ my-awesome-project/
cd my-awesome-project/

# Choose how to set the Project ID used for the task DB filename
# Option A) .env file (recommended for per-project config)
cp .env.example .env  # Copy template and edit, or:
echo 'TRAE_PROJECT_ID=my-awesome-project' >> .env
# Option B) Per-project file (alternative to .env)
echo "my-awesome-project" > .trae/project-id
# Option C) Session-only env var (good for CI or temporary work)
export TRAE_PROJECT_ID=my-awesome-project
# Option D) Do nothing – the folder name will be used automatically as fallback
```

### Step 2: Initialize Task Management System

```bash
# Initialize the SQLite database with example data
python .trae/task-management/task_manager.py init --seed

# Verify everything works
python .trae/task-management/task_manager.py status
```

### Step 3: Create Your First Feature Branch

```bash
# List available example features
ls .trae/features/

# Create a branch that matches a feature folder
git checkout -b feature/example-feature

# Validate branch naming (should pass)
python .trae/task-management/task_manager.py validate-branch
```

---

## 📋 Complete Project Customization

### Phase 1: Define Your Project

#### 1.1 Update Core Project Documents

**File: `.trae/project-overview/PRODUCT_PRD.md`**
- Replace `[PROJECT_NAME]` with your actual project name
- Replace placeholder content with your project's requirements
- Keep the numbered section structure (1, 1.1, 1.2, etc.)
- This becomes your **single source of truth** for requirements

**File: `README.md` (root level)**
- Update project title and description
- Replace placeholder installation/setup instructions
- Update technology stack information
- Keep references to `.trae/` documentation

**File: `.trae/project-overview/README.md`**
- Update project overview and feature descriptions
- Replace example features with your actual features
- Update technology stack and architecture information

#### 1.2 Set Up Your Feature Structure

```bash
# Remove example feature (after understanding its structure)
rm -rf .trae/features/example-feature/

# Create your actual feature directories
mkdir -p .trae/features/user-authentication/{docs,specs}
mkdir -p .trae/features/api-integration/{docs,specs}
mkdir -p .trae/features/dashboard/{docs,specs}

# Copy the example specification as a template
cp .trae/features/example-feature/specs/example-specification.md .trae/features/user-authentication/specs/authentication-spec.md
```

#### 1.3 Customize Database Schema (Optional)

**File: `.trae/task-management/schema.sql`**
- Add project-specific tables if needed
- Modify the `features`, `tasks`, or `branches` tables for your workflow
- Add custom fields or constraints

**File: `.trae/task-management/seed_data.sql`**
- Replace example features with your actual features
- Add real tasks for your project's first phase
- Set appropriate priorities and dependencies

---

### Phase 2: Configure Your Development Workflow

#### 2.1 Update Project Rules

**File: `.trae/rules/project_rules.md`**
- Update mandatory checks for your project type
- Modify AI behavior guidelines for your technology stack
- Update branch naming examples to match your features
- Customize CLI commands section if you modify the database

**File: `.trae/rules/git_rules.md`**
- Adjust commit message conventions for your team
- Update branch examples to match your features
- Modify merge/review requirements

#### 2.2 Set Up Pre-commit Automation (Recommended)

```bash
# Install the pre-commit hook
cp .trae/rules/pre-commit-hook.sh .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit

# Test it works
git add .
git commit -m "test: verify pre-commit hook"
# Should validate branch and database initialization
```

#### 2.3 Initialize with Your Real Data

```bash
# Clear example data and start fresh
rm .trae/task-management/*.db

# Reinitialize with your customized seed data
python .trae/task-management/task_manager.py init --seed

# Generate your project's status document
python .trae/task-management/task_manager.py sync-markdown
```

---

### Phase 3: Start Development

#### 3.1 Choose Your First Feature

```bash
# List available features from your database
python .trae/task-management/task_manager.py list-tasks

# Create a proper feature branch
git checkout main
git checkout -b feature/user-authentication

# Validate branch (should pass)
python .trae/task-management/task_manager.py validate-branch
```

#### 3.2 Write Feature Specifications

**Use `.trae/features/example-feature/specs/example-specification.md` as your template:**

1. **Copy the template:**
   ```bash
   cp .trae/features/example-feature/specs/example-specification.md \
      .trae/features/user-authentication/specs/auth-spec.md
   ```

2. **Customize the specification:**
   - Update title and description
   - Reference relevant PRD sections (e.g., "PRD: 2.1, 3.2, 5.1")
   - Define your actual implementation tasks
   - Set realistic effort estimates and dependencies

3. **Create feature documentation:**
   ```bash
   # Create feature overview
   echo "# User Authentication Feature" > .trae/features/user-authentication/docs/README.md
   ```

#### 3.3 Track Your Progress

```bash
# Update task status as you work
python .trae/task-management/task_manager.py update-task 1 in_progress

# Regenerate status document
python .trae/task-management/task_manager.py sync-markdown

# Check updated status
cat .trae/project-overview/PROJECT_STATUS.md
```

---

## 🎯 Understanding the System

### What Each Component Does

**`.trae/project-overview/PRODUCT_PRD.md`**
- **Purpose:** Single source of truth for all requirements
- **Structure:** Numbered sections (1, 1.1, 1.2) for easy referencing
- **Usage:** Referenced by all feature specs for traceability

**`.trae/features/[feature]/`**
- **Purpose:** Contains all documentation and specs for one feature
- **Structure:** `docs/` for guides, `specs/` for technical requirements
- **Usage:** Branch names must match folder names exactly

**`.trae/task-management/task_manager.py`**
- **Purpose:** CLI for managing tasks, branches, and status generation
- **Commands:** `init`, `status`, `validate-branch`, `list-tasks`, `update-task`, `sync-markdown`
- **Usage:** Central tool for project coordination

**`.trae/project-overview/PROJECT_STATUS.md`**
- **Purpose:** Auto-generated overview of current project state
- **Source:** Generated from SQLite database via `sync-markdown`
- **Usage:** Never edit manually - always use CLI to update

### Key Principles

1. **Branch Names = Feature Folders:** Every branch must match a folder in `.trae/features/`
2. **PRD References:** All specs reference numbered PRD sections for traceability
3. **Database-Driven Status:** PROJECT_STATUS.md is generated from the database
4. **CLI-First Workflow:** Use `task_manager.py` for all task management

### Common Workflows

**Starting a new feature:**
```bash
# 1. Create feature folder structure
mkdir -p .trae/features/my-feature/{docs,specs}

# 2. Add tasks to database (manually edit seed_data.sql and reinit, or use CLI)
python .trae/task-management/task_manager.py update-task <id> todo

# 3. Create matching branch
git checkout -b feature/my-feature

# 4. Validate setup
python .trae/task-management/task_manager.py validate-branch
```

**Daily development:**
```bash
# Check current priorities
python .trae/task-management/task_manager.py status

# Update task progress
python .trae/task-management/task_manager.py update-task 5 in_progress

# Sync documentation
python .trae/task-management/task_manager.py sync-markdown

# Commit changes
git add . && git commit -m "feat: implement user login validation"
```

---

## 🔧 Troubleshooting

### Common Issues

**"Database not found" error:**
```bash
# Solution: Initialize the database
python .trae/task-management/task_manager.py init --seed
```

**"Branch name doesn't match feature folder" error:**
```bash
# Solution: Create matching feature folder or rename branch
mkdir -p .trae/features/my-branch-name/{docs,specs}
# OR
git checkout -b feature/existing-feature-folder
```

**"TRAE_PROJECT_ID not set" warning:**
```bash
# Solution: Use .env file (recommended for per-project config)
echo 'TRAE_PROJECT_ID=my-project' >> .env
# Alternative: Use per-project file
echo 'my-project' > .trae/project-id
# Or: Set environment variable for this session only
export TRAE_PROJECT_ID=my-project
```

### Getting Help

1. **Check example feature:** `.trae/features/example-feature/` shows proper structure
2. **Review project rules:** `.trae/rules/project_rules.md` has complete guidelines
3. **Validate setup:** Run `python .trae/task-management/task_manager.py status`
4. **Check database:** Use `sqlite3 .trae/task-management/[project].db` for direct access

---

## ✅ Success Checklist

- [ ] Copied template to new project directory
- [ ] Set project ID via `.env` (recommended), `.trae/project-id`, or `TRAE_PROJECT_ID`
- [ ] Customized `PRODUCT_PRD.md` with real requirements
- [ ] Created feature folders matching your project needs
- [ ] Updated `seed_data.sql` with real features and tasks
- [ ] Initialized database with `init --seed`
- [ ] Generated initial status with `sync-markdown`
- [ ] Created and validated first feature branch
- [ ] Set up pre-commit hook (optional but recommended)
- [ ] Updated main README.md with project-specific information

**You're ready to start development!** The task management system will guide your progress and keep documentation synchronized automatically.
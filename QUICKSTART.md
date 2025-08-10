# Trae Project Template - Quickstart Guide

**Goal:** Transform this template into a fully functional project with streamlined documentation, proper task management, and efficient development workflow.

## 🎯 NEW STREAMLINED APPROACH

**IMPORTANT**: This template now uses a **single Master Coordination Guide** instead of scattered documentation files. This makes setup faster and coordination clearer.

### For AI Assistants
✅ **Follow ONLY**: [Master Coordination Guide](./.trae/documents/MASTER_COORDINATION_GUIDE.md)  
❌ **Ignore**: Old scattered documentation files (marked as deprecated)

### For Developers
✅ **Start with**: [Master Coordination Guide](./.trae/documents/MASTER_COORDINATION_GUIDE.md)  
✅ **Then**: Follow this quickstart for initial setup

## Requirements
- macOS, Linux, or Windows (via WSL)
- Python 3.9+ (with standard library sqlite3 module)
- Git (for version control and branching)
- Optional: A code editor/IDE and shell access

## 🚀 Quick Setup (3 minutes)

### Step 1: Copy Template and Set Project Identity

```bash
# Copy template to your new project location
cp -r trae-project-template/ my-awesome-project/
cd my-awesome-project/

# Set project ID (recommended: .env file)
cp .env.example .env
echo 'TRAE_PROJECT_ID=my-awesome-project' >> .env
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

**✅ You're ready! Now follow the [Master Coordination Guide](./.trae/documents/MASTER_COORDINATION_GUIDE.md) for all development workflow.**

---

## 📋 Complete Project Customization

### Phase 1: Customize Master Coordination Guide

**File: `.trae/documents/MASTER_COORDINATION_GUIDE.md`**

1. **Replace placeholders:**
   - `[PROJECT_NAME]` → Your actual project name
   - `[project_id]` → Your project identifier
   - `[Brief project description]` → Your project description
   - `[Current development phase]` → Your current phase
   - `[List main technologies]` → Your tech stack

2. **Update project context section:**
   - Add your specific tech stack
   - List your Phase 1 features
   - Customize development standards for your project

3. **Customize workflow sections:**
   - Adjust pre-work checklist if needed
   - Update branch naming examples
   - Add project-specific troubleshooting

### Phase 2: Define Your Project Requirements

**File: `.trae/project-overview/PRODUCT_PRD.md`**
- Replace `[PROJECT_NAME]` with your actual project name
- Replace placeholder content with your project's requirements
- Keep the numbered section structure (1, 1.1, 1.2, etc.)
- This becomes your **single source of truth** for requirements

**File: `README.md` (root level)**
- Update project title and description
- Replace placeholder installation/setup instructions
- Update technology stack information

### Phase 3: Set Up Your Feature Structure

```bash
# Remove example feature (after understanding its structure)
rm -rf .trae/features/example-feature/

# Create your actual feature directories
mkdir -p .trae/features/user-authentication/{docs,specs}
mkdir -p .trae/features/api-integration/{docs,specs}
mkdir -p .trae/features/dashboard/{docs,specs}
```

### Phase 4: Customize Database with Your Features

**File: `.trae/task-management/seed_data.sql`**
- Replace example features with your actual features
- Add real tasks for your project's first phase
- Set appropriate priorities and dependencies

```bash
# Clear example data and start fresh
rm .trae/task-management/*.db

# Reinitialize with your customized seed data
python .trae/task-management/task_manager.py init --seed

# Generate your project's status document
python .trae/task-management/task_manager.py sync-markdown
```

---

## 🎯 Understanding the New System

### Key Components

**`.trae/documents/MASTER_COORDINATION_GUIDE.md`** 🎯
- **Purpose:** Single source of truth for ALL workflow guidance
- **Contains:** Pre-work checklist, task management, development process, troubleshooting
- **Usage:** The ONLY file AI assistants and developers need to follow

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

### What's Different (New vs Old)

✅ **NEW APPROACH:**
- Single Master Coordination Guide
- Streamlined workflow
- Clear step-by-step guidance
- No redundancy or confusion

❌ **OLD APPROACH (Deprecated):**
- Multiple scattered files (project_rules.md, DEVELOPMENT_WORKFLOW.md, TASK_MANAGEMENT.md)
- Redundant information
- Coordination issues
- Harder to maintain

### Key Principles

1. **Single Source of Truth:** Master Coordination Guide contains ALL workflow information
2. **Branch Names = Feature Folders:** Every branch must match a folder in `.trae/features/`
3. **PRD References:** All specs reference numbered PRD sections for traceability
4. **Database-Driven Status:** PROJECT_STATUS.md is generated from the database
5. **CLI-First Workflow:** Use `task_manager.py` for all task management

---

## 🔧 Common Workflows

### Starting a New Feature

```bash
# 1. Follow Master Coordination Guide pre-work checklist
git status && git checkout main && git pull
echo 'TRAE_PROJECT_ID=my-project' >> .env
python .trae/task-management/task_manager.py init --seed
python .trae/task-management/task_manager.py sync-markdown

# 2. Create feature folder structure
mkdir -p .trae/features/my-feature/{docs,specs}

# 3. Create matching branch
git checkout -b feature/my-feature

# 4. Validate setup
python .trae/task-management/task_manager.py validate-branch
```

### Daily Development

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
# Solution: Use .env file (recommended)
echo 'TRAE_PROJECT_ID=my-project' >> .env
```

### Getting Help

1. **Check Master Coordination Guide:** `.trae/documents/MASTER_COORDINATION_GUIDE.md` has complete guidance
2. **Check example feature:** `.trae/features/example-feature/` shows proper structure
3. **Validate setup:** Run `python .trae/task-management/task_manager.py status`
4. **Check database:** Use `sqlite3 .trae/task-management/[project].db` for direct access

---

## ✅ Success Checklist

- [ ] Copied template to new project directory
- [ ] Set project ID via `.env` file
- [ ] **Customized Master Coordination Guide with project-specific information**
- [ ] Customized `PRODUCT_PRD.md` with real requirements
- [ ] Created feature folders matching your project needs
- [ ] Updated `seed_data.sql` with real features and tasks
- [ ] Initialized database with `init --seed`
- [ ] Generated initial status with `sync-markdown`
- [ ] Created and validated first feature branch
- [ ] Updated main README.md with project-specific information

**🎉 You're ready to start development!**

**Next Steps:**
1. Follow the [Master Coordination Guide](./.trae/documents/MASTER_COORDINATION_GUIDE.md) for all development workflow
2. Use the pre-work checklist before starting any feature
3. Update task status regularly using the CLI
4. Keep the Master Coordination Guide as your single source of truth

**Remember:** The Master Coordination Guide is the ONLY file you need for project coordination. All other documentation is supplementary.
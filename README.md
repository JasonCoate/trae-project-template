# Trae Project Template

This template demonstrates the streamlined organizational structure and best practices developed for Trae AI projects, featuring a feature-based architecture with consolidated documentation, traceability, and integrated task management.

## 🚀 Quick Start

### For AI Assistants
1. **Follow**: [Master Coordination Guide](./.trae/documents/MASTER_COORDINATION_GUIDE.md)
2. **Customize**: Update project_rules.md with project-specific requirements

### For Developers
1. **Start with**: [Master Coordination Guide](./.trae/documents/MASTER_COORDINATION_GUIDE.md)
2. **Quick setup**: Follow the pre-work checklist in the guide
3. **Customize**: Update project-specific sections in the guide

## ✅ Optimal AI Onboarding Process

**For New Projects:**
1. **Point AI to QUICKSTART.md** - Contains complete 3-minute setup process
2. **Point AI to project_rules.md** - Essential for Trae IDE to work correctly with AI agents
3. **Point AI to Master Coordination Guide** - Single source of truth for all workflow
4. **Provide your PRD** - AI can update the template's PRD file with your requirements
5. **You're ready to go!** - AI will follow the consolidated workflow

## 🎯 Why This Works Well

**Single Source of Truth**: The Master Coordination Guide eliminates the confusion of multiple scattered files.

**Clear Setup Path**: QUICKSTART.md provides step-by-step instructions for both AI assistants and developers, with specific sections for each.

**PRD Integration**: The template's PRD structure is designed to be easily replaced with your project's requirements while maintaining the numbered referencing system.

**Immediate Productivity**: Once setup is complete, AI assistants have everything they need in one place - no more hunting through multiple documentation files.

## 📋 Recommended Workflow

```
1. Give AI: "Follow the QUICKSTART.md to set up this template for [project name]"
2. Give AI: "Follow the project_rules.md for Trae IDE compatibility"
3. Give AI: "Update the template PRD with this: [your PRD content]"
4. Give AI: "Follow the Master Coordination Guide for all development"
5. Start building features!
```

This approach leverages the streamlined documentation system, making it much easier for AI to understand project requirements and follow consistent workflows.

## Directory Structure

```
.trae/
├── documents/             # NEW: Single source of truth
│   └── MASTER_COORDINATION_GUIDE.md  # Complete workflow guide
├── features/              # Feature-based organization
│   └── example-feature/   # Example feature structure
│       ├── docs/          # Feature documentation
│       │   └── README.md  # Feature overview
│       └── specs/         # Feature specifications
│           └── example-specification.md
├── project-overview/       # Project-wide documentation
│   ├── PRODUCT_PRD.md     # Main Requirements Reference
│   ├── PROJECT_STATUS.md  # Auto-generated status (DO NOT EDIT)
│   ├── DEVELOPMENT_WORKFLOW.md # DEPRECATED - redirects to Master Guide
│   ├── TASK_MANAGEMENT.md # DEPRECATED - redirects to Master Guide
│   └── README.md          # Project overview
├── rules/                 # Project rules and guidelines
│   ├── project_rules.md   # Trae IDE project-specific AI rules
│   ├── git_rules.md       # Git workflow rules
│   └── pre-commit-hook.sh # Pre-commit validation hook
└── task-management/       # SQLite-based task tracking system
    ├── task_manager.py    # CLI for task and branch management
    ├── schema.sql         # Database schema definition
    └── seed_data.sql      # Example seed data
.env.example              # Environment variable template
.gitignore                # Standard ignores
QUICKSTART.md            # Initial setup guide
```

## Key Features of This Template

### 1. 🎯 Single Source of Truth
The **Master Coordination Guide** consolidates all workflow information:
- Pre-work checklist for AI assistants
- Complete task management workflow
- Feature development process
- Branch naming and validation
- Code quality standards
- Common troubleshooting

### 2. 📁 Feature-Based Organization
Each feature has its own directory under `.trae/features/` with:
- `docs/` - Feature documentation and guides
- `specs/` - Detailed technical specifications
- Branch names must match folder names exactly

### 3. 🔗 PRD Reference System
All feature specifications include:
- **PRD References** section linking to relevant PRD sections
- Cross-references in objectives showing traceability
- Consistent numbering for easy navigation

### 4. 📊 Integrated Task Management
- Centralized SQLite database: `.trae/task-management/<project>.db`
- CLI interface: `python .trae/task-management/task_manager.py`
- Auto-generated status: `.trae/project-overview/PROJECT_STATUS.md`
- Branch validation against `.trae/features/` structure

### 5. 🌿 Streamlined Branch Workflow
```bash
# Branch names MUST match feature folder names
.trae/features/user-management/ → feature/user-management
.trae/features/api-integration/ → feature/api-integration
```

## Essential Setup Commands

```bash
# 1. Set project identifier
echo 'TRAE_PROJECT_ID=[your-project-name]' >> .env

# 2. Initialize task database
python .trae/task-management/task_manager.py init --seed

# 3. Generate status documentation
python .trae/task-management/task_manager.py sync-markdown

# 4. Validate setup
python .trae/task-management/task_manager.py validate-branch
```

## Customization for New Projects

### 1. Update Master Coordination Guide
Edit `.trae/documents/MASTER_COORDINATION_GUIDE.md`:
- Replace `[PROJECT_NAME]` with your project name
- Replace `[project_id]` with your project identifier
- Update project context section
- Customize tech stack information
- Add project-specific features list

### 2. Update Product Requirements
Edit `.trae/project-overview/PRODUCT_PRD.md`:
- Define your product vision and requirements
- Use numbered sections for easy referencing
- Include all major features and specifications

### 3. Create Feature Structure
```bash
# Create feature directories
mkdir .trae/features/[feature-name]
mkdir .trae/features/[feature-name]/docs
mkdir .trae/features/[feature-name]/specs

# Create matching branches
git checkout -b feature/[feature-name]
```

### 4. Initialize Task Database
```bash
# Customize seed data first
edit .trae/task-management/seed_data.sql

# Then initialize
python .trae/task-management/task_manager.py init --seed
```

## Documentation Structure

**IMPORTANT**: This template uses a streamlined approach:

✅ **USE**: Master Coordination Guide (single source of truth)
✅ **CUSTOMIZE**: project_rules.md for Trae IDE project-specific AI behavior

The Master Coordination Guide consolidates all workflow information into a single, comprehensive document.

## Benefits of This System

- **Simplified**: One file instead of multiple scattered documents
- **Consistent**: Single workflow for all team members and AI assistants
- **Efficient**: Faster onboarding and fewer coordination issues
- **Maintainable**: Updates in one place instead of multiple files
- **Clear**: Step-by-step guidance without redundancy

## Example Usage

See the `example-feature` directory for a complete demonstration of:
- Proper PRD referencing
- Feature specification structure
- Development metadata inclusion
- Implementation task organization
- Testing and success criteria definition

---

**Start with the [Master Coordination Guide](./.trae/documents/MASTER_COORDINATION_GUIDE.md) - it's the only file you need for complete project coordination!**
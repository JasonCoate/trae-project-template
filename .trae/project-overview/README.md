# [PROJECT_NAME] Project Overview

## Project Description
[PROJECT_NAME] is [brief description of what the project does and its main purpose]. Built with [technology stack] and designed for [target audience or use case].

## Project Structure

This project follows a **feature-based architecture** where each core feature has its own dedicated directory with specifications, documentation, and implementation tracking.

### Core Features

#### 🏗️ [Feature Name 1](../features/[feature-1]/)
**Priority: High** | **Status: [Status]**
- [Brief description of feature]
- [Key capabilities or components]
- [Current development status]

#### 🧩 [Feature Name 2](../features/[feature-2]/)
**Priority: Medium** | **Status: [Status]**
- [Brief description of feature]
- [Key capabilities or components]
- [Current development status]

#### 🎨 [Feature Name 3](../features/[feature-3]/)
**Priority: Low** | **Status: [Status]**
- [Brief description of feature]
- [Key capabilities or components]
- [Current development status]

## Development Phases

### Foundation Phase
**Focus:** Core system architecture and basic functionality
- [List key foundation features]
- [Essential infrastructure components]
- [Basic user workflows]

### Enhancement Phase
**Focus:** Advanced features and user experience improvements
- [List enhancement features]
- [UI/UX improvements]
- [Performance optimizations]

### Optimization Phase
**Focus:** Analytics, integrations, and advanced capabilities
- [List optimization features]
- [Analytics and reporting]
- [Third-party integrations]

## Quick Start

### Prerequisites
- [List required software/tools]
- [System requirements]
- [Account requirements]

### Installation
```bash
# Clone the repository
git clone [repository-url]
cd [project-name]

# Install dependencies
[installation commands]

# Setup configuration
[configuration steps]

# Start development server
[start commands]
```

### Development Setup
1. **Read Documentation**
   - Review `.trae/project-overview/PRODUCT_PRD.md` for requirements
   - Check `.trae/project-overview/PROJECT_STATUS.md` for current priorities and workflow
   - Follow development workflow outlined in `PROJECT_STATUS.md`

2. **Choose a Feature**
   - Select from active features in `PROJECT_STATUS.md`
   - Review feature specifications in `.trae/features/[feature]/specs/`
   - Check dependencies and prerequisites

3. **Start Development**
   - Create feature branch following naming conventions
   - Implement according to specifications
   - Test thoroughly and document changes

## Architecture Overview

### Technology Stack
- **Frontend:** [Frontend technologies]
- **Backend:** [Backend technologies]
- **Database:** [Database technology]
- **Infrastructure:** [Hosting/deployment platform]

### Key Components
- **[Component 1]:** [Description and purpose]
- **[Component 2]:** [Description and purpose]
- **[Component 3]:** [Description and purpose]

### Data Flow
```
[User] → [Frontend] → [API] → [Backend] → [Database]
       ←            ←       ←          ←
```

## Feature Status Summary

| Feature | Priority | Status | Progress | Dependencies |
|---------|----------|--------|----------|-------------|
| [Feature 1] | High | In Progress | 75% | None |
| [Feature 2] | Medium | Planned | 0% | Feature 1 |
| [Feature 3] | Low | Planned | 0% | Feature 2 |

## Task Management (Integrated)

This project uses an integrated SQLite-based task management system. See the full guide: `.trae/project-overview/TASK_MANAGEMENT.md`.

Quick commands:
```bash
# Choose how to set the Project ID
# A) .env file (per-project)
echo 'TRAE_PROJECT_ID=my-project' >> .env
# B) .trae/project-id file
echo 'my-project' > .trae/project-id
# C) Session-only environment variable
export TRAE_PROJECT_ID=my-project

python .trae/task-management/task_manager.py init --seed
python .trae/task-management/task_manager.py validate-branch
python .trae/task-management/task_manager.py sync-markdown
python .trae/task-management/task_manager.py list-tasks --feature example-feature
python .trae/task-management/task_manager.py update-task 1 completed
```

## Development Guidelines

### Code Standards
- Follow [coding style guide]
- Implement comprehensive error handling
- Add meaningful comments and documentation
- Ensure security best practices

### Testing Requirements
- Write unit tests for all new functionality
- Perform integration testing
- Validate user experience flows
- Test security and performance

### Documentation
- Update feature documentation with changes
- Maintain API documentation
- Keep README files current
- Document architectural decisions

## Project Resources

### Documentation
- **[Project Rules](../rules/project_rules.md)** - **MAIN COORDINATION FILE** - Start here for all development work
- **[Project Status](PROJECT_STATUS.md)** - Current progress tracking and active tasks
- **[Product Requirements](PRODUCT_PRD.md)** - Complete project requirements

### Development Tools
- **Version Control:** Git with [branching strategy]
- **Code Quality:** [Linting and formatting tools]
- **Testing:** [Testing frameworks and tools]
- **Deployment:** [Deployment platform and process]

### Communication
- **Issues:** [Issue tracking system]
- **Discussions:** [Team communication platform]
- **Documentation:** [Documentation platform]
- **Code Review:** [Code review process]

## Contributing

### Getting Started
1. **START HERE**: Read [Project Rules](../rules/project_rules.md) - the main coordination file
2. Follow the mandatory pre-feature workflow in Project Rules
3. Check [Project Status](PROJECT_STATUS.md) for current priorities and available tasks
4. Review feature specifications in `.trae/features/`
5. Follow coding standards and testing requirements

### Pull Request Process
1. Create feature branch from main
2. Implement changes following specifications
3. Test thoroughly and update documentation
4. Submit pull request with clear description
5. Address review feedback promptly

### Code Review Guidelines
- Review for functionality and requirements compliance
- Check code quality and standards adherence
- Verify security and performance considerations
- Ensure documentation is updated

## Support and Resources

### Getting Help
- Check existing documentation first
- Search through project issues
- Ask questions in team communication channels
- Consult with feature owners or maintainers

### Useful Links
- [Project Repository](repository-url)
- [Documentation Site](docs-url)
- [Issue Tracker](issues-url)
- [Team Communication](communication-url)

---

**Last Updated:** [Date]  
**Project Version:** [Version]  
**Maintainers:** [List of maintainers]
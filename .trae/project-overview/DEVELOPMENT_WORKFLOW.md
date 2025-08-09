# [PROJECT_NAME] Development Workflow

This document outlines the development workflow for the feature-based [PROJECT_NAME] project structure.

## Feature-Based Development Process

### 1. Feature Selection

**Before starting any work:**
1. Review `.trae/project-overview/FEATURE_STATUS.md` for current priorities
2. Check feature dependencies to ensure prerequisites are met
3. Select a feature that aligns with current development objectives
4. Review feature-specific documentation in `.trae/features/[feature-name]/`

### 2. Branch Management

**Creating Feature Branches:**
```bash
# Start from main branch
git checkout main
git pull origin main

# Create feature branch
git checkout -b feature/[feature-name]

# Examples:
git checkout -b feature/user-management
git checkout -b feature/api-integration
git checkout -b feature/dashboard
```

**Branch Naming Convention:**
- `feature/[feature-name]` - Main feature development
- `feature/[feature-name]-[sub-feature]` - Sub-feature or specific component
- `fix/[feature-name]-[issue]` - Bug fixes for specific features
- `docs/[feature-name]` - Documentation updates for features

### 3. Development Cycle

#### Phase 1: Planning
1. **Read Feature Specifications**
   - Review `.trae/features/[feature]/docs/README.md`
   - Study specifications in `.trae/features/[feature]/specs/`
   - Understand requirements and acceptance criteria

2. **Check Dependencies**
   - Verify prerequisite features are complete
   - Review integration points with other features
   - Ensure required APIs or components are available

3. **Update Status**
   - Mark feature as "In Progress" in `FEATURE_STATUS.md`
   - Create or update feature branch
   - Communicate start of work to team

#### Phase 2: Implementation
1. **Follow Specifications**
   - Implement according to feature specs
   - Reference PRD sections as specified
   - Maintain code quality standards

2. **Regular Commits**
   - Make frequent, atomic commits
   - Follow commit message conventions
   - Push to feature branch regularly

3. **Testing**
   - Test functionality as you develop
   - Verify against acceptance criteria
   - Document any issues or blockers

#### Phase 3: Review and Integration
1. **Self Review**
   - Test all functionality thoroughly
   - Check code quality and documentation
   - Verify PRD requirements are met

2. **Pull Request**
   - Create PR with clear description
   - Reference related issues or features
   - Request appropriate reviewers

3. **Update Documentation**
   - Update `FEATURE_STATUS.md` with completion
   - Update `PROJECT_STATUS.md` if needed
   - Document any new dependencies

### 4. Quality Standards

#### Code Quality
- Follow project coding standards
- Implement proper error handling
- Add comprehensive comments
- Ensure security best practices

#### Testing Requirements
- Test all new functionality
- Verify cross-browser compatibility
- Test with different user roles/permissions
- Validate input sanitization and security

#### Documentation
- Update feature documentation
- Add inline code comments
- Update API documentation if applicable
- Keep README files current

### 5. Feature Completion Checklist

- [ ] All acceptance criteria met
- [ ] Code reviewed and approved
- [ ] Tests passing
- [ ] Documentation updated
- [ ] Security validated
- [ ] Performance acceptable
- [ ] Feature status updated
- [ ] Dependencies documented

### 6. Communication Guidelines

#### Daily Updates
- Update feature status in `FEATURE_STATUS.md`
- Communicate blockers or issues promptly
- Share progress in team communications

#### Documentation
- Keep feature docs current
- Document decisions and trade-offs
- Update project status regularly

#### Collaboration
- Review others' code when requested
- Share knowledge and best practices
- Help resolve blockers across features

## Emergency Procedures

### Hotfixes
1. Create hotfix branch from main
2. Implement minimal fix
3. Test thoroughly
4. Fast-track review and merge
5. Update all relevant documentation

### Rollback Process
1. Identify problematic commit/feature
2. Create rollback branch
3. Revert changes safely
4. Test rollback thoroughly
5. Update status documentation

## Tools and Resources

### Key Files
- `.trae/project-overview/PRODUCT_PRD.md` - Requirements reference
- `.trae/project-overview/FEATURE_STATUS.md` - Current feature status
- `.trae/project-overview/PROJECT_STATUS.md` - Overall project progress
- `.trae/features/[feature]/` - Feature-specific documentation

### Development Tools
- Version control: Git
- Code quality: [Specify linting/formatting tools]
- Testing: [Specify testing frameworks]
- Documentation: Markdown files in `.trae/` structure

This workflow ensures consistent, high-quality development while maintaining clear communication and documentation throughout the project lifecycle.
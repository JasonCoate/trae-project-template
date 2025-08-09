# [PROJECT_NAME] Development Workflow

This document outlines the development workflow for the feature-based [PROJECT_NAME] project structure.

## Feature-Based Development Process

### 1. Feature Selection

**Before starting any work:**
1. Review `.trae/project-overview/PROJECT_STATUS.md` for current priorities
2. Check feature dependencies to ensure prerequisites are met
3. Select a feature that aligns with current phase objectives
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
git checkout -b feature/frontend-ui
```

**Branch Naming Convention:**
- `feature/[feature-name]` - Main feature development
- `feature/[feature-name]-[sub-feature]` - Sub-feature or specific component
- `fix/[feature-name]-[issue]` - Bug fixes for specific features
- `docs/[feature-name]` - Documentation updates for features

### 3. Development Cycle

#### Phase 1: Planning
1. **Read Feature Specifications**
   - Review `.trae/features/[feature]/README.md`
   - Study phase-specific specs in `.trae/features/[feature]/specs/`
   - Understand requirements and acceptance criteria

2. **Check Dependencies**
   - Verify prerequisite features are complete
   - Review integration points with other features
   - Ensure required APIs or components are available

3. **Update Documentation**
   - Mark feature as "In Progress" in PROJECT_STATUS.md
   - Update "Current Working Files" section
   - Document planned approach and timeline

#### Phase 2: Implementation
1. **Follow Coding Standards**
   - Adhere to project-specific guidelines in project_rules.md
   - Use established naming conventions
   - Implement proper error handling and validation

2. **Incremental Development**
   - Break feature into small, testable components
   - Commit frequently with descriptive messages
   - Update progress in PROJECT_STATUS.md regularly

3. **Testing as You Go**
   - Test each component before moving to the next
   - Verify integration with existing features
   - Document any issues or blockers immediately

#### Phase 3: Review and Integration
1. **Quality Assurance**
   - Run full test suite
   - Verify cross-browser/platform compatibility
   - Check security and performance implications

2. **Documentation Update**
   - Update feature documentation
   - Mark tasks as complete in PROJECT_STATUS.md
   - Document any architectural decisions or changes

3. **Code Review and Merge**
   - Create pull request with detailed description
   - Address review feedback
   - Merge to main branch after approval

## Workflow Guidelines

### Daily Development Routine
1. **Start of Day:**
   - Check PROJECT_STATUS.md for current priorities
   - Review any blockers or dependencies
   - Plan tasks for the day

2. **During Development:**
   - Update progress regularly
   - Document decisions and blockers
   - Test incrementally

3. **End of Day:**
   - Commit work with descriptive messages
   - Update PROJECT_STATUS.md with progress
   - Note any blockers for next day

### Communication and Documentation
- **Progress Updates:** Update PROJECT_STATUS.md when starting, progressing, or completing tasks
- **Decision Documentation:** Record architectural decisions and trade-offs
- **Blocker Management:** Document blockers immediately with resolution plans
- **Knowledge Sharing:** Update feature documentation for future reference

### Quality Standards
- Follow project coding standards and best practices
- Implement comprehensive error handling and validation
- Test across different user roles and environments
- Ensure responsive design and accessibility compliance
- Validate security measures and input sanitization

### Integration Points
- **API Integration:** Ensure proper error handling and fallbacks
- **Database Changes:** Document schema changes and migration requirements
- **Frontend Components:** Maintain consistency with design system
- **Third-party Services:** Handle service failures gracefully

## Feature Completion Checklist

### Before Marking Feature Complete:
- [ ] All acceptance criteria met
- [ ] Code reviewed and approved
- [ ] Tests passing (unit, integration, e2e)
- [ ] Documentation updated
- [ ] Security review completed
- [ ] Performance impact assessed
- [ ] Cross-browser testing completed
- [ ] Accessibility compliance verified
- [ ] PROJECT_STATUS.md updated

### Post-Completion:
- [ ] Feature branch merged to main
- [ ] Deployment completed (if applicable)
- [ ] Monitoring and alerts configured
- [ ] Team notified of completion
- [ ] Next feature dependencies updated

---

## Emergency Procedures

### Critical Bug Fixes
1. Create hotfix branch from main: `hotfix/[issue-description]`
2. Implement minimal fix with thorough testing
3. Update PROJECT_STATUS.md with emergency status
4. Fast-track review and deployment
5. Document incident and prevention measures

### Rollback Procedures
1. Identify problematic commit/deployment
2. Create rollback branch if needed
3. Update PROJECT_STATUS.md with rollback status
4. Communicate impact and timeline to stakeholders
5. Implement fix and redeploy

---

*This workflow should be adapted based on project-specific requirements and team preferences.*
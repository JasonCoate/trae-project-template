# Git and Version Control Rules

These rules guide AI behavior for git operations and version control practices in this project.

## Feature Branch Workflow

### Branch Management
- **Never commit directly to main branch** - All development must happen on feature branches
- **Create feature branches from main** - Always start new branches from the latest main
- **Branch names MUST match feature folder names** - For feature development, branch names must exactly match the corresponding folder names in `.trae/features/`
  - Example: For `.trae/features/user-management/` → use `feature/user-management`
  - Example: For `.trae/features/api-integration/` → use `feature/api-integration`
  - Example: For `.trae/features/dashboard/` → use `feature/dashboard`
- **Non-feature branches** follow this pattern:
  - `fix/description` - For bug fixes
  - `refactor/description` - For code refactoring
  - `test/description` - For test-related changes
  - `docs/description` - For documentation updates
  - `chore/description` - For maintenance tasks
- **Keep branches focused** - One feature/fix per branch
- **Delete branches after merge** - Clean up merged feature branches

## Conventional Commits Standard

### Commit Message Format
```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Commit Types
- **feat**: A new feature for the user
- **fix**: A bug fix
- **docs**: Documentation only changes
- **style**: Changes that do not affect the meaning of the code (formatting, etc)
- **refactor**: A code change that neither fixes a bug nor adds a feature
- **perf**: A code change that improves performance
- **test**: Adding missing tests or correcting existing tests
- **build**: Changes that affect the build system or external dependencies
- **ci**: Changes to CI configuration files and scripts
- **chore**: Other changes that don't modify src or test files
- **revert**: Reverts a previous commit

### Breaking Changes
- Add `!` after the type/scope for breaking changes: `feat(api)!: change endpoint structure`
- Include `BREAKING CHANGE:` in the footer with description

### Project-Specific Scopes
Use these scopes to categorize changes within the project:
- `[scope1]`: [Description of scope 1]
- `[scope2]`: [Description of scope 2]
- `[scope3]`: [Description of scope 3]
- `[scope4]`: [Description of scope 4]
- `[scope5]`: [Description of scope 5]

### Commit Message Examples
```
feat([scope]): implement [feature] functionality

- Add [component 1]
- Implement [component 2]
- Create [component 3]

Task: [Task reference]
```

```
fix([scope]): resolve [issue] problems

- Add proper [fix detail 1]
- Update [fix detail 2]
- Test [fix detail 3]

Fixes #[issue_number]
```

```
feat([scope])!: change [component] structure

- Update [change 1]
- Migrate [change 2]
- Add [change 3]

BREAKING CHANGE: [Description of breaking change]
```

## AI Workflow Guidelines

### Feature Development Process
1. **Start from main**: Create new feature branch from latest main
2. **Implement incrementally**: Make focused commits for each logical change
3. **Test before committing**: Ensure functionality works before each commit
4. **Reference tasks**: Include task numbers from `.trae/specs/` files in commit messages
5. **Keep commits atomic**: Each commit should represent a complete, working change

### AI Commit Behavior
- **Commit after each task completion** from `.trae/specs/` files
- **Use descriptive commit messages** that explain what was implemented and why
- **Include task references** when completing specification tasks
- **Group related changes** in logical commits (don't split related files)
- **Test functionality** before committing to ensure working state
- **Follow conventional commits** format strictly for consistency

### Branch Workflow for AI
- **Always work on feature branches** - Never commit directly to main
- **Create meaningful branch names** that describe the feature being implemented
- **Keep branches focused** - One feature or fix per branch
- **Commit frequently** with clear, descriptive messages
- **Reference project documentation** in commit messages when implementing specs
-- Seed data for Trae Template Task Management Database
-- Customize these entries per project or delete if not needed.

-- Example Features
INSERT INTO features (name, title, description, phase, priority, status, branch_name, estimated_effort, dependencies, prd_references) VALUES
('example-feature', 'Example Feature', 'Replace with your feature description', 1, 'medium', 'not_started', 'feature/example-feature', '1-2 weeks', '[]', '[]');

-- Example Tasks
INSERT INTO tasks (feature_id, title, description, category, type, status, priority, file_path, checklist_items) VALUES
(1, 'Set up project structure', 'Initialize repo and basic structure', 'documentation', 'write', 'todo', 10, '', '[]'),
(1, 'Implement core module', 'Create the core functionality', 'backend', 'implement', 'todo', 8, '', '[]');

-- Example Branch
INSERT INTO branches (name, feature_id, status) VALUES
('feature/example-feature', 1, 'active');
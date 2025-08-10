-- Trae Template Task Management Database Schema
-- SQLite3 database for centralized task tracking and feature alignment

CREATE TABLE IF NOT EXISTS features (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    title TEXT NOT NULL,
    description TEXT,
    phase INTEGER NOT NULL,
    priority TEXT CHECK(priority IN ('low', 'medium', 'high', 'critical')) DEFAULT 'medium',
    status TEXT CHECK(status IN ('not_started', 'in_progress', 'completed', 'blocked')) DEFAULT 'not_started',
    branch_name TEXT NOT NULL,
    estimated_effort TEXT,
    dependencies TEXT, -- JSON array of feature IDs
    prd_references TEXT, -- JSON array of PRD section references
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    feature_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    category TEXT NOT NULL, -- backend, frontend, testing, documentation (customize as needed)
    type TEXT NOT NULL, -- implement, verify, test, write (customize as needed)
    status TEXT CHECK(status IN ('todo', 'in_progress', 'completed', 'blocked')) DEFAULT 'todo',
    priority INTEGER DEFAULT 0, -- 0=lowest, higher numbers = higher priority
    file_path TEXT, -- Associated file path if applicable
    line_numbers TEXT, -- JSON object with start/end line numbers
    checklist_items TEXT, -- JSON array of sub-tasks
    estimated_hours REAL,
    actual_hours REAL,
    assigned_to TEXT,
    due_date DATE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (feature_id) REFERENCES features (id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS task_dependencies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_id INTEGER NOT NULL,
    depends_on_task_id INTEGER NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (task_id) REFERENCES tasks (id) ON DELETE CASCADE,
    FOREIGN KEY (depends_on_task_id) REFERENCES tasks (id) ON DELETE CASCADE,
    UNIQUE(task_id, depends_on_task_id)
);

CREATE TABLE IF NOT EXISTS branches (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    feature_id INTEGER,
    status TEXT CHECK(status IN ('active', 'merged', 'abandoned')) DEFAULT 'active',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    merged_at DATETIME,
    FOREIGN KEY (feature_id) REFERENCES features (id)
);

CREATE TABLE IF NOT EXISTS work_sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_id INTEGER NOT NULL,
    branch_name TEXT NOT NULL,
    start_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    end_time DATETIME,
    notes TEXT,
    files_modified TEXT, -- JSON array of file paths
    commits TEXT, -- JSON array of commit hashes
    FOREIGN KEY (task_id) REFERENCES tasks (id)
);

-- Indexes for performance
CREATE INDEX IF NOT EXISTS idx_tasks_feature_id ON tasks(feature_id);
CREATE INDEX IF NOT EXISTS idx_tasks_status ON tasks(status);
CREATE INDEX IF NOT EXISTS idx_tasks_priority ON tasks(priority DESC);
CREATE INDEX IF NOT EXISTS idx_features_status ON features(status);
CREATE INDEX IF NOT EXISTS idx_features_phase ON features(phase);
CREATE INDEX IF NOT EXISTS idx_branches_feature_id ON branches(feature_id);
CREATE INDEX IF NOT EXISTS idx_work_sessions_task_id ON work_sessions(task_id);

-- Triggers to update timestamps
CREATE TRIGGER IF NOT EXISTS update_features_timestamp 
    AFTER UPDATE ON features
    BEGIN
        UPDATE features SET updated_at = CURRENT_TIMESTAMP WHERE id = NEW.id;
    END;

CREATE TRIGGER IF NOT EXISTS update_tasks_timestamp 
    AFTER UPDATE ON tasks
    BEGIN
        UPDATE tasks SET updated_at = CURRENT_TIMESTAMP WHERE id = NEW.id;
    END;

-- Views for common queries
CREATE VIEW IF NOT EXISTS active_tasks AS
SELECT 
    t.*,
    f.name as feature_name,
    f.title as feature_title,
    f.branch_name as feature_branch
FROM tasks t
JOIN features f ON t.feature_id = f.id
WHERE t.status IN ('todo', 'in_progress')
ORDER BY t.priority DESC, t.created_at ASC;

CREATE VIEW IF NOT EXISTS feature_progress AS
SELECT 
    f.*,
    COUNT(t.id) as total_tasks,
    COUNT(CASE WHEN t.status = 'completed' THEN 1 END) as completed_tasks,
    COUNT(CASE WHEN t.status = 'in_progress' THEN 1 END) as in_progress_tasks,
    COUNT(CASE WHEN t.status = 'blocked' THEN 1 END) as blocked_tasks,
    ROUND(
        (COUNT(CASE WHEN t.status = 'completed' THEN 1 END) * 100.0) / 
        NULLIF(COUNT(t.id), 0), 2
    ) as completion_percentage
FROM features f
LEFT JOIN tasks t ON f.id = t.feature_id
GROUP BY f.id;
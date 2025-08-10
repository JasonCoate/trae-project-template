#!/usr/bin/env python3
"""
Trae Project Task Management System
SQLite3-based task tracking and branch validation for any Trae project.

This is a template file. Customize PROJECT_IDENTIFIER for your specific project.

Usage:
    python task_manager.py init                    # Initialize database
    python task_manager.py status                  # Show project status
    python task_manager.py validate-branch         # Validate current branch
    python task_manager.py list-tasks [feature]    # List tasks
    python task_manager.py update-task <id> <status> # Update task status
    python task_manager.py sync-markdown           # Sync with PROJECT_STATUS.md
"""

import argparse
import os
import sqlite3
import sys
import textwrap
from datetime import datetime
from typing import Optional

# ---------------
# Template Settings - Customize per project
# ---------------
# Resolve all paths relative to project root to support running CLI from subdirectories
PROJECT_ROOT = os.getcwd()


def _load_dotenv(root: str) -> None:
    """Load environment variables from a .env file at the project root if present.
    This is a minimal parser supporting KEY=VALUE with optional quotes and comments.
    Existing environment variables are not overridden.
    """
    try:
        dotenv_path = os.path.join(root, '.env')
        if not os.path.isfile(dotenv_path):
            return
        with open(dotenv_path, 'r', encoding='utf-8') as f:
            for raw in f:
                line = raw.strip()
                if not line or line.startswith('#'):
                    continue
                if '=' not in line:
                    continue
                key, val = line.split('=', 1)
                key = key.strip()
                val = val.strip().strip('"').strip("'")
                if key and key not in os.environ:
                    os.environ[key] = val
    except Exception:
        # Silently ignore .env parse errors to avoid breaking CLI usage
        pass


# Load .env before resolving project identifier
_load_dotenv(PROJECT_ROOT)


def _read_project_id_file(root: str) -> Optional[str]:
    try:
        pid_path = os.path.join(root, '.trae', 'project-id')
        if os.path.isfile(pid_path):
            with open(pid_path, 'r', encoding='utf-8') as f:
                val = f.read().strip()
                return val or None
    except Exception:
        return None
    return None


PROJECT_IDENTIFIER = os.environ.get('TRAE_PROJECT_ID') or _read_project_id_file(PROJECT_ROOT) or os.path.basename(PROJECT_ROOT)
DB_DIR = os.path.join(PROJECT_ROOT, '.trae', 'task-management')
DB_PATH = os.path.join(DB_DIR, f'{PROJECT_IDENTIFIER}.db')
SCHEMA_FILE = os.path.join(DB_DIR, 'schema.sql')
SEED_FILE = os.path.join(DB_DIR, 'seed_data.sql')
PROJECT_STATUS_MD = os.path.join(PROJECT_ROOT, '.trae', 'project-overview', 'PROJECT_STATUS.md')
FEATURES_DIR = os.path.join(PROJECT_ROOT, '.trae', 'features')


# ----------
# Utilities
# ----------
class Console:
    @staticmethod
    def info(msg):
        print(f"[INFO] {msg}")

    @staticmethod
    def warn(msg):
        print(f"[WARN] {msg}")

    @staticmethod
    def error(msg):
        print(f"[ERROR] {msg}")


def find_project_root():
    """Find the project root directory"""
    current = os.getcwd()
    
    # Look for PROJECT_IDENTIFIER.php first, then other common indicators
    root_indicators = [
        f'{PROJECT_IDENTIFIER}.php',
        'package.json',
        'composer.json',
        'requirements.txt',
        'Cargo.toml',
        'go.mod',
        '.git',
        'pyproject.toml',
        'pom.xml'
    ]
    
    while current != '/':
        for indicator in root_indicators:
            if os.path.exists(os.path.join(current, indicator)):
                return current
        current = os.path.dirname(current)
    
    # Fallback to current directory
    return os.getcwd()


def ensure_dirs():
    os.makedirs(DB_DIR, exist_ok=True)


def get_db_connection():
    ensure_dirs()
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def run_sql_script(conn, file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        script = f.read()
    conn.executescript(script)
    conn.commit()


# -------------------------
# Database Init and Seeding
# -------------------------

def init_db(seed=False):
    conn = get_db_connection()
    if not os.path.exists(SCHEMA_FILE):
        Console.error(f"Schema file not found at {SCHEMA_FILE}")
        sys.exit(1)
    
    Console.info("Initializing database schema...")
    run_sql_script(conn, SCHEMA_FILE)
    
    if seed and os.path.exists(SEED_FILE):
        Console.info("Seeding database with example data...")
        run_sql_script(conn, SEED_FILE)
    
    Console.info(f"Database initialized at {DB_PATH}")


# ---------------------
# Feature/Task Queries
# ---------------------

def fetch_features(conn):
    return conn.execute("SELECT * FROM feature_progress ORDER BY phase ASC, priority DESC, id ASC").fetchall()


def fetch_tasks_by_feature(conn, feature_id):
    return conn.execute(
        "SELECT * FROM tasks WHERE feature_id = ? ORDER BY priority DESC, id ASC",
        (feature_id,)
    ).fetchall()


def list_tasks(conn, feature_name=None):
    if feature_name:
        feature = conn.execute("SELECT id, name FROM features WHERE name = ?", (feature_name,)).fetchone()
        if not feature:
            Console.error(f"Feature '{feature_name}' not found.")
            sys.exit(1)
        tasks = fetch_tasks_by_feature(conn, feature['id'])
        return feature, tasks
    else:
        tasks = conn.execute(
            "SELECT t.*, f.name as feature_name FROM tasks t JOIN features f ON t.feature_id = f.id ORDER BY t.status ASC, t.priority DESC, t.id ASC"
        ).fetchall()
        return None, tasks


def update_task_status(conn, task_id, status):
    valid = {'todo', 'in_progress', 'completed', 'blocked'}
    if status not in valid:
        Console.error(f"Invalid status '{status}'. Valid: {', '.join(valid)}")
        sys.exit(1)
    
    cur = conn.execute("UPDATE tasks SET status = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?", (status, task_id))
    conn.commit()
    
    if cur.rowcount == 0:
        Console.warn(f"Task {task_id} not found.")
    else:
        Console.info(f"Task {task_id} updated to '{status}'.")


# ----------------------
# Branch Validations
# ----------------------

def get_current_branch():
    """Get current Git branch name"""
    try:
        import subprocess
        result = subprocess.run(
            ['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
            capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    except Exception:
        return "unknown"


def validate_branch(conn, current_branch):
    """Enforce branch names to match features folder names"""
    expected_dirs = []
    if os.path.isdir(FEATURES_DIR):
        expected_dirs = [d for d in os.listdir(FEATURES_DIR) if os.path.isdir(os.path.join(FEATURES_DIR, d))]
    
    valid_branches = {f"feature/{d}" for d in expected_dirs}

    if current_branch not in valid_branches:
        Console.warn("Branch name does not match a feature folder in .trae/features/")
        if expected_dirs:
            Console.info("Valid branch names:")
            for d in sorted(expected_dirs):
                print(f"  - feature/{d}")
        else:
            Console.info("No feature folders found. Create one under .trae/features/<feature-name>/")
        return False

    # If feature exists in DB, ensure mapping
    feature_name = current_branch.split('/', 1)[1]
    feature = conn.execute("SELECT id, branch_name FROM features WHERE name = ?", (feature_name,)).fetchone()
    if feature:
        if feature['branch_name'] != current_branch:
            Console.warn(f"Feature '{feature_name}' exists but branch_name differs (DB: {feature['branch_name']}, Current: {current_branch}). Updating DB...")
            conn.execute("UPDATE features SET branch_name = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?", (current_branch, feature['id']))
            conn.commit()
    
    return True


# ----------------------
# Markdown Sync
# ----------------------

def generate_markdown_content(conn):
    features = fetch_features(conn)
    lines = []
    
    lines.append(f"# {PROJECT_IDENTIFIER} Project Status\n\n")
    lines.append(f"**Project:** {PROJECT_IDENTIFIER}  \n")
    lines.append(f"**Version:** 1.0  \n")
    lines.append(f"**Current Phase:** Phase 1 (Foundation)  \n")
    lines.append(f"**Last Updated:** {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC  \n")
    lines.append(f"**Current Branch:** {get_current_branch()}  \n\n")
    lines.append("---\n\n")
    lines.append("## Project Overview\n\n")
    lines.append("[Customize this section with your project description]\n\n")
    lines.append("### Phase Timeline\n")
    lines.append("- **Phase 1:** Foundation (Customize phases for your project)\n")
    lines.append("- **Phase 2:** Implementation\n")
    lines.append("- **Phase 3:** Enhancement\n\n")
    lines.append("---\n\n")
    lines.append("## Features Progress\n\n")

    for f in features:
        completion = f['completion_percentage'] or 0
        status_emoji = {
            'completed': '✅',
            'in_progress': '🔄',
            'not_started': '⏳',
            'blocked': '🚫'
        }.get(f['status'], '❓')
        
        lines.append(f"### {status_emoji} {f['title']} ({completion:.1f}% complete)\n")
        lines.append(f"**Branch:** `{f['branch_name']}`  \n")
        lines.append(f"**Phase:** {f['phase']} | **Priority:** {f['priority']} | **Status:** {f['status']}  \n")
        if f['description']:
            lines.append(f"{f['description']}\n")
        lines.append(f"**Tasks:** {f['total_tasks']} total, {f['completed_tasks']} completed, {f['in_progress_tasks']} in progress\n\n")

        tasks = fetch_tasks_by_feature(conn, f['id'])
        if tasks:
            lines.append("#### Tasks\n")
            for t in tasks:
                status_emoji = {
                    'completed': '✅',
                    'in_progress': '🔄',
                    'todo': '⏳',
                    'blocked': '🚫'
                }.get(t['status'], '❓')
                lines.append(f"- {status_emoji} (#{t['id']}) [p{t['priority']}] {t['title']} — {t['status']}\n")
            lines.append("\n")

    lines.append("---\n\n")
    lines.append("*This file is automatically generated from the task management database.*\n")
    lines.append(f"*Last updated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC*\n")
    
    return ''.join(lines)


def sync_markdown(conn):
    content = generate_markdown_content(conn)
    os.makedirs(os.path.dirname(PROJECT_STATUS_MD), exist_ok=True)
    with open(PROJECT_STATUS_MD, 'w', encoding='utf-8') as f:
        f.write(content)
    Console.info(f"Synced project status to {PROJECT_STATUS_MD}")


# ----------------------
# CLI Interface
# ----------------------

def main():
    parser = argparse.ArgumentParser(description='Trae Project Task Manager CLI')
    sub = parser.add_subparsers(dest='command')

    # Init command
    init_cmd = sub.add_parser('init', help='Initialize the task database from schema.sql')
    init_cmd.add_argument('--seed', action='store_true', help='Seed with example data')

    # Status command
    sub.add_parser('status', help='Print features and summary status')

    # Validate branch command
    validate_cmd = sub.add_parser('validate-branch', help='Validate current branch naming against .trae/features/')
    validate_cmd.add_argument('--branch', help='Branch name to validate (default: from git)')

    # List tasks command
    list_cmd = sub.add_parser('list-tasks', help='List tasks across features or for a specific feature')
    list_cmd.add_argument('--feature', help='Feature name (folder under .trae/features)')

    # Update task command
    update_cmd = sub.add_parser('update-task', help='Update a task status')
    update_cmd.add_argument('id', type=int, help='Task ID')
    update_cmd.add_argument('status', choices=['todo', 'in_progress', 'completed', 'blocked'], help='New status')

    # Sync markdown command
    sub.add_parser('sync-markdown', help='Write PROJECT_STATUS.md from DB')

    args = parser.parse_args()

    if args.command == 'init':
        init_db(seed=args.seed)
        return

    # For all other commands, require database to exist
    if not os.path.exists(DB_PATH):
        Console.error(f"Database not found at {DB_PATH}. Run 'python task_manager.py init' first.")
        sys.exit(1)

    conn = get_db_connection()

    if args.command == 'status':
        features = fetch_features(conn)
        print(f"\n📊 {PROJECT_IDENTIFIER} Project Status")
        print(f"{'='*50}")
        for f in features:
            completion = f['completion_percentage'] or 0
            status_emoji = {
                'completed': '✅',
                'in_progress': '🔄',
                'not_started': '⏳',
                'blocked': '🚫'
            }.get(f['status'], '❓')
            print(f"{status_emoji} {f['title']} ({f['name']}) - Phase {f['phase']} - {f['status']} - {completion:.1f}% complete")
        return

    if args.command == 'validate-branch':
        branch = args.branch or get_current_branch()
        if branch == "unknown":
            Console.error('Could not determine current branch. Pass --branch <name>.')
            sys.exit(1)
        ok = validate_branch(conn, branch)
        sys.exit(0 if ok else 2)

    if args.command == 'list-tasks':
        feature, tasks = list_tasks(conn, feature_name=args.feature)
        if feature:
            print(f"Tasks for feature: {feature['name']}")
        for t in tasks:
            status_emoji = {
                'todo': '⏳',
                'in_progress': '🔄',
                'completed': '✅',
                'blocked': '🚫'
            }.get(t['status'], '❓')
            feature_name = getattr(t, 'feature_name', '')
            feature_part = f" ({feature_name})" if feature_name else ""
            print(f"{status_emoji} (#{t['id']}) [p{t['priority']}] {t['title']} — {t['status']}{feature_part}")
        return

    if args.command == 'update-task':
        update_task_status(conn, args.id, args.status)
        return

    if args.command == 'sync-markdown':
        sync_markdown(conn)
        return

    parser.print_help()


if __name__ == '__main__':
    main()
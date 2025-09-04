"""
Project Manager Module
=====================
Handles project setup, organization, and file management for hackathons
"""

import os
import json
import asyncio
import shutil
from typing import Dict, List, Any, Optional
from pathlib import Path
from datetime import datetime

class ProjectManager:
    """Manages hackathon project structure and organization"""
    
    def __init__(self):
        self.project_templates = self._load_project_templates()
        self.current_project = None
    
    def _load_project_templates(self) -> Dict:
        """Load project templates for different types"""
        return {
            "web_app": {
                "structure": [
                    "frontend/src/components",
                    "frontend/src/pages", 
                    "frontend/src/utils",
                    "frontend/public",
                    "backend/app",
                    "backend/models",
                    "backend/routes",
                    "backend/utils",
                    "database",
                    "docs",
                    "tests",
                    "deploy"
                ],
                "files": {
                    "README.md": "# {project_name}\n\nHackathon project created with AI Assistant\n\n## Quick Start\n\n```bash\n# Backend\ncd backend\npip install -r requirements.txt\npython main.py\n\n# Frontend\ncd frontend\nnpm install\nnpm start\n```",
                    ".gitignore": "*.pyc\n__pycache__/\nnode_modules/\n.env\ndist/\nbuild/\n.DS_Store",
                    "docker-compose.yml": "version: '3.8'\nservices:\n  app:\n    build: .\n    ports:\n      - '8000:8000'"
                }
            },
            "api": {
                "structure": [
                    "app",
                    "models", 
                    "routes",
                    "utils",
                    "tests",
                    "docs"
                ],
                "files": {
                    "README.md": "# {project_name} API\n\nRESTful API for hackathon project",
                    "requirements.txt": "fastapi\nuvicorn\npydantic\nsqlalchemy\npsycopg2-binary",
                    "main.py": "from fastapi import FastAPI\n\napp = FastAPI()\n\n@app.get('/')\ndef root():\n    return {'message': 'API is running!'}"
                }
            },
            "data_science": {
                "structure": [
                    "data/raw",
                    "data/processed",
                    "notebooks",
                    "src",
                    "models",
                    "reports",
                    "visualizations"
                ],
                "files": {
                    "README.md": "# {project_name}\n\nData Science project for hackathon",
                    "requirements.txt": "pandas\nnumpy\nscikit-learn\nmatplotlib\nseaborn\njupyter",
                    "main.py": "import pandas as pd\nimport numpy as np\n\nprint('Data Science project initialized!')"
                }
            }
        }
    
    async def setup_project(self, project_name: str, tech_stack: Dict, idea: Dict) -> str:
        """
        Setup a new hackathon project with optimal structure
        
        Args:
            project_name: Name of the project
            tech_stack: Technology stack information
            idea: Project idea details
            
        Returns:
            Path to the created project
        """
        # Sanitize project name
        safe_name = self._sanitize_name(project_name)
        project_path = Path.cwd() / safe_name
        
        # Determine project type
        project_type = self._determine_project_type(tech_stack, idea)
        
        # Create project structure
        await self._create_project_structure(project_path, project_type, project_name)
        
        # Generate project files
        await self._generate_project_files(project_path, project_type, project_name, tech_stack, idea)
        
        # Initialize git repository
        await self._init_git_repo(project_path)
        
        # Create project metadata
        metadata = {
            "name": project_name,
            "type": project_type,
            "tech_stack": tech_stack,
            "idea": idea,
            "created_at": datetime.now().isoformat(),
            "structure": self.project_templates[project_type]["structure"]
        }
        
        await self._save_metadata(project_path, metadata)
        
        self.current_project = {
            "name": project_name,
            "path": str(project_path),
            "type": project_type,
            "metadata": metadata
        }
        
        return str(project_path)
    
    async def create_app_structure(self, project_name: str, app_type: str, components: Dict) -> str:
        """Create application structure with generated components"""
        project_path = Path(self.current_project["path"]) if self.current_project else Path.cwd() / project_name
        
        # Create directories for each component type
        for component_type, files in components.items():
            component_dir = project_path / component_type
            component_dir.mkdir(parents=True, exist_ok=True)
            
            # Write files
            for file_path, content in files.items():
                full_path = component_dir / file_path
                full_path.parent.mkdir(parents=True, exist_ok=True)
                
                with open(full_path, 'w', encoding='utf-8') as f:
                    f.write(content)
        
        return str(project_path)
    
    def _determine_project_type(self, tech_stack: Dict, idea: Dict) -> str:
        """Determine the best project template based on tech stack and idea"""
        primary_stack = tech_stack.get("primary", [])
        
        if any(tech in primary_stack for tech in ["react", "vue", "angular"]) and \
           any(tech in primary_stack for tech in ["fastapi", "flask", "express"]):
            return "web_app"
        elif any(tech in primary_stack for tech in ["fastapi", "flask", "express", "django"]):
            return "api"
        elif any(tech in primary_stack for tech in ["pandas", "numpy", "tensorflow", "pytorch"]):
            return "data_science"
        else:
            return "web_app"  # Default to web app
    
    async def _create_project_structure(self, project_path: Path, project_type: str, project_name: str):
        """Create the directory structure for the project"""
        project_path.mkdir(parents=True, exist_ok=True)
        
        template = self.project_templates.get(project_type, self.project_templates["web_app"])
        
        for directory in template["structure"]:
            dir_path = project_path / directory
            dir_path.mkdir(parents=True, exist_ok=True)
    
    async def _generate_project_files(self, project_path: Path, project_type: str, project_name: str, tech_stack: Dict, idea: Dict):
        """Generate initial project files"""
        template = self.project_templates.get(project_type, self.project_templates["web_app"])
        
        for file_name, content in template["files"].items():
            file_path = project_path / file_name
            
            # Replace placeholders in content
            formatted_content = content.format(
                project_name=project_name,
                **tech_stack,
                **idea
            )
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(formatted_content)
    
    async def _init_git_repo(self, project_path: Path):
        """Initialize git repository"""
        try:
            import subprocess
            result = subprocess.run(
                ["git", "init"],
                cwd=project_path,
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                # Add initial commit
                subprocess.run(["git", "add", "."], cwd=project_path)
                subprocess.run(
                    ["git", "commit", "-m", "Initial commit - Hackathon project setup"],
                    cwd=project_path,
                    capture_output=True
                )
        except Exception:
            pass  # Git not available, skip
    
    async def _save_metadata(self, project_path: Path, metadata: Dict):
        """Save project metadata"""
        metadata_path = project_path / ".hackathon_metadata.json"
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2)
    
    def _sanitize_name(self, name: str) -> str:
        """Sanitize project name for filesystem"""
        # Remove special characters and spaces
        import re
        sanitized = re.sub(r'[^\w\-_]', '_', name)
        return sanitized.lower()
    
    async def add_feature(self, feature_name: str, feature_type: str = "component") -> Dict:
        """Add a new feature to the current project"""
        if not self.current_project:
            raise ValueError("No active project")
        
        project_path = Path(self.current_project["path"])
        
        # Determine where to add the feature based on project type
        if feature_type == "component" and self.current_project["type"] == "web_app":
            # Add React component
            component_path = project_path / "frontend" / "src" / "components" / f"{feature_name.title()}.js"
            component_content = self._generate_component_template(feature_name)
            
            with open(component_path, 'w', encoding='utf-8') as f:
                f.write(component_content)
            
        elif feature_type == "api" and self.current_project["type"] in ["web_app", "api"]:
            # Add API endpoint
            route_path = project_path / "backend" / "routes" / f"{feature_name.lower()}.py"
            route_content = self._generate_route_template(feature_name)
            
            with open(route_path, 'w', encoding='utf-8') as f:
                f.write(route_content)
        
        return {
            "feature": feature_name,
            "type": feature_type,
            "location": str(component_path if 'component_path' in locals() else route_path),
            "status": "created"
        }
    
    def _generate_component_template(self, component_name: str) -> str:
        """Generate a basic React component template"""
        return f"""import React, {{ useState }} from 'react';

const {component_name.title()} = () => {{
    const [loading, setLoading] = useState(false);

    return (
        <div className="{component_name.lower()}">
            <h2>{component_name.title()}</h2>
            <p>Feature implementation goes here</p>
        </div>
    );
}};

export default {component_name.title()};
"""
    
    def _generate_route_template(self, route_name: str) -> str:
        """Generate a basic FastAPI route template"""
        return f"""from fastapi import APIRouter, HTTPException
from typing import List

router = APIRouter(prefix="/{route_name.lower()}", tags=["{route_name.title()}"])

@router.get("/")
async def get_{route_name.lower()}s():
    \"\"\"Get all {route_name.lower()} items\"\"\"
    return {{"message": "List of {route_name.lower()} items"}}

@router.post("/")
async def create_{route_name.lower()}(item: dict):
    \"\"\"Create a new {route_name.lower()} item\"\"\"
    return {{"message": f"Created {route_name.lower()}: {{item}}"}}

@router.get("/{{item_id}}")
async def get_{route_name.lower()}(item_id: int):
    \"\"\"Get a specific {route_name.lower()} item\"\"\"
    return {{"id": item_id, "message": f"{route_name.title()} item"}}
"""
    
    async def get_project_status(self) -> Dict:
        """Get current project status and health"""
        if not self.current_project:
            return {"status": "No active project"}
        
        project_path = Path(self.current_project["path"])
        
        # Check file counts
        file_counts = {}
        for root, dirs, files in os.walk(project_path):
            rel_path = os.path.relpath(root, project_path)
            if rel_path != ".":
                file_counts[rel_path] = len(files)
        
        # Check if git repo
        has_git = (project_path / ".git").exists()
        
        # Check for common files
        has_readme = (project_path / "README.md").exists()
        has_requirements = any((project_path / f).exists() for f in ["requirements.txt", "package.json"])
        
        return {
            "project": self.current_project["name"],
            "path": self.current_project["path"],
            "type": self.current_project["type"],
            "file_counts": file_counts,
            "has_git": has_git,
            "has_readme": has_readme,
            "has_dependencies": has_requirements,
            "metadata": self.current_project.get("metadata", {})
        }
    
    async def backup_project(self, backup_name: str = None) -> str:
        """Create a backup of the current project"""
        if not self.current_project:
            raise ValueError("No active project")
        
        project_path = Path(self.current_project["path"])
        
        if not backup_name:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_name = f"{self.current_project['name']}_backup_{timestamp}"
        
        backup_path = project_path.parent / backup_name
        
        # Copy entire project directory
        shutil.copytree(project_path, backup_path)
        
        return str(backup_path)
    
    async def load_project(self, project_path: str) -> Dict:
        """Load an existing project"""
        path = Path(project_path)
        metadata_file = path / ".hackathon_metadata.json"
        
        if metadata_file.exists():
            with open(metadata_file, 'r', encoding='utf-8') as f:
                metadata = json.load(f)
            
            self.current_project = {
                "name": metadata["name"],
                "path": str(path),
                "type": metadata["type"],
                "metadata": metadata
            }
            
            return self.current_project
        else:
            raise ValueError("Not a valid hackathon project (missing metadata)")
    
    def get_templates(self) -> Dict:
        """Get available project templates"""
        return {
            name: {
                "description": f"Template for {name.replace('_', ' ')} projects",
                "structure": template["structure"],
                "files": list(template["files"].keys())
            }
            for name, template in self.project_templates.items()
        }
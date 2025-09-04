"""
Deployment Helper Module
=======================
Handles rapid deployment of hackathon projects to various platforms
"""

import asyncio
import json
import subprocess
from typing import Dict, List, Any, Optional
from pathlib import Path

class DeploymentHelper:
    """Handles deployment to various platforms optimized for hackathon demos"""
    
    def __init__(self):
        self.platforms = self._load_deployment_platforms()
        self.configs = self._load_deployment_configs()
    
    def _load_deployment_platforms(self) -> Dict:
        """Load supported deployment platforms"""
        return {
            "vercel": {
                "type": "frontend",
                "supported_frameworks": ["react", "vue", "angular", "static"],
                "deployment_time": "2-3 minutes",
                "custom_domain": True,
                "https": True,
                "cost": "free"
            },
            "netlify": {
                "type": "frontend", 
                "supported_frameworks": ["react", "vue", "angular", "static"],
                "deployment_time": "2-3 minutes",
                "custom_domain": True,
                "https": True,
                "cost": "free"
            },
            "heroku": {
                "type": "fullstack",
                "supported_frameworks": ["python", "node", "java", "php"],
                "deployment_time": "5-10 minutes",
                "custom_domain": True,
                "https": True,
                "cost": "free tier available"
            },
            "railway": {
                "type": "fullstack",
                "supported_frameworks": ["python", "node", "go", "rust"],
                "deployment_time": "3-5 minutes", 
                "custom_domain": True,
                "https": True,
                "cost": "free tier available"
            },
            "render": {
                "type": "fullstack",
                "supported_frameworks": ["python", "node", "go", "ruby"],
                "deployment_time": "5-8 minutes",
                "custom_domain": True,
                "https": True,
                "cost": "free tier available"
            }
        }
    
    def _load_deployment_configs(self) -> Dict:
        """Load deployment configuration templates"""
        return {
            "vercel": {
                "config_file": "vercel.json",
                "config_content": {
                    "builds": [{"src": "package.json", "use": "@vercel/static-build"}],
                    "routes": [{"src": "/(.*)", "dest": "/index.html"}]
                }
            },
            "netlify": {
                "config_file": "netlify.toml", 
                "config_content": """[build]
  publish = "build"
  command = "npm run build"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
"""
            },
            "heroku": {
                "config_file": "Procfile",
                "config_content": "web: uvicorn main:app --host=0.0.0.0 --port=${PORT:-5000}"
            }
        }
    
    async def deploy_project(self, project_path: str, tech_stack: Dict) -> Optional[str]:
        """
        Deploy project to the best platform based on tech stack
        
        Args:
            project_path: Path to the project
            tech_stack: Technology stack information
            
        Returns:
            Deployment URL if successful
        """
        # Select best platform
        platform = self._select_best_platform(tech_stack)
        
        # Prepare project for deployment
        await self._prepare_for_deployment(project_path, platform, tech_stack)
        
        # Deploy to platform
        deployment_url = await self._deploy_to_platform(project_path, platform)
        
        return deployment_url
    
    def _select_best_platform(self, tech_stack: Dict) -> str:
        """Select the best deployment platform based on tech stack"""
        primary_stack = tech_stack.get("primary", [])
        
        # Frontend-only projects
        if any(tech in primary_stack for tech in ["react", "vue", "angular"]) and \
           not any(tech in primary_stack for tech in ["python", "node", "java"]):
            return "vercel"  # Best for frontend
        
        # Python projects
        elif "python" in primary_stack or "fastapi" in primary_stack or "flask" in primary_stack:
            return "railway"  # Good Python support
        
        # Node.js projects
        elif "node" in primary_stack or "express" in primary_stack:
            return "vercel"  # Excellent Node.js support
        
        # Default to Heroku for full-stack
        else:
            return "heroku"
    
    async def _prepare_for_deployment(self, project_path: str, platform: str, tech_stack: Dict):
        """Prepare project files for deployment"""
        path = Path(project_path)
        
        # Create deployment configuration
        config = self.configs.get(platform)
        if config:
            config_path = path / config["config_file"]
            
            if config["config_file"].endswith(".json"):
                with open(config_path, 'w') as f:
                    json.dump(config["config_content"], f, indent=2)
            else:
                with open(config_path, 'w') as f:
                    f.write(config["config_content"])
        
        # Create environment variables template
        env_example = path / ".env.example"
        if not env_example.exists():
            env_content = self._generate_env_template(tech_stack)
            with open(env_example, 'w') as f:
                f.write(env_content)
        
        # Ensure build scripts exist
        await self._ensure_build_scripts(path, platform, tech_stack)
    
    def _generate_env_template(self, tech_stack: Dict) -> str:
        """Generate environment variables template"""
        env_vars = [
            "# Environment Variables",
            "NODE_ENV=production",
            "PORT=8000"
        ]
        
        primary_stack = tech_stack.get("primary", [])
        
        if "database" in primary_stack:
            env_vars.extend([
                "DATABASE_URL=your_database_url_here",
                "DB_NAME=your_database_name"
            ])
        
        if "auth" in tech_stack.get("features", []):
            env_vars.extend([
                "JWT_SECRET=your_jwt_secret_here",
                "AUTH_SECRET=your_auth_secret_here"
            ])
        
        return "\n".join(env_vars)
    
    async def _ensure_build_scripts(self, project_path: Path, platform: str, tech_stack: Dict):
        """Ensure necessary build scripts exist"""
        primary_stack = tech_stack.get("primary", [])
        
        # For React projects
        if "react" in primary_stack:
            package_json = project_path / "package.json"
            if package_json.exists():
                with open(package_json, 'r') as f:
                    package_data = json.load(f)
                
                # Ensure build script exists
                if "scripts" not in package_data:
                    package_data["scripts"] = {}
                
                if "build" not in package_data["scripts"]:
                    package_data["scripts"]["build"] = "react-scripts build"
                
                with open(package_json, 'w') as f:
                    json.dump(package_data, f, indent=2)
        
        # For Python projects
        elif any(tech in primary_stack for tech in ["python", "fastapi", "flask"]):
            requirements_file = project_path / "requirements.txt"
            if not requirements_file.exists():
                requirements = self._generate_python_requirements(tech_stack)
                with open(requirements_file, 'w') as f:
                    f.write(requirements)
    
    def _generate_python_requirements(self, tech_stack: Dict) -> str:
        """Generate Python requirements for deployment"""
        requirements = ["gunicorn==21.2.0"]  # For production WSGI server
        
        primary_stack = tech_stack.get("primary", [])
        
        if "fastapi" in primary_stack:
            requirements.extend([
                "fastapi==0.104.0",
                "uvicorn==0.24.0"
            ])
        elif "flask" in primary_stack:
            requirements.extend([
                "flask==3.0.0",
                "flask-cors==4.0.0"
            ])
        
        return "\n".join(requirements)
    
    async def _deploy_to_platform(self, project_path: str, platform: str) -> Optional[str]:
        """Deploy to the specified platform"""
        path = Path(project_path)
        
        try:
            if platform == "vercel":
                return await self._deploy_vercel(path)
            elif platform == "netlify":
                return await self._deploy_netlify(path)
            elif platform == "heroku":
                return await self._deploy_heroku(path)
            elif platform == "railway":
                return await self._deploy_railway(path)
            else:
                return await self._deploy_generic(path, platform)
        
        except Exception as e:
            print(f"Deployment failed: {e}")
            return None
    
    async def _deploy_vercel(self, project_path: Path) -> Optional[str]:
        """Deploy to Vercel"""
        try:
            # Check if Vercel CLI is installed
            result = subprocess.run(["vercel", "--version"], capture_output=True, text=True)
            if result.returncode != 0:
                print("Vercel CLI not installed. Please install with: npm i -g vercel")
                return None
            
            # Deploy
            result = subprocess.run(
                ["vercel", "--prod", "--yes"],
                cwd=project_path,
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                # Extract URL from output
                lines = result.stdout.split('\n')
                for line in lines:
                    if 'https://' in line and 'vercel.app' in line:
                        return line.strip()
            
            return None
            
        except Exception as e:
            print(f"Vercel deployment error: {e}")
            return None
    
    async def _deploy_netlify(self, project_path: Path) -> Optional[str]:
        """Deploy to Netlify"""
        try:
            # Build the project first
            build_result = subprocess.run(
                ["npm", "run", "build"],
                cwd=project_path,
                capture_output=True,
                text=True
            )
            
            if build_result.returncode != 0:
                print("Build failed")
                return None
            
            # Deploy with Netlify CLI
            result = subprocess.run(
                ["netlify", "deploy", "--prod", "--dir=build"],
                cwd=project_path,
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                # Extract URL from output
                lines = result.stdout.split('\n')
                for line in lines:
                    if 'https://' in line and 'netlify.app' in line:
                        return line.strip()
            
            return None
            
        except Exception:
            return None
    
    async def _deploy_heroku(self, project_path: Path) -> Optional[str]:
        """Deploy to Heroku"""
        try:
            # Create Heroku app
            app_name = f"hackathon-{project_path.name.lower()}"
            
            result = subprocess.run(
                ["heroku", "create", app_name],
                cwd=project_path,
                capture_output=True,
                text=True
            )
            
            # Deploy via git
            subprocess.run(["git", "add", "."], cwd=project_path)
            subprocess.run(
                ["git", "commit", "-m", "Deploy to Heroku"],
                cwd=project_path,
                capture_output=True
            )
            
            deploy_result = subprocess.run(
                ["git", "push", "heroku", "main"],
                cwd=project_path,
                capture_output=True,
                text=True
            )
            
            if deploy_result.returncode == 0:
                return f"https://{app_name}.herokuapp.com"
            
            return None
            
        except Exception:
            return None
    
    async def _deploy_railway(self, project_path: Path) -> Optional[str]:
        """Deploy to Railway"""
        try:
            result = subprocess.run(
                ["railway", "up"],
                cwd=project_path,
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                # Railway will provide the URL in the output
                lines = result.stdout.split('\n')
                for line in lines:
                    if 'https://' in line and 'railway.app' in line:
                        return line.strip()
            
            return None
            
        except Exception:
            return None
    
    async def _deploy_generic(self, project_path: Path, platform: str) -> Optional[str]:
        """Generic deployment instructions"""
        instructions = {
            "render": [
                "1. Push code to GitHub",
                "2. Connect repository in Render dashboard",
                "3. Configure build and start commands",
                "4. Deploy automatically"
            ]
        }
        
        print(f"Manual deployment steps for {platform}:")
        for step in instructions.get(platform, ["Check platform documentation"]):
            print(f"  {step}")
        
        return f"Manual deployment required for {platform}"
    
    async def check_deployment_status(self, url: str) -> Dict:
        """Check if deployment is working"""
        try:
            import requests
            response = requests.get(url, timeout=10)
            
            return {
                "url": url,
                "status": "healthy" if response.status_code == 200 else "unhealthy",
                "status_code": response.status_code,
                "response_time": response.elapsed.total_seconds()
            }
        
        except Exception as e:
            return {
                "url": url,
                "status": "error",
                "error": str(e)
            }
    
    async def get_help(self, query: str, context: Dict) -> Dict:
        """Get help with deployment"""
        suggestions = [
            "Deploy project: 'Deploy my React app'",
            "Platform recommendation: 'Best platform for Python FastAPI?'",
            "Setup deployment: 'How to prepare for deployment?'",
            "Check status: 'Is my deployment working?'"
        ]
        
        return {
            "response": f"I can help you with deployment: {query}",
            "suggestions": suggestions,
            "examples": {
                "deploy": "await assistant.deployment_helper.deploy_project('./my-project', tech_stack)",
                "platforms": "assistant.deployment_helper.platforms.keys()",
                "status": "await assistant.deployment_helper.check_deployment_status(url)"
            }
        }
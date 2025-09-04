#!/usr/bin/env python3
"""
Ultimate Hackathon AI Assistant
==============================
Your complete AI companion for dominating hackathons!
Equipped with coding, development, programming, and design skills.
"""

import os
import sys
import json
import asyncio
import logging
from datetime import datetime
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
import subprocess
from pathlib import Path

# Import specialized modules
from modules.code_generator import CodeGenerator
from modules.project_manager import ProjectManager
from modules.idea_generator import IdeaGenerator
from modules.design_assistant import DesignAssistant
from modules.deployment_helper import DeploymentHelper
from modules.research_agent import ResearchAgent
from modules.pitch_assistant import PitchAssistant
from modules.tech_stack_advisor import TechStackAdvisor

class HackathonAIAssistant:
    """
    The Ultimate Hackathon AI Assistant
    
    Features:
    - Multi-language code generation
    - Project planning and management
    - Idea generation and validation
    - UI/UX design assistance
    - Rapid deployment
    - Market research
    - Pitch deck creation
    - Technology recommendations
    """
    
    def __init__(self, config_file: str = "config.json"):
        self.config = self._load_config(config_file)
        self.setup_logging()
        
        # Initialize specialized modules
        self.code_generator = CodeGenerator()
        self.project_manager = ProjectManager()
        self.idea_generator = IdeaGenerator()
        self.design_assistant = DesignAssistant()
        self.deployment_helper = DeploymentHelper()
        self.research_agent = ResearchAgent()
        self.pitch_assistant = PitchAssistant()
        self.tech_stack_advisor = TechStackAdvisor()
        
        self.session_id = self._generate_session_id()
        self.project_context = {}
        
        print("🚀 Hackathon AI Assistant initialized!")
        print("Ready to help you WIN! 🏆")
    
    def _load_config(self, config_file: str) -> Dict:
        """Load configuration from file"""
        default_config = {
            "ai_models": {
                "primary": "gpt-4",
                "fallback": "gpt-3.5-turbo",
                "coding": "code-davinci-002"
            },
            "development": {
                "default_languages": ["python", "javascript", "typescript"],
                "preferred_frameworks": ["react", "fastapi", "flask"],
                "deployment_platforms": ["vercel", "heroku", "aws"]
            },
            "hackathon": {
                "time_limit_hours": 48,
                "team_size": 4,
                "judging_criteria": ["innovation", "technical_implementation", "design", "business_value"]
            }
        }
        
        if os.path.exists(config_file):
            with open(config_file, 'r') as f:
                user_config = json.load(f)
                default_config.update(user_config)
        
        return default_config
    
    def setup_logging(self):
        """Setup logging configuration"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('hackathon_assistant.log'),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def _generate_session_id(self) -> str:
        """Generate unique session ID"""
        return f"hackathon_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    
    async def start_new_project(self, project_name: str, theme: str = "", constraints: List[str] = None):
        """
        Start a new hackathon project
        
        Args:
            project_name: Name of the project
            theme: Hackathon theme or prompt
            constraints: Any constraints (tech stack, time, etc.)
        """
        print(f"🎯 Starting new project: {project_name}")
        
        # Generate project ideas
        ideas = await self.idea_generator.generate_ideas(theme, constraints or [])
        
        # Get technology recommendations
        tech_stack = await self.tech_stack_advisor.recommend_stack(theme, ideas)
        
        # Setup project structure
        project_path = await self.project_manager.setup_project(
            project_name, tech_stack, ideas[0] if ideas else {}
        )
        
        self.project_context = {
            "name": project_name,
            "theme": theme,
            "path": project_path,
            "tech_stack": tech_stack,
            "ideas": ideas,
            "start_time": datetime.now(),
            "constraints": constraints or []
        }
        
        print(f"✅ Project '{project_name}' initialized!")
        print(f"📁 Location: {project_path}")
        print(f"💡 Generated {len(ideas)} ideas")
        print(f"🛠️  Recommended tech stack: {', '.join(tech_stack.get('primary', []))}")
        
        return self.project_context
    
    async def generate_code(self, prompt: str, language: str = "python", framework: str = None):
        """Generate code based on prompt"""
        return await self.code_generator.generate(
            prompt, language, framework, self.project_context
        )
    
    async def create_full_app(self, app_type: str, features: List[str], design_style: str = "modern"):
        """
        Create a complete application rapidly
        
        Args:
            app_type: Type of app (web, mobile, api, etc.)
            features: List of features to implement
            design_style: Design style preference
        """
        print(f"🏗️  Creating {app_type} app with {len(features)} features...")
        
        # Generate app architecture
        architecture = await self.tech_stack_advisor.design_architecture(app_type, features)
        
        # Create UI/UX design
        design = await self.design_assistant.create_design(app_type, features, design_style)
        
        # Generate all code components
        code_components = await self.code_generator.generate_full_app(
            app_type, features, architecture, design
        )
        
        # Setup project files
        app_path = await self.project_manager.create_app_structure(
            self.project_context["name"], app_type, code_components
        )
        
        print(f"✅ {app_type.title()} app created successfully!")
        print(f"📁 Location: {app_path}")
        
        return {
            "path": app_path,
            "architecture": architecture,
            "design": design,
            "components": code_components
        }
    
    async def optimize_for_demo(self):
        """Optimize project for hackathon demo"""
        print("🎬 Optimizing project for demo...")
        
        # Code optimization
        await self.code_generator.optimize_code(self.project_context["path"])
        
        # Create demo assets
        demo_assets = await self.pitch_assistant.create_demo_assets(self.project_context)
        
        # Setup deployment
        deployment_url = await self.deployment_helper.deploy_project(
            self.project_context["path"], 
            self.project_context["tech_stack"]
        )
        
        print(f"✅ Demo optimization complete!")
        if deployment_url:
            print(f"🌐 Live demo: {deployment_url}")
        
        return {
            "demo_assets": demo_assets,
            "deployment_url": deployment_url
        }
    
    async def create_pitch_deck(self, target_audience: str = "judges"):
        """Create compelling pitch deck"""
        return await self.pitch_assistant.create_pitch_deck(
            self.project_context, target_audience
        )
    
    async def research_market(self, topic: str):
        """Research market and competition"""
        return await self.research_agent.research_topic(topic)
    
    async def get_help(self, query: str):
        """Get contextual help and suggestions"""
        context = {
            "project": self.project_context,
            "session": self.session_id,
            "query": query
        }
        
        # Determine the best module to handle the query
        if "code" in query.lower() or "implement" in query.lower():
            return await self.code_generator.get_help(query, context)
        elif "design" in query.lower() or "ui" in query.lower():
            return await self.design_assistant.get_help(query, context)
        elif "deploy" in query.lower():
            return await self.deployment_helper.get_help(query, context)
        elif "idea" in query.lower() or "feature" in query.lower():
            return await self.idea_generator.get_help(query, context)
        else:
            return await self._general_help(query, context)
    
    async def _general_help(self, query: str, context: Dict):
        """Provide general help and guidance"""
        suggestions = [
            "💡 Generate new ideas: `assistant.idea_generator.generate_ideas(theme)`",
            "🏗️  Create full app: `assistant.create_full_app('web', ['auth', 'dashboard'])`",
            "🎨 Design assistance: `assistant.design_assistant.create_wireframe()`",
            "🚀 Deploy project: `assistant.deployment_helper.deploy_project()`",
            "📊 Research market: `assistant.research_market('your topic')`",
            "🎯 Optimize for demo: `assistant.optimize_for_demo()`",
            "📈 Create pitch deck: `assistant.create_pitch_deck()`"
        ]
        
        return {
            "response": f"I can help you with: {query}",
            "suggestions": suggestions,
            "context": context
        }
    
    def status(self):
        """Get current project status"""
        if not self.project_context:
            return {"status": "No active project"}
        
        elapsed_time = datetime.now() - self.project_context["start_time"]
        
        return {
            "project": self.project_context["name"],
            "elapsed_time": str(elapsed_time),
            "tech_stack": self.project_context.get("tech_stack", {}),
            "ideas_count": len(self.project_context.get("ideas", [])),
            "session_id": self.session_id
        }

# CLI Interface
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Ultimate Hackathon AI Assistant")
    parser.add_argument("--interactive", "-i", action="store_true", help="Start interactive mode")
    parser.add_argument("--project", "-p", help="Start new project")
    parser.add_argument("--theme", "-t", help="Hackathon theme")
    
    args = parser.parse_args()
    
    assistant = HackathonAIAssistant()
    
    if args.interactive:
        # Start interactive mode
        print("🤖 Interactive mode - type 'help' for commands")
        while True:
            try:
                command = input("\n💻 hackathon-ai> ").strip()
                if command.lower() in ['exit', 'quit']:
                    break
                elif command.lower() == 'help':
                    print("Available commands:")
                    print("- start <project_name> [theme]: Start new project")
                    print("- status: Show project status")
                    print("- generate <prompt>: Generate code")
                    print("- deploy: Deploy current project")
                    print("- pitch: Create pitch deck")
                    print("- help: Show this help")
                    print("- exit: Exit assistant")
                elif command.startswith('start '):
                    parts = command.split(' ', 2)
                    project_name = parts[1] if len(parts) > 1 else "hackathon_project"
                    theme = parts[2] if len(parts) > 2 else ""
                    asyncio.run(assistant.start_new_project(project_name, theme))
                elif command == 'status':
                    status = assistant.status()
                    for key, value in status.items():
                        print(f"{key}: {value}")
                else:
                    result = asyncio.run(assistant.get_help(command))
                    print(result.get("response", "Command not recognized"))
            except KeyboardInterrupt:
                print("\n👋 Goodbye! Good luck with your hackathon!")
                break
            except Exception as e:
                print(f"❌ Error: {e}")
    
    elif args.project:
        asyncio.run(assistant.start_new_project(args.project, args.theme or ""))
    
    else:
        print("🚀 Hackathon AI Assistant ready!")
        print("Use --interactive for interactive mode or --project to start a new project")
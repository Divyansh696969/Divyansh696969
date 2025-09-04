"""
Tech Stack Advisor Module
========================
Recommends optimal technology stacks for hackathon projects
"""

import asyncio
from typing import Dict, List, Any, Optional

class TechStackAdvisor:
    """Provides technology stack recommendations optimized for hackathons"""
    
    def __init__(self):
        self.tech_stacks = self._load_tech_stacks()
        self.compatibility_matrix = self._load_compatibility_matrix()
        self.learning_curves = self._load_learning_curves()
        self.deployment_options = self._load_deployment_options()
    
    def _load_tech_stacks(self) -> Dict:
        """Load predefined technology stacks"""
        return {
            "web_fullstack": {
                "frontend": ["react", "vue", "angular"],
                "backend": ["node.js", "python", "fastapi"],
                "database": ["postgresql", "mongodb", "sqlite"],
                "deployment": ["vercel", "netlify", "heroku"],
                "best_for": ["web applications", "dashboards", "apis"],
                "setup_time": "30-60 minutes",
                "learning_curve": "medium"
            },
            "rapid_prototype": {
                "frontend": ["react", "streamlit", "gradio"],
                "backend": ["fastapi", "flask", "express"],
                "database": ["sqlite", "json", "in-memory"],
                "deployment": ["vercel", "streamlit-cloud", "replit"],
                "best_for": ["quick demos", "mvps", "proof of concepts"],
                "setup_time": "15-30 minutes",
                "learning_curve": "low"
            },
            "ai_ml": {
                "frontend": ["streamlit", "gradio", "react"],
                "backend": ["python", "fastapi", "jupyter"],
                "ml_frameworks": ["tensorflow", "pytorch", "scikit-learn", "huggingface"],
                "database": ["postgresql", "mongodb", "vector-db"],
                "deployment": ["streamlit-cloud", "huggingface-spaces", "railway"],
                "best_for": ["ai demos", "ml models", "data analysis"],
                "setup_time": "45-90 minutes",
                "learning_curve": "high"
            },
            "mobile_first": {
                "mobile": ["react-native", "flutter", "ionic"],
                "backend": ["node.js", "python", "firebase"],
                "database": ["firebase", "supabase", "mongodb"],
                "deployment": ["expo", "firebase", "app-store"],
                "best_for": ["mobile apps", "cross-platform", "native feel"],
                "setup_time": "60-120 minutes",
                "learning_curve": "medium-high"
            },
            "blockchain": {
                "frontend": ["react", "next.js", "web3-ui"],
                "blockchain": ["ethereum", "polygon", "solana"],
                "smart_contracts": ["solidity", "rust", "javascript"],
                "web3_tools": ["metamask", "web3.js", "ethers.js"],
                "deployment": ["ipfs", "vercel", "fleek"],
                "best_for": ["dapps", "defi", "nfts", "crypto"],
                "setup_time": "90-180 minutes",
                "learning_curve": "high"
            },
            "iot_hardware": {
                "hardware": ["raspberry-pi", "arduino", "esp32"],
                "backend": ["python", "node.js", "mqtt"],
                "frontend": ["react", "mobile-app", "dashboard"],
                "cloud": ["aws-iot", "azure-iot", "firebase"],
                "deployment": ["cloud", "edge", "hybrid"],
                "best_for": ["iot projects", "sensors", "automation"],
                "setup_time": "120-240 minutes",
                "learning_curve": "high"
            }
        }
    
    def _load_compatibility_matrix(self) -> Dict:
        """Load technology compatibility information"""
        return {
            "frontend_backend": {
                "react": ["node.js", "python", "java", "go"],
                "vue": ["node.js", "python", "php"],
                "angular": ["node.js", "java", ".net"],
                "streamlit": ["python"],
                "gradio": ["python"]
            },
            "backend_database": {
                "node.js": ["mongodb", "postgresql", "mysql", "sqlite"],
                "python": ["postgresql", "mongodb", "sqlite", "redis"],
                "fastapi": ["postgresql", "mongodb", "sqlite"],
                "flask": ["postgresql", "sqlite", "mysql"]
            },
            "deployment_stack": {
                "vercel": ["react", "next.js", "vue", "node.js"],
                "netlify": ["react", "vue", "angular", "static"],
                "heroku": ["python", "node.js", "java", "ruby"],
                "streamlit-cloud": ["streamlit", "python"]
            }
        }
    
    def _load_learning_curves(self) -> Dict:
        """Load learning curve information for technologies"""
        return {
            "beginner_friendly": {
                "technologies": ["react", "python", "sqlite", "vercel"],
                "time_to_productivity": "2-4 hours",
                "documentation": "excellent",
                "community": "large"
            },
            "intermediate": {
                "technologies": ["vue", "angular", "fastapi", "postgresql"],
                "time_to_productivity": "4-8 hours",
                "documentation": "good",
                "community": "medium-large"
            },
            "advanced": {
                "technologies": ["blockchain", "ml", "iot", "microservices"],
                "time_to_productivity": "8+ hours",
                "documentation": "variable",
                "community": "specialized"
            }
        }
    
    def _load_deployment_options(self) -> Dict:
        """Load deployment platform characteristics"""
        return {
            "vercel": {
                "cost": "free tier",
                "setup_time": "5 minutes",
                "custom_domain": True,
                "best_for": ["frontend", "serverless"],
                "limitations": ["function timeouts", "bandwidth limits"]
            },
            "netlify": {
                "cost": "free tier",
                "setup_time": "5 minutes", 
                "custom_domain": True,
                "best_for": ["jamstack", "static sites"],
                "limitations": ["build minutes", "bandwidth"]
            },
            "heroku": {
                "cost": "free tier ending",
                "setup_time": "10 minutes",
                "custom_domain": True,
                "best_for": ["full-stack", "databases"],
                "limitations": ["dyno hours", "slow cold starts"]
            },
            "railway": {
                "cost": "free tier",
                "setup_time": "5 minutes",
                "custom_domain": True,
                "best_for": ["python", "node.js", "databases"],
                "limitations": ["resource limits", "newer platform"]
            }
        }
    
    async def recommend_stack(self, theme: str, ideas: List[Dict]) -> Dict:
        """
        Recommend optimal technology stack based on theme and ideas
        
        Args:
            theme: Hackathon theme
            ideas: List of project ideas
            
        Returns:
            Recommended technology stack with alternatives
        """
        # Analyze requirements
        requirements = self._analyze_requirements(theme, ideas)
        
        # Score different stacks
        stack_scores = await self._score_stacks(requirements)
        
        # Select primary recommendation
        primary_stack = self._select_primary_stack(stack_scores, requirements)
        
        # Generate alternatives
        alternatives = self._generate_alternatives(stack_scores, primary_stack)
        
        # Create setup guide
        setup_guide = self._create_setup_guide(primary_stack)
        
        return {
            "primary": primary_stack,
            "alternatives": alternatives,
            "requirements": requirements,
            "setup_guide": setup_guide,
            "estimated_setup_time": self._estimate_setup_time(primary_stack),
            "learning_resources": self._get_learning_resources(primary_stack),
            "deployment_strategy": self._recommend_deployment(primary_stack)
        }
    
    def _analyze_requirements(self, theme: str, ideas: List[Dict]) -> Dict:
        """Analyze project requirements from theme and ideas"""
        requirements = {
            "project_type": "web",
            "complexity": "medium",
            "time_constraint": "48_hours",
            "team_experience": "mixed",
            "demo_requirements": ["web_interface"],
            "scalability_needs": "low",
            "data_requirements": "simple"
        }
        
        if not ideas:
            return requirements
        
        main_idea = ideas[0]
        
        # Analyze domain
        domain = main_idea.get("domain", "").lower()
        if domain in ["healthcare", "finance"]:
            requirements["security_needs"] = "high"
            requirements["compliance"] = "important"
        
        # Analyze technologies mentioned
        technologies = main_idea.get("technologies", [])
        if any("machine_learning" in tech or "ai" in tech for tech in technologies):
            requirements["project_type"] = "ai_ml"
            requirements["complexity"] = "high"
        elif any("mobile" in tech for tech in technologies):
            requirements["project_type"] = "mobile"
        elif any("blockchain" in tech for tech in technologies):
            requirements["project_type"] = "blockchain"
            requirements["complexity"] = "high"
        
        # Analyze features
        features = main_idea.get("features", [])
        if any("real-time" in feature.lower() for feature in features):
            requirements["real_time"] = True
        if any("dashboard" in feature.lower() or "analytics" in feature.lower() for feature in features):
            requirements["data_visualization"] = True
        
        return requirements
    
    async def _score_stacks(self, requirements: Dict) -> Dict:
        """Score technology stacks based on requirements"""
        scores = {}
        
        for stack_name, stack_info in self.tech_stacks.items():
            score = 0
            
            # Project type match
            if requirements["project_type"] in stack_info["best_for"]:
                score += 40
            elif requirements["project_type"] == "web" and "web" in stack_info["best_for"][0]:
                score += 30
            
            # Time constraint
            setup_time = self._parse_time(stack_info["setup_time"])
            if setup_time <= 30:  # 30 minutes
                score += 20
            elif setup_time <= 60:  # 1 hour
                score += 15
            else:
                score += 5
            
            # Learning curve
            learning_curve = stack_info["learning_curve"]
            if learning_curve == "low":
                score += 20
            elif learning_curve == "medium":
                score += 15
            else:
                score += 5
            
            # Special requirements
            if requirements.get("real_time") and "websockets" in str(stack_info):
                score += 10
            if requirements.get("data_visualization") and stack_name == "ai_ml":
                score += 15
            if requirements.get("security_needs") == "high" and stack_name in ["web_fullstack"]:
                score += 10
            
            scores[stack_name] = {
                "score": score,
                "details": stack_info
            }
        
        return scores
    
    def _parse_time(self, time_str: str) -> int:
        """Parse time string to minutes"""
        if "15-30" in time_str:
            return 22  # Average
        elif "30-60" in time_str:
            return 45
        elif "45-90" in time_str:
            return 67
        elif "60-120" in time_str:
            return 90
        elif "90-180" in time_str:
            return 135
        else:
            return 60  # Default
    
    def _select_primary_stack(self, stack_scores: Dict, requirements: Dict) -> Dict:
        """Select the best primary technology stack"""
        # Sort by score
        sorted_stacks = sorted(stack_scores.items(), key=lambda x: x[1]["score"], reverse=True)
        
        best_stack_name, best_stack_data = sorted_stacks[0]
        
        # Create detailed recommendation
        stack_details = best_stack_data["details"]
        
        return {
            "name": best_stack_name,
            "frontend": stack_details.get("frontend", [])[:2],  # Top 2 options
            "backend": stack_details.get("backend", [])[:2],
            "database": stack_details.get("database", [])[:2],
            "deployment": stack_details.get("deployment", [])[:2],
            "additional": {
                k: v for k, v in stack_details.items() 
                if k not in ["frontend", "backend", "database", "deployment"]
            },
            "score": best_stack_data["score"],
            "rationale": self._generate_rationale(best_stack_name, requirements)
        }
    
    def _generate_rationale(self, stack_name: str, requirements: Dict) -> str:
        """Generate explanation for stack recommendation"""
        rationales = {
            "rapid_prototype": "Optimized for quick demos and MVPs with minimal setup time",
            "web_fullstack": "Perfect balance of capabilities and ease of use for web applications",
            "ai_ml": "Specialized for machine learning and AI demos with great visualization tools",
            "mobile_first": "Best for mobile-focused applications with cross-platform support",
            "blockchain": "Essential for crypto and decentralized application development",
            "iot_hardware": "Required for projects involving physical sensors and hardware"
        }
        
        base_rationale = rationales.get(stack_name, "Good general-purpose technology stack")
        
        # Add specific reasons based on requirements
        if requirements.get("time_constraint") == "48_hours":
            base_rationale += ". Chosen for rapid development capabilities."
        
        if requirements.get("project_type") != "web":
            base_rationale += f" Specifically optimized for {requirements['project_type']} projects."
        
        return base_rationale
    
    def _generate_alternatives(self, stack_scores: Dict, primary_stack: Dict) -> List[Dict]:
        """Generate alternative stack recommendations"""
        sorted_stacks = sorted(stack_scores.items(), key=lambda x: x[1]["score"], reverse=True)
        
        alternatives = []
        for stack_name, stack_data in sorted_stacks[1:3]:  # Top 2 alternatives
            alternatives.append({
                "name": stack_name,
                "score": stack_data["score"],
                "key_differences": self._compare_with_primary(stack_name, primary_stack["name"]),
                "when_to_choose": self._when_to_choose_alternative(stack_name)
            })
        
        return alternatives
    
    def _compare_with_primary(self, alternative: str, primary: str) -> List[str]:
        """Compare alternative with primary stack"""
        comparisons = {
            ("rapid_prototype", "web_fullstack"): ["Faster setup", "Less robust", "Better for demos"],
            ("ai_ml", "web_fullstack"): ["ML capabilities", "Steeper learning curve", "Better for data"],
            ("mobile_first", "web_fullstack"): ["Native mobile feel", "Longer development", "App store ready"]
        }
        
        key = (alternative, primary)
        return comparisons.get(key, ["Different focus area", "Alternative approach", "Consider team skills"])
    
    def _when_to_choose_alternative(self, stack_name: str) -> str:
        """Explain when to choose this alternative"""
        explanations = {
            "rapid_prototype": "Choose if you need to demo quickly and don't need full features",
            "web_fullstack": "Choose for production-ready applications with full feature set",
            "ai_ml": "Choose if your project heavily involves machine learning or data analysis",
            "mobile_first": "Choose if mobile experience is critical to your solution",
            "blockchain": "Choose for crypto, DeFi, or decentralized applications",
            "iot_hardware": "Choose if you're building with physical sensors or devices"
        }
        
        return explanations.get(stack_name, "Consider based on your specific project needs")
    
    def _create_setup_guide(self, primary_stack: Dict) -> List[Dict]:
        """Create step-by-step setup guide"""
        stack_name = primary_stack["name"]
        
        guides = {
            "rapid_prototype": [
                {"step": 1, "title": "Install Node.js and Python", "time": "5 min"},
                {"step": 2, "title": "Create React app", "command": "npx create-react-app my-app", "time": "3 min"},
                {"step": 3, "title": "Setup FastAPI backend", "command": "pip install fastapi uvicorn", "time": "2 min"},
                {"step": 4, "title": "Deploy to Vercel", "command": "vercel deploy", "time": "5 min"}
            ],
            "web_fullstack": [
                {"step": 1, "title": "Setup development environment", "time": "10 min"},
                {"step": 2, "title": "Initialize frontend", "command": "npx create-react-app frontend", "time": "5 min"},
                {"step": 3, "title": "Setup backend API", "command": "mkdir backend && cd backend", "time": "5 min"},
                {"step": 4, "title": "Configure database", "command": "pip install sqlalchemy", "time": "10 min"},
                {"step": 5, "title": "Deploy application", "time": "15 min"}
            ],
            "ai_ml": [
                {"step": 1, "title": "Install Python ML stack", "command": "pip install streamlit pandas numpy", "time": "5 min"},
                {"step": 2, "title": "Setup Jupyter environment", "command": "pip install jupyter", "time": "3 min"},
                {"step": 3, "title": "Install ML frameworks", "command": "pip install scikit-learn tensorflow", "time": "10 min"},
                {"step": 4, "title": "Create Streamlit app", "command": "streamlit hello", "time": "5 min"},
                {"step": 5, "title": "Deploy to Streamlit Cloud", "time": "10 min"}
            ]
        }
        
        return guides.get(stack_name, [
            {"step": 1, "title": "Setup development environment", "time": "15 min"},
            {"step": 2, "title": "Install dependencies", "time": "10 min"},
            {"step": 3, "title": "Create project structure", "time": "5 min"},
            {"step": 4, "title": "Deploy application", "time": "15 min"}
        ])
    
    def _estimate_setup_time(self, primary_stack: Dict) -> Dict:
        """Estimate total setup time"""
        setup_guide = self._create_setup_guide(primary_stack)
        
        # Extract time from setup guide
        total_minutes = 0
        for step in setup_guide:
            time_str = step.get("time", "5 min")
            minutes = int(time_str.split()[0])
            total_minutes += minutes
        
        return {
            "total_time": f"{total_minutes} minutes",
            "breakdown": {step["title"]: step["time"] for step in setup_guide},
            "parallel_tasks": "Some steps can be done in parallel to save time",
            "buffer_time": "Add 50% buffer for troubleshooting"
        }
    
    def _get_learning_resources(self, primary_stack: Dict) -> Dict:
        """Get learning resources for the stack"""
        stack_name = primary_stack["name"]
        
        resources = {
            "rapid_prototype": {
                "tutorials": [
                    "React Quick Start - 30 min",
                    "FastAPI Tutorial - 45 min",
                    "Vercel Deployment Guide - 15 min"
                ],
                "documentation": [
                    "React Docs: reactjs.org",
                    "FastAPI Docs: fastapi.tiangolo.com"
                ],
                "quick_references": [
                    "React Cheatsheet",
                    "FastAPI Quick Reference"
                ]
            },
            "ai_ml": {
                "tutorials": [
                    "Streamlit Tutorial - 60 min",
                    "Pandas Basics - 90 min",
                    "Scikit-learn Quick Start - 45 min"
                ],
                "documentation": [
                    "Streamlit Docs: docs.streamlit.io",
                    "Pandas Docs: pandas.pydata.org"
                ],
                "quick_references": [
                    "Python Data Science Cheatsheet",
                    "Streamlit Cheatsheet"
                ]
            }
        }
        
        return resources.get(stack_name, {
            "tutorials": ["Official documentation", "YouTube tutorials", "Stack Overflow"],
            "documentation": ["Check official websites for each technology"],
            "quick_references": ["GitHub awesome lists", "Developer cheatsheets"]
        })
    
    def _recommend_deployment(self, primary_stack: Dict) -> Dict:
        """Recommend deployment strategy"""
        deployment_options = primary_stack.get("deployment", ["vercel"])
        primary_deployment = deployment_options[0]
        
        return {
            "recommended": primary_deployment,
            "alternatives": deployment_options[1:],
            "strategy": self._get_deployment_strategy(primary_deployment),
            "estimated_time": "5-15 minutes",
            "requirements": self._get_deployment_requirements(primary_deployment)
        }
    
    def _get_deployment_strategy(self, platform: str) -> Dict:
        """Get deployment strategy for platform"""
        strategies = {
            "vercel": {
                "approach": "Git-based deployment",
                "steps": ["Connect GitHub repo", "Configure build settings", "Deploy"],
                "benefits": ["Automatic deployments", "Preview URLs", "Custom domains"]
            },
            "netlify": {
                "approach": "Drag-and-drop or Git",
                "steps": ["Build locally", "Upload build folder", "Configure redirects"],
                "benefits": ["Simple setup", "Form handling", "Split testing"]
            },
            "heroku": {
                "approach": "Git deployment with buildpacks",
                "steps": ["Create Heroku app", "Configure buildpack", "Git push to deploy"],
                "benefits": ["Full-stack support", "Add-ons ecosystem", "Scaling options"]
            }
        }
        
        return strategies.get(platform, {
            "approach": "Platform-specific deployment",
            "steps": ["Check platform documentation"],
            "benefits": ["Varies by platform"]
        })
    
    def _get_deployment_requirements(self, platform: str) -> List[str]:
        """Get deployment requirements"""
        requirements = {
            "vercel": ["GitHub account", "Build scripts in package.json"],
            "netlify": ["Build folder or GitHub repo", "Redirect rules if needed"],
            "heroku": ["Heroku account", "Procfile", "Requirements.txt"],
            "railway": ["GitHub account", "Start command configuration"]
        }
        
        return requirements.get(platform, ["Platform account", "Project configuration"])
    
    async def design_architecture(self, app_type: str, features: List[str]) -> Dict:
        """Design application architecture"""
        architecture = {
            "pattern": "microservices" if len(features) > 5 else "monolith",
            "layers": ["presentation", "business", "data"],
            "components": self._design_components(app_type, features),
            "data_flow": self._design_data_flow(features),
            "scalability": self._assess_scalability_needs(features),
            "security": self._design_security_layer(features)
        }
        
        return architecture
    
    def _design_components(self, app_type: str, features: List[str]) -> Dict:
        """Design system components"""
        components = {
            "frontend": ["user_interface", "state_management", "routing"],
            "backend": ["api_server", "business_logic", "data_access"],
            "database": ["primary_storage", "caching_layer"],
            "external": ["third_party_apis", "authentication_service"]
        }
        
        # Add feature-specific components
        if any("real-time" in feature.lower() for feature in features):
            components["backend"].append("websocket_handler")
        
        if any("ai" in feature.lower() or "ml" in feature.lower() for feature in features):
            components["backend"].extend(["ml_model_service", "prediction_engine"])
        
        return components
    
    def _design_data_flow(self, features: List[str]) -> List[str]:
        """Design data flow through the system"""
        return [
            "User input → Frontend validation",
            "Frontend → API Gateway",
            "API Gateway → Business Logic",
            "Business Logic → Database",
            "Database → Response formatting",
            "Response → Frontend rendering"
        ]
    
    def _assess_scalability_needs(self, features: List[str]) -> Dict:
        """Assess scalability requirements"""
        return {
            "expected_load": "low-medium (hackathon demo)",
            "bottlenecks": ["database queries", "external API calls"],
            "scaling_strategy": "horizontal scaling for production",
            "caching_needs": "moderate" if len(features) > 3 else "minimal"
        }
    
    def _design_security_layer(self, features: List[str]) -> List[str]:
        """Design security considerations"""
        security_measures = [
            "Input validation",
            "HTTPS encryption",
            "Authentication tokens"
        ]
        
        if any("auth" in feature.lower() for feature in features):
            security_measures.extend([
                "Password hashing",
                "Session management",
                "Authorization middleware"
            ])
        
        return security_measures
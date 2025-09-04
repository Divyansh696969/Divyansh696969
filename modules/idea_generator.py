"""
Idea Generator Module
====================
Generates innovative hackathon project ideas based on themes and constraints
"""

import asyncio
import json
import random
from typing import Dict, List, Any, Optional
from datetime import datetime

class IdeaGenerator:
    """Generates creative and feasible hackathon project ideas"""
    
    def __init__(self):
        self.idea_templates = self._load_idea_templates()
        self.tech_combinations = self._load_tech_combinations()
        self.problem_domains = self._load_problem_domains()
        self.innovation_patterns = self._load_innovation_patterns()
    
    def _load_idea_templates(self) -> Dict:
        """Load idea generation templates"""
        return {
            "problem_solution": {
                "pattern": "Create a {solution_type} that helps {target_audience} {action} by {method}",
                "examples": [
                    "Create a mobile app that helps students learn by gamifying study sessions",
                    "Create a web platform that helps small businesses manage inventory by using AI predictions"
                ]
            },
            "enhancement": {
                "pattern": "Build a tool that makes {existing_thing} {improvement} for {audience}",
                "examples": [
                    "Build a tool that makes online meetings more engaging for remote teams",
                    "Build a tool that makes code reviews faster for developers"
                ]
            },
            "automation": {
                "pattern": "Automate {manual_process} using {technology} to save {benefit}",
                "examples": [
                    "Automate expense reporting using AI to save hours of manual work",
                    "Automate social media posting using ML to save marketing effort"
                ]
            },
            "marketplace": {
                "pattern": "Connect {group_a} with {group_b} through {platform_type}",
                "examples": [
                    "Connect freelance developers with startup founders through a skill-matching platform",
                    "Connect local farmers with urban consumers through a direct-sales app"
                ]
            }
        }
    
    def _load_tech_combinations(self) -> Dict:
        """Load interesting technology combinations"""
        return {
            "ai_powered": {
                "technologies": ["machine_learning", "nlp", "computer_vision", "recommendation_systems"],
                "applications": ["content_generation", "prediction", "automation", "personalization"]
            },
            "real_time": {
                "technologies": ["websockets", "streaming", "live_updates", "collaboration"],
                "applications": ["gaming", "communication", "monitoring", "trading"]
            },
            "mobile_first": {
                "technologies": ["react_native", "flutter", "pwa", "mobile_apis"],
                "applications": ["lifestyle", "productivity", "social", "utility"]
            },
            "blockchain": {
                "technologies": ["smart_contracts", "defi", "nft", "tokenization"],
                "applications": ["finance", "voting", "supply_chain", "identity"]
            },
            "iot_connected": {
                "technologies": ["sensors", "raspberry_pi", "arduino", "cloud_integration"],
                "applications": ["home_automation", "health_monitoring", "environmental", "agriculture"]
            }
        }
    
    def _load_problem_domains(self) -> Dict:
        """Load different problem domains and their characteristics"""
        return {
            "healthcare": {
                "problems": [
                    "medication adherence",
                    "patient data management", 
                    "telemedicine accessibility",
                    "mental health support",
                    "fitness tracking",
                    "elderly care"
                ],
                "audiences": ["patients", "doctors", "caregivers", "hospitals"],
                "constraints": ["privacy", "regulations", "accuracy"]
            },
            "education": {
                "problems": [
                    "remote learning engagement",
                    "skill assessment",
                    "personalized learning paths",
                    "student collaboration",
                    "teacher workload",
                    "accessibility"
                ],
                "audiences": ["students", "teachers", "parents", "institutions"],
                "constraints": ["age_appropriate", "scalability", "cost"]
            },
            "environment": {
                "problems": [
                    "carbon footprint tracking",
                    "waste management",
                    "renewable energy optimization",
                    "water conservation",
                    "sustainable transportation",
                    "recycling systems"
                ],
                "audiences": ["individuals", "communities", "businesses", "governments"],
                "constraints": ["data_availability", "behavior_change", "measurement"]
            },
            "finance": {
                "problems": [
                    "budgeting and savings",
                    "investment education",
                    "fraud detection",
                    "financial inclusion",
                    "cryptocurrency management",
                    "small business accounting"
                ],
                "audiences": ["consumers", "small_businesses", "banks", "investors"],
                "constraints": ["security", "regulations", "trust"]
            },
            "productivity": {
                "problems": [
                    "time management",
                    "team collaboration",
                    "project planning",
                    "automation workflows",
                    "document management",
                    "communication efficiency"
                ],
                "audiences": ["professionals", "teams", "managers", "freelancers"],
                "constraints": ["integration", "learning_curve", "customization"]
            }
        }
    
    def _load_innovation_patterns(self) -> List[str]:
        """Load patterns that make ideas more innovative"""
        return [
            "gamification",
            "ai_personalization", 
            "community_driven",
            "real_time_collaboration",
            "predictive_analytics",
            "voice_interface",
            "ar_vr_integration",
            "blockchain_verification",
            "iot_automation",
            "social_impact"
        ]
    
    async def generate_ideas(self, theme: str = "", constraints: List[str] = None, count: int = 5) -> List[Dict]:
        """
        Generate innovative hackathon project ideas
        
        Args:
            theme: Hackathon theme or focus area
            constraints: List of constraints (tech stack, time, etc.)
            count: Number of ideas to generate
            
        Returns:
            List of project ideas with details
        """
        ideas = []
        constraints = constraints or []
        
        # Analyze theme to determine relevant domains
        relevant_domains = self._analyze_theme(theme)
        
        for i in range(count):
            idea = await self._generate_single_idea(theme, relevant_domains, constraints, i)
            ideas.append(idea)
        
        # Rank ideas by feasibility and innovation
        ranked_ideas = self._rank_ideas(ideas, constraints)
        
        return ranked_ideas
    
    async def _generate_single_idea(self, theme: str, domains: List[str], constraints: List[str], seed: int) -> Dict:
        """Generate a single project idea"""
        # Use seed for reproducible randomness
        random.seed(seed + hash(theme))
        
        # Select domain
        domain = random.choice(domains) if domains else random.choice(list(self.problem_domains.keys()))
        domain_info = self.problem_domains[domain]
        
        # Select problem
        problem = random.choice(domain_info["problems"])
        audience = random.choice(domain_info["audiences"])
        
        # Select technology approach
        tech_category = random.choice(list(self.tech_combinations.keys()))
        tech_info = self.tech_combinations[tech_category]
        
        # Select innovation pattern
        innovation = random.choice(self.innovation_patterns)
        
        # Generate idea using template
        template_type = random.choice(list(self.idea_templates.keys()))
        
        # Create the main idea
        idea = {
            "title": self._generate_title(problem, tech_category, innovation),
            "description": self._generate_description(problem, audience, tech_info, innovation, theme),
            "domain": domain,
            "target_audience": audience,
            "problem": problem,
            "technology_category": tech_category,
            "technologies": tech_info["technologies"][:3],  # Limit to 3 technologies
            "innovation_pattern": innovation,
            "template_type": template_type,
            "feasibility_score": 0,  # Will be calculated later
            "innovation_score": 0,   # Will be calculated later
            "features": self._generate_features(problem, tech_info, innovation),
            "mvp_timeline": self._estimate_timeline(tech_info["technologies"][:3]),
            "potential_impact": self._assess_impact(domain, problem, audience),
            "technical_challenges": self._identify_challenges(tech_info["technologies"][:3], constraints),
            "market_potential": self._assess_market_potential(domain, audience),
            "demo_suggestions": self._generate_demo_suggestions(problem, tech_info)
        }
        
        return idea
    
    def _analyze_theme(self, theme: str) -> List[str]:
        """Analyze theme to determine relevant problem domains"""
        if not theme:
            return list(self.problem_domains.keys())
        
        theme_lower = theme.lower()
        relevant_domains = []
        
        # Map theme keywords to domains
        theme_mappings = {
            "health": ["healthcare"],
            "education": ["education"],
            "learn": ["education"],
            "environment": ["environment"],
            "green": ["environment"],
            "climate": ["environment"],
            "finance": ["finance"],
            "money": ["finance"],
            "productivity": ["productivity"],
            "work": ["productivity"],
            "social": ["education", "productivity"],
            "ai": ["healthcare", "education", "finance", "productivity"],
            "mobile": ["healthcare", "education", "productivity"],
            "blockchain": ["finance"]
        }
        
        for keyword, domains in theme_mappings.items():
            if keyword in theme_lower:
                relevant_domains.extend(domains)
        
        # Remove duplicates and return, or return all if no matches
        return list(set(relevant_domains)) if relevant_domains else list(self.problem_domains.keys())
    
    def _generate_title(self, problem: str, tech_category: str, innovation: str) -> str:
        """Generate a catchy title for the idea"""
        # Title generation patterns
        patterns = [
            f"{problem.title().replace('_', ' ')} Assistant",
            f"Smart {problem.title().replace('_', ' ')} Platform",
            f"{innovation.title().replace('_', ' ')} for {problem.title().replace('_', ' ')}",
            f"{problem.title().replace('_', ' ')} Revolution",
            f"AI-Powered {problem.title().replace('_', ' ')} Solution"
        ]
        
        return random.choice(patterns)
    
    def _generate_description(self, problem: str, audience: str, tech_info: Dict, innovation: str, theme: str) -> str:
        """Generate a detailed description of the idea"""
        tech_list = ", ".join(tech_info["technologies"][:2])
        application = random.choice(tech_info["applications"])
        
        description = f"A cutting-edge solution that addresses {problem.replace('_', ' ')} for {audience} through {application}. "
        description += f"The platform leverages {tech_list} and incorporates {innovation.replace('_', ' ')} to create an engaging user experience. "
        
        if theme:
            description += f"Specifically designed for the {theme} challenge, this solution aims to make a significant impact in the target domain."
        
        return description
    
    def _generate_features(self, problem: str, tech_info: Dict, innovation: str) -> List[str]:
        """Generate key features for the idea"""
        base_features = [
            "User authentication and profiles",
            "Real-time data processing",
            "Mobile-responsive design",
            "Analytics dashboard"
        ]
        
        # Problem-specific features
        problem_features = {
            "medication_adherence": ["Pill reminder system", "Dosage tracking", "Doctor notifications"],
            "remote_learning": ["Virtual classrooms", "Progress tracking", "Interactive assignments"],
            "carbon_footprint": ["Activity logging", "Impact visualization", "Goal setting"],
            "budgeting": ["Expense categorization", "Savings goals", "Financial insights"],
            "time_management": ["Task prioritization", "Calendar integration", "Productivity metrics"]
        }
        
        # Technology-specific features
        tech_features = {
            "machine_learning": ["Predictive recommendations", "Pattern analysis", "Automated insights"],
            "computer_vision": ["Image recognition", "Visual search", "Object detection"],
            "blockchain": ["Secure transactions", "Transparent records", "Decentralized storage"],
            "iot": ["Sensor integration", "Remote monitoring", "Automated triggers"]
        }
        
        # Innovation-specific features
        innovation_features = {
            "gamification": ["Achievement system", "Leaderboards", "Progress badges"],
            "real_time_collaboration": ["Live editing", "Team notifications", "Shared workspaces"],
            "voice_interface": ["Voice commands", "Speech recognition", "Audio feedback"]
        }
        
        features = base_features.copy()
        
        # Add problem-specific features
        if problem in problem_features:
            features.extend(problem_features[problem])
        
        # Add tech-specific features
        for tech in tech_info["technologies"][:2]:
            if tech in tech_features:
                features.extend(tech_features[tech][:2])
        
        # Add innovation features
        if innovation in innovation_features:
            features.extend(innovation_features[innovation])
        
        return features[:8]  # Limit to 8 features for feasibility
    
    def _estimate_timeline(self, technologies: List[str]) -> Dict:
        """Estimate development timeline based on technologies"""
        # Base time estimates (in hours)
        tech_complexity = {
            "machine_learning": 12,
            "computer_vision": 15,
            "blockchain": 18,
            "react": 8,
            "fastapi": 6,
            "websockets": 10,
            "database": 4
        }
        
        total_hours = sum(tech_complexity.get(tech, 8) for tech in technologies) + 10  # Base setup time
        
        return {
            "total_hours": total_hours,
            "days_estimate": total_hours // 8,
            "phases": {
                "setup": "4 hours",
                "backend": f"{total_hours * 0.4:.0f} hours",
                "frontend": f"{total_hours * 0.3:.0f} hours", 
                "integration": f"{total_hours * 0.2:.0f} hours",
                "testing": f"{total_hours * 0.1:.0f} hours"
            }
        }
    
    def _assess_impact(self, domain: str, problem: str, audience: str) -> Dict:
        """Assess potential impact of the solution"""
        impact_levels = {
            "healthcare": {"social": "high", "economic": "high", "technical": "medium"},
            "education": {"social": "high", "economic": "medium", "technical": "medium"},
            "environment": {"social": "high", "economic": "medium", "technical": "high"},
            "finance": {"social": "medium", "economic": "high", "technical": "medium"},
            "productivity": {"social": "medium", "economic": "high", "technical": "low"}
        }
        
        base_impact = impact_levels.get(domain, {"social": "medium", "economic": "medium", "technical": "medium"})
        
        return {
            "social_impact": base_impact["social"],
            "economic_impact": base_impact["economic"],
            "technical_impact": base_impact["technical"],
            "target_users": f"1000+ {audience}",
            "scalability": "high" if domain in ["education", "productivity"] else "medium"
        }
    
    def _identify_challenges(self, technologies: List[str], constraints: List[str]) -> List[str]:
        """Identify potential technical challenges"""
        tech_challenges = {
            "machine_learning": ["Data quality and quantity", "Model training time", "Inference optimization"],
            "blockchain": ["Transaction costs", "Scalability issues", "User adoption"],
            "computer_vision": ["Image processing performance", "Lighting conditions", "Hardware requirements"],
            "real_time": ["Network latency", "Concurrent users", "Data synchronization"]
        }
        
        challenges = []
        for tech in technologies:
            if tech in tech_challenges:
                challenges.extend(tech_challenges[tech][:2])
        
        # Add constraint-specific challenges
        if "time" in constraints:
            challenges.append("Limited development time")
        if "team_size" in constraints:
            challenges.append("Small team coordination")
        
        return challenges[:5]  # Limit to top 5 challenges
    
    def _assess_market_potential(self, domain: str, audience: str) -> Dict:
        """Assess market potential"""
        market_sizes = {
            "healthcare": "Large ($4.5T global market)",
            "education": "Large ($6T global market)",
            "environment": "Growing ($1.1T green tech market)",
            "finance": "Massive ($22T global market)",
            "productivity": "Stable ($65B productivity software market)"
        }
        
        return {
            "market_size": market_sizes.get(domain, "Medium"),
            "competition": "Moderate" if domain in ["healthcare", "finance"] else "Low",
            "monetization": ["Subscription model", "Freemium", "B2B licensing"],
            "growth_potential": "High" if domain in ["environment", "education"] else "Medium"
        }
    
    def _generate_demo_suggestions(self, problem: str, tech_info: Dict) -> List[str]:
        """Generate suggestions for demonstrating the solution"""
        demo_suggestions = [
            "Live user interface walkthrough",
            "Real-time feature demonstration",
            "Before/after comparison scenarios",
            "User testimonial videos",
            "Performance metrics visualization"
        ]
        
        # Add problem-specific demos
        problem_demos = {
            "medication_adherence": ["Mock pill reminder demonstration", "Doctor dashboard view"],
            "remote_learning": ["Live virtual classroom session", "Student progress tracking"],
            "carbon_footprint": ["Real-time carbon calculation", "Impact visualization charts"],
            "budgeting": ["Expense tracking demo", "Savings goal achievement"]
        }
        
        if problem in problem_demos:
            demo_suggestions.extend(problem_demos[problem])
        
        return demo_suggestions[:6]
    
    def _rank_ideas(self, ideas: List[Dict], constraints: List[str]) -> List[Dict]:
        """Rank ideas by feasibility and innovation"""
        for idea in ideas:
            # Calculate feasibility score (0-100)
            feasibility = 50  # Base score
            
            # Adjust based on technology complexity
            tech_complexity = len(idea["technologies"]) * 10
            feasibility -= min(tech_complexity, 30)
            
            # Adjust based on timeline
            if idea["mvp_timeline"]["total_hours"] <= 24:
                feasibility += 20
            elif idea["mvp_timeline"]["total_hours"] <= 48:
                feasibility += 10
            
            # Adjust based on constraints
            if "time" in constraints and idea["mvp_timeline"]["total_hours"] > 30:
                feasibility -= 15
            
            idea["feasibility_score"] = max(0, min(100, feasibility))
            
            # Calculate innovation score (0-100)
            innovation = 40  # Base score
            
            # Bonus for AI/ML
            if any("machine_learning" in tech or "ai" in tech for tech in idea["technologies"]):
                innovation += 20
            
            # Bonus for novel combinations
            if idea["innovation_pattern"] in ["ar_vr_integration", "blockchain_verification", "voice_interface"]:
                innovation += 15
            
            # Bonus for social impact
            if idea["potential_impact"]["social_impact"] == "high":
                innovation += 10
            
            idea["innovation_score"] = min(100, innovation)
            
            # Calculate overall score
            idea["overall_score"] = (idea["feasibility_score"] * 0.6 + idea["innovation_score"] * 0.4)
        
        # Sort by overall score
        return sorted(ideas, key=lambda x: x["overall_score"], reverse=True)
    
    async def refine_idea(self, idea: Dict, feedback: str) -> Dict:
        """Refine an existing idea based on feedback"""
        refined_idea = idea.copy()
        
        # Analyze feedback for specific improvements
        feedback_lower = feedback.lower()
        
        if "simple" in feedback_lower or "complex" in feedback_lower:
            # Simplify by reducing features
            refined_idea["features"] = refined_idea["features"][:5]
            refined_idea["technologies"] = refined_idea["technologies"][:2]
        
        if "innovative" in feedback_lower or "unique" in feedback_lower:
            # Add more innovative features
            innovative_features = [
                "AI-powered recommendations",
                "Machine learning optimization", 
                "Blockchain verification",
                "AR/VR interface"
            ]
            refined_idea["features"].extend(innovative_features[:2])
        
        if "feasible" in feedback_lower or "timeline" in feedback_lower:
            # Adjust timeline to be more realistic
            refined_idea["mvp_timeline"]["total_hours"] *= 1.5
            refined_idea["mvp_timeline"]["days_estimate"] = refined_idea["mvp_timeline"]["total_hours"] // 8
        
        # Recalculate scores
        refined_idea["feasibility_score"] = min(100, refined_idea["feasibility_score"] + 10)
        
        return refined_idea
    
    async def get_help(self, query: str, context: Dict) -> Dict:
        """Get help with idea generation"""
        suggestions = [
            "Generate ideas: 'Generate 3 ideas for healthcare hackathon'",
            "Refine idea: 'Make this idea more innovative'", 
            "Analyze theme: 'What domains work best for AI theme?'",
            "Check feasibility: 'Is this idea feasible in 48 hours?'"
        ]
        
        return {
            "response": f"I can help you with idea generation: {query}",
            "suggestions": suggestions,
            "examples": {
                "generate": "await assistant.idea_generator.generate_ideas('AI for Good', ['time_limited'], 5)",
                "refine": "await assistant.idea_generator.refine_idea(idea, 'make it simpler')",
                "domains": "assistant.idea_generator._load_problem_domains().keys()"
            }
        }
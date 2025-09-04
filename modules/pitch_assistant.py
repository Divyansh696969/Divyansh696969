"""
Pitch Assistant Module
=====================
Creates compelling pitch decks and presentations for hackathon demos
"""

import asyncio
from typing import Dict, List, Any, Optional
from datetime import datetime

class PitchAssistant:
    """Helps create winning hackathon pitches and presentations"""
    
    def __init__(self):
        self.pitch_templates = self._load_pitch_templates()
        self.storytelling_frameworks = self._load_storytelling_frameworks()
        self.demo_strategies = self._load_demo_strategies()
    
    def _load_pitch_templates(self) -> Dict:
        """Load pitch deck templates optimized for hackathons"""
        return {
            "classic_startup": {
                "slides": [
                    {"title": "Problem", "content": "What problem are you solving?"},
                    {"title": "Solution", "content": "How does your solution address this problem?"},
                    {"title": "Market", "content": "How big is the opportunity?"},
                    {"title": "Product Demo", "content": "Show your working prototype"},
                    {"title": "Business Model", "content": "How will you make money?"},
                    {"title": "Competition", "content": "Who else is solving this?"},
                    {"title": "Traction", "content": "What progress have you made?"},
                    {"title": "Team", "content": "Why are you the right team?"},
                    {"title": "Ask", "content": "What do you need to succeed?"}
                ]
            },
            "hackathon_focused": {
                "slides": [
                    {"title": "Hook", "content": "Grab attention with compelling story"},
                    {"title": "Problem", "content": "Real problem with emotional impact"},
                    {"title": "Solution Demo", "content": "Live demonstration of working solution"},
                    {"title": "Technical Innovation", "content": "What's technically impressive?"},
                    {"title": "Impact", "content": "Who benefits and how much?"},
                    {"title": "Next Steps", "content": "What would you build next?"}
                ]
            },
            "social_impact": {
                "slides": [
                    {"title": "The Challenge", "content": "Social/environmental problem"},
                    {"title": "Our Solution", "content": "How technology helps"},
                    {"title": "Live Demo", "content": "Show impact in action"},
                    {"title": "Real Impact", "content": "Quantify the difference made"},
                    {"title": "Scalability", "content": "How to reach more people"},
                    {"title": "Call to Action", "content": "How audience can help"}
                ]
            }
        }
    
    def _load_storytelling_frameworks(self) -> Dict:
        """Load storytelling frameworks for compelling narratives"""
        return {
            "hero_journey": {
                "structure": [
                    "Ordinary World (Current State)",
                    "Call to Adventure (Problem Discovery)",
                    "Meeting the Mentor (Inspiration/Research)",
                    "Crossing Threshold (Building Solution)",
                    "Tests and Trials (Development Challenges)",
                    "Revelation (Key Insight/Breakthrough)",
                    "Transformation (Solution Impact)",
                    "Return (Sharing with World)"
                ]
            },
            "problem_agitation_solution": {
                "structure": [
                    "Problem (What's wrong?)",
                    "Agitation (Why it matters now?)",
                    "Solution (How we fix it?)",
                    "Benefits (What's the outcome?)"
                ]
            },
            "before_after_bridge": {
                "structure": [
                    "Before (Current painful state)",
                    "After (Desired future state)",
                    "Bridge (Our solution as the path)"
                ]
            }
        }
    
    def _load_demo_strategies(self) -> Dict:
        """Load effective demo strategies for hackathons"""
        return {
            "live_demo": {
                "description": "Show the actual working product",
                "pros": ["Authentic", "Interactive", "Impressive"],
                "cons": ["Risk of failure", "Technical issues"],
                "best_for": ["Technical judges", "Working prototypes"],
                "tips": ["Have backup plans", "Practice extensively", "Keep it simple"]
            },
            "guided_storytelling": {
                "description": "Walk through user scenarios with mockups",
                "pros": ["Controlled", "Clear narrative", "Easy to follow"],
                "cons": ["Less impressive", "Not interactive"],
                "best_for": ["Early prototypes", "Complex workflows"],
                "tips": ["Use real user scenarios", "Include emotional moments", "Show clear value"]
            },
            "data_story": {
                "description": "Show impact through data and visualizations",
                "pros": ["Quantifiable impact", "Professional", "Memorable"],
                "cons": ["Can be dry", "Requires real data"],
                "best_for": ["Analytics solutions", "B2B products"],
                "tips": ["Use compelling visualizations", "Tell story with numbers", "Compare before/after"]
            }
        }
    
    async def create_pitch_deck(self, project_context: Dict, target_audience: str = "judges") -> Dict:
        """
        Create a compelling pitch deck for the project
        
        Args:
            project_context: Project information and context
            target_audience: Target audience (judges, investors, etc.)
            
        Returns:
            Complete pitch deck with slides and speaker notes
        """
        # Select appropriate template
        template = self._select_pitch_template(project_context, target_audience)
        
        # Choose storytelling framework
        framework = self._select_storytelling_framework(project_context)
        
        # Generate slide content
        slides = await self._generate_slide_content(project_context, template, framework)
        
        # Create speaker notes
        speaker_notes = self._generate_speaker_notes(slides, project_context)
        
        # Add demo strategy
        demo_strategy = self._recommend_demo_strategy(project_context)
        
        # Generate presentation flow
        presentation_flow = self._create_presentation_flow(slides, demo_strategy)
        
        return {
            "template": template,
            "framework": framework,
            "slides": slides,
            "speaker_notes": speaker_notes,
            "demo_strategy": demo_strategy,
            "presentation_flow": presentation_flow,
            "timing_guide": self._create_timing_guide(slides),
            "backup_plans": self._create_backup_plans(demo_strategy),
            "q_and_a_prep": self._prepare_q_and_a(project_context)
        }
    
    def _select_pitch_template(self, project_context: Dict, target_audience: str) -> str:
        """Select the best pitch template"""
        theme = project_context.get("theme", "").lower()
        domain = project_context.get("ideas", [{}])[0].get("domain", "").lower()
        
        if any(word in theme for word in ["social", "impact", "environment", "good"]):
            return "social_impact"
        elif target_audience == "investors":
            return "classic_startup"
        else:
            return "hackathon_focused"
    
    def _select_storytelling_framework(self, project_context: Dict) -> str:
        """Select storytelling framework based on project"""
        ideas = project_context.get("ideas", [])
        if ideas and ideas[0].get("potential_impact", {}).get("social_impact") == "high":
            return "hero_journey"
        else:
            return "problem_agitation_solution"
    
    async def _generate_slide_content(self, project_context: Dict, template: str, framework: str) -> List[Dict]:
        """Generate content for each slide"""
        template_slides = self.pitch_templates[template]["slides"]
        slides = []
        
        # Get project details
        project_name = project_context.get("name", "Our Solution")
        ideas = project_context.get("ideas", [{}])
        main_idea = ideas[0] if ideas else {}
        
        for slide_template in template_slides:
            slide = await self._generate_single_slide(
                slide_template, project_context, main_idea, project_name
            )
            slides.append(slide)
        
        return slides
    
    async def _generate_single_slide(self, slide_template: Dict, project_context: Dict, main_idea: Dict, project_name: str) -> Dict:
        """Generate content for a single slide"""
        slide_title = slide_template["title"]
        
        # Generate content based on slide type
        if slide_title in ["Problem", "The Challenge"]:
            content = self._generate_problem_slide(main_idea)
        elif slide_title in ["Solution", "Our Solution"]:
            content = self._generate_solution_slide(main_idea, project_name)
        elif slide_title in ["Market"]:
            content = self._generate_market_slide(main_idea)
        elif slide_title in ["Product Demo", "Solution Demo", "Live Demo"]:
            content = self._generate_demo_slide(project_context)
        elif slide_title in ["Technical Innovation"]:
            content = self._generate_technical_slide(project_context)
        elif slide_title in ["Impact", "Real Impact"]:
            content = self._generate_impact_slide(main_idea)
        elif slide_title in ["Team"]:
            content = self._generate_team_slide(project_context)
        elif slide_title in ["Next Steps", "Call to Action"]:
            content = self._generate_next_steps_slide(main_idea)
        elif slide_title in ["Hook"]:
            content = self._generate_hook_slide(main_idea)
        else:
            content = self._generate_generic_slide(slide_template, main_idea)
        
        return {
            "title": slide_title,
            "content": content,
            "visual_suggestions": self._suggest_visuals(slide_title, content),
            "speaking_time": self._estimate_speaking_time(content)
        }
    
    def _generate_problem_slide(self, main_idea: Dict) -> Dict:
        """Generate problem slide content"""
        problem = main_idea.get("problem", "market inefficiency").replace("_", " ").title()
        audience = main_idea.get("target_audience", "users")
        
        return {
            "headline": f"{audience.title()} struggle with {problem}",
            "bullet_points": [
                f"Current solutions for {problem} are inadequate",
                f"This affects {main_idea.get('potential_impact', {}).get('target_users', 'thousands of users')}",
                f"The cost of inaction is significant"
            ],
            "story_element": f"Imagine being a {audience} who faces {problem} daily...",
            "data_point": "Research shows this is a $X billion problem"
        }
    
    def _generate_solution_slide(self, main_idea: Dict, project_name: str) -> Dict:
        """Generate solution slide content"""
        innovation = main_idea.get("innovation_pattern", "advanced technology").replace("_", " ")
        technologies = main_idea.get("technologies", ["cutting-edge technology"])
        
        return {
            "headline": f"{project_name}: {main_idea.get('title', 'Revolutionary Solution')}",
            "bullet_points": [
                f"Leverages {', '.join(technologies[:2])} for superior results",
                f"Incorporates {innovation} for engaging user experience",
                f"Addresses core issues that existing solutions miss"
            ],
            "value_proposition": main_idea.get("description", "Our solution transforms how users interact with technology"),
            "key_features": main_idea.get("features", ["Advanced features"])[:3]
        }
    
    def _generate_market_slide(self, main_idea: Dict) -> Dict:
        """Generate market slide content"""
        market_potential = main_idea.get("market_potential", {})
        
        return {
            "headline": "Massive Market Opportunity",
            "market_size": market_potential.get("market_size", "Large addressable market"),
            "bullet_points": [
                f"Target market: {main_idea.get('target_audience', 'growing user base')}",
                f"Growth potential: {market_potential.get('growth_potential', 'High')}",
                f"Competition level: {market_potential.get('competition', 'Moderate')}"
            ],
            "opportunity": "Perfect timing to capture market share"
        }
    
    def _generate_demo_slide(self, project_context: Dict) -> Dict:
        """Generate demo slide content"""
        return {
            "headline": "Live Demonstration",
            "demo_flow": [
                "Show user problem scenario",
                "Demonstrate solution in action", 
                "Highlight key differentiators",
                "Show measurable results"
            ],
            "key_moments": [
                "Wow moment - show most impressive feature",
                "User benefit - demonstrate clear value",
                "Technical achievement - highlight innovation"
            ],
            "fallback_plan": "Prepared video demo if live demo fails"
        }
    
    def _generate_technical_slide(self, project_context: Dict) -> Dict:
        """Generate technical innovation slide"""
        tech_stack = project_context.get("tech_stack", {})
        
        return {
            "headline": "Technical Innovation",
            "innovations": [
                "Novel use of AI/ML algorithms",
                "Innovative architecture design",
                "Creative problem-solving approach"
            ],
            "tech_stack": tech_stack.get("primary", ["Modern technologies"]),
            "achievement": "Built working prototype in 48 hours"
        }
    
    def _generate_impact_slide(self, main_idea: Dict) -> Dict:
        """Generate impact slide content"""
        impact = main_idea.get("potential_impact", {})
        
        return {
            "headline": "Real-World Impact",
            "metrics": [
                f"Social impact: {impact.get('social_impact', 'High')}",
                f"Target users: {impact.get('target_users', '1000+ users')}",
                f"Scalability: {impact.get('scalability', 'High potential')}"
            ],
            "success_story": "Imagine the difference we can make...",
            "call_to_action": "Help us bring this solution to the world"
        }
    
    def _generate_team_slide(self, project_context: Dict) -> Dict:
        """Generate team slide content"""
        return {
            "headline": "The Team",
            "team_strengths": [
                "Diverse technical expertise",
                "Deep domain knowledge",
                "Proven execution ability"
            ],
            "unique_qualifications": "Perfect combination of skills for this challenge",
            "commitment": "Passionate about solving this problem"
        }
    
    def _generate_next_steps_slide(self, main_idea: Dict) -> Dict:
        """Generate next steps slide content"""
        return {
            "headline": "What's Next?",
            "immediate_steps": [
                "Refine prototype based on feedback",
                "Conduct user testing and validation",
                "Build partnerships with key stakeholders"
            ],
            "future_vision": "Scale to help millions of users worldwide",
            "ask": "Looking for mentorship and collaboration opportunities"
        }
    
    def _generate_hook_slide(self, main_idea: Dict) -> Dict:
        """Generate compelling opening hook"""
        audience = main_idea.get("target_audience", "people")
        problem = main_idea.get("problem", "challenges").replace("_", " ")
        
        return {
            "headline": f"What if {audience} never had to worry about {problem} again?",
            "story_opener": f"Every day, millions of {audience} face {problem}...",
            "shocking_stat": "This problem costs the world billions annually",
            "transition": "Today, we're going to show you the solution"
        }
    
    def _generate_generic_slide(self, slide_template: Dict, main_idea: Dict) -> Dict:
        """Generate generic slide content"""
        return {
            "headline": slide_template["title"],
            "content": slide_template["content"],
            "placeholder": "Content to be customized based on project specifics"
        }
    
    def _suggest_visuals(self, slide_title: str, content: Dict) -> List[str]:
        """Suggest visual elements for each slide"""
        visual_suggestions = {
            "Problem": ["Pain point illustrations", "User frustration scenarios", "Current state diagrams"],
            "Solution": ["Product screenshots", "Architecture diagrams", "Before/after comparisons"],
            "Demo": ["Live screen recording", "User workflow animations", "Feature highlights"],
            "Impact": ["Infographics", "Success metrics", "Growth projections"],
            "Team": ["Team photos", "Skill matrix", "Achievement highlights"]
        }
        
        return visual_suggestions.get(slide_title, ["Supporting graphics", "Clean typography", "Brand consistent design"])
    
    def _estimate_speaking_time(self, content: Dict) -> str:
        """Estimate speaking time for slide content"""
        # Rough estimation based on content amount
        word_count = sum(len(str(v).split()) for v in content.values())
        minutes = max(1, word_count // 100)  # ~100 words per minute
        return f"{minutes} minute{'s' if minutes > 1 else ''}"
    
    def _generate_speaker_notes(self, slides: List[Dict], project_context: Dict) -> List[Dict]:
        """Generate speaker notes for each slide"""
        speaker_notes = []
        
        for slide in slides:
            notes = {
                "slide_title": slide["title"],
                "key_points": self._extract_key_speaking_points(slide),
                "transitions": self._suggest_transitions(slide),
                "timing": slide["speaking_time"],
                "emphasis": self._suggest_emphasis_points(slide)
            }
            speaker_notes.append(notes)
        
        return speaker_notes
    
    def _extract_key_speaking_points(self, slide: Dict) -> List[str]:
        """Extract key points to emphasize while speaking"""
        content = slide["content"]
        
        key_points = []
        if "headline" in content:
            key_points.append(f"Lead with: {content['headline']}")
        if "bullet_points" in content:
            key_points.extend([f"Emphasize: {point}" for point in content["bullet_points"][:2]])
        if "story_element" in content:
            key_points.append(f"Tell story: {content['story_element']}")
        
        return key_points
    
    def _suggest_transitions(self, slide: Dict) -> List[str]:
        """Suggest smooth transitions between slides"""
        return [
            "Build on previous point",
            "Address natural follow-up question",
            "Create anticipation for next topic"
        ]
    
    def _suggest_emphasis_points(self, slide: Dict) -> List[str]:
        """Suggest what to emphasize during presentation"""
        return [
            "Pause for effect after key statistics",
            "Make eye contact during emotional moments",
            "Use gestures to reinforce main points"
        ]
    
    def _recommend_demo_strategy(self, project_context: Dict) -> str:
        """Recommend the best demo strategy"""
        tech_stack = project_context.get("tech_stack", {})
        
        # If we have a working prototype, go for live demo
        if any(tech in tech_stack.get("primary", []) for tech in ["react", "fastapi", "flask"]):
            return "live_demo"
        else:
            return "guided_storytelling"
    
    def _create_presentation_flow(self, slides: List[Dict], demo_strategy: str) -> Dict:
        """Create optimal presentation flow"""
        total_time = len(slides) * 1.5  # Rough estimate
        
        return {
            "total_estimated_time": f"{total_time:.0f} minutes",
            "structure": "Problem → Solution → Demo → Impact → Ask",
            "demo_placement": "After solution introduction, before impact",
            "energy_management": "Start strong, peak at demo, end with call to action",
            "interaction_points": ["Q&A after demo", "Invite judges to try solution"]
        }
    
    def _create_timing_guide(self, slides: List[Dict]) -> Dict:
        """Create timing guide for presentation"""
        return {
            "total_time": "5-7 minutes ideal for hackathons",
            "slide_distribution": "30-45 seconds per slide",
            "demo_time": "60-90 seconds for live demo",
            "buffer_time": "30 seconds for transitions and pauses",
            "q_and_a": "2-3 minutes for questions"
        }
    
    def _create_backup_plans(self, demo_strategy: str) -> List[str]:
        """Create backup plans for demo failures"""
        if demo_strategy == "live_demo":
            return [
                "Have pre-recorded video demo ready",
                "Prepare static screenshots walkthrough",
                "Practice narrating without visuals",
                "Have mobile hotspot as internet backup"
            ]
        else:
            return [
                "Have printed slides as backup",
                "Prepare to present without visuals",
                "Practice key points from memory"
            ]
    
    def _prepare_q_and_a(self, project_context: Dict) -> Dict:
        """Prepare for Q&A session"""
        return {
            "likely_questions": [
                "How is this different from existing solutions?",
                "What are the biggest technical challenges?",
                "How would you monetize this?",
                "What would you do with more time/resources?",
                "Who is your target customer?"
            ],
            "answer_framework": "Acknowledge → Answer → Redirect to strengths",
            "difficult_questions": [
                "If you don't know, say so and explain how you'd find out",
                "If it's a known limitation, acknowledge and show how you'd address it",
                "Always tie back to the core value proposition"
            ]
        }
    
    async def create_demo_assets(self, project_context: Dict) -> Dict:
        """Create supporting assets for the demo"""
        return {
            "demo_script": await self._create_demo_script(project_context),
            "user_scenarios": self._create_user_scenarios(project_context),
            "talking_points": self._create_demo_talking_points(project_context),
            "backup_materials": self._create_backup_demo_materials(project_context)
        }
    
    async def _create_demo_script(self, project_context: Dict) -> List[str]:
        """Create step-by-step demo script"""
        return [
            "1. Set context: 'Let me show you how Sarah, our target user, would use this'",
            "2. Show problem: 'First, here's the current painful process'",
            "3. Introduce solution: 'Now, watch how our solution changes everything'",
            "4. Demonstrate key features: 'Notice how easy this is...'",
            "5. Show results: 'In just 30 seconds, we've solved a problem that used to take hours'",
            "6. Tie back to impact: 'Imagine this scaled to millions of users'"
        ]
    
    def _create_user_scenarios(self, project_context: Dict) -> List[Dict]:
        """Create realistic user scenarios for demo"""
        ideas = project_context.get("ideas", [{}])
        main_idea = ideas[0] if ideas else {}
        
        return [
            {
                "persona": "Primary user",
                "scenario": f"Needs to solve {main_idea.get('problem', 'common problem')}",
                "pain_points": "Current process is slow and frustrating",
                "solution_benefit": "Our solution makes it fast and enjoyable"
            }
        ]
    
    def _create_demo_talking_points(self, project_context: Dict) -> List[str]:
        """Create key talking points during demo"""
        return [
            "Highlight ease of use",
            "Emphasize speed improvement",
            "Point out innovative features",
            "Show measurable results",
            "Connect to broader impact"
        ]
    
    def _create_backup_demo_materials(self, project_context: Dict) -> Dict:
        """Create backup materials in case demo fails"""
        return {
            "screenshot_walkthrough": "Series of annotated screenshots",
            "video_demo": "Pre-recorded demo video",
            "printed_storyboard": "Physical backup slides",
            "verbal_description": "Script for demo without visuals"
        }
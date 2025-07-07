#!/usr/bin/env python3
"""
Demo Script for Hackathon AI Assistant
======================================
Shows off the key capabilities of your AI assistant
"""

import asyncio
import json
from hackathon_ai_assistant import HackathonAIAssistant
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

async def demo_idea_generation():
    """Demo the idea generation capabilities"""
    console.print(Panel("💡 Idea Generation Demo", style="bold blue"))
    
    assistant = HackathonAIAssistant()
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("Generating innovative ideas...", total=None)
        
        # Generate ideas for a climate change hackathon
        ideas = await assistant.idea_generator.generate_ideas(
            theme="Climate Change", 
            constraints=["48_hours", "mobile_first"], 
            count=3
        )
        
        progress.update(task, completed=1)
    
    # Display results
    table = Table(title="Generated Ideas")
    table.add_column("Rank", style="cyan")
    table.add_column("Title", style="bold")
    table.add_column("Score", style="green")
    table.add_column("Domain", style="yellow")
    
    for i, idea in enumerate(ideas, 1):
        table.add_row(
            str(i),
            idea['title'],
            f"{idea.get('overall_score', 0):.0f}/100",
            idea['domain'].title()
        )
    
    console.print(table)
    
    # Show detailed view of top idea
    if ideas:
        top_idea = ideas[0]
        console.print(f"\n📋 Top Idea Details:")
        console.print(f"Description: {top_idea['description'][:200]}...")
        console.print(f"Technologies: {', '.join(top_idea['technologies'][:3])}")
        console.print(f"Timeline: {top_idea['mvp_timeline']['total_hours']} hours")

async def demo_code_generation():
    """Demo the code generation capabilities"""
    console.print(Panel("🏗️ Code Generation Demo", style="bold green"))
    
    assistant = HackathonAIAssistant()
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("Generating FastAPI application...", total=None)
        
        # Generate a FastAPI app
        result = await assistant.code_generator.generate(
            prompt="Create a FastAPI app for carbon footprint tracking with user authentication",
            language="python",
            framework="fastapi"
        )
        
        progress.update(task, completed=1)
    
    console.print("✅ Generated complete FastAPI application!")
    console.print(f"📄 File: {result['file_name']}")
    console.print(f"🔧 Dependencies: {', '.join(result['dependencies'][:5])}")
    
    # Show code snippet
    code_preview = result['code'][:500] + "..." if len(result['code']) > 500 else result['code']
    console.print(Panel(code_preview, title="Generated Code Preview", border_style="green"))

async def demo_tech_stack_recommendation():
    """Demo the tech stack advisor"""
    console.print(Panel("🛠️ Tech Stack Recommendation Demo", style="bold yellow"))
    
    assistant = HackathonAIAssistant()
    
    # Simulate a healthcare AI project
    mock_ideas = [{
        "domain": "healthcare",
        "technologies": ["machine_learning", "nlp"],
        "features": ["dashboard", "real-time analytics", "AI recommendations"]
    }]
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("Analyzing requirements and recommending tech stack...", total=None)
        
        recommendations = await assistant.tech_stack_advisor.recommend_stack(
            theme="Healthcare AI", 
            ideas=mock_ideas
        )
        
        progress.update(task, completed=1)
    
    # Display recommendations
    primary = recommendations['primary']
    console.print(f"🎯 Recommended Stack: {primary['name']}")
    console.print(f"⭐ Score: {primary['score']}/100")
    console.print(f"💭 Rationale: {primary['rationale']}")
    
    # Show tech details
    tech_table = Table(title="Technology Stack Details")
    tech_table.add_column("Layer", style="cyan")
    tech_table.add_column("Technologies", style="white")
    
    tech_table.add_row("Frontend", ", ".join(primary.get('frontend', [])))
    tech_table.add_row("Backend", ", ".join(primary.get('backend', [])))
    tech_table.add_row("Database", ", ".join(primary.get('database', [])))
    tech_table.add_row("Deployment", ", ".join(primary.get('deployment', [])))
    
    console.print(tech_table)

async def demo_research_capabilities():
    """Demo the market research capabilities"""
    console.print(Panel("📊 Market Research Demo", style="bold magenta"))
    
    assistant = HackathonAIAssistant()
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("Conducting market research...", total=None)
        
        # Research the EdTech market
        research = await assistant.research_agent.research_topic("Educational Technology for Remote Learning")
        
        progress.update(task, completed=1)
    
    console.print("✅ Market Research Complete!")
    
    # Show key insights
    market = research['market_analysis']
    console.print(f"🏢 Domain: {market['domain'].title()}")
    console.print(f"📈 Market Size: {market['market_size']}")
    console.print(f"📊 Growth Rate: {market['growth_rate']}")
    console.print(f"🎯 Key Trends: {', '.join(market['key_trends'][:3])}")
    
    # Show opportunities
    if research.get('opportunities'):
        console.print("\n🚀 Top Opportunities:")
        for i, opp in enumerate(research['opportunities'][:3], 1):
            console.print(f"  {i}. {opp['description']} (Potential: {opp['potential']})")

async def demo_pitch_generation():
    """Demo pitch deck generation"""
    console.print(Panel("📈 Pitch Deck Generation Demo", style="bold red"))
    
    assistant = HackathonAIAssistant()
    
    # Mock project context
    mock_context = {
        "name": "EcoTracker",
        "theme": "Climate Change",
        "ideas": [{
            "title": "AI-Powered Carbon Footprint Tracker",
            "description": "Smart application that uses AI to track and reduce personal carbon footprint",
            "domain": "environment",
            "target_audience": "environmentally conscious individuals",
            "potential_impact": {"social_impact": "high", "target_users": "10M+ users"},
            "technologies": ["machine_learning", "mobile_app", "data_analytics"]
        }]
    }
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("Creating winning pitch deck...", total=None)
        
        pitch_deck = await assistant.pitch_assistant.create_pitch_deck(mock_context, "judges")
        
        progress.update(task, completed=1)
    
    console.print("✅ Pitch Deck Created!")
    
    # Show slide overview
    slides_table = Table(title="Pitch Deck Structure")
    slides_table.add_column("Slide #", style="cyan")
    slides_table.add_column("Title", style="bold")
    slides_table.add_column("Time", style="yellow")
    
    for i, slide in enumerate(pitch_deck['slides'], 1):
        slides_table.add_row(str(i), slide['title'], slide['speaking_time'])
    
    console.print(slides_table)
    console.print(f"📊 Total Presentation Time: {pitch_deck['timing_guide']['total_time']}")
    console.print(f"🎯 Demo Strategy: {pitch_deck['demo_strategy'].title()}")

async def run_full_demo():
    """Run the complete demo"""
    console.print(Panel("🚀 Ultimate Hackathon AI Assistant Demo", title="Welcome", style="bold blue"))
    console.print("This demo showcases the key capabilities that will help you WIN hackathons!\n")
    
    demos = [
        ("💡 Idea Generation", demo_idea_generation),
        ("🏗️ Code Generation", demo_code_generation),
        ("🛠️ Tech Stack Recommendation", demo_tech_stack_recommendation),
        ("📊 Market Research", demo_research_capabilities),
        ("📈 Pitch Deck Creation", demo_pitch_generation)
    ]
    
    for title, demo_func in demos:
        console.print(f"\n{title}")
        console.print("=" * 50)
        try:
            await demo_func()
        except Exception as e:
            console.print(f"❌ Demo error: {e}", style="red")
        
        input("\nPress Enter to continue to next demo...")
    
    console.print(Panel("🏆 Demo Complete! Ready to dominate your next hackathon?", style="bold green"))
    console.print("🚀 Start with: python run_assistant.py --web")

if __name__ == "__main__":
    console.print("🎬 Starting Hackathon AI Assistant Demo...")
    asyncio.run(run_full_demo())
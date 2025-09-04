#!/usr/bin/env python3
"""
Web Interface for Hackathon AI Assistant
========================================
Beautiful Streamlit interface for easy interaction with your AI assistant
"""

import streamlit as st
import asyncio
import json
from datetime import datetime
from hackathon_ai_assistant import HackathonAIAssistant

# Configure page
st.set_page_config(
    page_title="🚀 Hackathon AI Assistant",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better appearance
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        text-align: center;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2rem;
    }
    .feature-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
    .status-success {
        background-color: #d4edda;
        color: #155724;
        padding: 0.75rem;
        border-radius: 5px;
        border: 1px solid #c3e6cb;
    }
    .status-info {
        background-color: #cce7ff;
        color: #004085;
        padding: 0.75rem;
        border-radius: 5px;
        border: 1px solid #9fcdff;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'assistant' not in st.session_state:
    st.session_state.assistant = HackathonAIAssistant()
    st.session_state.project_active = False
    st.session_state.project_context = None

def main():
    # Header
    st.markdown('<h1 class="main-header">🚀 Ultimate Hackathon AI Assistant</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #666;">Your complete AI companion for dominating hackathons! 🏆</p>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown("## 🎯 Quick Actions")
        
        # Project status
        if st.session_state.project_active:
            st.markdown('<div class="status-success">✅ Project Active</div>', unsafe_allow_html=True)
            st.write(f"**Project:** {st.session_state.project_context['name']}")
            if st.button("📊 View Project Status"):
                show_project_status()
        else:
            st.markdown('<div class="status-info">ℹ️ No Active Project</div>', unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Quick tools
        st.markdown("### 🛠️ Quick Tools")
        if st.button("💡 Generate Ideas"):
            st.session_state.page = "ideas"
        if st.button("🏗️ Create App"):
            st.session_state.page = "create_app"
        if st.button("🎨 Design Helper"):
            st.session_state.page = "design"
        if st.button("🚀 Deploy Project"):
            st.session_state.page = "deploy"
        if st.button("📈 Create Pitch"):
            st.session_state.page = "pitch"
        
        st.markdown("---")
        st.markdown("### 📚 Resources")
        st.markdown("- [React Docs](https://reactjs.org)")
        st.markdown("- [FastAPI Docs](https://fastapi.tiangolo.com)")
        st.markdown("- [Vercel Deployment](https://vercel.com)")
        st.markdown("- [Hackathon Tips](https://hackathon.guide)")
    
    # Main content
    if 'page' not in st.session_state:
        st.session_state.page = "home"
    
    if st.session_state.page == "home":
        show_home_page()
    elif st.session_state.page == "start_project":
        show_start_project_page()
    elif st.session_state.page == "ideas":
        show_ideas_page()
    elif st.session_state.page == "create_app":
        show_create_app_page()
    elif st.session_state.page == "design":
        show_design_page()
    elif st.session_state.page == "deploy":
        show_deploy_page()
    elif st.session_state.page == "pitch":
        show_pitch_page()

def show_home_page():
    # Hero section
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        ### 🎯 Ready to WIN your next hackathon?
        
        This AI assistant is your secret weapon! It combines:
        - **🧠 Advanced AI** for code generation and problem-solving
        - **💡 Creative ideation** with feasibility analysis
        - **🏗️ Rapid prototyping** with full-stack code generation
        - **🎨 Design assistance** for beautiful UIs
        - **🚀 One-click deployment** to showcase your demo
        - **📈 Pitch creation** to impress judges
        """)
        
        if st.button("🚀 Start New Project", key="start_project_btn", help="Begin your hackathon journey!"):
            st.session_state.page = "start_project"
    
    # Features grid
    st.markdown("## 🌟 Core Features")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3>💡 Idea Generation</h3>
            <p>Generate innovative project ideas based on hackathon themes with feasibility scoring and market analysis.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h3>🏗️ Full-Stack Development</h3>
            <p>Generate complete applications with React frontends, FastAPI backends, and database schemas.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3>🎨 Design Assistant</h3>
            <p>Create beautiful UIs with design systems, color schemes, and responsive layouts optimized for demos.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h3>🚀 Rapid Deployment</h3>
            <p>Deploy your projects to Vercel, Netlify, or Heroku with one command for live demos.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h3>📊 Market Research</h3>
            <p>Conduct competitive analysis and market research to strengthen your project's value proposition.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h3>📈 Pitch Creation</h3>
            <p>Generate compelling pitch decks with storytelling frameworks and demo strategies.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Success stories section
    st.markdown("## 🏆 Built for Success")
    st.markdown("""
    This assistant incorporates best practices from winning hackathon teams:
    - **⚡ Speed**: Generate working prototypes in minutes, not hours
    - **🎯 Focus**: Stay on track with guided workflows and time management
    - **💎 Quality**: Professional-grade code and design from the start
    - **🎭 Demo-Ready**: Everything optimized for impressive presentations
    """)

def show_start_project_page():
    st.markdown("## 🎯 Start New Hackathon Project")
    
    with st.form("new_project_form"):
        st.markdown("### Project Details")
        
        col1, col2 = st.columns(2)
        with col1:
            project_name = st.text_input("Project Name", value="", help="Choose a memorable name for your project")
            theme = st.text_input("Hackathon Theme", value="", help="e.g., 'AI for Good', 'FinTech Innovation', 'Climate Change'")
        
        with col2:
            time_limit = st.selectbox("Time Limit", ["24 hours", "48 hours", "72 hours", "1 week"], index=1)
            team_size = st.selectbox("Team Size", ["1 (Solo)", "2-3 people", "4-5 people", "6+ people"], index=1)
        
        constraints = st.multiselect(
            "Constraints & Requirements",
            ["Must use specific API", "Mobile-first", "AI/ML required", "Blockchain", "Hardware/IoT", "Accessibility focus"],
            help="Select any specific requirements or constraints"
        )
        
        st.markdown("### Additional Context")
        additional_context = st.text_area(
            "Tell us more about your hackathon, target audience, or specific goals",
            height=100,
            help="This helps us generate better ideas and recommendations"
        )
        
        submitted = st.form_submit_button("🚀 Initialize Project")
        
        if submitted and project_name:
            with st.spinner("Initializing your hackathon project..."):
                # Call the assistant to start new project
                try:
                    context = asyncio.run(st.session_state.assistant.start_new_project(
                        project_name, theme, constraints
                    ))
                    st.session_state.project_context = context
                    st.session_state.project_active = True
                    
                    st.success("🎉 Project initialized successfully!")
                    
                    # Show project overview
                    st.markdown("### 📋 Project Overview")
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.markdown(f"**Name:** {context['name']}")
                        st.markdown(f"**Theme:** {context['theme']}")
                        st.markdown(f"**Ideas Generated:** {len(context['ideas'])}")
                    
                    with col2:
                        st.markdown(f"**Tech Stack:** {', '.join(context['tech_stack'].get('primary', []))}")
                        st.markdown(f"**Start Time:** {context['start_time'].strftime('%Y-%m-%d %H:%M')}")
                    
                    # Show top ideas
                    if context['ideas']:
                        st.markdown("### 💡 Top Generated Ideas")
                        for i, idea in enumerate(context['ideas'][:3], 1):
                            with st.expander(f"Idea {i}: {idea['title']} (Score: {idea.get('overall_score', 0):.0f})"):
                                st.write(f"**Description:** {idea['description']}")
                                st.write(f"**Domain:** {idea['domain'].title()}")
                                st.write(f"**Technologies:** {', '.join(idea['technologies'])}")
                                st.write(f"**Feasibility:** {idea.get('feasibility_score', 0):.0f}/100")
                    
                    if st.button("Continue to Development 🔧"):
                        st.session_state.page = "create_app"
                
                except Exception as e:
                    st.error(f"Error initializing project: {str(e)}")
        elif submitted:
            st.warning("Please enter a project name to continue.")

def show_ideas_page():
    st.markdown("## 💡 Idea Generation")
    
    if not st.session_state.project_active:
        st.warning("Please start a project first to generate ideas.")
        if st.button("Start New Project"):
            st.session_state.page = "start_project"
        return
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### Generate New Ideas")
        theme = st.text_input("Theme or Focus Area", value=st.session_state.project_context.get('theme', ''))
        constraints = st.multiselect("Constraints", ["Time limited", "Beginner friendly", "AI/ML focus", "Mobile first"])
        count = st.slider("Number of ideas to generate", 1, 10, 5)
        
        if st.button("🎯 Generate Ideas"):
            with st.spinner("Generating innovative ideas..."):
                try:
                    ideas = asyncio.run(st.session_state.assistant.idea_generator.generate_ideas(theme, constraints, count))
                    st.session_state.generated_ideas = ideas
                    st.success(f"Generated {len(ideas)} new ideas!")
                except Exception as e:
                    st.error(f"Error generating ideas: {str(e)}")
    
    with col2:
        st.markdown("### 📊 Idea Quality Factors")
        st.markdown("""
        - **Feasibility (60%)**: Can be built in time
        - **Innovation (40%)**: Uniqueness and creativity
        - **Market Impact**: Potential user value
        - **Technical Complexity**: Implementation difficulty
        """)
    
    # Display generated ideas
    if hasattr(st.session_state, 'generated_ideas'):
        st.markdown("### 🌟 Generated Ideas")
        
        for i, idea in enumerate(st.session_state.generated_ideas, 1):
            with st.expander(f"💡 {idea['title']} - Score: {idea.get('overall_score', 0):.0f}/100"):
                col1, col2 = st.columns([3, 1])
                
                with col1:
                    st.write(f"**Description:** {idea['description']}")
                    st.write(f"**Target Audience:** {idea['target_audience'].title()}")
                    st.write(f"**Domain:** {idea['domain'].title()}")
                    
                    # Features
                    if idea.get('features'):
                        st.write("**Key Features:**")
                        for feature in idea['features'][:5]:
                            st.write(f"  • {feature}")
                    
                    # Timeline
                    if idea.get('mvp_timeline'):
                        st.write(f"**Estimated Time:** {idea['mvp_timeline']['total_hours']} hours")
                
                with col2:
                    # Scores
                    st.metric("Feasibility", f"{idea.get('feasibility_score', 0):.0f}/100")
                    st.metric("Innovation", f"{idea.get('innovation_score', 0):.0f}/100")
                    
                    if st.button(f"Select Idea {i}", key=f"select_idea_{i}"):
                        st.session_state.selected_idea = idea
                        st.success(f"Selected: {idea['title']}")

def show_create_app_page():
    st.markdown("## 🏗️ Create Full Application")
    
    if not st.session_state.project_active:
        st.warning("Please start a project first.")
        return
    
    with st.form("create_app_form"):
        st.markdown("### Application Configuration")
        
        col1, col2 = st.columns(2)
        with col1:
            app_type = st.selectbox("Application Type", ["web", "mobile", "api", "cli", "desktop"])
            design_style = st.selectbox("Design Style", ["modern", "minimal", "colorful", "professional", "playful"])
        
        with col2:
            framework_preference = st.selectbox("Framework Preference", ["react", "vue", "angular", "streamlit", "gradio"])
            database_type = st.selectbox("Database", ["sqlite", "postgresql", "mongodb", "firebase"])
        
        features = st.multiselect(
            "Features to Include",
            ["authentication", "dashboard", "analytics", "real-time chat", "file upload", 
             "search", "notifications", "api integration", "payment processing", "admin panel"],
            default=["authentication", "dashboard"]
        )
        
        submitted = st.form_submit_button("🚀 Generate Complete App")
        
        if submitted:
            with st.spinner("Generating your complete application... This may take a few minutes."):
                try:
                    # Generate the full app
                    result = asyncio.run(st.session_state.assistant.create_full_app(app_type, features, design_style))
                    
                    st.success("🎉 Application generated successfully!")
                    
                    # Show generation results
                    st.markdown("### 📁 Generated Components")
                    
                    for component_type, files in result["components"].items():
                        with st.expander(f"📂 {component_type.title()} ({len(files)} files)"):
                            for filename in files.keys():
                                st.write(f"• {filename}")
                    
                    # Show next steps
                    st.markdown("### 🔄 Next Steps")
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        if st.button("🎨 Customize Design"):
                            st.session_state.page = "design"
                    
                    with col2:
                        if st.button("🚀 Deploy App"):
                            st.session_state.page = "deploy"
                    
                    with col3:
                        if st.button("📈 Create Pitch"):
                            st.session_state.page = "pitch"
                
                except Exception as e:
                    st.error(f"Error generating app: {str(e)}")

def show_design_page():
    st.markdown("## 🎨 Design Assistant")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### Design Configuration")
        
        # Color scheme selection
        color_scheme = st.selectbox(
            "Color Scheme",
            ["Tech Blue", "Success Green", "Vibrant Purple", "Elegant Gray", "Warm Orange"]
        )
        
        # Design style
        design_patterns = st.multiselect(
            "Design Patterns",
            ["Dashboard Layout", "Landing Page", "Mobile-First", "Card-Based", "Sidebar Navigation"],
            default=["Dashboard Layout"]
        )
        
        # Typography
        font_style = st.selectbox("Typography", ["Modern Sans", "Classic Serif", "Tech Mono", "Friendly Round"])
        
        # Generate design
        if st.button("🎨 Generate Design System"):
            with st.spinner("Creating your design system..."):
                st.success("Design system generated!")
                
                # Show color palette
                st.markdown("#### 🎨 Color Palette")
                if color_scheme == "Tech Blue":
                    colors = {"Primary": "#2563eb", "Secondary": "#64748b", "Accent": "#06b6d4"}
                    for name, color in colors.items():
                        st.markdown(f'<div style="background-color: {color}; padding: 10px; margin: 5px; border-radius: 5px; color: white;">{name}: {color}</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 🎯 Design Tips")
        st.markdown("""
        **For Hackathon Success:**
        - Keep it simple and clean
        - Use consistent spacing
        - Make it mobile-friendly
        - Ensure good contrast
        - Use modern UI patterns
        
        **Demo-Friendly Colors:**
        - High contrast for projectors
        - Professional appearance
        - Memorable brand colors
        """)

def show_deploy_page():
    st.markdown("## 🚀 Deploy Your Project")
    
    if not st.session_state.project_active:
        st.warning("Please start a project first.")
        return
    
    st.markdown("### Deployment Options")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        #### Vercel
        - ✅ Free tier
        - ⚡ Fast deployment
        - 🌐 Custom domains
        - 🎯 Best for: React, Next.js
        """)
        if st.button("Deploy to Vercel"):
            deploy_to_platform("vercel")
    
    with col2:
        st.markdown("""
        #### Netlify
        - ✅ Free tier
        - 📁 Drag & drop
        - 🔄 Git integration
        - 🎯 Best for: Static sites
        """)
        if st.button("Deploy to Netlify"):
            deploy_to_platform("netlify")
    
    with col3:
        st.markdown("""
        #### Railway
        - ✅ Free tier
        - 🐍 Great Python support
        - 💾 Database included
        - 🎯 Best for: Full-stack
        """)
        if st.button("Deploy to Railway"):
            deploy_to_platform("railway")

def deploy_to_platform(platform):
    with st.spinner(f"Deploying to {platform}..."):
        try:
            if st.session_state.project_context:
                result = asyncio.run(st.session_state.assistant.deployment_helper.deploy_project(
                    st.session_state.project_context['path'],
                    st.session_state.project_context['tech_stack']
                ))
                
                if result:
                    st.success(f"🎉 Successfully deployed to {platform}!")
                    st.markdown(f"**Live URL:** {result}")
                    
                    # Show deployment instructions
                    st.markdown("### 📋 Deployment Complete")
                    st.markdown(f"""
                    Your project is now live! Here's what you can do:
                    
                    1. 🔗 **Share the URL** with judges and teammates
                    2. 📱 **Test on mobile** to ensure responsiveness  
                    3. ⚡ **Check performance** and loading speed
                    4. 🎯 **Prepare your demo** using the live version
                    """)
                else:
                    st.error("Deployment failed. Please check your project configuration.")
        except Exception as e:
            st.error(f"Deployment error: {str(e)}")

def show_pitch_page():
    st.markdown("## 📈 Create Pitch Deck")
    
    if not st.session_state.project_active:
        st.warning("Please start a project first.")
        return
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### Pitch Configuration")
        
        target_audience = st.selectbox("Target Audience", ["Judges", "Investors", "Technical Panel", "General Audience"])
        pitch_length = st.selectbox("Pitch Length", ["3 minutes", "5 minutes", "7 minutes", "10 minutes"])
        focus_areas = st.multiselect(
            "Focus Areas",
            ["Technical Innovation", "Business Impact", "Social Good", "User Experience", "Market Opportunity"],
            default=["Technical Innovation", "User Experience"]
        )
        
        if st.button("📈 Generate Pitch Deck"):
            with st.spinner("Creating your winning pitch deck..."):
                try:
                    pitch_deck = asyncio.run(st.session_state.assistant.create_pitch_deck(
                        st.session_state.project_context, target_audience.lower()
                    ))
                    
                    st.success("🎉 Pitch deck created successfully!")
                    
                    # Show pitch overview
                    st.markdown("### 📊 Pitch Overview")
                    st.write(f"**Template:** {pitch_deck['template'].title()}")
                    st.write(f"**Framework:** {pitch_deck['framework'].title()}")
                    st.write(f"**Total Slides:** {len(pitch_deck['slides'])}")
                    st.write(f"**Estimated Time:** {pitch_deck['timing_guide']['total_time']}")
                    
                    # Show slides
                    st.markdown("### 🎯 Slide Breakdown")
                    for i, slide in enumerate(pitch_deck['slides'], 1):
                        with st.expander(f"Slide {i}: {slide['title']} ({slide['speaking_time']})"):
                            content = slide['content']
                            if 'headline' in content:
                                st.write(f"**Headline:** {content['headline']}")
                            if 'bullet_points' in content:
                                for point in content['bullet_points']:
                                    st.write(f"• {point}")
                            
                            # Visual suggestions
                            if slide.get('visual_suggestions'):
                                st.write("**Visual Suggestions:**")
                                for suggestion in slide['visual_suggestions'][:3]:
                                    st.write(f"  - {suggestion}")
                
                except Exception as e:
                    st.error(f"Error creating pitch deck: {str(e)}")
    
    with col2:
        st.markdown("### 🎯 Pitch Tips")
        st.markdown("""
        **Winning Pitch Elements:**
        - Hook audience in first 30 seconds
        - Clear problem statement
        - Live demo (if possible)
        - Quantify your impact
        - Strong call to action
        
        **Demo Best Practices:**
        - Practice extensively
        - Have backup plans
        - Show, don't just tell
        - Keep it simple
        - End with impact
        """)

def show_project_status():
    if st.session_state.project_context:
        st.markdown("## 📊 Project Status")
        context = st.session_state.project_context
        
        # Time tracking
        elapsed = datetime.now() - context['start_time']
        hours = elapsed.total_seconds() / 3600
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Hours Elapsed", f"{hours:.1f}")
        with col2:
            st.metric("Ideas Generated", len(context.get('ideas', [])))
        with col3:
            st.metric("Tech Stack", len(context.get('tech_stack', {}).get('primary', [])))

if __name__ == "__main__":
    main()
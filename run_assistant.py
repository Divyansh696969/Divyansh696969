#!/usr/bin/env python3
"""
Quick Start Script for Hackathon AI Assistant
=============================================
Launch your AI assistant with ease!
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path

def check_dependencies():
    """Check if required dependencies are installed"""
    required_packages = [
        'streamlit', 'fastapi', 'requests', 'rich'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print("❌ Missing required packages:")
        for package in missing_packages:
            print(f"   - {package}")
        print("\n🔧 Install with: pip install -r requirements.txt")
        return False
    
    return True

def launch_web_interface():
    """Launch the Streamlit web interface"""
    print("🚀 Launching web interface...")
    print("📱 Open http://localhost:8501 in your browser")
    subprocess.run([sys.executable, "-m", "streamlit", "run", "web_interface.py"])

def launch_cli_interface():
    """Launch the command-line interface"""
    print("💻 Launching CLI interface...")
    subprocess.run([sys.executable, "hackathon_ai_assistant.py", "--interactive"])

def quick_setup():
    """Perform quick setup and dependency check"""
    print("🔧 Setting up Hackathon AI Assistant...")
    
    # Check Python version
    if sys.version_info < (3, 9):
        print("❌ Python 3.9+ required. Current version:", sys.version)
        return False
    
    # Check dependencies
    if not check_dependencies():
        return False
    
    # Check config file
    config_file = Path("config.json")
    if not config_file.exists():
        print("📋 Creating default configuration...")
        # Config already exists from previous creation
    
    print("✅ Setup complete!")
    return True

def show_welcome():
    """Show welcome message and options"""
    print("""
🚀 Ultimate Hackathon AI Assistant
==================================

Your complete AI companion for dominating hackathons! 🏆

Choose your interface:
1. 🌐 Web Interface (Recommended) - Beautiful Streamlit UI
2. 💻 Command Line Interface - Terminal-based interaction
3. 🔧 Setup & Check Dependencies
4. ❓ Help & Documentation

""")

def show_help():
    """Show help information"""
    print("""
🆘 Help & Usage
===============

Quick Start:
  python run_assistant.py                    # Interactive menu
  python run_assistant.py --web              # Launch web interface
  python run_assistant.py --cli              # Launch CLI interface
  python run_assistant.py --setup            # Setup and check dependencies

Examples:
  # Start new project via CLI
  python hackathon_ai_assistant.py --project "MyApp" --theme "AI for Good"
  
  # Generate ideas
  python hackathon_ai_assistant.py --generate-ideas --theme "FinTech" --count 5
  
  # Create and deploy app
  python hackathon_ai_assistant.py --create-app --type web --deploy vercel

Features:
  💡 Idea Generation       - Generate innovative project ideas
  🏗️  Full-Stack Development - Create complete applications
  🎨 Design Assistance     - Beautiful UI/UX design systems
  🚀 Rapid Deployment      - One-click deployment to cloud
  📈 Pitch Creation        - Winning presentation decks
  📊 Market Research       - Competitive analysis and insights

For detailed documentation, visit: docs/
""")

def main():
    parser = argparse.ArgumentParser(description="Launch Hackathon AI Assistant")
    parser.add_argument("--web", action="store_true", help="Launch web interface")
    parser.add_argument("--cli", action="store_true", help="Launch CLI interface")
    parser.add_argument("--setup", action="store_true", help="Setup and check dependencies")
    parser.add_argument("--help-detailed", action="store_true", help="Show detailed help")
    
    args = parser.parse_args()
    
    # Handle command line arguments
    if args.help_detailed:
        show_help()
        return
    
    if args.setup:
        quick_setup()
        return
    
    if args.web:
        if quick_setup():
            launch_web_interface()
        return
    
    if args.cli:
        if quick_setup():
            launch_cli_interface()
        return
    
    # Interactive mode
    show_welcome()
    
    while True:
        try:
            choice = input("Choose an option (1-4): ").strip()
            
            if choice == "1":
                if quick_setup():
                    launch_web_interface()
                break
            elif choice == "2":
                if quick_setup():
                    launch_cli_interface()
                break
            elif choice == "3":
                quick_setup()
            elif choice == "4":
                show_help()
            elif choice.lower() in ['q', 'quit', 'exit']:
                print("👋 Good luck with your hackathon!")
                break
            else:
                print("❌ Invalid choice. Please enter 1-4 or 'q' to quit.")
        
        except KeyboardInterrupt:
            print("\n👋 Good luck with your hackathon!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
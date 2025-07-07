"""
Design Assistant Module
======================
Provides UI/UX design assistance for hackathon projects
"""

import asyncio
from typing import Dict, List, Any, Optional

class DesignAssistant:
    """Helps with UI/UX design decisions and creates design assets"""
    
    def __init__(self):
        self.design_patterns = self._load_design_patterns()
        self.color_schemes = self._load_color_schemes()
        self.ui_components = self._load_ui_components()
    
    def _load_design_patterns(self) -> Dict:
        """Load common design patterns for hackathons"""
        return {
            "dashboard": {
                "layout": "sidebar + main content",
                "components": ["navigation", "metrics cards", "charts", "data tables"],
                "best_practices": ["clear hierarchy", "consistent spacing", "responsive design"]
            },
            "landing_page": {
                "layout": "hero + features + cta",
                "components": ["hero section", "feature grid", "testimonials", "call-to-action"],
                "best_practices": ["compelling headline", "clear value proposition", "social proof"]
            },
            "mobile_app": {
                "layout": "tab navigation + screens",
                "components": ["bottom navigation", "cards", "forms", "lists"],
                "best_practices": ["thumb-friendly", "minimal text", "clear icons"]
            }
        }
    
    def _load_color_schemes(self) -> Dict:
        """Load color schemes optimized for demos"""
        return {
            "tech_blue": {
                "primary": "#2563eb",
                "secondary": "#64748b", 
                "accent": "#06b6d4",
                "background": "#f8fafc",
                "text": "#1e293b"
            },
            "success_green": {
                "primary": "#059669",
                "secondary": "#6b7280",
                "accent": "#10b981", 
                "background": "#f0fdf4",
                "text": "#065f46"
            },
            "vibrant_purple": {
                "primary": "#7c3aed",
                "secondary": "#a78bfa",
                "accent": "#f59e0b",
                "background": "#faf5ff", 
                "text": "#581c87"
            }
        }
    
    def _load_ui_components(self) -> Dict:
        """Load reusable UI component templates"""
        return {
            "button": {
                "primary": "bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700",
                "secondary": "bg-gray-200 text-gray-800 px-6 py-3 rounded-lg hover:bg-gray-300"
            },
            "card": {
                "default": "bg-white rounded-lg shadow-md p-6",
                "elevated": "bg-white rounded-lg shadow-lg p-6 border"
            },
            "input": {
                "default": "border border-gray-300 rounded-md px-3 py-2 focus:ring-2 focus:ring-blue-500"
            }
        }
    
    async def create_design(self, app_type: str, features: List[str], design_style: str = "modern") -> Dict:
        """Create design specifications for the application"""
        # Select appropriate design pattern
        pattern = self._select_design_pattern(app_type, features)
        
        # Choose color scheme
        colors = self._select_color_scheme(design_style, features)
        
        # Generate layout structure
        layout = self._generate_layout(pattern, features)
        
        # Create component specifications
        components = self._generate_components(features, colors)
        
        return {
            "style": design_style,
            "pattern": pattern,
            "colors": colors,
            "layout": layout,
            "components": components,
            "typography": self._generate_typography(),
            "spacing": self._generate_spacing(),
            "responsive_breakpoints": self._generate_breakpoints()
        }
    
    def _select_design_pattern(self, app_type: str, features: List[str]) -> str:
        """Select the best design pattern for the app"""
        if app_type == "web" and any(f in features for f in ["dashboard", "analytics", "metrics"]):
            return "dashboard"
        elif app_type == "web" and any(f in features for f in ["landing", "marketing", "homepage"]):
            return "landing_page"
        elif app_type == "mobile":
            return "mobile_app"
        else:
            return "dashboard"  # Default
    
    def _select_color_scheme(self, style: str, features: List[str]) -> Dict:
        """Select appropriate color scheme"""
        if any(f in features for f in ["finance", "business", "professional"]):
            return self.color_schemes["tech_blue"]
        elif any(f in features for f in ["health", "environment", "sustainability"]):
            return self.color_schemes["success_green"]
        else:
            return self.color_schemes["vibrant_purple"]
    
    def _generate_layout(self, pattern: str, features: List[str]) -> Dict:
        """Generate layout structure"""
        base_layout = self.design_patterns[pattern]["layout"]
        components = self.design_patterns[pattern]["components"]
        
        return {
            "structure": base_layout,
            "sections": components,
            "grid_system": "12-column responsive grid",
            "navigation": "top navigation bar" if pattern != "mobile_app" else "bottom tab navigation"
        }
    
    def _generate_components(self, features: List[str], colors: Dict) -> Dict:
        """Generate component specifications"""
        components = {}
        
        # Header component
        components["header"] = {
            "type": "navigation",
            "background": colors["primary"],
            "text_color": "white",
            "height": "64px",
            "elements": ["logo", "navigation_menu", "user_profile"]
        }
        
        # Feature-specific components
        for feature in features:
            if "auth" in feature.lower():
                components["auth_form"] = {
                    "type": "form",
                    "fields": ["email", "password"],
                    "button_color": colors["primary"],
                    "validation": "real-time"
                }
            
            if "dashboard" in feature.lower():
                components["dashboard"] = {
                    "type": "grid_layout", 
                    "cards": ["metrics", "charts", "recent_activity"],
                    "card_style": self.ui_components["card"]["elevated"]
                }
        
        return components
    
    def _generate_typography(self) -> Dict:
        """Generate typography specifications"""
        return {
            "font_family": "Inter, -apple-system, BlinkMacSystemFont, sans-serif",
            "headings": {
                "h1": "text-4xl font-bold",
                "h2": "text-3xl font-semibold", 
                "h3": "text-2xl font-medium"
            },
            "body": "text-base leading-relaxed",
            "small": "text-sm text-gray-600"
        }
    
    def _generate_spacing(self) -> Dict:
        """Generate spacing system"""
        return {
            "scale": "4px base unit",
            "sizes": {
                "xs": "4px",
                "sm": "8px", 
                "md": "16px",
                "lg": "24px",
                "xl": "32px"
            }
        }
    
    def _generate_breakpoints(self) -> Dict:
        """Generate responsive breakpoints"""
        return {
            "mobile": "320px - 768px",
            "tablet": "768px - 1024px", 
            "desktop": "1024px+"
        }
    
    async def create_wireframe(self, features: List[str]) -> Dict:
        """Create wireframe structure"""
        wireframe = {
            "pages": [],
            "components": [],
            "user_flow": []
        }
        
        # Generate pages based on features
        for feature in features:
            page = {
                "name": f"{feature}_page",
                "sections": self._generate_page_sections(feature),
                "interactions": self._generate_page_interactions(feature)
            }
            wireframe["pages"].append(page)
        
        return wireframe
    
    def _generate_page_sections(self, feature: str) -> List[str]:
        """Generate sections for a feature page"""
        common_sections = ["header", "main_content", "footer"]
        
        feature_sections = {
            "auth": ["login_form", "signup_link", "forgot_password"],
            "dashboard": ["sidebar", "metrics_grid", "charts_section"],
            "profile": ["user_info", "settings_form", "preferences"]
        }
        
        return common_sections + feature_sections.get(feature, ["content_area"])
    
    def _generate_page_interactions(self, feature: str) -> List[str]:
        """Generate interactions for a feature page"""
        interactions = {
            "auth": ["form_validation", "login_submit", "error_handling"],
            "dashboard": ["filter_data", "refresh_metrics", "export_data"],
            "profile": ["edit_profile", "save_changes", "upload_avatar"]
        }
        
        return interactions.get(feature, ["basic_navigation"])
    
    async def generate_css(self, design: Dict) -> str:
        """Generate CSS based on design specifications"""
        css = f"""
/* Base styles */
:root {{
  --primary-color: {design['colors']['primary']};
  --secondary-color: {design['colors']['secondary']};
  --accent-color: {design['colors']['accent']};
  --background-color: {design['colors']['background']};
  --text-color: {design['colors']['text']};
}}

body {{
  font-family: {design['typography']['font_family']};
  background-color: var(--background-color);
  color: var(--text-color);
  margin: 0;
  padding: 0;
}}

/* Utility classes */
.btn-primary {{
  background-color: var(--primary-color);
  color: white;
  padding: 12px 24px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  transition: background-color 0.2s;
}}

.btn-primary:hover {{
  background-color: var(--secondary-color);
}}

.card {{
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  padding: 24px;
  margin: 16px 0;
}}

/* Layout */
.container {{
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 16px;
}}

.grid {{
  display: grid;
  gap: 24px;
}}

@media (min-width: 768px) {{
  .grid-cols-2 {{ grid-template-columns: repeat(2, 1fr); }}
  .grid-cols-3 {{ grid-template-columns: repeat(3, 1fr); }}
}}
"""
        return css
    
    async def get_help(self, query: str, context: Dict) -> Dict:
        """Get help with design decisions"""
        suggestions = [
            "Create design system: 'Create design for dashboard app'",
            "Generate wireframe: 'Create wireframe for mobile app'",
            "Color recommendations: 'Suggest colors for healthcare app'",
            "Layout help: 'Best layout for analytics dashboard'"
        ]
        
        return {
            "response": f"I can help you with design: {query}",
            "suggestions": suggestions,
            "examples": {
                "design": "await assistant.design_assistant.create_design('web', ['dashboard', 'auth'], 'modern')",
                "wireframe": "await assistant.design_assistant.create_wireframe(['auth', 'dashboard'])",
                "css": "await assistant.design_assistant.generate_css(design_spec)"
            }
        }
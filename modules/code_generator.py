"""
Code Generator Module
====================
Advanced code generation for rapid hackathon development
"""

import os
import json
import asyncio
from typing import Dict, List, Any, Optional
from pathlib import Path
import subprocess

class CodeGenerator:
    """Advanced code generator for hackathon projects"""
    
    def __init__(self):
        self.templates = self._load_templates()
        self.language_configs = self._load_language_configs()
        self.framework_templates = self._load_framework_templates()
    
    def _load_templates(self) -> Dict:
        """Load code templates for different languages and patterns"""
        return {
            "python": {
                "fastapi_app": """
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="{app_name}", description="{description}")

# Enable CORS for hackathon demos
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class {model_name}(BaseModel):
    {model_fields}

@app.get("/")
async def root():
    return {{"message": "Welcome to {app_name}!"}}

@app.get("/health")
async def health_check():
    return {{"status": "healthy"}}

{endpoints}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
""",
                "flask_app": """
from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for hackathon demos

@app.route('/')
def home():
    return jsonify({{"message": "Welcome to {app_name}!"}})

@app.route('/health')
def health():
    return jsonify({{"status": "healthy"}})

{routes}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
""",
                "data_analysis": """
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class {class_name}:
    def __init__(self, data_path: str = None):
        self.data = None
        self.model = None
        self.scaler = StandardScaler()
        
        if data_path:
            self.load_data(data_path)
    
    def load_data(self, path: str):
        \"\"\"Load data from various formats\"\"\"
        if path.endswith('.csv'):
            self.data = pd.read_csv(path)
        elif path.endswith('.json'):
            self.data = pd.read_json(path)
        else:
            raise ValueError("Unsupported file format")
        
        print(f"Data loaded: {{self.data.shape}}")
        return self.data
    
    def analyze(self):
        \"\"\"Quick data analysis for hackathon insights\"\"\"
        if self.data is None:
            raise ValueError("No data loaded")
        
        analysis = {{
            "shape": self.data.shape,
            "columns": list(self.data.columns),
            "missing_values": self.data.isnull().sum().to_dict(),
            "summary": self.data.describe().to_dict()
        }}
        
        return analysis
    
    def visualize(self, save_path: str = "analysis_plots.png"):
        \"\"\"Create quick visualizations\"\"\"
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        
        # Distribution plots
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns[:4]
        for i, col in enumerate(numeric_cols):
            if i < 4:
                row, col_idx = divmod(i, 2)
                self.data[col].hist(ax=axes[row, col_idx], bins=30)
                axes[row, col_idx].set_title(f'Distribution of {{col}}')
        
        plt.tight_layout()
        plt.savefig(save_path)
        return save_path

{additional_methods}
"""
            },
            "javascript": {
                "react_component": """
import React, {{ useState, useEffect }} from 'react';
import './{{component_name}}.css';

const {{component_name}} = ({{ {props} }}) => {{
    const [state, setState] = useState({initial_state});

    useEffect(() => {{
        // Initialize component
        {useEffect_code}
    }}, []);

    {methods}

    return (
        <div className="{{component_name.lower()}}">
            <h2>{{component_name}}</h2>
            {jsx_content}
        </div>
    );
}};

export default {{component_name}};
""",
                "express_server": """
const express = require('express');
const cors = require('cors');
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static('public'));

// Routes
app.get('/', (req, res) => {{
    res.json({{ message: 'Welcome to {app_name}!' }});
}});

app.get('/health', (req, res) => {{
    res.json({{ status: 'healthy' }});
}});

{routes}

app.listen(PORT, () => {{
    console.log(`🚀 Server running on port ${{PORT}}`);
}});
""",
                "react_app": """
import React from 'react';
import {{ BrowserRouter as Router, Routes, Route }} from 'react-router-dom';
import Header from './components/Header';
import Home from './pages/Home';
import './App.css';

function App() {{
    return (
        <Router>
            <div className="App">
                <Header />
                <main>
                    <Routes>
                        <Route path="/" element={{<Home />}} />
                        {additional_routes}
                    </Routes>
                </main>
            </div>
        </Router>
    );
}}

export default App;
"""
            }
        }
    
    def _load_language_configs(self) -> Dict:
        """Load language-specific configurations"""
        return {
            "python": {
                "file_extension": ".py",
                "test_extension": "_test.py",
                "package_manager": "pip",
                "virtual_env": "venv",
                "entry_point": "main.py"
            },
            "javascript": {
                "file_extension": ".js",
                "test_extension": ".test.js",
                "package_manager": "npm",
                "entry_point": "index.js"
            },
            "typescript": {
                "file_extension": ".ts",
                "test_extension": ".test.ts",
                "package_manager": "npm",
                "entry_point": "index.ts"
            }
        }
    
    def _load_framework_templates(self) -> Dict:
        """Load framework-specific templates"""
        return {
            "react": {
                "package.json": {
                    "name": "{project_name}",
                    "version": "1.0.0",
                    "dependencies": {
                        "react": "^18.2.0",
                        "react-dom": "^18.2.0",
                        "react-router-dom": "^6.8.0",
                        "axios": "^1.3.0",
                        "@mui/material": "^5.11.0",
                        "@emotion/react": "^11.10.0",
                        "@emotion/styled": "^11.10.0"
                    },
                    "scripts": {
                        "start": "react-scripts start",
                        "build": "react-scripts build",
                        "deploy": "npm run build && serve -s build"
                    }
                }
            },
            "fastapi": {
                "requirements.txt": [
                    "fastapi==0.104.0",
                    "uvicorn==0.24.0",
                    "pydantic==2.5.0",
                    "python-multipart==0.0.6",
                    "python-jose==3.3.0",
                    "passlib==1.7.4",
                    "bcryptjs==3.2.2"
                ]
            }
        }
    
    async def generate(self, prompt: str, language: str = "python", framework: str = None, context: Dict = None) -> Dict:
        """
        Generate code based on prompt
        
        Args:
            prompt: Description of what to generate
            language: Programming language
            framework: Framework to use
            context: Project context
        """
        # Parse the prompt to understand what needs to be generated
        code_type = self._analyze_prompt(prompt)
        
        if framework and framework in self.framework_templates:
            template = self._get_framework_template(framework, code_type)
        else:
            template = self._get_language_template(language, code_type)
        
        # Generate the code
        generated_code = self._apply_template(template, prompt, context or {})
        
        # Add imports and dependencies
        code_with_imports = self._add_imports(generated_code, language, framework)
        
        return {
            "code": code_with_imports,
            "language": language,
            "framework": framework,
            "file_name": self._generate_filename(prompt, language),
            "dependencies": self._get_dependencies(language, framework),
            "instructions": self._generate_setup_instructions(language, framework)
        }
    
    async def generate_full_app(self, app_type: str, features: List[str], architecture: Dict, design: Dict) -> Dict:
        """Generate a complete application"""
        components = {}
        
        if app_type == "web":
            components = await self._generate_web_app(features, architecture, design)
        elif app_type == "api":
            components = await self._generate_api_app(features, architecture)
        elif app_type == "mobile":
            components = await self._generate_mobile_app(features, architecture, design)
        elif app_type == "cli":
            components = await self._generate_cli_app(features, architecture)
        
        return components
    
    async def _generate_web_app(self, features: List[str], architecture: Dict, design: Dict) -> Dict:
        """Generate a complete web application"""
        components = {
            "frontend": {},
            "backend": {},
            "database": {},
            "config": {}
        }
        
        # Generate React frontend
        if "react" in architecture.get("frontend", []):
            components["frontend"]["App.js"] = self._generate_react_app(features, design)
            components["frontend"]["package.json"] = self._generate_package_json("react", features)
            
            # Generate components for each feature
            for feature in features:
                component_code = self._generate_react_component(feature, design)
                components["frontend"][f"components/{feature.title()}.js"] = component_code
        
        # Generate FastAPI backend
        if "fastapi" in architecture.get("backend", []):
            components["backend"]["main.py"] = self._generate_fastapi_app(features)
            components["backend"]["requirements.txt"] = self._generate_requirements(features)
            
            # Generate models and routes
            for feature in features:
                model_code = self._generate_pydantic_model(feature)
                route_code = self._generate_fastapi_routes(feature)
                components["backend"][f"models/{feature}.py"] = model_code
                components["backend"][f"routes/{feature}.py"] = route_code
        
        # Generate database schema
        components["database"]["schema.sql"] = self._generate_database_schema(features)
        
        # Generate configuration files
        components["config"]["docker-compose.yml"] = self._generate_docker_compose(architecture)
        components["config"]["Dockerfile"] = self._generate_dockerfile(architecture)
        components["config"][".env.example"] = self._generate_env_file(features)
        
        return components
    
    def _analyze_prompt(self, prompt: str) -> str:
        """Analyze prompt to determine code type"""
        prompt_lower = prompt.lower()
        
        if any(word in prompt_lower for word in ["api", "endpoint", "route", "fastapi", "flask"]):
            return "api"
        elif any(word in prompt_lower for word in ["component", "react", "ui", "interface"]):
            return "component"
        elif any(word in prompt_lower for word in ["function", "method", "algorithm"]):
            return "function"
        elif any(word in prompt_lower for word in ["class", "model", "object"]):
            return "class"
        elif any(word in prompt_lower for word in ["database", "sql", "query"]):
            return "database"
        else:
            return "general"
    
    def _get_language_template(self, language: str, code_type: str) -> str:
        """Get template for specific language and code type"""
        templates = self.templates.get(language, {})
        
        if code_type == "api" and language == "python":
            return templates.get("fastapi_app", "")
        elif code_type == "component" and language == "javascript":
            return templates.get("react_component", "")
        
        return templates.get("general", "# Generated code\n{code}")
    
    def _apply_template(self, template: str, prompt: str, context: Dict) -> str:
        """Apply template with context variables"""
        # Extract variables from context
        app_name = context.get("name", "HackathonApp")
        description = prompt
        
        # Simple template variable replacement
        code = template.format(
            app_name=app_name,
            description=description,
            **context
        )
        
        return code
    
    def _add_imports(self, code: str, language: str, framework: str = None) -> str:
        """Add necessary imports to the code"""
        imports = []
        
        if language == "python":
            if "FastAPI" in code:
                imports.extend([
                    "from fastapi import FastAPI, HTTPException",
                    "from fastapi.middleware.cors import CORSMiddleware",
                    "import uvicorn"
                ])
            if "pandas" in code:
                imports.append("import pandas as pd")
            if "numpy" in code:
                imports.append("import numpy as np")
        
        elif language == "javascript":
            if "React" in code:
                imports.append("import React from 'react';")
            if "useState" in code:
                imports.append("import { useState } from 'react';")
        
        if imports:
            return "\n".join(imports) + "\n\n" + code
        
        return code
    
    def _generate_filename(self, prompt: str, language: str) -> str:
        """Generate appropriate filename"""
        # Extract main concept from prompt
        words = prompt.split()
        main_word = words[0] if words else "generated"
        
        extension = self.language_configs[language]["file_extension"]
        return f"{main_word.lower()}{extension}"
    
    def _get_dependencies(self, language: str, framework: str = None) -> List[str]:
        """Get list of dependencies needed"""
        deps = []
        
        if language == "python":
            deps.extend(["requests", "python-dotenv"])
            if framework == "fastapi":
                deps.extend(["fastapi", "uvicorn"])
            elif framework == "flask":
                deps.extend(["flask", "flask-cors"])
        
        elif language == "javascript":
            if framework == "react":
                deps.extend(["react", "react-dom", "axios"])
            elif framework == "express":
                deps.extend(["express", "cors"])
        
        return deps
    
    def _generate_setup_instructions(self, language: str, framework: str = None) -> List[str]:
        """Generate setup instructions"""
        instructions = []
        
        if language == "python":
            instructions.extend([
                "1. Create virtual environment: python -m venv venv",
                "2. Activate virtual environment: source venv/bin/activate (Linux/Mac) or venv\\Scripts\\activate (Windows)",
                "3. Install dependencies: pip install -r requirements.txt",
                "4. Run the application: python main.py"
            ])
        
        elif language == "javascript":
            instructions.extend([
                "1. Install dependencies: npm install",
                "2. Start development server: npm start",
                "3. Build for production: npm run build"
            ])
        
        return instructions
    
    async def optimize_code(self, project_path: str):
        """Optimize code for better performance and readability"""
        optimizations = []
        
        # Run code formatters
        try:
            subprocess.run(["black", project_path], check=False, capture_output=True)
            optimizations.append("Applied Python code formatting")
        except:
            pass
        
        try:
            subprocess.run(["prettier", "--write", f"{project_path}/**/*.js"], check=False, capture_output=True)
            optimizations.append("Applied JavaScript code formatting")
        except:
            pass
        
        return optimizations
    
    async def get_help(self, query: str, context: Dict) -> Dict:
        """Get help with code generation"""
        suggestions = [
            "Generate FastAPI app: 'Create a REST API for user management'",
            "Generate React component: 'Create a dashboard component with charts'",
            "Generate data analysis: 'Create a data analysis script for CSV files'",
            "Generate full app: 'Create a todo app with authentication'"
        ]
        
        return {
            "response": f"I can help you generate code for: {query}",
            "suggestions": suggestions,
            "examples": {
                "python_api": "await assistant.generate_code('Create FastAPI app with user authentication', 'python', 'fastapi')",
                "react_component": "await assistant.generate_code('Create React dashboard component', 'javascript', 'react')",
                "data_analysis": "await assistant.generate_code('Create data analysis for sales data', 'python')"
            }
        }
    
    def _generate_react_app(self, features: List[str], design: Dict) -> str:
        """Generate React App.js"""
        routes = []
        for feature in features:
            route = f'<Route path="/{feature.lower()}" element={{<{feature.title()} />}} />'
            routes.append(route)
        
        return self.templates["javascript"]["react_app"].format(
            additional_routes="\n                        ".join(routes)
        )
    
    def _generate_react_component(self, feature: str, design: Dict) -> str:
        """Generate React component for a feature"""
        return self.templates["javascript"]["react_component"].format(
            component_name=feature.title(),
            props="",
            initial_state="{}",
            useEffect_code="// Component initialization",
            methods="// Component methods",
            jsx_content="<div>Feature implementation</div>"
        )
    
    def _generate_fastapi_app(self, features: List[str]) -> str:
        """Generate FastAPI main app"""
        endpoints = []
        for feature in features:
            endpoint = f"""
@app.get("/{feature.lower()}")
async def get_{feature.lower()}():
    return {{"message": "{feature} endpoint"}}
"""
            endpoints.append(endpoint)
        
        return self.templates["python"]["fastapi_app"].format(
            app_name="HackathonApp",
            description="Hackathon Project API",
            model_name="Item",
            model_fields="name: str\n    description: str",
            endpoints="\n".join(endpoints)
        )
    
    def _generate_package_json(self, framework: str, features: List[str]) -> str:
        """Generate package.json for JavaScript projects"""
        template = self.framework_templates.get(framework, {}).get("package.json", {})
        return json.dumps(template, indent=2)
    
    def _generate_requirements(self, features: List[str]) -> str:
        """Generate requirements.txt"""
        base_reqs = self.framework_templates["fastapi"]["requirements.txt"]
        
        # Add feature-specific requirements
        additional_reqs = []
        if "auth" in [f.lower() for f in features]:
            additional_reqs.extend(["python-jose[cryptography]", "passlib[bcrypt]"])
        if "database" in [f.lower() for f in features]:
            additional_reqs.extend(["sqlalchemy", "psycopg2-binary"])
        
        return "\n".join(base_reqs + additional_reqs)
    
    def _generate_pydantic_model(self, feature: str) -> str:
        """Generate Pydantic model for a feature"""
        return f"""
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class {feature.title()}Base(BaseModel):
    name: str
    description: Optional[str] = None

class {feature.title()}Create({feature.title()}Base):
    pass

class {feature.title()}({feature.title()}Base):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True
"""
    
    def _generate_fastapi_routes(self, feature: str) -> str:
        """Generate FastAPI routes for a feature"""
        return f"""
from fastapi import APIRouter, HTTPException
from typing import List

router = APIRouter(prefix="/{feature.lower()}", tags=["{feature}"])

@router.get("/", response_model=List[{feature.title()}])
async def get_{feature.lower()}s():
    # Implementation here
    return []

@router.post("/", response_model={feature.title()})
async def create_{feature.lower()}(item: {feature.title()}Create):
    # Implementation here
    return item

@router.get("/{{item_id}}", response_model={feature.title()})
async def get_{feature.lower()}(item_id: int):
    # Implementation here
    return {{"id": item_id}}
"""
    
    def _generate_database_schema(self, features: List[str]) -> str:
        """Generate database schema"""
        tables = []
        for feature in features:
            table = f"""
CREATE TABLE {feature.lower()}s (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""
            tables.append(table)
        
        return "\n".join(tables)
    
    def _generate_docker_compose(self, architecture: Dict) -> str:
        """Generate docker-compose.yml"""
        return """
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:password@db:5432/hackathon
    depends_on:
      - db
    volumes:
      - .:/app

  db:
    image: postgres:13
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=hackathon
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

volumes:
  postgres_data:
"""
    
    def _generate_dockerfile(self, architecture: Dict) -> str:
        """Generate Dockerfile"""
        return """
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
"""
    
    def _generate_env_file(self, features: List[str]) -> str:
        """Generate .env.example file"""
        env_vars = [
            "DATABASE_URL=postgresql://user:password@localhost:5432/hackathon",
            "SECRET_KEY=your-secret-key-here",
            "DEBUG=True"
        ]
        
        if "auth" in [f.lower() for f in features]:
            env_vars.extend([
                "JWT_SECRET_KEY=your-jwt-secret",
                "ACCESS_TOKEN_EXPIRE_MINUTES=30"
            ])
        
        return "\n".join(env_vars)
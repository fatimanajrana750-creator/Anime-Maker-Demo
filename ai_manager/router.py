import os

class AIRouter:
    def __init__(self):
        self.openai_key = os.getenv("OPENAI_API_KEY", "placeholder_key")
        self.hf_key = os.getenv("HUGGINGFACE_API_KEY", "placeholder_key")
        self.gemini_key = os.getenv("GEMINI_API_KEY", "placeholder_key")
        self.groq_key = os.getenv("GROQ_API_KEY", "placeholder_key")
        self.cloudinary_url = os.getenv("CLOUDINARY_URL", "placeholder_key")

    def route_request(self, department, prompt):
        valid_departments = ["animation", "fixer", "converter"]
        
        if department not in valid_departments:
            return {"is_valid": False, "error_code": 404}
            
        if department == "animation":
            return {"is_valid": True, "target": "Hugging Face API", "prompt": prompt}
        elif department == "fixer":
            return {"is_valid": True, "target": "Gemini and Groq API", "prompt": prompt}
        elif department == "converter":
            return {"is_valid": True, "target": "Cloudinary API", "prompt": prompt}
        
        return {"is_valid": False}
      

import os

class AIRouter:
    def __init__(self):
        self.openai_key = os.getenv("OPENAI_API_KEY", "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")
        self.hf_key = os.getenv("HUGGINGFACE_API_KEY", "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")
        self.gemini_key = os.getenv("GEMINI_API_KEY", "AQ.Ab8RN6I92EPfJ0M0g5FIIGzYKkt_9H9Nj7f38Aoa9_um0eTXsg")
        self.groq_key = os.getenv("GROQ_API_KEY", "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")
        self.cloudinary_url = os.getenv("CLOUDINARY_URL", "tIECm9Y6QfBz6VSNxluapzgQMXk")

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
        

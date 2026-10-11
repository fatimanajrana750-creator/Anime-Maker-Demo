from flask import Flask, request, jsonify
from ai_manager.router import AIRouter

app = Flask(__name__)
router = AIRouter()

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "online",
        "message": "Anime Maker MVP Backend is running successfully."
    })

@app.route("/process", methods=["POST"])
def process_pipeline():
    data = request.json
    prompt = data.get("prompt", "")
    department = data.get("department", "animation")
    
    # Process through AI router with boolean validation
    route_response = router.route_request(department, prompt)
    
    if route_response.get("is_valid", False):
        return jsonify({
            "success": True,
            "data": route_response,
            "message": "Pipeline execution completed without errors."
        })
    else:
        return jsonify({
            "success": False,
            "error": "Invalid department or routing failure."
        }), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
  

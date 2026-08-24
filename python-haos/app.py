from flask import Flask, request, jsonify
import eiscp

app = Flask(__name__)
receiver = eiscp.eISCP('192.168.98.127')

@app.route("/onkyo/power", methods=["POST"])
def power():
    data = request.get_json()
    cond = data["power"]
    
    try:
        receiver.command(f"power={cond}")
        return jsonify({
                "status":"success",
                "power": f"{cond}"
            })
    except Exception as error:
	    return jsonify({
		    "success": False,
		    "error": str(error)
	        }), 500	

@app.route("/onkyo/volume", methods=["POST"])
def set_volume():
    data = request.get_json()

    try:
        volume = float(data["volume"])

        if not 0 <= volume <= 100:
            return jsonify({
                "success": False,
                "error": "Volume must be between 0 and 100"
            }), 400

        onkyo_volume = round(volume * 88 / 100)

        receiver.command(f"volume={onkyo_volume}")

        return jsonify({
            "success": True,
            "volume": volume,
            "onkyo_volume": onkyo_volume
        })

    except Exception as error:
        return jsonify({
            "success": False,
            "error": str(error)
        }), 500

app.run(host="0.0.0.0", port=1111)

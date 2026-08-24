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
    volume = float(data["volume"])

    try:
        receiver.command(
            f"volume={int(volume * 2)}"
        )

        return jsonify({
            "success": True,
            "volume": volume
        })
    except Exception as error:
        return jsonify({
                "error": error
            })

app.run(host="0.0.0.0", port=1111)

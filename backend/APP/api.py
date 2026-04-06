from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, emit

app = Flask(__name__)
CORS(app)

# ✅ FIX: proper CORS for socket
socketio = SocketIO(app, cors_allowed_origins="*")


# ✅ Store votes
votes = {}

# ---------------- HOME ROUTE (avoid 405 error) ----------------
@app.route("/", methods=["GET"])
def home():
    return "Backend running 🚀"

# ---------------- VOTE API ----------------voted_users = set()

@app.route("/vote", methods=["POST"])
def vote():
    data = request.json
    aadhaar = data.get("aadhaar")
    party = data.get("party")

    if not aadhaar or not party:
        return jsonify({"error": "Missing data"}), 400

    if aadhaar in votes:
        return jsonify({"error": "Already voted"}), 400

    votes.add(aadhaar)

    votes[party] = votes.get(party, 0) + 1

    socketio.emit("vote_update", votes)

    return jsonify({"msg": "Vote recorded", "votes": votes})


# ---------------- SOCKET CONNECT ----------------
@socketio.on("connect")   # ✅ FIX: correct event
def handle_connect():
    print("Client connected")

    # Send current votes immediately
    emit("vote_update", votes)


# ---------------- RUN ----------------
if __name__ == "__main__":
    socketio.run(app, debug=True , port=5000)




# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import sqlite3

# app = Flask(__name__)
# CORS(app)

# # 🔌 DB connection
# def get_db():
#     return sqlite3.connect("voting.db")


# # ✅ Register API
# @app.route("/register", methods=["POST"])
# def register():
#     data = request.json
#     conn = get_db()
#     cursor = conn.cursor()

#     try:
#         cursor.execute(
#             "INSERT INTO users (name, mobile, aadhaar, city, state) VALUES (?,?,?,?,?)",
#             (data["name"], data["mobile"], data["aadhaar"], data["city"], data["state"])
#         )
#         conn.commit()
#         return jsonify({"message": "User Registered ✅"})
#     except:
#         return jsonify({"error": "Aadhaar already exists ❌"})


# # ✅ Vote API
# @app.route("/vote", methods=["POST"])
# def vote():
#     data = request.json
#     conn = get_db()
#     cursor = conn.cursor()

#     # ❌ Prevent duplicate vote
#     cursor.execute("SELECT * FROM votes WHERE aadhaar=?", (data["aadhaar"],))
#     if cursor.fetchone():
#         return jsonify({"error": "Already voted ❌"})

#     cursor.execute(
#         "INSERT INTO votes (aadhaar, party) VALUES (?,?)",
#         (data["aadhaar"], data["party"])
#     )
#     conn.commit()

#     return jsonify({"message": "Vote submitted ✅"})


# # ✅ Get Results
# @app.route("/results", methods=["GET"])
# def results():
#     conn = get_db()
#     cursor = conn.cursor()

#     cursor.execute("SELECT party, COUNT(*) FROM votes GROUP BY party")
#     data = cursor.fetchall()

#     result = {row[0]: row[1] for row in data}
#     return jsonify(result)


# # ✅ Aadhaar Search
# @app.route("/search/<aadhaar>", methods=["GET"])
# def search(aadhaar):
#     conn = get_db()
#     cursor = conn.cursor()

#     cursor.execute("""
#         SELECT users.name, users.city, users.state, votes.party
#         FROM users
#         LEFT JOIN votes ON users.aadhaar = votes.aadhaar
#         WHERE users.aadhaar=?
#     """, (aadhaar,))

#     user = cursor.fetchone()

#     if user:
#         return jsonify({
#             "name": user[0],
#             "city": user[1],
#             "state": user[2],
#             "party": user[3]
#         })
#     else:
#         return jsonify({"error": "Not found ❌"})


# if __name__ == "__main__":
#     app.run(debug=True)
from application import app, db

db.create_all()

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
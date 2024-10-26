from app import app, Config


def main():
    print("DB is up?")
    # Config.mock_up()
    app.run(debug=True)

if __name__=="__mian__":
    main()
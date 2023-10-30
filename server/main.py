from __init__ import create_app
from flask_jwt_extended import get_jwt, get_jwt_identity, set_access_cookies, create_access_token
from datetime import datetime, timedelta, timezone

app = create_app()

# Use implicit refreshing with cookies
@app.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            set_access_cookies(response, access_token)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original response
        return response

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
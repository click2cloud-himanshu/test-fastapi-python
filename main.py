


from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.api_route('/yesy', methods=["GET"])
def testApp():
    return "Test app is running"

@app.api_route('/testingcicd', methods=["GET"])
def testAppcicd():
    return "Testing CI CD"


if __name__== "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

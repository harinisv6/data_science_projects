from fastapi import FastAPI
app=FastAPI()
@app.get("/8128")
def read_root():
    return("clg name:Mookambigai college of engineering,"
           "address:kalamavur,keeranur,"
           "code:8128")
@app.get("/8121")
def read_root1():
    return("clg name:M.A.M college of engineering,"
           "address:trichy_chennai trunk road,siruganur,"
           "code:8121")
@app.get("/8113")
def read_root2():
    return("clg name:J.J college of engineering,"
           "address:Ammapettai,poolangulathupatti,"
           "code:8113")
@app.get("/8107")
def read_root3():
    return("clg name:CARE college of engineering,"
           "address:Dindugal main road,thayanur,"
           "code:8107")
@app.get("/8115")
def read_root4():
    return("clg name:K.Ramakrishnan college of engineering,"
           "address:Samayapuram,trichy,"
           "code:8115")
@app.get("/3811")
def read_root5():
    return("clg name:M.I.E.T college of engineering,"
           "address:Gundur,trichy,"
           "code:3811")
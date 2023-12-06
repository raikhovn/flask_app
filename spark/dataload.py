import random

def load(n: int, file: str):

    dataA = [('001','Smith','M',40,'DA',4000),
    ('002','Rose','M',35,'DA',3000),
    ('003','Williams','M',30,'DE',2500),
    ('004','Anne','F',30,'DE',3000),
    ('005','Mary','F',35,'BE',4000),
    ('006','James','M',30,'FE',3500)]

    with open("C:/Users/raikh/VscodeProjects/flask_app/spark/" + file, "w") as fp:
   
       
        for r in range(n):
            i = random.randint(0, n)
            fp.write("".join('{},{},{},{},{},{}\n'.format(i,dataA[ i % 6][1], dataA[ i % 6][2], dataA[ i % 6][3], dataA[ i % 6][4], dataA[ i % 6][5] ))) 


                



if __name__ == "__main__":
    load(50000, "dataA.txt")
    load(40000, "dataB.txt")
    print("Done")
  
 
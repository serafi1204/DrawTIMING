with open('sample.txt', 'w') as f:
    ss = ""
    
    for i in range(5):
        ss += f"Wave{i}:{i+1}:"
        for j in range(6):
            ss +=f"s{i}{j} {j*i+j} {j*i+j+i},"
        ss += "\n"
    f.write(ss)